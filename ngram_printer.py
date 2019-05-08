#Lab Assignment #9 - Due 3/18

#Problem 1

#This script asks users to enter a number of characters (n) and then reads a filename
#Once open, the contents will be displayed n characters per line at a time


count = 0 

while True:
    print("How many characters should I display at a time?")
    n = int(input())
    print("What file should I display?")
    filename = input(">" )
    try:
        with open(filename) as fileobj:
            line = fileobj.read(n)
            while line != "":
                print(line)
                line = fileobj.read(n)
            break 
                
                    
                
          
         
            
            
    except OSError:
            print("There was an error trying to access that file.")
