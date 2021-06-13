import pymysql

class MySQLDB:
    def __new__(cls, host, user, password, database):
        """ test connection """
        try:
            connect = pymysql.connect(host = host,
                            user = user,
                            password = password,
                            database = database)

        except Exception as e:
            print("Failed to connect database: ", e)
            return None

        else:
            connect.close()
            return super().__new__(cls)

    def __init__(self, host, user, password, database):
        """ initialize args """
        self.host, self.user, self.password, self.database = host, user, password, database

    def query(self,sqls):
        """ execute the sqls """
        assert isinstance(sqls,list), 'sqls must be a list'
        connect = pymysql.connect(host = self.host,
                            user = self.user,
                            password = self.password,
                            database = self.database,
                            cursorclass = pymysql.cursors.DictCursor)
        cursor = connect.cursor()
        try:
            for sql in sqls:
                cursor.execute(sql)

            data = cursor.fetchall()
        except Exception as e:
            print("Failed to query: ", e)
            data = None
        finally:
            connect.close()
            return data

# if __name__=="__main__":
#     # A TEST FOR MySQLDB
#     db_mysql = MySQLDB(host='localhost',
#                     user='root',
#                     password='password',
#                     database='mysql')

#     sql="""select * from user"""

#     print(db_mysql.query([sql]))
    
    