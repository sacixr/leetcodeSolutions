'''Is Palindrome Problem
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.'''

def isPalindrome(s) -> bool:
    # if the string is just empty, removing the alphanumeric characters means removing the space. an empty string reversed is in fact a palindrome
    if s == " " or s == "":
        return True
    else:
        # we filter through the string and remove all non-alphanumeric symbols
        # due to the way filtering works, we join all filtered results together without spaces
        string = "".join(filter(str.isalnum, s))
        # if the lowercase version of the string is the same as the reverse of the lowercase string, we have a palindrome
        if string.lower() == (string[::-1]).lower():
            return True
        # else, we return false
        else:
            return False
        
# If you would like to see this code working, please run the file and make sure you have python installed.
string = "A man, a plan, a canal: Panama"
print("Our string is", string)
print("Palindrome?", isPalindrome(string))

string = "race a car"
print("\nOur string is", string)
print("Palindrome?", isPalindrome(string))

string = " "
print("\nOur string is", string)
print("Palindrome?", isPalindrome(string))