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
