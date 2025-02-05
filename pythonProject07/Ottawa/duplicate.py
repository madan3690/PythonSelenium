def abc():
    s="madanmohanseetha"
    q=''
    for i in s:
        if i not in q:
            q=q+i

    print(q)


def remove_common():
    # string1 = input("Enter string 1: ")
    # string2 = input("Enter string 2: ")
    string1 ='madan'
    string2 ='mohan'
    s1 = set(string1)
    s2 = set(string2)
    lst = s1 & s2 # extract unique from2
    print(lst)
# remove_common()

# for letter in 'geeksforgeeks':
#
#     if letter == 'e' or letter == 's':
#         break
#     print('Current Letter :', letter)

def prime_numbers():
    # n1 = int(input("PLease, Enter the n1:"))
    # n2 = int(input("PLease, Enter the n2:"))
    # print("The prime Numbers in the range are:")
    # for number in range(n1, n2 + 1):
    #     if number > 1:  # prime number should be >1
    #         for i in range(2, number):  # range
    #             if (number % i) == 0:
    #                 break
    #     else:
    #         print(number)
    n1=3
    n2=45
    for i in range(n1,n2+1):
        if i>1:
            for j in range(2,i):
                if(i%j)==0:
                    break
        else:
            print(i)


prime_numbers()
