#File: ErrorHandle.py
#Author: Frederick ROddy
#Paramaters: Takes in Takes in 3 command line arguments after calling the program
#Useage: This program is used to display error messages based on the code passed to it.
#   it calls the textbroker (sys.argv[2]) and passes it Service.txt (sys.argv[3]), the keywork (error), and the operator
#   equal. It will get back the error message file (ie msgEng.tst or msgGer.txt). It will then call that file with
#   the error code (sys.argv[1]) that was passed to it with the operator equal.


import subprocess
import sys

#we call the texthandler with the file (Service.txt), a keyword (error), and operator (equal)
f = subprocess.run(['python', sys.argv[2], sys.argv[3], 'Error',"equal"],capture_output=True, shell=True)

#We Take the raw output from f and clean it up 
r = f.stdout.decode()
r = r.rstrip()
r = r.replace("'","")

#we call the texthandler with the file (R), a keyword (The error code), and operator (equal)
p = subprocess.run(['python', sys.argv[2] ,r, sys.argv[1],"equal"],capture_output=True, shell=True)

#We Take the raw output from p and clean it up 
q = p.stdout.decode()
q = q.rstrip()
q = q.replace("'","")

print('Error: '+sys.argv[1]+ ' '+ q) # The string is found

sys.exit()