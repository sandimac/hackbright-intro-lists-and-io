def convert_file_to_list(text_file):
    file_open = open(text_file)
    file_list = file_open.readlines()
    file_open.close()
    return file_list 

print convert_file_to_list("sandi_fav_foods.txt")
print convert_file_to_list("katherine_fav_foods.txt")



