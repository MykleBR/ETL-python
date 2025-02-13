1 - Descompactar o dados.zip para obter origem-dados.csv e tipos.csv.

2 - Ler os dois arquivos CSV e remover possíveis inconsistências de formatação.

3 - Filtrar os dados para considerar apenas os registros com status == "CRITICO".

4 - Ordenar os registros filtrados pelo campo created_at.

5 - Incluír o campo nome_tipo, mapeando os valores do tipo usando o tipos.csv.

6 - Gerar um arquivo insert-dados.sql contendo os comandos INSERT INTO dados_finais (...) VALUES (...).

7 - Criar uma query SQL final que retorna a contagem de itens agrupados por dia e tipo.
