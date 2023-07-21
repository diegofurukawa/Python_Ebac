#Importar SQLite para dentro do Projeto
import sqlite3 as sqlite

# Criar uma conexão
con = sqlite.connect('database.db')

#Inserindo Dados na tabela
#insertdata = ['Mari Afonso','Diego','(11)994329402','Cliente do Diego', '17/07/2013' ,'17/07/2023']
#insertdata = [1, 'Nome do Contato','(11)994329402', 'email@email.com','17/07/2023']

def fn_insert_form(i):
    with con:
        cur = con.cursor()
        #query = ("INSERT INTO customer (cNameCustomer, cSalesMan, nPhoneNumber, cDescription, dStartOfContract, dCreateCustomer) VALUES (?, ?, ?, ?, ?, ?)")
        query = ("INSERT INTO contact (idCustomer, cNameContact, cPhoneContact, cEmailContact, dCreateContact) VALUES (?, ?, ?, ?, ?)")
        cur.execute(query, i)