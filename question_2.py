import csv


# function to write csv file

def create_csv_file():
    with open('employee_file.csv', mode='w') as csv_file:
        fields_name = ['first_name', 'last_name'] ## create header fields
        data = {
            1: {'first_name' : 'Michael', 'last_name': 'Jordan'},
            2: {'first_name' : 'Christian', 'last_name': 'Ronaldo'},
            3: {'first_name' : 'Bill', 'last_name': 'Gates'},
            4: {'first_name' : 'Steve', 'last_name': 'Jobs'},
            5: {'first_name' : 'Michael', 'last_name': 'Schumacher'},
            6: {'first_name' : 'Frodo', 'last_name': 'Baggins'},
            7: {'first_name' : 'Barack', 'last_name': 'Obama'},
            8: {'first_name' : 'Tiger', 'last_name': 'Woods'},
        } ## create datas
        writer = csv.DictWriter(csv_file, fieldnames=fields_name)
        writer.writeheader() ## wirite table header
        for i in data:
            writer.writerow(
                {
                    'first_name': data[i]['first_name'],
                    'last_name': data[i]['last_name'],
                }
            )
# function to read csv file

def read_csv_file(file):
    data_dict = []
    with open(file, mode='r') as csv_file:
        csv_render = csv.DictReader(csv_file)
        for row in csv_render:
            full_name = row['first_name'] + ' ' + row['last_name']
            data_dict.append(full_name)
        sort_data = sorted_name(data_dict)
        print(sort_data)

# function to sorted list name

def sorted_name(data_dict):
    sort_data = sorted(data_dict, key=lambda x: x.split(" ")[-1])
    # sorted by last_name so i use lambda funcion to split and get the last element of list to sorted
    return sort_data
             
create_csv_file()
read_csv_file('employee_file.csv')
