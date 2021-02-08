# 02_REPL.py

# The builtin Python `string` module includes several constants that categorized ASCII text:

# From lib/python3.7/string.py

# whitespace = ' \t\n\r\v\f'
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_letters = ascii_lowercase + ascii_uppercase
# digits = '0123456789'
# hexdigits = digits + 'abcdef' + 'ABCDEF'
# octdigits = '01234567'
# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
# printable = digits + ascii_letters + punctuation + whitespace


>>> import string
>>> question = "What's wrong with ASCII?!?!? !?!?!"
>>> question.rstrip( string.punctuation + string.whitespace )
"What's wrong with ASCII"
>>> question.isascii()
True
>>> question.isprintable()
True
>>> blanks = ' \t \n'
>>> blanks.isprintable()
False
>>> string.printable
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
>>> string.printable.isprintable()
False