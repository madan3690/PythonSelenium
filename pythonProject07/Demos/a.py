# s="abcba"
# if s==s[::-1]:
#     print("Polidrome")
# for i in range(len(s)):
#     print(s[i])


def is_palindrome(s):
    i,j=0,len(s)-1
    if s[i]!=s[j]:
        return False
        i+=i;
        j-=j;
    return True

p="aetabatea"
print(is_palindrome(p))


