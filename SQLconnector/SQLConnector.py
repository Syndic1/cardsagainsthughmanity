import mysql.connector
from mysql.connector import errorcode

class sql_connect:
    
    ##SQL Connector for Cards against Hughmanity

    
    def __init__(self):
        pass
    

    ## Function to run 1 query, then return the result into an object call queryOutput

    def query(self, query):
        
        self.queryin = query

        try:    
            connection = mysql.connector.connect(user='game',   
            password = 'Airsoft10!!',   
            host = 'syndikos.ddns.net',
            database = 'cah')
    
       ## Error handling
        
        except mysql.connector.Error as err:    
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        #Runs the taken in query and returns the output
        try:
            connection
                
        except:
            return

        else:           
            curs = connection.cursor()
            runquery = curs.execute(self.queryin)
            output = curs.fetchall()    
            curs.close
            connection.close
    
            return output
