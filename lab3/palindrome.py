
# Input function lets you input a string into the variable
string = input("Please enter a string: ")
i = 0

stringrev = ""

#print prints to the console
print(string)

stringlen = len(string)

j = stringlen

print(stringlen)
#reverses the string into the stringrev
for i in range(0, stringlen):

  stringrev += string[j - 1]
  j = j - 1


print(stringrev)
#makes both lower case so that it can compare wothout case
stringrev = stringrev.casefold()
string = string.casefold()

if(string == stringrev):
  print("Is a palindrome")
else:
  print("Not a palindrome")