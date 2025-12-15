# All the questions which ask in TryCatch Classes Test With Code

# 🟢 EASY LEVEL

# Write a program to display text 5 times.
text = input("Enter Your Texts : ")

for i in range(1,6):
    print(text)

#Print numbers from 1 to 10 using a while loop and then reverse it.
i = 1
while(i<=10):
    print(i)
    i += 1

j = 10
while(j>=1):
    print(j)
    j -= 1

# Program to find the sum of natural numbers from 1 to 1000.
sum = 0

for i in range(1,1001):
    sum = sum+i

print(sum)

# Write a program to check whether a number is a leap year or not.
num = int(input("Enter Number To Check Leap Year Not : "))

if(num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print("Is Leap Year!")
else:
    print("Is Not Leap Year!")

# Write a program to reverse a number (without converting to string).
num = int(input("ENter number to reverse numbner : "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

print(rev)

# Write a program to reverse a string.
str1 = input("Enter string to reverse it : ")
print(str1[::-1])

# Check whether a number is palindrome or not.
num = int(input("ENter number to check whether a number is palindrome or not : "))

if str(num) == str(num)[::-1]:
    print("Number is palindrom")
else:
    print("number is not palindrom")

# Print only even values from an array.
arr = [1,2,3,4,5,6]

for i in arr:
    if(i % 2 == 0):
        print(i)

# Sort an array in ascending order.
arr = [1,3,2,4,6,78,54,33]
arr.sort()
print(arr)

# Sort an array in descending order.
arr = [1,3,2,4,6,78,54,33]
arr.sort(reverse=True)
print(arr)

# Find the sum of the last two numbers.
arr = [1,2,3,4,5,6,7,7]
arr1 = arr[-1]
arr2 = arr[-2]

print(arr1+arr2)

# Print a normal star pattern.
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# Print inverse star pattern.
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# Print vowels from a given string.
str1 = "Hello From Nikhil Chauhan"

vowels = "aeiouAEIOU"

result = []

for i in str1:
    if i in vowels:
        result.append(i)

print(result)

# Print the largest integer in an array.
arr = [1,22,33,5555,6,77,88]

largestNumber = max(arr)
print(largestNumber)

# Check if a number is prime or not.
num = int(input("Enter number to check prime or not : "))

if num < 2:
    print("Is not a prime number")
else:
    isPrime = True

    for i in range(2,num):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        print("is prime number")
    else:
        print("is not a prime number")


# Find the missing number from an array.
arr = [1,2,3,5]

for i in range(1,arr[-1]):
    if i not in arr:
        print(i)

# 🟡 MEDIUM LEVEL

# Print Fibonacci series using recursion.

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
num = int(input("Enter number to print fibonacci series : "))

for i in range(num):
    print(fibonacci(i))

# Another way 

a, b = 0, 1

n = int(input("Enter how many terms: "))

for i in range(n):
    print(a)
    a, b = b, a + b

# Remove duplicate values from an array (numbers or strings).
arr = ["name",1,"name",1,2,3,"nikhil"]

newset = set(arr)

newList = list(newset)
print(newList)

# Find duplicates from two arrays and print into a new array.
arr1 = [1,2,3,4]
arr2 = [3,4,5,6]

arr3 = []

for i in arr1:
    if i in arr2:
        arr3.append(i)

print(arr3)

# Given a string, reverse each word in the sentence.
str1 = "Nikhil Chauhan"

newStr = []

newList = str1.split()

for i in newList:
    newStr.append(i[::-1])

finalStr = " ".join(newStr)
print(finalStr)

# Print if divisiable by 3 print “Fizz”, if divisiable by 5 print“Buzz”, or if divisiable by both print“FizzBuzz”
num = int(input("Enter number : "))

if(num % 3 == 0 and num % 5 == 0):
    print("print“FizzBuzz”")
elif(num % 3 == 0):
    print("Fizz")
elif(num % 5 == 0):
    print("Buzz")

# Swap two numbers without using a third variable.
a,b = 1,2
b,a = a,b

print(a,b)

# Find the next number in the series: 2, 3, 6, 18, 108, …
a = [2,3]

for i in range(4):
    a.append(a[-1]*a[-2])

print(a)

# Count each character in a string (e.g., “ncfghfn”).
str1 = "ncfghfn"
char_count = {}

for char in str1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

# # Another way 

from collections import Counter

str1 = "ncfghfn"
char_count = Counter(str1)

print(char_count)

# Print each number from a nested array.
arr = [1,2,[3,4],[5,[6]],7,8]

def nested(num):
    for i in num:
        if type(i) == list:
            nested(i)
        else:
            print(i)

nested(arr)

# Program to find the factorial of a number.
num = int(input("Enter number for factorial : "))
mul = 1

for i in range(1,num+1):
    mul = mul*i

print(mul)

# Find the sum of n natural numbers.
num = int(input("Enter number for sum : "))

sum = 0

for i in range(1,num+1):
    sum = sum+i

print(sum)

#  🔵 HARD LEVEL

# Armstrong number
num = int(input("Enter a number: "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit * digit * digit
    temp //= 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")

# Another way 

num = 153
s = sum(int(d)**3 for d in str(num))
print(s == num)


# Find the 2nd largest element in an array.
arr = [10,20,50,60,70]
arr.sort(reverse=True)
print(arr[1])

# Find the 4th last largest element in a list.
arr = [10,20,30,40,50]
arr.sort(reverse=True)
print(arr[3])

# Write a function to flatten a nested array.
arr = [1, 2, [3, 4], [5, [6, 7]], 8]

arr1 = []

def fun(arr):
    for i in arr:
        if type(i) == list:
            fun(i)
        else:
            arr1.append(i)

fun(arr)
print(arr1)

# Find maximum number of consecutive 1’s in a binary array. arr = [0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1]
arr = [0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1]

max_count = 0
current_count = 0

for i in arr:
    if i == 1:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print(max_count)

# Sort an array without using the sort() method.
li = [5, 2, 9, 1, 7]

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[i] > li[j]:      # Swap if bigger
            li[i], li[j] = li[j], li[i]

print("Ascending:", li)

li = [5, 2, 9, 1, 7]

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[i] < li[j]:     # Swap if smaller
            li[i], li[j] = li[j], li[i]

print("Descending:", li)


# Convert integer to words (e.g., 0 → ZERO).
num = int(input("Enter a number: "))

words = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]

# handle negative numbers
if num < 0:
    print("MINUS", end=" ")
    num = -num

# if number is 0
if num == 0:
    print("ZERO")
else:
    result = ""
    while num > 0:
        digit = num % 10
        result = words[digit] + " " + result
        num //= 10

    print(result.strip())

# Find the largest substring in a given string.
s = input("Enter string: ")

longest = ""
current = ""

for ch in s:
    if ch not in current:
        current += ch
    else:
        # remove characters until the repeating one is removed
        current = current[current.index(ch) + 1:] + ch

    if len(current) > len(longest):
        longest = current

print("Largest substring:", longest)

# Use map to square numbers and filter to get even numbers.
arr = [1,2,3,4]

newArr = list(map(lambda x:x*x,arr))
print(newArr)

newArr2 = list(filter(lambda x:x % 2 == 0,newArr))
print(newArr2)

# Calculate an electric bill: first 10 days = 1000, from 11th day onwards bill increases by percentage each day.
bill = 1000

for day in range(11, 31):  # Assuming month = 30 days (you can change)
    increase_percent = day - 10
    bill += (bill * increase_percent) / 100

print("Final Bill:", bill)
