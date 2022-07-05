import psycopg2

#DB接続
def get_connection():
    con = psycopg2.connect( 
        host = "localhost",
        password = "password",
        user = "postgres",
        port = "5433")

    #DB接続確認
    if con is not None:
        print("Connection Success !")
    else:
        print("Connection failed !")

    return con


def insert(num, data):
    con = get_connection()
    if con is not None:
        try:
            # Open a cursor to perform database operations
            cur = con.cursor()  

            # Execute a command: this creates a new table
            # cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

            # Pass data to fill a query placeholders and let Psycopg perform
            # the correct conversion (no more SQL injections!)
            # cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (num, data))
            cur.execute("INSERT INTO test (id, num, data) VALUES(%s, %s, %s)", (7, num, data))

            # Make the changes to the database persistent
            con.commit()

            # Close communication with the database
            cur.close()
            con.close()
        
        except Exception as error:
            con.rollback()
            con.close()
            print("Unexpected Error: {}".format(error))


insert(10, "apple")