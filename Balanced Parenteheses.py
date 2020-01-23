from stack import  Stack
a=input('enter order of paranthesis: ', )
b= Stack()
balanced = True

for i in a:
    if b.size == 0 and i == ')' :
        balanced = False
        break

    elif i =='(':
        b.push(i)

    elif i == ')' and b.size != 0:
        b.pop()

if balanced == True and b.size == 0 :
    print('Balanced')
else:
    print('Unbalanced')