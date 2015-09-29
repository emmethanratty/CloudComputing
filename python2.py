x = 1
temp = 0
a = 0
sum = 0

for i in range(0,4000000):
  a = x + temp
  x = a
  temp = x



  if((x%2) == 0):
    sum += temp
temp = x

print(sum)
