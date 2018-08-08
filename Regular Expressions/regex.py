import re

# Write a Python program that matches a string that has an a followed by zero or more b's

pt = re.compile("ab*")

# Write a Python program that matches a string that has an a followed by one or more b's

pt = re.compile("ab+")

# Write a Python program that matches a string that has an a followed by zero or one 'b'

pt = re.compile("ab{0,1}")

# Write a Python program that matches a string that has an a followed by three 'b'

pt = re.compile("ab{3}")

# Write a Python program that matches a string that has an a followed by two to three 'b'

pt = re.compile("ab{2,3}")

# Write a Python program to find sequences of lowercase letters joined with a underscore

pt = re.compile("^[a-z]+_[a-z]+$")

# Write a Python program to find sequences of one upper case letter followed by lower case letters

pt = re.compile("^[A-Z]{1}[a-z]+$")

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'

pt = re.compile("^a.*b$")

# Write a Python program that matches a word at the beginning of a string

pt = re.compile("^\\w")

# Write a Python program that matches a word at end of string, with optional punctuation

pt = re.compile("\\w+\\S*$")

# Write a Python program that matches a word containing 'z'

pt = re.compile("z", re.IGNORECASE)

# Write a Python program that matches a word containing 'z', not start or end of the word. (Revise)

pt = re.compile("\\Bz\\B")

# Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores

pt = re.compile("^[A-Za-z0-9_]*$")

# Write a Python program where a string will start with a specific number.

pt = re.compile("^5")

# Write a Python program to remove leading zeros from an IP address.

pt = re.compile("\\.0*")
pt.sub(".","192.09.60.007")

# Write a Python program to check for a number at the end of a string.
pt = re.compile(".*[0-9]$")

# Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

pt = re.compile("[0-9]{1,3}")
pt.findall("Exercises number 1, 12, 13, and 345 are important")

"""
Write a Python program to search some literals strings in a string
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'
"""

for pattern in ['fox', 'dog', 'horse']:
    pt = re.compile(pattern)
    pt_ob = pt.search("The quick brown fox jumps over the lazy dog.")
    if pt_ob:
        print("The '{}' animal found at location {} to {} in the string".format(pattern, 
                                                                                pt_ob.start(),
                                                                                pt_ob.end() 
                                                                            ))


"""
Write a Python program to find the substrings within a string
Sample text :

'Python exercises, PHP exercises, C# exercises'

Pattern :

'exercises'
"""

pt = re.compile("exercises")
for x in pt.finditer("Python exercises, PHP exercises, C# exercises"):
    print("The word 'exercises' was found at {} to {}".format(x.start(), x.end()))

# Write a Python program to replace whitespaces with an underscore and vice versa

pt = re.compile("\\s")
pt.sub("_","My name is Khan")

pt = re.compile("_")
pt.sub(" ","My name is Khan")

# Write a Python program to extract year, month and date from a an url

date = re.compile("/(\d{4})/(\d{2})/(\d{2})/")
print(date.findall("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"))

# Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format

date = re.compile("(\\d{4})-(\\d{2})-(\\d{2})")
date_brk = date.findall("2018-08-09")
final_date = date_brk[0][0]+'-'+date_brk[0][2]+'-'+date_brk[0][1]

# Write a Python program to match if two words from a list of words starting with letter 'P'

words = ['Python PHP','Javascript','C++']
for word in words:
    pt = re.search("(p\\w+)\\W(p\\w+)", word, flags=2)
    if pt:
        print(pt.groups())

# Write a Python program to separate and print the numbers of a given string

pt = re.compile("[0-9]+")
pt = re.compile("\d+")
pt.findall("1st of July 1998 was an important year for 10 people")

#Write a Python program to find all words starting with 'a' or 'e' in a given string.

pt = re.compile("[ae]\\w+")
pt.findall("This is an example")

# Write a Python program to abbreviate 'Road' as 'Rd.' in a given string
pt = re.compile("road", flags=2)
pt.sub("Rd.", "Take the left Road turn to Mumbai Road")

# Write a Python program to replace all occurrences of space, comma, or dot with a colon

pt = re.compile("[ ,\\.]")
pt.sub(":","This, is a dark hour.")

# Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.

pt = re.compile("[ ,.]")
pt.sub(":", "This, is a dark hour.", count=2)

# Write a Python program to find all five characters long word in a string.

pt = re.compile("\\b\\w{5}\\b")
pt.findall("This is the story of Harry Potter and the Prisoner of Azkaban")

# Write a Python program to find all three, four, five characters long words in a string.

pt = re.compile("\\b\\w{3,5}\\b")
pt.findall("This is the story of Harry Potter and the Prisoner of Azkaban")

# Write a Python program to find all words which are at least 4 characters long in a string.
pt = re.compile("\\b\\w{4,}\\b")
pt.findall("This is the story of Harry Potter and the Prisoner of Azkaban")

# Write a python program to convert snake case string to camel case string.
# example HarryPotterAndThePrisonerOfAzkaban to Harry_Potter_And_The_Prisoner_Of_Azkaban

pt = re.compile("(.)([A-Z][a-z]+)")
str1 = pt.sub(r"\1_\2", "HarryPotterAndThePrisonerOfAzkaban")
print(re.sub("([a-z0-9])([A-Z])", r"\1_\2", str1))
