##The winning number is 120888
##The output array should have:
#[ 000088, 000188, 000288, ..., Etc ]

# 1. run for loop from 000000 to 999999
# 2. check if the last 2 digit is same the last input 2 digits
# 3. add the number to list

def calculate_loterly_number(number):
    if len(number) < 6 or len(number) > 6:
        return []
    string_number = ''
    data_list = []
    last_secount_digit = number[4:]
    for i in range(0, 1000000):
        string_number = '{:06}'.format(i)
        if string_number[4:] == last_secount_digit:
            data_list.append(string_number)
    print(data_list)

data = '120888'
calculate_loterly_number(data)
