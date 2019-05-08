#Lab Assignment 9

#Problem 6


#This script opens up a source file and a destination file. Once open,
#the file is read and written to a new file

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
                target_file.write(line)
        break
    
    
            
    except OSError:
        print("There was an error working with the destination file")

    source_file.close()
        
        
