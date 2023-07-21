#Importando SQLite
import sqlite3 as lite

#Criando Conexao
con = lite.connect('dados.db')


#CRUD -- Create | Read | Update | Delete

#Inserindo Dados
def inserir_form(i):
    dados = ['TESTE', 'LOCAL', 'DESCRICAO', 'MARCA', '11/11/2011', '123456', 'SERIE', 'CAMINHO']
    with con:
        cur=con.cursor()
        query = ('INSERT INTO inventario (nome,local,descricao,marca,data_da_compra,valor_da_compra,serie,imagem) VALUES (?,?,?,?,?,?,?,?)')
        cur.execute(query, i)
    
    
#Atualizar Dados
#atulizar_dados = ['TESTE354', 'LOCAL', 'DESCRICAO', 'MARCA', '11/11/2011', '123456', 'SERIE', 'CAMINHO', '1']
def atualizar_form(i):
    with con:
        cur=con.cursor()
        query = "UPDATE inventario SET nome = ?,local = ?,descricao = ?,marca = ?,data_da_compra = ?,valor_da_compra = ?,serie = ?,imagem = ? WHERE id = ?"
        cur.execute(query, i)
    

#Deletar Dados
#deletar_dados = ['2']
def deletar_form(i):
    with con:
        cur=con.cursor()
        query = "DELETE FROM inventario WHERE id = ?"
        cur.execute(query, i)
    
    
#Ver Dados
def ver_form():
    ver_dados = []

    with con:
        cur = con.cursor()
        query = ('SELECT * FROM inventario')
        cur.execute(query)
        
        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
            
        #print(ver_dados)
    return ver_dados
    
#Ver Dados Unitarios
# id = ['0']

def ver_item(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = ('SELECT * FROM inventario WHERE id = ?')
        cur.execute(query, id)
        
        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)
            
        #print(ver_dados_individual)
        return ver_dados_individual