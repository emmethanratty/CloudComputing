
# Input function lets you input a string into the variable
string = input("Please enter a string: ")
i = 0

stringrev = ""

#print prints to the console
print(string)

stringlen = len(string)

j = stringlen

print(stringlen)

for i in range(0, stringlen):

  stringrev += string[j - 1]
  j = j - 1


print(stringrev)

if(string == stringrev):
  print("Is a palindrome")
else:
  print("Not a palindrome")