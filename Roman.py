#Author: Shunyu Yao (shunyu@vt.edu)
#Date: Feb 25, 2022
#IDE: VIM - Vi IMproved 8.0
#
#romanToInt: Given an input Roman numeral string, translate it into its integer value.
#   input: String
#   output: Int
def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    return_int = 0
    RN_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
    s_reversed = s[::-1]     

    last_int = 0
    for c in s_reversed:
        if RN_dict[c] >= last_int:
            return_int += RN_dict[c]
        else:
            return_int -= RN_dict[c]
        last_int = RN_dict[c]
    return return_int

#Function by Sarthak Kahaliya
#Using Text Editor Sublime Text 3

def intToRoman(self, num: int):

    # mapping Integer Values to Roman values in a Dictonary
    dictonary = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    stack = list(dictonary.keys())
    output = ""

    # Lopping through every digit of number (key) to Convert it into its Roman (value)
    while num > 0:
        if stack[-1] > num:
            stack.pop()
        else:
            num -= stack[-1]

            # adding the Value to the Output
            output += dictonary[stack[-1]]  

    return output
