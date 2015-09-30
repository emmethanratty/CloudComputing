month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = 1
year = 1901
sunday = 2
count = 0
i = 0

monthcount = 0;

for year in range(1901,2000):
  #print(year)

  for day in range(1,month[i] + 1):
    #print(day)
    if(sunday == 7 and day == 1):
        count = count + 1
    day = day + 1
    sunday = sunday + 1
    i = i + 1

    if(i > 12):
      i = 1
    if(sunday > 7):
      sunday = 1
    #print(i)
  day = 1

print(count);