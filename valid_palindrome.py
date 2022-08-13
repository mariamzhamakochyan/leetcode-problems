def is_polindrome(string):
    new_str = string.lower()
    news = ''
    knew_str = ''
    for i in string:
        if i.isalnum():
           news += i
           hnew_str = news[::-1]
    if news == knew_str:
       return True
    else:
       return False
string = "I have a rally good day today. I'm not hungry. HeHeHE"
print(is_polindrome(string))
