
def happy_new_year():
    countdown = 10
    while countdown in range(10, 0, -1):
        print(countdown)
        countdown -= 1

    print("Happy New Year!")
    
    

# Unit test for happy_new_year()
import pytest  
import io
import sys  


def test_prints_10_to_1_hny():
    '''prints 10 to 1 countdown then "Happy New Year!"'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    happy_new_year()
    sys.stdout = sys.__stdout__
    answer = captured_out.getvalue()
    
    #answer.split(\n) produces a list that ends in ''
    answer_list = answer.split('\n')
    #second to last value should be the HNY string
    assert answer_list[-2] == "Happy New Year!", "Your final line does not match 'Happy New Year!', check spelling/capitalization!"
    digit_strings = [str(i) for i in range(1,11)]
    remaining_digits = [i for i in digit_strings if i not in answer_list] 
    assert remaining_digits == [], f"You didn't print all digits 1-10, missing {', '.join(remaining_digits)}"

   
