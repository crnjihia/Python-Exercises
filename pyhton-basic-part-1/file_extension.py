def get_file_extension():
    filename = input("Enter a filename: ")
    extension = filename.split('.')[-1]
    print("Extension:", extension)

get_file_extension()
