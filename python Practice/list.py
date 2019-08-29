class ListNode:
	def __init__(self,value=None):
		self.data=value
		self.next=None
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
l = List()
n1 = ListNode("1")
n2 = ListNode("2")
n3 = ListNode("3")
n4 = ListNode("4")
l.add(n1)
l.add(n2)
l.add(n3)
l.add(n4)
l.printList()