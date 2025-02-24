import zipfile
import pandas as pd
import os

# Nome do arquivo zipado e diretório de extração
zip_file = "dados.zip"
extract_dir = "dados_extraidos"

# Descompactar o arquivo zip
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# Ler os arquivos CSV
origem_dados_path = os.path.join(extract_dir, "origem-dados.csv")
tipos_path = os.path.join(extract_dir, "tipos.csv")

df_origem = pd.read_csv(origem_dados_path)
df_tipos = pd.read_csv(tipos_path)

# Remover espaços extras nos nomes das colunas
df_origem.columns = df_origem.columns.str.strip()
df_tipos.columns = df_tipos.columns.str.strip()

# Normalizar a coluna 'status' para evitar problemas de formatação
df_origem["status"] = df_origem["status"].str.strip().str.upper()

# Verificar colunas disponíveis
print("Colunas disponíveis em df_origem:", df_origem.columns.tolist())

# Exibir valores únicos na coluna 'status' para depuração
print("Valores únicos na coluna 'status':", df_origem["status"].unique())

# Filtrar apenas os dados com status "CRITICO" (sem acento, conforme encontrado no CSV)
df_critico = df_origem[df_origem["status"] == "CRITICO"].copy()

# Verificar se o DataFrame filtrado não está vazio
if df_critico.empty:
    print("Nenhum dado com status 'CRITICO' encontrado.")
else:
    print("Número de linhas em df_critico:", len(df_critico))
    print("Amostra de dados filtrados:")
    print(df_critico.head())

# Ordenar pelo campo "created_at"
df_critico = df_critico.sort_values(by="created_at")

# Verificar se a coluna "tipo" existe
if "tipo" not in df_critico.columns:
    print("Erro: Coluna 'tipo' não encontrada em df_critico.")
else:
    # Criar dicionário de mapeamento do tipo
    mapa_tipos = dict(zip(df_tipos["id"], df_tipos["nome"]))

    # Incluir a coluna "nome_tipo"
    df_critico["nome_tipo"] = df_critico["tipo"].map(mapa_tipos)

    # Gerar script SQL para inserir os dados no banco
    sql_file = "insert-dados.sql"
    table_name = "dados_finais"
    columns = list(df_critico.columns)
    batch_size = 50
    values_list = []

    with open(sql_file, "w", encoding="utf-8") as f:
        for i, (_, row) in enumerate(df_critico.iterrows(), start=1):
            formatted_values = [
                f"'{value}'" if isinstance(value, str) else str(value)
                for value in row
            ]
            
            row_string = "(" + ", ".join(formatted_values) + ")"
            values_list.append(row_string)
            
            # linhas em grupos de 50
            if i % batch_size == 0:
                insert_statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES\n" + ",\n".join(values_list) + ";\n"
                f.write(insert_statement)
                values_list = []

        # valores restantes
        if values_list:
            insert_statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES\n" + ",\n".join(values_list) + ";\n"
            f.write(insert_statement)

    # Query SQL para agrupar por dia e tipo
    query_agrupada = f"""
    SELECT DATE(created_at) AS dia, nome_tipo, COUNT(*) AS quantidade
    FROM {table_name}
    GROUP BY DATE(created_at), nome_tipo
    ORDER BY dia;
    """

    print("Processamento concluído. O arquivo 'insert-dados.sql' foi gerado com sucesso!")
    print("Query para agrupamento:")
    print(query_agrupada)
