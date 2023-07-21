#Importando SQLite
import sqlite3 as lite

#Criando Conexao
con = lite.connect('dados.db')

#Criando Tabela do Banco de dados
with con:
    cur=con.cursor()
    cur.execute('CREATE TABLE inventario(id integer primary key autoincrement,nome text,local text,descricao text,marca text,data_da_compra date,valor_da_compra decimal,serie text,imagem text)')