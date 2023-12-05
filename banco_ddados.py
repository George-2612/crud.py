import sqlite3

conexao = sqlite3.connect('auto_peca') #CRIANDO O BANCO CHAMADO auto_peca
cursor = conexao.cursor()       #UTILIZANDO O BANCO

def criar_tabela():
    conexao = sqlite3.connect("auto_peca")
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS peca (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            codigo INTEGER NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

def cadastrar_peca(nome, codigo):
    conexao = sqlite3.connect("auto_peca")
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO peca (nome, codigo) VALUES (?, ?)', (nome, codigo))
    conexao.commit()
    conexao.close()

def listar_peca():
    conexao = sqlite3.connect("auto_peca")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM peca')
    peca = cursor.fetchall()
    for peca in peca:
        print(f"ID: {peca[0]}, nome: {peca[1]}, codigo: {peca[2]}")
    conexao.close()

def atualizar_peca(peca_id, novo_nome, novo_codigo):
    conexao = sqlite3.connect("auto_peca")
    cursor = conexao.cursor()
    cursor.execute('UPDATE peca SET nome=?, codigo=? WHERE id=?', (novo_nome, novo_codigo, peca_id))
    conexao.commit()
    conexao.close()

def excluir_peca(peca_id):
    conexao = sqlite3.connect("auto_peca")
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM peca WHERE id=?', (peca_id,))
    conexao.commit()
    conexao.close()


criar_tabela()
# Loop principal
while True:
    print("\nEscolha uma operação:")
    print("1 - Cadastrar peca")
    print("2 - Listar peca")
    print("3 - Atualizar peca")
    print("4 - Excluir peca")
    print("0 - Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == "1":
            nome = input("Digite o nome da peça: ")
            codigo = int(input("Digite o codigo da peça: "))
            cadastrar_peca(nome, codigo)
    
    elif escolha == "2":
        listar_peca()
    
    elif escolha == "3":
        peca_id = int(input("Digite o ID da peca que deseja atualizar: "))
        novo_nome = input("Digite o novo nome: ")
        novo_codigo = int(input("Digite o novo ano: "))
        atualizar_peca(peca_id, novo_nome, novo_codigo)
    
    elif escolha == "4":
        peca_id = int(input("Digite o ID da peca que deseja excluir: "))
        excluir_peca(peca_id)
    
    elif escolha == "0":
        print("Saindo do programa. Até mais!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")