#Importar SQLite para dentro do Projeto
import sqlite3 as sqlite

# Criar uma conexão
con = sqlite.connect('database.db')

#Criar uma tabela
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE customer (idCustomer INTEGER PRIMARY KEY AUTOINCREMENT,cNameCustomer TEXT,cSalesMan TEXT,nPhoneNumber TEXT,cDescription TEXT,dStartOfContract DATE,dCreateCustomer DATE)")    
    cur.execute("CREATE TABLE contact (idContact  INTEGER PRIMARY KEY AUTOINCREMENT,idCustomer INTEGER,cNameContact TEXT,cPhoneContact TEXT,cEmailContact TEXT,dCreateContact DATE)")
    
    #cur.execute("CREATE TABLE peerrouter (idASN text PRIMARY KEY, interfaceconnection text, router TEXT, barratrinta TEXT)")
    #cur.execute("CREATE TABLE contractedmodel (OnDemand text, AutoMitigation text, AlwaysOn TEXT, RouteControl TEXT)")
    #cur.execute("CREATE TABLE protectedip (ip text, security TEXT)")