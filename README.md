Esse script faz os seguintes passos utilizando o comando no terminal:

    python processar_dados.py
  

1 - Descompactar o dados.zip para obter origem-dados.csv e tipos.csv.

2 - Ler os dois arquivos CSV e remover possíveis inconsistências de formatação.

3 - Filtrar os dados para considerar apenas os registros com status == "CRITICO".

4 - Ordenar os registros filtrados pelo campo created_at.

5 - Incluír o campo nome_tipo, mapeando os valores do tipo usando o tipos.csv.

6 - Gerar um arquivo insert-dados.sql contendo os comandos INSERT INTO dados_finais (...) VALUES (...).

7 - Criar uma query SQL final que retorna a contagem de itens agrupados por dia e tipo.





#     INSERT INTO dados_finais (created_at, product_code, customer_code, status, tipo, nome_tipo) VALUES
# ('2023-05-11 16:13:26', 122357859, 55794953, 'CRITICO', 7, 'Capivara'),
# ('2023-05-11 16:13:46', 122350228, 56130239, 'CRITICO', 1, 'Elefante'),
# ('2023-05-11 16:13:49', 126344080, 55803769, 'CRITICO', 8, 'Lontra'),
# ('2023-05-11 16:13:50', 134111037, 55848130, 'CRITICO', 8, 'Lontra'),
# ('2023-05-11 16:14:03', 126237601, 55839718, 'CRITICO', 8, 'Lontra'),
# ('2023-05-11 16:14:08', 132549136, 55845097, 'CRITICO', 8, 'Lontra'),
# ('2023-05-11 16:14:15', 122348882, 55424257, 'CRITICO', 4, 'Urso'),
# ('2023-05-11 16:14:16', 134044177, 55266984, 'CRITICO', 2, 'Camelo'),
# ('2023-05-11 16:14:27', 126366482, 55894039, 'CRITICO', 8, 'Lontra');