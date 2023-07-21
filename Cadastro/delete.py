#Importar SQLite para dentro do Projeto
import sqlite3 as sqlite

# Criar uma conexão
con = sqlite.connect('database.db')
 


#Deletando Dados na tabela
#deletedata = [3]
def fn_delete_form(id):
    with con:
        cur = con.cursor()
        query = ("DELETE FROM customer WHERE idCustomer = ?")
        cur.execute(query, id)