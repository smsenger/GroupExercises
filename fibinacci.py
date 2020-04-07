#Program that asks the user for integer input, then outputs the integers of the fibinacci sequence. Will continue
#until reaching the number represented by user input (7 == the 7th integer in the f. sequence)

#asks for user input // Defines starting point of numbers in sequence
user_num = input('Please select a whole number: ')
num1 = 1
num2 = 1
count = 1


try:
    user_num = int(user_num)
    while count <= user_num:      #goes up until 'n'.prints out next 'n' numbers of the fibonacci sequence. 
        print(num1)
        total = num1 + num2        #adds two numbers together to get third number
        num1 = num2
        num2 = total
        count += 1
except: 
    user_retry = input('Please run program again and enter a valid whole number when prompted.')



#Alternative method: 
#Program that asks the user for numberical input, 'n', 
# user_num = input('Please select a whole number: ')
# num1 = 1
# num2 = 1
# count = 1

# While True:
#     try:
#         user_num = int(input('Please select a whole number: ')) 
#         break
#     except:
#         print('Please run program again and enter a valid whole number when prompted.')
        
#     while count <= user_num:      #goes up until 'n'.prints out next 'n' numbers of the fibonacci sequence. 
#         print(num1)
#         total = num1 + num2
#         num1 = num2
#         num2 = total
#         count += 1

  
   




  


 


