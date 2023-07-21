#Importar SQLite para dentro do Projeto
import sqlite3 as sqlite

# Criar uma conexão
con = sqlite.connect('database.db')
 
#Atualizando Dados na tabela
#updatedata = ['Diego Henrique Silva Furukawa','Cliente do Bruno Furukawa',1]

def fn_update_form(i):
    with con:
        cur = con.cursor()
        query = ("UPDATE customer SET nameCustomer = ?, descriptionCustomer = ? WHERE idCustomer = ?")
        cur.execute(query, i)