F = 1
currnum = 1
tempnum = 0
previous = 1
stingnum = str(currnum)
i = 0;

#while to count the fth number
while i < 1000:
  #fo the fib seq
  tempnum = currnum
  currnum = currnum + previous
  previous = tempnum

  F = F + 1

  stringnum = str(currnum)
  i = len(stringnum)

#prints the number

print(F)


