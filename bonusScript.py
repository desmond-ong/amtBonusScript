# Simple python code for automatically bonusing workers on mTurk.
# Written by Desmond Ong (github.com/desmond-ong), 15 July 2013. Send comments to dco@stanford.edu.
# version 1.2, updated Jul 22, 2015

# Instructions:
#   1) replace "filename" with the name of the input file,
#   2) write the bonus message to participants,
#   3) fill in the location where CLT is installed.
# Then
#   4) run "python bonusScript.py"
#		4b) Export your javahome if necessary
#   5) run "sh " filename "-bonusBashScript.sh"
#	6) check filename "-bonusResults" for any errors.
#
# Format for filename: a csv file with:
# AssignmentID (*not* HIT ID) in the first column,
# workerID in the second column,
# and bonus amount in the third column (in dollars, no dollar sign).
# E.g.
#
# AssignmentID   WorkerID    Bonus
# 2XXX11X1X1X1XXXXX1XXXXX1XXXXXX  X12XXXZXXXX73X  0.5
# 2XXX1XXXXX1XXXXXX1X1XXXXXXXXXX  X13XXX4X5XXX6X  0.27
#
#
# You may also need to export your javahome. First run:
# /usr/libexec/java_home
# then run, replacing the path on the RHS of the = with the output from the above command
# export JAVA_HOME=/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
#
# if you want to set the JAVA_HOME in your profile so that 
# it types that command for you automatically every time you start, edit:
#     ~/.bash_profile
# using your favorite editor (e.g. vim), and type that export line.
#    e.g. vim ~/.bash_profile
#       "i" for insert, type the export line, hit escape, then type :wq, and <return> to exit.
#
#
#
#
# --------------
# Change Log
# v1.2, Jul 22, 2015
#   - updated calculation to incorporate new AMT commission structure
#
# v1.1
#	- Made unique filenames (i.e. file will be filename + "-bonusScript.sh")
#   - Added summary stats after creating the bash script:
#		- how many people with how much bonus
#	- Added logging to an output file. 
#
# v1.0
#	- basic functionality: took in a file name, wrote out a bunch of bonus commands to a bash script file



filename = "exampleBonusFile.csv"
bonusMessage = "Bonus for doing my HIT :)"
locationofCLT = "/XXX/aws-mturk-clt-1.3.1"

import csv
import os
from decimal import Decimal

currentWD = os.getcwd() # gets the current working directory, to place the results file.

rowNum = 0
bonusTotal = 0
bonusPeople = 0
bonusScripts = ""

if filename.endswith('.csv'):
    outputFilename = filename[:-4]
else:
	outputFilename = filename

with open(filename, 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        if rowNum > 0: #skip the first row header
            if Decimal(row[2]) > 0:  # if bonus greater than 0
                bonusPeople += 1;
                bonusTotal += Decimal(row[2]);
                bonusScripts = bonusScripts + "./grantBonus.sh -workerid " + row[1] + " -amount " + row[2] + " -assignment " + row[0] + " -reason " + "\"" + bonusMessage + "\" >> '" + currentWD + "/" + outputFilename + "-bonusResults' \n"
                bonusScripts = bonusScripts + "echo ' --done bonusing participant number " + str(bonusPeople) + "' \n"
        rowNum += 1

bonusScripts = bonusScripts + "echo 'Remember to check " + outputFilename + "-bonusResults for any errors!' \n"

if (bonusPeople<10):
    commission = 20
    bonusTotalWithCommission = round((bonusTotal * Decimal(1.20))*100, 1)/100
else:
    commission = 40
    bonusTotalWithCommission = round((bonusTotal * Decimal(1.40))*100, 1)/100

summaryMessage = "\n--- Done! Wrote a script for " + str(bonusPeople) + " participants with a total bonus amount of $" + str(bonusTotal) + " (excluding AMT comission).\n"
summaryMessage = summaryMessage + "With a " + str(commission) + "% commission, the total cost is probably $" + str(bonusTotalWithCommission) + "\n"
summaryMessage = summaryMessage + "Run: sh " + outputFilename + "-bonusBashScript.sh (Be sure to have your JAVA_HOME set!)" + "\n"
summaryMessage = summaryMessage + "After running the script, console output will be copied to " + outputFilename + "-bonusResults" + "\n"
print(summaryMessage)

#write the bash script for running the bonus commands
outputFilename = outputFilename + "-bonusBashScript.sh"
bonusBashScript = open(outputFilename, 'w')
bonusBashScript.write("#!/usr/bin/env sh\npushd " + locationofCLT + "/bin\n" + bonusScripts + "popd")
bonusBashScript.close()
