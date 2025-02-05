#Find out common letters between two strings Using Python
def remove_common():
    string1 = input("Enter string 1: ")
    string2 = input("Enter string 2: ")
    s1 = set(string1)
    s2 = set(string2)
    print(s1,s2)
    lst = s1 & s2 # extract unique from2
    print(lst)
remove_common()