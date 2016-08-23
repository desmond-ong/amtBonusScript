amtBonusScript
==============

Python script for automated bonusing of Amazon Mechanical Turk workers.

Pre-requisites: You need Amazon Command Line Tools installed and working.

Instructions are given in comments at the top of the script file. Please contact me at dco (at) stanford (dot) edu with bug reports, suggestions for improvements in functionality and/or clarity, offers of help (e.g. porting to Windows), etc. Thanks!

#### Format for filename: a csv file with:
  - AssignmentID (*not* HIT ID) in the first column,
  - workerID in the second column,
  - and bonus amount in the third column (in dollars, no dollar sign).

E.g.

AssignmentID |  WorkerID | Bonus
--- | --- | ---
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  | AAAAAAAAAAAAAA  | 0.5
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY  | BBBBBBBBBBBBBB  | 0.27


## Known Bugs:
  - do not include ! in your bonus message, nor inverted commas like "
  - Java Runtime Environment (JRE 8 Update 51) breaks Command Line Tools, and back-dating to at least JRE 8 Update 45 (which you can download here: http://www.oracle.com/technetwork/java/javase/downloads/java-archive-javase8-2177648.html ) will fix CLT.


## Possible issues:
  - the output log file is written for OS X / Unix file systems; I'm not sure if it'll work perfectly on Windows.
  - I might automate exporting JAVA_HOME in a next update.
  - Also, having everything start with the same prefix (filename) is annonying when typing. I'll think about a way to fix this while retaining uniqueness of filenames.


## Notes:
  - longest bonus message that worked so far is 485 characters long.
  - As of 21 July 2015, Amazon has implemented a new commission structure. Prior, the fee that requesters paid to Amazon was a flat 10% (which includes bonuses). Thus if you bonused a worker $1.00, you would have to pay Amazon $0.10. (Assuming you don't use Masters or other qualifications). After 21 July 2015, it's 20% ~~(if you have less than 10 assignments) or 40% (if you have 10 or more assignments).~~
  - Note added 4 Aug 2016: apparently the commission on bonuses is a flat 20% regardless of # of subjects. I have changed the comment in the bonusScript to reflect that (it doesn't change the functionality at all; just the "helpful" message that it prints out at the end.)

## Problems and solutions:
* Problem: if you get the following error message:

> An error occurred: Error #1 for RequestId: XXXXX - AWS.MechanicalTurk.AssignmentDoesNotExist: Assignment XXXXX does not exist. (XXXXX)

> com.amazonaws.mturk.service.exception.ObjectDoesNotExistException: Error #1 for RequestId: XXXXX - AWS.MechanicalTurk.AssignmentDoesNotExist: Assignment XXXXX does not exist. (XXXXX)

* Solution: Check your requester credentials in the bin/mturk.properties file



## Change Log

v1.2, Jul 22, 2015
 - updated calculation to incorporate new AMT commission structure (40% on HITs with >10 assignments, 20% otherwise)

v1.1, Jul 15, 2013
 - Made unique filenames (i.e. file will be filename + "-bonusScript.sh")
 - Added summary stats after creating the bash script:
    - statistics of number of participants processed and their bonus amounts. The script outputs a message with how much you would need to add to your AMT requester account to pay for the bonuses.
 - Added logging to an output file. 

v1.0
 - basic functionality: took in a file name, wrote out a bunch of bonus commands to a bash script file

