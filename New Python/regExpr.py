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