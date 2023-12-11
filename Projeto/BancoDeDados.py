import psycopg2
from psycopg2 import sql

parametros = {
    "host": "localhost",  # Servidor
    "dbname": "projeto_te",  # Nome do banco de dados
    "user": "postgres",  # Nome do usuario
    "password": "1234"  # Senha do PGAdmin
}
# Inicio Funções da Tela Cadastro de Datas Importantes (Edson Rafael)
def conecta_bd():
    conexao = None
    try:  # Tente fazer alguma coisa
        conexao = psycopg2.connect(**parametros)  # Tentar fazer uma conexão com o Banco de Dados
        print('Conexão realizada com sucesso!')
    except Exception as erro:  # Exceção  # As erro (mostrar qual é o erro na conexão)
        print('Não foi possivel conectar ao BD!', erro)
    return conexao

def adicionar_data_ao_banco(data, descricao, tipo_data):
    conexao = conecta_bd()
    id_data_importante = None  # Inicializa com None para lidar com possíveis erros
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    sql.SQL("INSERT INTO Datas_Importantes (dia_data, descricao, tipo_data) VALUES (%s, %s, %s) RETURNING id_data_importante;"),
                    (data, descricao, tipo_data)
                )
                # Obter o ID após a inserção
                id_data_importante = cursor.fetchone()[0]
                print(f'Data adicionada com sucesso! ID: {id_data_importante}')
    except Exception as erro:
        print(f'Erro ao adicionar data: {erro}')
    finally:
        if conexao:
            conexao.close()

    return id_data_importante


def apagar_data_do_banco(id_data_importante):
    conexao = conecta_bd()
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    sql.SQL("DELETE FROM Datas_Importantes WHERE id_data_importante = %s;"),
                    (id_data_importante,)
                )
                print(f'Data removida do banco com sucesso! ID: {id_data_importante}')
    except Exception as erro:
        print(f'Erro ao remover data do banco: {erro}')
    finally:
        if conexao:
            conexao.close()

# Adicione esta função para realizar a atualização no banco de dados
def atualizar_data_no_banco(id_data_importante, nova_data, nova_descricao, novo_tipo_data):
    conexao = conecta_bd()
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    sql.SQL("UPDATE Datas_Importantes SET dia_data = %s, descricao = %s, tipo_data = %s WHERE id_data_importante = %s;"),
                    (nova_data, nova_descricao, novo_tipo_data, id_data_importante)
                )
                print(f'Dados atualizados no banco com sucesso! ID: {id_data_importante}')
    except Exception as erro:
        print(f'Erro ao atualizar dados no banco: {erro}')
    finally:
        if conexao:
            conexao.close()

def carregar_dados_do_banco():
    conexao = conecta_bd()
    dados = []
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT id_data_importante, dia_data, descricao, tipo_data FROM Datas_Importantes;")
                rows = cursor.fetchall()
                dados = [(row[0], row[1], row[2], row[3]) for row in rows]

    except Exception as erro:
        print(f'Erro ao carregar dados do banco: {erro}')
    finally:
        if conexao:
            conexao.close()

    return dados
#Final da Funções da Tela Cadastro de Datas Importantes (Edson Rafael)
 
conexao = conecta_bd()