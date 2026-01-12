def isValid(s:str)->bool:
    """
    Determine if the string of parentheses are valid
    """
    stack=[]
    hashmap={
        ')':'(',
        '}':'{',
        ']':'['
        }
    for char in s:
        # if the charcter is an opening bracket , push it to the stack
        if char in '({[':
            stack.append(char)
        # if its a closing bracket then pop it out
        elif char in ')]}':
            # if th stack is empty early exit , invalid
            if not stack:
                print(False)
                return False
            # pop the last stack character and compare if it matches the expected one 
            last_char=stack.pop()
            print(f"Last char in stack {last_char}")
            if last_char !=hashmap[char]:
                print(False)
                return False
                
            print(True)
    
    return len(stack)==0

isValid('{[{}]}')