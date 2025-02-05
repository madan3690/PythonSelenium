"""
1.Convert a given string to int using a single line of code.
a = '5'
2.Write a code snippet to convert a string to a list.
str1 = "Analytics based"
3.Write a code snippet to reverse a string. original_str = "Python Selenium"
4.Write a code snippet to sort a list in Python.
my_list = [3, 2, 1]
"""


#Area of Triangle LeapYear
# 1/2*b*h
b = float(input("enter the Base :"))
h = 20
area = b * h / 2
print(area)
#------------------------------------------------------------------------#

def CheckLeap(Year):
    if (Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0):
        print("Given year is a leap year")
    else:
        print("Given year is not a leap year")
        Year = int(input("Enter the year:"))  # or
        # Year = 1700
        CheckLeap(Year)
#Positive - Negativeinteger
#------------------------------------------------------------------------#
def Numbercheck(a):
#check if the number is positive
    if a >0:
        print("Number given is positive")
    elif a < 0:
        print("Number is negative")
    else:
        print("Number is Zero")

a = float(input("Enter the number :"))
Numbercheck(a)
#------------------------------------------------------------------------#

#11,23 B/w given 2 numbers find the prime number
n1 = int(input("PLease, Enter the n1:"))
n2 = int(input("PLease, Enter the n2:"))
print("The prime Numbers in the range are:")
for number in range(n1,n2+1):
    if number >1: # prime number should be >1
        for i in range(2,number): # range
             if(number % i) == 0:
                break
    else:
             print(number)

#------------------------------------------------------------------------#
#check if the word is a palandrome
def ispalandrome(s):
    return s ==s[::-1]
s = "Mom"
a = ispalandrome(s)
if a:
    print("yes")
else:
    print("No")

#------------------------------------------------------------------------#
#check if the given string has vowels
def vowels(string):
    for char in string:
        if char in "AEIOUaeiou":
            print(char)
vowels("Atharv")

#------------------------------------------------------------------------#
#print sum of numbers
nums = (1, 2, 3, 4)
sum_nums = 0
for num in nums:
    sum_nums = sum_nums + num
print(f'Sum of numbers is {sum_nums}')

#------------------------------------------------------------------------#
#print even number
num = int(input("Enter the number:"))
def print_evennumbers():
    if num %2==0:
        print("Even number")
    else:
        print("Odd number")
print_evennumbers()

#------------------------------------------------------------------------#

# Prints all letters except 'e' and 's'

for letter in 'geeksforgeeks':

    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

#------------------------------------------------------------------------#
#google interview qa#
"""
Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere. 

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""

def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False
#------------------------------------------------------------------------#
"""
Given an array of ints, return the number of 9's in the array. 

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""

def array_count9(nums):
    return nums.count(9)
#------------------------------------------------------------------------#
"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4. 

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""

def array_front9(nums):
    return 9 in nums[:4]

#------------------------------------------------------------------------#
"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front; 

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""

def front_times(str, n):
    return str[:3] * n


#------------------------------------------------------------------------#
"""
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring). 

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""

def last2(str):
    last2 = str[-2:]
    return sum(1 for i in range(len(str)-2) if str[i:i+2] == last2)

#------------------------------------------------------------------------#




"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo". 

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(str):
    print( str[::2])

str = 'Hello'
string_bits(str)
#------------------------------------------------------------------------#
"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings. 

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""

def string_match(a, b):
    shorter = min(len(a), len(b))
    return sum(1 for i in range(shorter-1) if a[i:i+2] == b[i:i+2])

# ------------------------------------------------------------------------#
"""
Given a non-empty string like "Code" return a string like "CCoCodCode". 

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""

def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result += str[:i+1]
    return result
#------------------------------------------------------------------------#
"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string. 

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""

def string_times(str, n):
    return str * n
#------------------------------------------------------------------------#
"""
Given an array of ints, return a new array length 2 containing the first and last elements from the original array.
 The original array will be length 1 or more.

make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]
"""

def make_ends(nums):
    print( [nums[0], nums[-1]])
nums = ([1, 2, 3])
nums1 = ([1, 2, 3, 4])
nums2 = ([7, 4, 6, 2])
make_ends(nums)
make_ends(nums1)
make_ends(nums2)
#------------------------------------------------------------------------#
"""
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more. 

common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
"""

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

#------------------------------------------------------------------------#
"""
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more. 

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([3, 2, 1]) → False
"""

def first_last6(nums):
    return 6 in (nums[0], nums[-1])
#------------------------------------------------------------------------#
"""
Given an int array length 2, return True if it contains a 2 or a 3. 

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""

def has23(nums):
    return 2 in nums or 3 in nums
#------------------------------------------------------------------------#
"""
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}. 

make_pi() → [3, 1, 4]
"""

def make_pi():
    return [3, 1, 4]

#------------------------------------------------------------------------#
"""
Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. Return the changed array. 

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""

def max_end3(nums):
    return [nums[0]] * 3 if nums[0] >= nums[-1] else [nums[-1]] * 3
#------------------------------------------------------------------------#
"""
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements. 

middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
"""

def middle_way(a, b):
    return [a[1], b[1]]

#------------------------------------------------------------------------#

"""
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}. 

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""

def reverse3(nums):
    return nums[::-1]
#------------------------------------------------------------------------#
"""
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}. 

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]
#------------------------------------------------------------------------#
"""
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are the same. 

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""

def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]
#------------------------------------------------------------------------#
"""
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0. 

sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2
"""

def sum2(nums):
    return nums[0] + nums[1] if len(nums) > 1 else sum(nums)
#------------------------------------------------------------------------#
"""
Given an array of ints length 3, return the sum of all the elements. 

sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""

def sum3(nums):
    return sum(nums)
#------------------------------------------------------------------------
# expected out put = my name aru
list1 = ["my", "name"]
list2 = ["aru"]

add = list1 + list2
print(add)
# convert  to string
print(' '.join(add))
#------------------------------------------------------------------------
#convert the list to dict
l1 = ["a", "b","c"]
l2 = [1,2,3]
#method 1 to convert to dict
# convert  to dict
z = zip(l1,l2)
print(list(z))

#method 2 to convert to dict
# convert  to dict
dict1 = dict(zip(l1,l2))
print(dict1)


#method 3 to convert to dict
# convert  to dict
dict2 = {l1[i]:l2[i] for i in range(len(l1))}
print(dict2)


#method 4 to convert to dict
dict3 = { }
for key in l1:
    for value in l2:
        dict3[key]= value

#------------------------------------------------------------------------
#remove duplicates from the string
def remove_duplicate(duplicate):
    final_list = []
    for char in duplicate:
        if char not in final_list:
            final_list.append(char)
    st =''.join(final_list)
    return st
duplicate = 'adsjfkjasdfkaksdfasss'
print(remove_duplicate(duplicate))

#------------------------------------------------------------------------
#remove duplicates from the list

def remove_duplicate(duplicate):
    final_list = []
    for element in duplicate:
        if element not in final_list:
            final_list.append(element)
    return final_list
duplicate = [1,1,2,2,2,2,3,4,5,5,5,5,6]
print(remove_duplicate(duplicate))

#------------------------------------------------------------------------


#Find out common letters between two strings Using Python
def remove_common():
    string1 = input("Enter string 1: ")
    string2 = input("Enter string 2: ")
    s1 = set(string1)
    s2 = set(string2)
    lst = s1 & s2 # extract unique from2
    print(lst)
remove_common()

#------------------------------------------------------------------------
