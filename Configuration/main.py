from configparser import ConfigParser

# create configparser object
parser = ConfigParser(inline_comment_prefixes = ('#'))

# reads the file
parser.read("audio.conf")

# get a particular config item
parser.get('General','MASTER')

# get all the main sections 
parser.sections()

# gets all items from a section in a tuple form
parser.items('General')