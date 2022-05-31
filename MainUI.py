#File: MainUi.py
#Author: Frederick Roddy 
#Paramaters: Takes in 3 (for translate) or 4 (for taxes) command line arguments after calling the program
#Useage:This program is used to simulate the UI that a user would use. 
#   We define where our textbroker and service.Txt files is so we do not have to hard code them 
#   It checks to make sure that there are enough arguments to go to the MainSB program. 
#   Combines the arguments after the program and combines it into a single string
#   It then Calls Textbroker to find where the MainSB file is located
#   It passes everthing after MainUI to the the MainSB file


import subprocess
import sys

#We define the values here so we can change them once and it propegrates across the programs
TB = "TextBroker.py"
SF = "Service.Txt"



#Checks to make sure we have enough arguments
if len(sys.argv) < 2:
    p = subprocess.run(['python',TB,SF,"ErrorHandle.py", "703"],capture_output=True, shell=True)
    print(p.stdout.decode())
    sys.exit()
    
    
#We take all the sys.argv and combine it into a single string with spaces as it is typed without ' and MainUi.py
ArgTwo = ""

for i in range(1,len(sys.argv)) :
    ArgTwo = ArgTwo +" " + sys.argv[i]

ArgTwo = ArgTwo.replace("'","")


#We call the text broker to find the main service broker file
f = subprocess.run(['python', TB,SF,'MainSB','equal'],capture_output=True, shell=True)

#We Take the raw output from f and clean it up so we get MainSB.py without newlines and '
r = f.stdout.decode()
r = r.rstrip()
r = r.replace("'","") 

#We call the main service broker with all of the commandline arguments besided 'python MainUI.py'
p = subprocess.run(['python', r, TB, SF ,ArgTwo],capture_output=True, shell=True)

print(p.stdout.decode())