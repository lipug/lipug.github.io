# There are multiple ways of specifying Unicode code points in Python 3. The following are all equivalent:

>>> (
...     'a' ==
...     '\141' ==
...     '\x61' ==
...     '\N{LATIN SMALL LETTER A}' ==
...     '\u0061' ==
...     '\U00000061'
... )
True


# Not all representations are equal though. For example: `'\xNN'` can only specify a 2-digit code point. 
# `'\Unnnnnnnn'` is the only escape sequence that can specify every Unicode code point.

# UTF-8 isn't the only encoding you're likely to come across in the wild. Two other Unicode encodings 
# are UTF-16 and UTF-32. The encoding for these are not compatible, encoding in one and decoding 
# in the other will not work:

>>> letters = "αβγδ"
>>> rawdata = letters.encode("utf-8")
>>> rawdata.decode("utf-8")
'αβγδ'
>>> rawdata.decode("utf-16")  # 😧
'뇎닎돎듎'


# Python 3 provides a custom encoding called "unicode-escape". 
# This encoding allows you to encode a string to its Unicode code point.


>>> '€'.encode('unicode-escape')
b'\\u20ac'
>>> '🐍'.encode('unicode-escape')
b'\\U0001f40d'
>>> 'café'.encode('unicode-escape')
b'caf\\xe9'
>>> 'é'.encode('unicode-escape')
b'\\xe9'


# This encoding can be useful for storing Unicode strings in an ASCII compatible format. 
# The ASCII can then be converted back by taking the representation of the data.
