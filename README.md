amtBonusScript
==============

Python script for automated bonusing of Amazon Mechanical Turk workers.

Pre-requisites: You need Amazon Command Line Tools installed and working.

Instructions are given in comments at the top of the script file. Please contact me at dco-at-stanford.edu with bug reports, suggestions for improvements in functionality and/or clarity, offers of help (e.g. porting to Windows), etc. Thanks!

### Known Bugs:
  - do not include ! in your bonus message, nor inverted commas like "


### Possible issues:
  - the output log file is written for OS X / Unix file systems; I'm not sure if it'll work perfectly on Windows.
  - I might automate exporting JAVA_HOME in a next update.
  - Also, having everything start with the same prefix (filename) is annonying when typing. I'll think about a way to fix this while retaining uniqueness of filenames.


### Notes:
  - longest bonus message that worked so far is 485 characters long.


### Problems and solutions:
- Problem: if you get the following error message:

> An error occurred: Error #1 for RequestId: XXXXX - AWS.MechanicalTurk.AssignmentDoesNotExist: Assignment XXXXX does not exist. (XXXXX)

> com.amazonaws.mturk.service.exception.ObjectDoesNotExistException: Error #1 for RequestId: XXXXX - AWS.MechanicalTurk.AssignmentDoesNotExist: Assignment XXXXX does not exist. (XXXXX)

   Solution: Check your requester credentials in the bin/mturk.properties file



###### Change Log

v1.1, Jul 15 2013
 - Made unique filenames (i.e. file will be filename + "-bonusScript.sh")
 - Added summary stats after creating the bash script:
    - statistics of number of participants processed and their bonus amounts. The script outputs a message with how much you would need to add to your AMT requester account to pay for the bonuses.
 - Added logging to an output file. 

v1.0
 - basic functionality: took in a file name, wrote out a bunch of bonus commands to a bash script file

