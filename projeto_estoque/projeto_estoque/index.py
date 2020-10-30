from PyQt5 import uic, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco_youtube"
)
cursor = banco.cursor()
def funcao_login():
    usuario = login.lE_user.text()
    senha = login.lE_password.text()

    if usuario == 'vilmar' and senha == '1234':
       funcao_exibir_opcoes()
    else:
        login.lE_user.clear()
        login.lE_password.clear()

def funcao_adicionar():
    categorias = adicionar.cB_categoria.currentText()
    nome_produto = adicionar.lE_nome.text()
    codigo_produtos = adicionar.lE_codigo.text()
    quantidade_produtos = adicionar.lE_quantidade.text()
    preco_compra = adicionar.lE_PCompra.text()
    preco_venda = adicionar.lE_PVenda.text()
    descricao = adicionar.lE_descricao.text()

    comando = ("INSERT INTO produtos (Nome,categoria,preco_compra,preco_venda,codigo,quantidade,Descricao) VALUES (%s,%s,%s,%s,%s,%s,%s)")
    dados = (str(nome_produto),str(categorias),str(preco_compra),str(preco_venda),str(codigo_produtos),str(quantidade_produtos),str(descricao))
    cursor.execute(comando,dados)

    banco.commit()

    adicionar.lE_nome.clear()
    adicionar.lE_codigo.clear()
    adicionar.lE_quantidade.clear()
    adicionar.lE_PCompra.clear()
    adicionar.lE_PVenda.clear()
    adicionar.lE_descricao.clear()

def funcao_consultar():
    funcao_exibir_consultar()
    categoria2 = consultar.cb_categoria2.currentText()
    comando = ("SELECT * FROM produtos WHERE categoria = ("+categoria2+")")
    cursor.execute(comando)
    linhas = cursor.fetchall()

    consultar.tabela1.setRowCount(len(linhas))
    consultar.tabela1.setColumnCount(7)

    for i in range (0, len(linhas)):
        for j in range(0,7):
            consultar.tabela1.setItem(i,j,QtWidgets.QTableWidgetItem(str(linhas[i][j])))

    banco.commit()

def funcao_deletar():
    funcao_exibir_deletar()
    categoria3 = deletar.categoria3.currentText()
    nome = deletar.lE_nome2.text()
    comando2 = ("DELETE FROM produtos WHERE categoria = ("+categoria3+") AND Nome=('"+nome+"')")
    cursor.execute(comando2) 
    
    banco.commit()

    deletar.lE_nome2.clear()

def funcao_exibir_opcoes():
    opcoes.show()
def funcao_exibir_adicionar():
   adicionar.show()
def funcao_exibir_deletar():
    deletar.show()
def funcao_exibir_consultar():
    consultar.show()

def fecha_adicionar():
    adicionar.close()
def fecha_consultar():
    consultar.close()
def fecha_deletar():
    deletar.close()


app = QtWidgets . QApplication([])

opcoes = uic.loadUi("opcoes.ui")
login = uic.loadUi("tela_login.ui")
adicionar = uic . loadUi("adicionar.ui")
deletar = uic.loadUi("deletar.ui")
consultar = uic.loadUi("consultar.ui")

login.pB_login.clicked.connect(funcao_login)
opcoes.pB_adicionar.clicked.connect(funcao_exibir_adicionar)
opcoes.pB_consultar.clicked.connect(funcao_exibir_consultar)
opcoes.pB_deletar.clicked.connect(funcao_exibir_deletar)

adicionar.pB_voltar.clicked.connect(fecha_adicionar)
consultar.pB_voltar.clicked.connect(fecha_consultar)
deletar.pB_voltar.clicked.connect(fecha_deletar)

adicionar.pB_cadastrar.clicked.connect(funcao_adicionar)
consultar.pB_consultar.clicked.connect(funcao_consultar)
deletar.pB_deletar.clicked.connect(funcao_deletar)

login.show()
app.exec()
