def is_palindrome(num):
    return str(num) == str(num)[::-1]


number = int(input("Enter a number: "))

if is_palindrome(number):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")