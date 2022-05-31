#File: TextBroker.py
#Author: Frederick ROddy
#Paramaters: Take in three arguments a file to open, a keyword and an operator 
#Useage: This program takes the command line arguments passed to it and calls our check_string function
#   It depends on the operator but will either check that the key is in the file or that the key is less then 
#   a value in the file. If it doesnt find it then it will return an False bool value that can be used for error
#   handeling.

import subprocess
import sys

#function to open the file (n), look for keyword (n) with an operator (l) if It cant find it it returns a false value

def check_string(n,m,l):
    with open(n) as temp_f:
        datafile = temp_f.readlines()
        stripped = [line.split(",",1)[0] for line in datafile]
        count = 0
    if l == "equal":
        for line in datafile:
            if m in line:
                return line # The string is found
    elif l == 'less':
        for line in stripped:
            if line == 'Over':
                return(datafile[count])
                
            if  int(m) < int(line) and line != 'Over':
                
                if count == 0:
                    return(datafile[0])
                else:
                    return(datafile[count-1])
                break
            count= count+1
    return False  # The string does not exist in the file


#We call the function to check for the keyword, if it is found it returns everything from the line its found on
#       after the comma, If it returns a false value because it cant find anything it calls the error handler
try:
    code = check_string(sys.argv[1],sys.argv[2],sys.argv[3])

    if code == False:
        print(code)

    else:

        code2 = code.split(",",1)[-1]
    
        print(code2)
        
#If something goes wrong it calls the error handler instead of auto quiting
except:
    p = subprocess.run(['python',"ErrorHandle.py", '404',"Textbroker.py"],capture_output=True, shell=True)


    print(p.stdout.decode())