# create regex for phone
#create regex for email
#get text from clip board
#Extract data
#copy data to clipboard

import re, pyperclip

phoneRegEx = re.compile(r'''(               # there are many groups so added brackets to whole expression to make it one big group which is group 0 (first group)
                                            # as findall() returns tuples if there are more than one group
           ((\d\d\d) | (\(\d\d\d)\))?       #area code optional e.g 345 or (345) or no area code
           (\s|-)                           #dash e.g. space or dash
           \d\d\d                           #first 3 digits e.g. 345
           -                                #dash e.g. dash
           \d\d\d\d                         #last 4 digits e.g. 6789
           (((ext(\.)?\s)|x)                #ext words e.g.ext ext. extx
            (\d{2-5}))? )                    #ext nums e.g. 23 235 2345 23456 or no extension
           ''', re.VERBOSE)

emailRegEx = re.compile(r'''
           [a-zA-z0-9_.+]+                  #name
           @                                # @
           [a-zA-z0-9_.+]+                  #domain name
           ''', re.VERBOSE)

text = pyperclip.paste()

numbers = phoneRegEx.findall(text)
emails = emailRegEx.findall(text)

allNumbers = []
for phoneNumber in numbers: 
    allNumbers.append(phoneNumber[0]) # need to extract the first index from the tuple as that contains the actual phone number

print(numbers)
print(allNumbers)
print(emails)

results = '\n'.join(allNumbers) + '\n' + '\n'.join(emails)

pyperclip.copy(results)