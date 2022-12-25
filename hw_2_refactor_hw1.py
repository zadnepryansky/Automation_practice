from hw_1 import plates_list

your_code = input('Enter licence plates: ')
needed_code = your_code.upper()


def info_about_plates():
    print(f'Unique licence plates in plates list: {len(set(plates_list))} ')
    if needed_code in plates_list:  # find license plates
        print(f'Founded license plate - is on the list')
    else:
        print(f'The license plate is not on the list')


def parsing_data(data=needed_code) -> list or bool:
    counter = 0
    for _ in data.upper():
        counter += 1
    if counter == 8:
        numbers = list(filter(str.isdigit, needed_code))

        new_data = []
        new_data.extend([needed_code[0:2], needed_code[6:8]])
        new_data.extend(numbers)

        return new_data
    else:
        print('Wrong input format')
        return False


def sum_of_number(data=needed_code) -> int:
    sum_of_numbers = 0
    for i in needed_code:
        if i.isdigit():
            sum_of_numbers += int(i)
    return sum_of_numbers


info_about_plates()
data = parsing_data()
print(data)
print(f'Sum of the numbers: {sum_of_number()}')
