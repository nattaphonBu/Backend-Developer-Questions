#Examples
#The input number is 209324
#The output array should have:
# [ 209324, 209342, 209234, 209243, ..., Etc ]

# 1. get the number from  input and send to function permutation
# 2. check digit of number for find permutation is posible
#  2.1 if digit = 0 no permutation
#  2.2 if digit = 1 it mean 1 posible permutation
# 3. for loop the range(len(input)) to iterable for find permutation
#  3.1 set m equal i value for get value from iteable.
#  3.2 set the remindlist( remind list is the not m value) for send to function permutation for find posible to permutation
#  3.3 for loop send remindlist(recursive) and start to number 2.
#    3.3.1 add data to list 
# 4. return list

def permutation(number_list):
    if len(number_list) == 0:
        return []
    if len(number_list) == 1:
        return str(number_list)
    data_list = []
    for i in range(len(number_list)):
        m = number_list[i]
        remlist = number_list[:i] + number_list[i+1:]
        for p in permutation(remlist):
            number = str(m) + p
            data_list.append(number)
    return data_list

# number = '209324'
number = '001000'
number_list = permutation(number)
number_list = dict.fromkeys(number_list) # Use dict.fromkeys() to get unique value
print('The input number is {}'.format(number))
print('The output array should have: ')
print(list(number_list)) # Change from dict type to list type 
