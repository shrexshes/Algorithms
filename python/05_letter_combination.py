"""
Letter combination of a Phone Number problem 

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

2 → "abc"
3 → "def"
4 → "ghi"
5 → "jkl"
6 → "mno"
7 → "pqrs"
8 → "tuv"
9 → "wxyz"
"""
from typing import List

def letterCombination(digits:str)->List[str]:
    if not digits:
        return []
    hash_map={'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

    # initialize result list to collect  all the valid combinations
    result:List[str]=[]  

    #backtracking helper
    def backtrack(index:int,path:List[str])->None:
        print(f"index {index}")
        if index==len(digits):
            result.append(''.join(path)) # convert lists to string and add it to result
            return
        
        # get current digits and its corresponding letters
        current_digit=digits[index];
        letters=hash_map[current_digit]
        print(f" current digit : {current_digit}")
        print(f" letter_up : {letters}")

        for letter in letters:
            print(f"letter : {letter}")
            path.append(letter)
            print(f"path: {path}")
            backtrack(index + 1, path)
            path.pop()
        print("----------------")
        
    
    backtrack(0,[])
    return result

letterCombination("23")


