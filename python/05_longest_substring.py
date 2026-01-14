def longestSubstring(s:str)->int:
    if not s:
        return 0
    
    char_index_map={}

    left=0
    max_length=0

    for right in range(len(s)):
        char=s[right]

        if char in char_index_map and char_index_map[char] >=left:
            left = char_index_map[char] + 1 