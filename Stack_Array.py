class Stack:
    def __init__(self,n):
        self.top=-1
        self.size=n
        self.list=[-1]*n

    def push(self,data):
        if self.top==self.size-1:
            print("Overflow")
        else:
            self.top+=1
            self.list[self.top]=data

    def pop(self):
        if self.top==-1:
            print("Underflow")
        else:
            print("deleted element:",self.list[self.top])
            self.top-=1
    
    def peek(self):
        if self.top==-1:
            print("Underflow")

        else:
            print("peek element is:",self.list[self.top])
    
    def display(self):

        for i in range(self.top+1,-1,-1):
            if self.top==-1:
                print("Underflow")
                break
            else:
                print("|",self.list[self.top],"|")
                self.top-=1

s=Stack(15)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.peek()
s.display()

