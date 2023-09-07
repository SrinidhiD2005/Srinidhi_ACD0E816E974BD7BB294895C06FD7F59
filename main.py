def isLeapYear(year):
  if (Year % 4 == 0 and Year % 100 !=0) or year % 400 == 0:
    return True
  else:
    return False

Year = int(input("Enter a year:"))
if isLeapYear:
  print(Year," is a leap Year.")
else:
  print(Year," is not a leap Year.")
  