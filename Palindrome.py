from stack import Stack

def is_palindrome(orginal_str):
    string= orginal_str.lower()
    string= string.replace(' ','')

    a=Stack()
    rev_str=''

    for i in string:
        a.push(i)

    while a.size != 0 :
        rev_str += a.pop()

    if rev_str == string:
        return True
    else:
        return False

