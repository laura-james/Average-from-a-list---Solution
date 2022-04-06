# set up two variables for holding the count and the total
total = 0
count = 0
# ask user for number
num = input("Enter number (or blank to end): ")

#keep looping until user enters nothing
while num!="":
  #change the input - which is a string - to a float
  num = float(num)
  #add one to count
  count = count + 1
  # add num to the total
  total = total + num
  # ask for next number
  num = input("Enter number (or blank to end): ")

#if we've got here the user has obviously typed a blank
# work out average
average = total / count
# print it out
print(average)
  