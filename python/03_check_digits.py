import time
number_to_check= 85516600401

def total_number(number):
    total=0
    for digit in number:
        total += int(digit)
    return total

def odd_number_addition(number):
    total=0
    for i, odd_number in enumerate(reversed(number)):
        if i%2 ==0 :
            total +=int(odd_number)

    return total

def last_digit(number):
    get_last_digit=0
    for i, digit in enumerate(reversed(number)):
        if i==0:
            get_last_digit=digit
    return get_last_digit

def check_digit(number):
    start_time = time.perf_counter()
    
    str_number=str(number)

    #step 1 : get total number
    total=total_number(str_number)

    #step 2 : get odd number and add them 
    total_odd_num=odd_number_addition(str_number)

    double_odd_num=total_odd_num*2

    add_total_doubled_odd=total+double_odd_num

    last_digit_num= last_digit(str(add_total_doubled_odd))

    result=10-int(last_digit_num)
    print("result:",result)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.6f} seconds")
check_digit(number_to_check)


