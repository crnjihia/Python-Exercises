def generate_list_and_tuple():
    numbers = input("Enter comma-separated numbers: ")
    number_list = numbers.split(',')
    number_tuple = tuple(number_list)
    print("List:", number_list)
    print("Tuple:", number_tuple)

generate_list_and_tuple()
