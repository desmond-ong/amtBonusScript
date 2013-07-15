# Simple python code for automatically bonusing workers on mTurk.
# Written by Desmond Ong, 15 July 2013. Send comments to dco@stanford.edu.

# Instructions:
#   1) replace "filename" with the name of the input file,
#   2) write the bonus message to participants,
#   3) fill in the location where CLT is installed.
# Then
#   4) run "python bonusScript.py"
#   5) run "sh bonusBashScript.sh"

# You may also need to export your javahome. First run:
# /usr/libexec/java_home
# then run, replacing the path on the RHS of the = with the output from the above command
# export JAVA_HOME=/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home


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

filename = "xxx_bonus.csv"
bonusMessage = "Bonus for doing my HIT :)"
locationofCLT = "/XXX/aws-mturk-clt-1.3.1"

import csv

rowNum = 0
bonusScripts = ""

with open(filename, 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        if rowNum > 0:
            if row[2] > 0:  # if bonus greater than 0
                bonusScripts = bonusScripts + "./grantBonus.sh -workerid " + row[1] + " -amount " + row[2] + " -assignment " + row[0] + " -reason " + "\"" + bonusMessage + "\" \n"
        rowNum += 1


#write the bash script for running the bonus commands
bonusBashScript = open("bonusBashScript.sh", 'w')
bonusBashScript.write("#!/usr/bin/env sh\npushd " + locationofCLT + "/bin\n" + bonusScripts + "popd")
bonusBashScript.close()
