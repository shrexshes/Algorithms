def longestSubstring(s:str)->int:
    charSet=set() #set removes the extra repeating numbers in a list
    l=0
    res=0

    for r in range(len(s)):   #len=8 r=0, r=1,r=2 ,r=3
        print(f"r:{r}") #0 , 1 ,2 ,3
        while s[r] in charSet: #s=a , s=b , s=c ,s=a (true)
            charSet.remove(s[l]) #skip,#skip,#skip , l=0 -> charset(a remove)
            l+=1 #skip ,#skip,#skip , l=1
        print(f"man s[r] :{s[r]}")
        charSet.add(s[r])   #a charset=a ,charset =b, charset=c , charset=a
        res=max(res,r-l+1) #max(0,0-0+1) , max(1,1-0+1), max(2,2-0+1) , max(3,3-1 +1)
        print("res:",res) #1,2,3,3,

longestSubstring("abcabcbb")
