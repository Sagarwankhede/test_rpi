from Main import Variables


class Test:
	
	def __init__(self):
		
		self.vars = Variables()
		self.Select_Db()
		
	def Select_Db(self):
		
		print(self.vars.Port)
		
		self.vars.Port = 90
		print(self.vars.Port)
		
		
		
Test()
