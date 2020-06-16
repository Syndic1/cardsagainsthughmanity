##SQL Connector for Cards against Hughmanity
import mysql.connector
from mysql.connector import errorcode

## Function to run 1 query, then return the result into an object call queryOutput

def connect_to_sql_server(query):

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
            
    curs = connection.cursor()
    runquery = curs.execute(query)
    output = curs.fetchall()
    
    curs.close
    connection.close
    
    return output



queryOutput = connect_to_sql_server("SELECT * FROM black_cards")

for item in queryOutput:
    print(item)

    
                     
