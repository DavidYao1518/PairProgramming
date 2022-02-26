
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