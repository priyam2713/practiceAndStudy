#!/usr/bin/env python
# coding: utf-8

# # Priyam version

# In[4]:


# Constants
DIGITS_MAP = {
    '0': 'ZERO',
    '1': 'ONE', 
    '2': 'TWO',
    '3': 'THREE',
    '4': 'FOUR',
    '5': 'FIVE',
    '6': 'SIX',
    '7': 'SEVEN',
    '8': 'EIGHT',
    '9': 'NINE',
    '10': 'TEN',
    '20': 'TWENTY',
    '30': 'THIRTY',
    '40': 'FOURTY',
    '50': 'FIFTY',
    '60': 'SIXTY',
    '70': 'SEVENTY',
    '80': 'EIGHTY',
    '90': 'NINTY',
    '100': 'HUNDRED',
    '1000': 'THOUSAND'
}
MAX_DIGIT_LIMIT = 4    
# Function to Convert Number to Word
def spell_number_to_word(number, spell_word=[]):
    digits = list(str(number))
    count_of_digits = len(digits)
    i = 0
    if count_of_digits > MAX_DIGIT_LIMIT:
        return []
    while i < count_of_digits:
        if count_of_digits == 4:
            if digits[i] != '0':
                spell_word.extend([DIGITS_MAP[str(digits[i])], 'THOUSAND'])
        
        elif count_of_digits == 3:
            if digits[i] != '0':
                spell_word.extend([DIGITS_MAP[str(digits[i])], 'HUNDRED'])
        
        elif count_of_digits == 2:
            if digits[i] != '0':
                num = int(digits[i]) * 10
                spell_word.extend([DIGITS_MAP[str(num)]])

        elif count_of_digits == 1:
            if digits[i] != '0':
                spell_word.extend([DIGITS_MAP[str(digits[i])]])
            
        digits.remove(digits[i])
        count_of_digits -= 1
    return spell_word


if __name__ == "__main__":
    number = 9005
    if number < 0:
        print ("Not a valid input")
    else:
        spell_words = spell_number_to_word(number)
        if spell_words:
            print(" ".join(spell_words))
        else:
            print ("Implementing soon for More than four digits")


# # Navin version

# In[6]:


'''
Python program to print a given number in
words. The program handles numbers 
from 0 to 9999 

A function that prints given number in words 

'''

def convert_number_to_word(num):
    lengh=len(num)
    if(lengh==0 and lengh>4):
        print("please enter lenght of number below 4 not 0")
        return
    
	
    single_digit=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    # The first string is not used,  it is to make array indexing simple 
    two_digit= ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen","seventeen", "eighteen", "nineteen"]
    tens_multiple= ["", "", "twenty", "thirty", "forty",	"fifty", "sixty", "seventy", "eighty",   "ninety"]  
    
	# The first two string are not used, they are to make array indexing simple
    tens_power=["hundred","thausand"]

    # For single digit number 
    if(lengh==1):
        print(single_digit[ord(num[0])-48])
        return
    
    # Code path for first 2 digits
    c=0
    while(c<len(num)):
        if(lengh>=3):
            
            if(ord(num[c])-48!=0):
                print(single_digit[ord(num[c])-48],end=' ')
                print(tens_power[lengh-3], end=' ')
            lengh-=1
        
        # Code path for last 2 digits
        else:

            # Need to explicitly handle 
			# 10-19. Sum of the two digits
			# is used as index of "two_digits"
			# array of strings
            if(ord(num[c])-48==1):
                sum=(ord(num[c])-48)+(ord(num[c+1])-48)
                print(two_digit[sum])
                return
            # Need to explicitely handle 20
            elif(ord(num[c])-48==2 and ord(num[c])-48==0):
                print('twenty')
                return

            # Rest of the two digit 
			# numbers i.e., 21 to 99 
            else:
                i=ord(num[c])-48
                if(i>0):
                    print(tens_multiple[i], end=' ')
                else:
                    print("", end='')
                c+=1
                if(ord(num[c])-48!=0):
                    print(single_digit[ord(num[c])-48])
        c+=1


#Start Code
string =input("Enter the number : ")
convert_number_to_word(string)


# # Abhishek version

# In[7]:


num2words = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 
'Thirteen', 14: 'Fourteen',              15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',              19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 
40: 'Forty',              50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',              90: 'Ninety', 100: 'Hundred', 1000: 'Thousand'}


def convert_num_to_word(number):
    word_list = []
    if number > 9999:
        print('Currently utility only supported for 4 digits or lower')
        return []
    while number >= 0:
        if num2words.get(number, None):
            word_list.append(num2words[number])
            return word_list
        else:
            divisor = 10** (len(str(number)) - 1)
            quotient = (number // divisor) * 10 if divisor == 10 else (number // divisor)
            word_list.append(num2words[quotient]) if num2words.get(quotient, None) else None
            word_list.append(num2words[divisor]) if divisor > 10 else None
            number = number % divisor


word_list = convert_num_to_word(4009)
print(" ".join(word_list))


# In[ ]:




