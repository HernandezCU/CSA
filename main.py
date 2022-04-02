print("Create functions that will find the largest and smallest word in the list ")
#define text file to open
my_file = open('words.txt', 'r')

#read text file into list 
data = my_file.read().split("\n")

#display content of text file
print(type(data))
print(data)
