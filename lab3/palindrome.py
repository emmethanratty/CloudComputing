#change 1

str = input("Please enter a string: ")
#change 2
str = str.casefold()
#change 3
reverse_str = reversed(str)

if list(str) == list(reverse_str):
   print("Palindrome!")
else:
   print("Not a Palindrome.")