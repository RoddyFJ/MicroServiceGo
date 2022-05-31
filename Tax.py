#File: Tax.py
#Author: Frederick ROddy
#Paramaters: Takes in Takes in 5 command line arguments after calling the program
#Useage: This program is used to display the percentage amount you are taxed depending on the 
#   We combine the Status and Year to make a key (ie 2020J) that we pass to our TextHandler (sys.argv[1]) with our
#   Service.txt (sys.argv[2]) file and a operator ('equal') to find the file for the 2020J taxes (it returns 2020J.txt)
#   We then pass the TextBroker the file we just found (ie 2020J.txt) an amount and the operator less
#   It will return a percentage that the amount is supposed to be taxed. 
# 
#  


import subprocess
import sys

temp = sys.argv[3]
Argument = temp.split()

#We combine the status and year to make a Key work to search for
file = Argument[2]+Argument[1]

#we call the texthandler with the file (Service.txt), a keyword (file), and operator (equal)
p = subprocess.run(['python', sys.argv[1], sys.argv[2], file,'equal'],capture_output=True, shell=True)

#We Take the raw output from p and clean it up so we get the tax file without newlines and '
r = p.stdout.decode()
r = r.rstrip()
r = r.replace("'","") 

#if it returns false it could not find the tax file and will send the error handler the correct error code
if r == "False":
    p = subprocess.run(['python',"ErrorHandle.py", '903',sys.argv[1], sys.argv[2]],capture_output=True, shell=True)

    #We Take the raw output from p and clean it up 
    r = p.stdout.decode()
    r = r.rstrip()
    r = r.replace("'","")
    print(r)
    sys.exit(0)


#we call the texthandler with the file (r), a keyword (amount), and operator (less)
p = subprocess.run(['python', sys.argv[1], r, Argument[3],'less'],capture_output=True, shell=True)

#We Take the raw output from p and clean it up so we get the perecentage without newlines and '
r = p.stdout.decode()
r = r.rstrip()
r = r.replace("'","") 

#We print out to the screen
print("Your amount "+ Argument[3] +" is taxed at " + r)

sys.exit