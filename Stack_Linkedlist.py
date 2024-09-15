class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.temp=None

    def Create(self,data):
            newnode=Node(data)
            if(self.top is None):
                 self.top=newnode
            else:
                 newnode.next=self.top
                 self.top=newnode
    
    def Pop(self):
         if(self.top is None):
              print("Underflow")
         else:
              self.temp=self.top
              print(self.temp.data,"is deleted")
              self.top=self.top.next
              del(self.temp)

    def Peek(self):
         if(self.top is None):
              print("Underflow")
         else:
              print(self.top.data,"is Top element")

    def Display(self):
         self.temp=self.top
         while self.top is not None:
              print("|",self.top.data,"|")
              self.top=self.top.next

s=Stack()
s.Create(100)
s.Create(200)
s.Create(300)
s.Create(400)
s.Create(500)
s.Pop()
s.Peek()
s.Display()