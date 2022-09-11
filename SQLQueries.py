import sqlite3

#.execute(""" CREATE TABLE IF NOT EXISTS wardenMessages (
#    id integer,
#    name text,
#    msg text,
#    time integer)""")

#c.execute(""" CREATE TABLE IF NOT EXISTS warden (
#        id integer,
#        name text,
#        gems integer)""")

#c.execute(""" CREATE TABLE IF NOT EXISTS wardenMoniter 

conn = sqlite3.connect('warden.db')
c = conn.cursor()

class SQLQeries:

    def addGems(num:int,vicId:str):
        with conn:
            c.execute(
            'UPDATE warden SET gems = gems + ? WHERE id=?', 
            (num, vicId,))    
            
    def removeGems(num:int,vicId:str):
        with conn:
            c.execute(
            'UPDATE warden SET gems = gems - ? WHERE id=?', 
            (num, str(vicId),))    

    def setGems(num:int,vicId:str):
        with conn:
            c.execute(
            'UPDATE warden SET gems = ? WHERE id=?', 
            (num, str(vicId),))    

            
    def getTupleFromId(vicId:str):
        c.execute('SELECT * FROM warden WHERE id IN (SELECT id FROM warden WHERE id = ?)', (vicId,))
        testTable = c.fetchall()
        return testTable
