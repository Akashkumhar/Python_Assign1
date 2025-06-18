"""
1.Write a program in Python to perform the following
operation:
If a number is divisible by 3 it should print “SKILLBREW”
as a string
If a number is divisible by 5 it should print “BRUDITE” as a
string
If a number is divisible by both 3 and 5 it should print
“BRUDITE - NIRVANA” as a string.

"""
n = int(input("Enter a number : "))
if n % 3 == 0 and n % 5 == 0:
    print("number is divisible by both 3 and 5")
elif n % 3 == 0:
    print("number is divisible by 3")
elif n % 5 == 0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 5 and 3")

"""
2. Write a program that accepts a string as input from
the user and calculates the number of digits and
letters.
Input: Hello123
Output: Alphabets: 5 & Number : 3

"""

alpha = 0
num = 0
for i in list("hello2123"):
    if i.isalpha():
        alpha += 1
    elif i.isnumeric():
        num += 1
print( f"total alphabets : {alpha}" )
print( f"total numbers : {num}")



"""
3. Write a Python program to input marks for five
subjects Physics, Chemistry, Biology, Mathematics,
and Computer. Calculate the percentage and grade
according to the following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F

"""

phy = int(input("Enetr physics marks : "))
chem = int(input("Enetr chemistry marks : "))
bio = int(input("Enetr biology marks : "))
math = int(input("Enetr mathematics marks : "))
comp = int(input("Enetr computer marks : "))
total = phy + chem + bio + math + comp
per = total / 5
if per >= 90:
    print("Your Grade Is A")
elif per >= 80:
    print("Your Grade Is B")
elif per >= 70:
    print("Your Grade Is C")
elif per >= 60:
    print("Your Grade Is D")
elif per >= 40:
    print("Your Grade Is E")
else:
    print("Your Grade Is F")




"""
4. Write a Python program to find the sum of all odd
numbers between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25

"""

sum = 0
for i in range(1,10):
    if i % 2 != 0:
        sum += i
print(f"sum of odd numbers b/w 1 to 10 is {sum}")


"""
5. Write a Python program to find the factorial of a
number using a for loop.

"""

fact = 1
n = int(input("Enter a number : "))
for i in range(1,n+1):
    fact *= i
print(f"factorial of given number is : {fact}")


"""
6. Write a Python program to check if a given number
is a perfect number.
A Perfect number is a positive integer that is equal to the
sum of its proper divisors. For instance, 6 has divisors 1, 2,
and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.
Input: 5
Output: No

"""

n = int(input("Enter a number : "))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum += i
if sum == n:
    print("Yes")
else:
    print("No")


"""
7. Write a Python program to check if a string is an
anagram of another string.
string1 = "listen", string2 = "silent"
Output: True

"""


str1 = input("Enter your first strint : ")
str2 = input("Enter your second strint : ")
t = sorted(str1) == sorted(str2)
print(t)


"""
8. Write a Python program to calculate the LCM (Least
Common Multiple) of two numbers.
number1 = 12, number2 = 18
LCM of 12 and 18 are: 36

"""


num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
for i in range(num1,(num1 * num2) + 1):
    if i % num1 == 0 and i % num2 == 0:
        print(f"LCM of 2 numbers is {i}")
        break


"""
9. Write a Python program to count the frequency of
each element in a list.
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}

"""


input_list = [1, 2, 3,2, 4, 1, 2, 4, 5]
Frequency = {}
for item in input_list:
    if item in Frequency:
        Frequency[item] += 1
    else:
        Frequency[item] = 1
print("Frequncy count : ", Frequency)  





"""
10. Write a Python program to reverse the order of
words in a given sentence.
Input_sentence = “Hello, World! Welcome to Python
programming.”
Output after reverse = “programming. Python to Welcome
World! Hello,”

"""

input_string = "programming. Python to Welcome World! Hello"
reverse_words = input_string.split()[::-1]
reverse_sentance = ' '.join(reverse_words)
print(f"sentance after reverse the sentance : {reverse_sentance}")





"""
11. Write a Python program to calculate the sum of
digits of a given number until the sum becomes a
single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Again compute the sum of digits so that it can be reduced
to
on single digit.
Final Output: 6

"""


sum = 0
num = int(input("Enter a number : "))
while(num > 0):
    rem = num % 10
    sum += rem
    num = int(num / 10)
    if sum > 9:
        temp = sum
        sum = 0
        while(temp > 0):
            re = temp % 10
            sum += re
            temp = int(temp / 10)
print(sum)



"""
12. Write a Python program to reverse a number using
a while loop.
Sample Input: num = 12345
Sample Output: revnum = 54321

"""


revnum = 0
num = int(input("Enter a number : "))
while(num > 0):
    rem = num % 10
    revnum = (revnum * 10) + rem
    num = int(num / 10)
print(f"reverse of number is  {revnum}")