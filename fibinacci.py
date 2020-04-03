#Program that asks the user for numberical input, 'n', 
user_num = input('Please select a whole number: ')
num1 = 1
num2 = 1
count = 1

try:
    user_num = int(user_num)
    while count <= user_num:      #goes up until 'n'.prints out next 'n' numbers of the fibonacci sequence. 
        print(num1)
        total = num1 + num2
        num1 = num2
        num2 = total
        count += 1
except:
    user_retry = input('Please run program again and enter a valid whole number when prompted.')
  
   




  


 


