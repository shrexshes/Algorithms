"""
    Return the alternative arrangements of the two strings.
    :param first_str:
    :param second_str:
    :return: String
    >>> alternative_string_arrange("ABCD", "XY")
    'AXBYCD'
    >>> alternative_string_arrange("XY", "ABCD")
    'XAYBCD'
    >>> alternative_string_arrange("AB", "XYZ")
    'AXBYZ'
    >>> alternative_string_arrange("ABC", "")
    'ABC'
"""

def alternative_string_arrays(first_str:str,second_str:str)->str:
    #getting the length of first string and the second string
    
    first_str_length:int=len(first_str)
    second_str_length:int=len(second_str)
    
    #absolute length calculations : This line determines the length of the longer string between first_str and second_str. If both strings are of equal length, it will use either one.
    abs_length:int= (
        first_str_length if first_str_length > second_str_length else second_str_length
    )
    
    ouput_list:list=[] #an empty list is initialized 
    
    for char_count in range(abs_length):
        if char_count < first_str_length: #check if the char_count is less than first string length
            ouput_list.append(first_str[char_count])
        if char_count < second_str_length: #check if the char_count is less than second string length 
            ouput_list.append(second_str[char_count])
    return " ".join(ouput_list)


if __name__ == "__main__":
    print(alternative_string_arrays("AB", "XYZ"), end=" ") 
 
"""
Output:
A X B Y C D
"""   

