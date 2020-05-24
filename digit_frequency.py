


def has_same_digit(list_a, list_b):   #function w/two parameters
    if len(list_a) != len(list_b):
        return False
        print('List lengths unequal. Thank you for running this program.')
    else:    
        dictionary1 = {}

        for num in list_a:                #a for loop that runs through list to get each integer
            if dictionary1.get(num) > 0:
                dictionary1[num] += 1                 #make a dictionary of list elements, turn into key value pairs
            else:
                dictionary1[num] = 1

        dictionary2 = {}

        for num in list_a:                #a for loop that runs through list to get each integer
            if dictionary2.get(num) > 0
                dictionary2[num] += 1                #make a dictionary to count how many times something in a list
            else:
                dictionary2[num] = 1
        if dictionary1 == dictionary 2:
            return True
        else:
            return False
        for key in dictionary1.keys():
            if dictionary2[key] != dictionary1[key]:
                return False
        return True                             #lets the for loop run through comparing all pairs, if no false exits loop and returns True

        
print(has_same_digit([1, 2, 3, 4], [4, 3, 2, 1]))

#split this into one fn that loads data into dict., one that compares