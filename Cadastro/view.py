#Importar SQLite para dentro do Projeto
import sqlite3 as sqlite

# Criar uma conexão
con = sqlite.connect('database.db')
      
#Selecionando todos Dados na tabela
#selectalldata = []

def fn_select_all_form():
    selectalldata = []
    with con:
        cur = con.cursor()
        query = ("SELECT * FROM customer")
        cur.execute(query)
        
        rows = cur.fetchall()
        for row in rows:
            selectalldata.append(row)
            
        return selectalldata
        
    


#Selecionando Dado Especifico na tabela
def fn_select_id_form(id):
    selectdata = []
    with con:
        cur = con.cursor()
        query = ("SELECT * FROM customer WHERE idCustomer = ?")
        cur.execute(query, id)
        
        rows = cur.fetchall()
        for row in rows:
            selectdata.append(row)
        
    return selectdata 