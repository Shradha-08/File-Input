file = open("Xyz.txt")
#print(file.read())
search_word = input("Enter a word you want to search in file: ")
if(search_word in file.read()):
    print("Word found")
else:
    print("Not found")
