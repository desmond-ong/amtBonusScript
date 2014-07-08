amtBonusScript
==============

Python script for automated bonusing of Amazon Mechanical Turk workers

Instructions are given in comments at the top of the script file. Please contact me at dco-at-stanford.edu with bug reports, suggestions for improvements in functionality and/or clarity, offers of help (e.g. porting to Windows), etc. Thanks!

Possible issues:
  - the output log file is written for OS X / Unix file systems; I'm not sure if it'll work perfectly on Windows.
  - I might automate exporting JAVA_HOME in a next release.
  - Also, having everything start with the same prefix (filename) is annonying when typing. I'll think about a way to fix this while retaining uniqueness of filenames.


Change Log
v1.1
 - Made unique filenames (i.e. file will be filename + "-bonusScript.sh")
 - Added summary stats after creating the bash script:
 - how many people with how much bonus
 - Added logging to an output file. 

v1.0
 - basic functionality: took in a file name, wrote out a bunch of bonus commands to a bash script file

