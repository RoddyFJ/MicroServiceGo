#File: MainSB.py
#Author: Frederick ROddy
#Paramaters: Takes in Takes in 3 (for translate) or 4 (for taxes) command line arguments after calling the program
#Useage: This program is used to chose which module we call for our other service (Tax and Translate)
#   We Combine all the command line arguments and combine it into an array
#   We pass the third array variable (Tax or Translate) To the first array variable (TextBroker.py) With the second 
#       array variable (service.txt) with a value equal
#   We determin if it is calling a java or python file and codes the subprocess correctly
#   It calls the correct subprcocess (tax.py or translate.py with the correct parameters)

import sys
import subprocess

#We take the command line argument and turn it into a list with each argument being one of the. 
temp = sys.argv[3]
Argument = temp.split()

#We take all the sys.argv and combine it into a single string with spaces as it is typed without ' and MainSB.py
ArgTwo = ""
for i in range(3,len(sys.argv)) :
    ArgTwo = ArgTwo +" '" + sys.argv[i]

ArgTwo = ArgTwo[3:].replace("'","")


#We use try/Except so if something goes wrong we can send it to the error handler without it crashing
try:
    #We call the text broker to find the main service broker file using the keywork Tax/Translate/etc
    f = subprocess.run(['python', sys.argv[1],sys.argv[2],Argument[0],'equal'],capture_output=True, shell=True)
    
    #We Take the raw output from f and clean it up so we get MainSB.py without newlines and '
    r = f.stdout.decode()
    r = r.rstrip()
    r = r.replace("'","")
    
    #we Determine if the file to be called is java or python and code it correctly for the next subprocess call
    languageToCall = ""
    if ".java" in r:
        languateToCall = "java"

    if ".py" in r:
        languateToCall = "python"    
    
    #We call the different SB's (Tax or translate) with the commandline arguments minus MainSB.py, It also passes
    #   the location to the textbrokr and the service.txt file to use later
   
    p = subprocess.run([languateToCall, r, sys.argv[1],sys.argv[2], ArgTwo],capture_output=True, shell=True)

    print(p.stdout.decode())
    
    #If it fails to do something it sends it to the error handler


except:
    #We call the error handler with the location to the textbrokr and the service.txt file as well as an error code
    p = subprocess.run(['python', "ErrorHandle.py",sys.argv[1],sys.argv[2], "703"],capture_output=True, shell=True)


    print(p.stdout.decode())
