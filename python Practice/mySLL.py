class List:
	def __init__(self):
		self.head=None
	def add(self,node):
		if(self.head==None):
		 self.head=node
		else:
			irr=self.head
			while(irr.next!=None):
				irr=irr.next
			irr.next=node
	def printList(self):
		if(self.head==None):
			print("list is empty")
		else:
			irr=self.head
			while(irr!=None):
				print(irr.data)
				irr=irr.next
