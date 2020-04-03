fizz = 'fizz'
buzz = 'buzz'
num = int(input('Please enter a whole number: ')
count = 0

while count < num:
    if count % 3 == 0 and count % 5 == 0:   #print fizzbuzz if divisble by 3 and 5
      print(fizz + buzz)
    elif count % 3 == 0:     #print fizz if number divisable by 3
      print(fizz)
    elif count % 5 == 0:     #print buzz if divisble by 5
      print(buzz)
    else:
      print(count)