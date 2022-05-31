#File: Translate.py
#Author: Frederick ROddy
#Paramaters: Takes in Takes in 4 command line arguments after calling the program
#Useage: This program is used to display a translated word depending on language. It calls the textbroker (sys.argv[1])
#  and looks for the language file in service.txt (sys.argv[2]) using key [Argument[1]] and operator equal.
#  If i returns false then it sends it to the error handler with a 805 error
#  If it comes back as true Then it calls the textbroker again with the file that was found, the word to look up 
#  Argument [2] and the operator equal.
#  If that comes back false it will call the error handler with the key 813 



import subprocess
import sys

temp = sys.argv[3]
Argument = temp.split()

#we call the texthandler with the file (Service.txt), a keyword (language), and operator (equal)
p = subprocess.run(['python', sys.argv[1], sys.argv[2], Argument[1],'equal'],capture_output=True, shell=True)

#We Take the raw output from p and clean it up 
r = p.stdout.decode()
r = r.rstrip()
r = r.replace("'","") #this just takes the MainSB file location and strip newlines and '


#if it returns false it could not find the language file and will send the error handler the correct error code
if r == "False":
    p = subprocess.run(['python',"ErrorHandle.py", '805',sys.argv[1], sys.argv[2]],capture_output=True, shell=True)

    #We Take the raw output from p and clean it up 
    r = p.stdout.decode()
    r = r.rstrip()
    r = r.replace("'","")
    print(r)
    sys.exit()
    


#we call the texthandler with the file (R), a keyword (The work), and operator (equal)
p = subprocess.run(['python', sys.argv[1], r, Argument[2],'equal'],capture_output=True, shell=True)

#We Take the raw output from p and clean it up 
r = p.stdout.decode()
r = r.rstrip()
r = r.replace("'","") #this just takes the MainSB file location and strip newlines and '

#if it returns false it could not find the word and will send the error handler the correct error code
if r == "False":
    p = subprocess.run(['python',"ErrorHandle.py", '813',sys.argv[1], sys.argv[2]],capture_output=True, shell=True)

    #We Take the raw output from p and clean it up 
    r = p.stdout.decode()
    r = r.rstrip()
    r = r.replace("'","")
    print(r)
    sys.exit()

print("Your word " +Argument[2] + ' is ' + r)

sys.exit()