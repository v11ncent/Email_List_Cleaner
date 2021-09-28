import csv 
FROM_ADDRESS_INDEX = 3
NAME_INDEX = 2

def main():
    with open('./files/ContactList.csv', newline='', encoding='utf-8') as csv_file:
        read_file = csv.reader(csv_file, delimiter=',')
        next(read_file)
        read_file_list = remove_unwanted(list(read_file))
        count = 0
        for row in read_file_list:
            count += 1
            print(f'{row[FROM_ADDRESS_INDEX]} -- {row[NAME_INDEX]}')
        print(count)


def format_email(email):
    return email.casefold().strip()

def set_ignore_list(path):
    return_list = []
    with open(path, 'r') as ignore_file:
        for element in ignore_file.readlines():
            return_list.append(format_email(element))
    return return_list

def remove_duplicates(list):
    address_list = []
    unique_list = []
    for element in range(len(list)):
        if list[element][FROM_ADDRESS_INDEX] not in address_list:
            address_list.append(list[element][FROM_ADDRESS_INDEX])
            unique_list.append(list[element])
    return unique_list

def remove_unwanted(list):
    return_list = []
    unique_list = remove_duplicates(list)
    ignore_list = set_ignore_list('files/IgnoreListMine.txt')
    for element in range(len(unique_list)):
        email = format_email(unique_list[element][FROM_ADDRESS_INDEX]) 
        if email not in ignore_list:
            return_list.append(unique_list[element])
    return return_list

main()