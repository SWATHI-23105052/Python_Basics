class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top=None
    
    def push(self,data):
        newnode = Node(data)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next = self.top
            self.top=newnode

    def pop(self):
        if self.top is None:
            print("UnderFlow")
        else:
            temp=self.top
            pop_val=self.top.data
            self.top=self.top.next
            del temp
            return pop_val
        

def priority(char):
    if char=='^':
        return 3
    if char=='*' or char=='/':
        return 2
    if char=='+' or char=='-':
        return 1
    return 0

def infix_to_postfix(exp):
    s = Stack()
    result = []

    for char in exp:
        
        if char.isalnum():
            result.append(char)

        elif char == '(':
            s.push(char)

        elif char == ')':
            temp=s.pop()
            while temp!='(':
                result.append(temp)
                temp=s.pop()
            
        else:  
            while s.top is not None and priority(char)<=priority(s.top.data):
                result.append(s.pop())
            s.push(char)
            

    while s.top is not None:
        result.append(s.pop())

    return ''.join(result)

exp=input("Enter the expression: ")
print(infix_to_postfix(exp))

