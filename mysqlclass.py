import MySQLdb as db

'''
Hint---
-do not forget to add the ip address to the accessed hosts in your domain name so 
if the error says "_mysql_exceptions.OperationalError: "Access denied for user 'ahmedkhaled'@'199.188.236.168'" 
then you have to copy this ip to the remotesql ip list on your domain 
'''

class mysqlclass:
	HOST = ''
	USER = ''
	PASSWORD = ''
	DB = ''

	def __init__(self, host, user, password, db_name):
		mysqlclass.HOST = host
		mysqlclass.USER = user
		mysqlclass.PASSWORD = password
		mysqlclass.DB = db_name
		mysqlclass.connection = db.connect(host=mysqlclass.HOST,
			user=mysqlclass.USER, passwd=mysqlclass.PASSWORD, db=mysqlclass.DB)
		mysqlclass.handler = mysqlclass.connection.cursor()	

	def execute_query(self, query):
		self.handler.execute(query)

	def select_all(self, table_name):
		try:    
			self.execute_query("SELECT * FROM "+table_name)
			result = self.handler.fetchall()
			return result
		except Exception as e:
		    print (e)

	def close_connection():
		self.connection.close()


db = mysqlclass('DOMAIN_IP_ADDRESS','USER_NAME','PASSWORD','DATABASE_NAME')
print( db.select_all("TABLE_NAME") )
