"""This is a tool that will extract all the email addresses from a text file and write them to a new text file.
You should make sure that the email addresses are on their own line to make sure the regex will work."""

import re
import sys

emails = open('Emails.txt', 'w')
pasted = open(sys.argv[1], 'r')
rawText = pasted.read()
regex = r'.+@.+'
emailList = re.findall(regex, rawText)
for e in emailList:
    emails.write(e + '\n')
pasted.close()
emails.close()
