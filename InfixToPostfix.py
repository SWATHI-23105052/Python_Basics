class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,char):
        self.stack.append(char)

    def pop(self):
        return self.stack.pop()
    

def priority(char):
    if char=='^':
        return 3
    if char=='*' or char=='/':
        return 2
    if char=='+' or char=='-':
        return 1
    return 0

def infix_to_postfix(exp):
    postfix=[]
    s=Stack()

    for char in exp:
        if char=='(':
            s.push(char)
        elif char.isalnum():
            postfix.append(char)
        elif char==')':
            temp=s.pop()
            while temp!='(':
                postfix.append(temp)
                temp=s.pop()
        else:
            while s.stack and priority(char)<=priority(s.stack[-1]):
                postfix.append(s.pop())
            s.push(char)

    while s.stack:
        postfix.append(s.pop())
    
    return ''.join(postfix)

def Evaluate(result):
    postfix=[]
    s=Stack()
    


exp=input("Enter a expression:")
result=infix_to_postfix(exp)
print(result)
ans=Evaluate(result)
print(ans)
        