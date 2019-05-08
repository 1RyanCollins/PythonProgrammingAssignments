#Lab assignment 9

def modified(string):
    """Takes a string and returns a modified version of that string
        str -> str"""
    if string == string:
        string = string.replace("God", "Chuck Norris")
        string = string.replace("Jesus" , "Dwayne the Rock Johnson")
        #Note: Sorry for the blasphemy 

        return string 

    else:
        return string


"""Asks the user to open a file. This script reads line by line and
    modifies the contents to be written in the new file"""
    
while True:
    try:
        print("Enter the source filename.")
        source_filename = input("> ")

        source_file = open(source_filename, "r")
            
        break
       
    except OSError:
        print("There was an error working with the source file")

while True:
    try:
        print("Enter the destination filename.")
        destination_filename = input("> ")

        with open(destination_filename, "a") as target_file:
            for line in source_file:
                line = modified(line)
                target_file.write(line)
        break
    
    
            
    except OSError:
        print("There was an error working with the destination file")

    source_file.close()
