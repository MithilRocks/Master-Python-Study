# All main re definitions
import re

# this matches only at beginning. Returns None otherwise
x = re.match("an", "anand")
print(x.start(), x.end())

# this matches at any point in the string just once
y = re.search("na", "anand")
print(y.start(), y.end())

# this returns all matches in a list
z = re.findall("a", "anand")
print(z)

# this returns all matches in the form of an iterable.
# the iterable is a collection of sre objects
a = re.finditer("a", "anand")
for i in a:
    print(i.start(), i.end())

# splits at the specified pattern and returns a list.
# you can specify how many splits to make
b = re.split("an", "andAN", 1, flags=2)
print(b)

# replace pattern with string. specify count to how many times to replace
c = re.sub("an", "1", "anand", 1)
print(c)

# no difference from sub. just that it returns a tuple (new_string, count).
# count is number of substitutions made
d = re.subn("a", "1", "anand")
print(d)

# using flags, we can ignore case
# in this case flags=2 should be used
e = re.match("a", "Anand", flags=2)
print(e.start(), e.end())

# same as before. just a different way
f = re.match("a", "Anand", re.IGNORECASE)
print(f.start(), f.end())

# create an object of the regex expression.
# now we can use the above definitions in the object directly
g = re.compile("a")
print(g)
print(g.match("anand"))
print(g.split("anand"))
