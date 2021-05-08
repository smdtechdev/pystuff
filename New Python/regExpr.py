import re

phoneRegEx = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegEx.search('my number is 0208-432-3242') # search() returns a match object
print(mo.group())

phoneRegEx = re.compile(r'(\d\d\d\d)-(\d\d\d-\d\d\d\d)') # brackets allow you define to group
mo = phoneRegEx.search('my number is 0208-432-3242')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

phoneRegEx = re.compile(r'\(\d\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneRegEx.search('my number is (0208) 432-3242')
print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

batRegex = re.compile(r'Bat(wo)?man') # adds a wo group, question mark means the group can appear 0 or 1 times in order to match the pattern i.e. its optional
mo = batRegex.search('The adv of Batman') # wo appears 0 times here so the pattern matches
print(mo.group())
mo = batRegex.search('The adv of Batwoman') # wo appears 1 time so the pattern matches
print(mo.group())
mo = batRegex.search('The adv of Batwowowoman') # wo appears 3 times so the pattern does not match
#print(mo.group())

batRegex = re.compile(r'Bat(wo)*man') # adds a wo group, star  means the group can appear 0 or more times in order to match the pattern i.e. its optional
mo = batRegex.search('The adv of Batman') # wo appears 0 times here so the pattern matches
mo = batRegex.search('The adv of Batman') # wo appears 0 times here so the pattern matches
print(mo.group())
mo = batRegex.search('The adv of Batwoman') # wo appears 1 time so the pattern matches
print(mo.group())
mo = batRegex.search('The adv of Batwowowowowowoman') # wo appears 3 times so the pattern still matches
print(mo.group())

myregex = re.compile(r'\+\*\?') #if you need to search for regex objects you can use \ to escape the character
mo = myregex.search('I learned about +*? regex')
print(mo.group())

myregex = re.compile(r'(\+\*\?)+') # + means the group can appear 1 or more times in order to match the pattern
mo = myregex.search('I learned about +*?+*?+*?+*? regex')
print(mo.group())

haregex = re.compile(r'(Ha){3}') # curly brackets means the group must apear x number of times in order to match the pattern
mo = haregex.search('He was like HaHaHa')
print(mo.group())

phoneRegEx = re.compile(r'((\d\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}') # matches 3 phone numbers in a row that could have a 4 digit area could and could be separated by comma
mo = phoneRegEx.search('my number is 0208-432-3242,453-3443,0207-234-2532')
print(mo.group())
mo = phoneRegEx.search('my number is 0208-432-3242453-34430207-234-2532')
print(mo.group())

haregex = re.compile(r'(Ha){3,5}') # curly brackets means the group must apear between x and y number of times in order to match the pattern {,3} means 0 to 3 {3,} means 3 plus 
mo = haregex.search('He was like HaHaHa')
print(mo.group())
mo = haregex.search('He was like HaHaHaHa')
print(mo.group())

digitregex = re.compile(r'(\d){3,5}')
mo = digitregex.search('123456789')
print(mo.group()) # this will print 12345 as by default the match is greedy so will match the largest possible string
digitregex = re.compile(r'(\d){3,5}?')
mo = digitregex.search('123456789')
print(mo.group()) # this will print 123 as the ? specifies a non greedy match which will match the smallest possible string

phoneRegEx = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
cv = '''A PowerShell profile in very simple terms, is a script that 0208-342-3423 is auto-executed (read runs) whenever you start a PowerShell session. Why is this important? Suppose, you work on SharePoint administration for your daily bread and butter. Everytime, you would want to execute some cmdlets based on SharePoint, you would need to load PSSnapin for SharePoint. Same goes for Azure. Who would want to login everytime whenever you want to run some Azure cmdlets and go through that annoying pop-up box. It’s a good idea to have some commands auto-executed whenever you want to open PowerShell session. PowerShell profile allows you to configure your environment in advance. In this blog post, we’ll discuss how to configure a PowerShell profile.

The first thing before you configure profile, is to check if a PowerShell profile is 0208-555-2134 already configured or not. This would be done by use of below command: '''
mo = phoneRegEx.search(cv)
print(mo.group()) # .search() will only return the first match
results = phoneRegEx.findall(cv)
print(results) # .findall() will return all matches in a list format not a match object

phoneRegEx = re.compile(r'(\d\d\d\d)-(\d\d\d-\d\d\d\d)')
results = phoneRegEx.findall(cv)
print(results) # if you specify groups findall() will split the matches into tuples

# Regex char classes
# /d digits 0-9
# /D any characters thats not a digit 0-9   
# /w any letter numeric digit or underscore
# /W any character that is not a letter numeric digit or underscore
# /s any space, tab or new line
# /S any character that is not a space tab or new line

bars = '5 drums drumming, 4 guns gunning, 3 drinks drinking, 2 gal galling, 1 me meeing inna pear tree'
barsregex = re.compile(r'\d+\s\w+') # one or more digits followed by a space followed by one or more words
result = barsregex.findall(bars)
print(result)

vowelregex = re.compile(r'[aeiouAEIOU]') # [] allow you to specify your own regex char class
result = vowelregex.findall('Shut your damn eating mouth Im A GAWD')
print(result)

vowelregex = re.compile(r'[aeiou]', re.I) # re.I means ignore case
result = vowelregex.findall('Shut your damn eating mouth Im A GAWD')
print(result)

vowelregex = re.compile(r'[aeiouAEIOU]{2}') # will match when exactle two vowels appear in a row
result = vowelregex.findall('Shut your damn eating mouth')
print(result)

constanantregex = re.compile(r'[^aeiouAEIOU]') # ^ (caret) means match everything not specified (including spaces, punctuation etc)
result = constanantregex.findall('Shut your damn eating mouth.')
print(result)

beginWithHiregex = re.compile(r'^Hello') # caret at beginning means it must appear at the begining of the string to match
mo = beginWithHiregex.search('Hello There')
print(mo.group())
print(mo == None)
mo = beginWithHiregex.search('There you are Hello') # does not match so the mo is set to None
print(mo == None)

endsWithHiregex = re.compile(r'Hello World!$') # dollar at the end means it must appear at the end of the string to match
mo = endsWithHiregex.search('Hello World!')
print(mo.group())
print(mo == None)
mo = endsWithHiregex.search('Hello World! YO') # does not match so the mo is set to None
print(mo == None)

allDigitsregex = re.compile(r'^\d+$') # ^abc$ means the entire string has to begin and end with the pattern to match in this case it must begin and end with 1 or more digit
mo = allDigitsregex.search('123456789')
print(mo.group())
print(mo == None)
mo = allDigitsregex.search('123456g789') # does not match as g is not a digit so the entire string does not begind AND end with the pattern. so the mo is set to None
print('is mo set to none: ' + str(mo == None))

atregex = re.compile(r'.at') # . means wildard or anything except newline - so anything that ends in at for this example
result = atregex.findall('The cat in the hat was chillin with a bat in a rata')
print(result)

nameregex = re.compile(r'First Name: (.*) Last Name: (.*)') # .* means everything - in this example we need to match first name: then return what ever is next - this is greedy
result = nameregex.findall('First Name: Boss Last Name: Man')
print(result)


text = '<To serve beef> for dinner.>'
nongreedyregex = re.compile(r'<(.*?)>') # this matches a less than then anything else until the first greater than
result = nongreedyregex.findall(text)
print(result)
greedyregex = re.compile(r'<(.*)>') # this matches a less than then anything else until the last greater than
result = greedyregex.findall(text)
print(result)

text = 'To serve beef.\nTo serve chicken.\nTo do a mazza.'
nongreedyregex = re.compile(r'.*') 
result = nongreedyregex.search(text)
print(result.group()) # this will only match whatever is before the first newline as .* does not match newline and is greedy
nongreedyregex = re.compile(r'.*', re.DOTALL) # re.DOTALL arg in complile means dots mean match truely everything
result = nongreedyregex.search(text)
print(result.group()) # this will print all lines of text

nameregex = re.compile(r'Agent \w+') # find Agent plus one or more words
results = nameregex.findall('Agent Alice spoke to Agent Bob')
print(results)
encresults = nameregex.sub('REDACTED', 'Agent Alice spoke to Agent Bob') # substitute any matches with another string in this case REDACTED 
print(encresults)

nameregex = re.compile(r'Agent (\w)\w*') # Match a single word after Agent followed by 0 or more words
results = nameregex.findall('Agent Alice spoke to Agent Bob')
print(results)
encresults = nameregex.sub(r'Agent \1*****', 'Agent Alice spoke to Agent Bob') # substitue any matches with the match in the first group (denoted by \1) and appended stars, use r(raw string) as we need a literal backslash
print(encresults)

telregex = re.compile(r'''
                      \d\d\d\d  #area code
                      -         #first dash
                      \d\d\d    #first set of digits
                      -         #second dash
                      \d\d\d\d  #last set of digits ''', re.VERBOSE | re.DOTALL | re.IGNORECASE) # verbose allows you to add spaces and comments to make longer REx more readable
mo = telregex.findall('my number is 0208-345-3452 my other number is 0207-342-2421')
print(mo)