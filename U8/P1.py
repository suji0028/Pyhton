import os

def create_file(filename):
    try:
        with open(filename,"w") as file:
            file.write("Hello World!\n")
        print("File "+filename+" created successfully")
    except IOError:
        print("Error while creating file"+filename)

def read_file(filename):
    try:
        with open(filename,"r") as file:
            content = file.read()
            print(content)
    except IOError:
        print("Error while reading file"+filename)


def append_file(filename, text):
    try:
        with open(filename,"a") as file:
            file.write(text)
        print("The append to file "+filename+" is successful")
    except IOError:
        print("Error while appending to file"+filename)

def rename_file(old_filename, new_filename):
    try:
        os.rename(old_filename,new_filename)
        print("File "+old_filename+" renamed to "+new_filename)
    except IOError:
        print("Error while renaming file"+old_filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File "+filename+" deleted successfully")
    except IOError:
        print("Error while deleting file"+filename)


if __name__=="__main__":
    filename = "newfile.txt"
    newfilename = "newfile2.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename,"Appended text")
    read_file(filename)
    rename_file(filename,newfilename)
    read_file(newfilename)
    delete_file(newfilename)