def data(str):
    names = str.split()
    n = len(names) - 1
    return len(names[n])  
string = input("Enter the string: ")
print(data(string))
