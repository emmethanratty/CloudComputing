month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = 1
year = 1901
sunday = 1
count = 0
i = 0


daycount = 0
monthcount = 0;
yearcount = 0;
#this is a for loop to count the years
for year in range(1900,2000):

  yearcount = yearcount + 1
  #print(year)

  #this checks to see wether it is a leap year or not
  if((year%4) == 0):

    month[2] = month[2] + 1
    #for loop to count the year
    for i in range(0,12):


      monthcount = monthcount + 1
      #for loop to count the day
      for day in range(1,month[i] + 1):

        daycount = daycount + 1
        #print(day)
        #if to check to see if the sunday lands on the first say of the month
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

    month[2] = month[2] - 1

  #when its not a leap year smae code
  else:
    for i in range(0,12):

      monthcount = monthcount + 1

      for day in range(1,month[i] + 1):

        daycount = daycount + 1
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


print(yearcount)
print(monthcount)
print(daycount)
print(count);