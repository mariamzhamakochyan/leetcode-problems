def is_polindrome(string):
    new_str = string.lower()
    str1 = ''
    str2 = ''
    for i in new_str:
        if i.isalnum():
           str1 += i
           str2 = str1[::-1]
    if str1 == str2:
       return True
    else:
       return False
string = "I have a rally good day today. I'm not hungry. HeHeHE"
print(is_polindrome(string))
