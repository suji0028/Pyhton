# file = open("rku.txt", 'r')
# for each in file:
#     print(each)
#
# file.close()



# file = open("rku.txt", 'r')
# print(file.read())



# with open("rku.txt", 'r') as file:
#     data = file.read()
# print(data)



# file = open("rku.txt", 'r')
# print(file.read(5))



# with open("rku.txt", 'r') as file:
#     data = file.readlines()
#     for line in data:
#         words = line.split()
#         print(words)



# file = open("demo.txt", 'w')
# file.write("This is the end \n")
# file.write("Hold Your Breath ")
# file.write("and count to 10")
# file.close()



# file = open("example.txt", 'w')
# file.write("This is the beginning \n")
# file.write("bandook nahi\n")
# file.write("Revolver \n")
# file.close()
# print("Data Written Successfully")


#Read from a file
# file = open("example.txt",'r')
# content = file.read()
# print("File Content:\n",content)
# file.close()


#Append to a file
# file = open("example.txt",'a')
# file.write("This line is appended at the end.\n")
# file.close()
# print("Data appended successfully!")


# file = open("example.txt",'r+')
# print("Before Writing!",file.read())
# #move cursor to begining
# file.seek(0)
# file.write("Updated First Line! \n")
# file.close()



# file = open("newfile.txt",'w+')
# file.write("This is a new file created using w+ mode. \n")
# file.seek(0) #move current to start for read
# print("file content: ",file.read())
# file.close()



# file = open("example.txt",'a+')
# file.write("This line is appended using a+.\n")
# file.seek(0) #move current to start for read
# print("File Updated: \n",file.read())
# file.close()

