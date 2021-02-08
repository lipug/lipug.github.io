# 06_REPL.py
"""
The Unicode standard allows for the combination of characters into a single glyph. 
This is used for applying accents to characters and changing the skin tone of an emoji.

Some kinds of common diagraphs, or letter combinations, have their own code point, 
like æ. Others require the combination of two code points.
"""

>>> '\u00E6'
'æ'
>>> '\u0928'
'न'
>>> '\u0928\u093f'
'नि'
>>> '\u093f'
'ि'
>>> '\U0001F596'
'🖖'
>>> '\U0001F596\U0001F3FB'
'🖖🏻'
>>> '\U0001F596\U0001F3FC'
'🖖🏼'
>>> '\U0001F596\U0001F3FD'
'🖖🏽'
>>> '\U0001F596\U0001F3FE'
'🖖🏾'
>>> '\U0001F596\U0001F3FF'
'🖖🏿'

"""
The Devangari script has characters that are combined to create new letters. 
The न character is a letter on its own, but it can be combined with the 'ि' character 
to create नि. A similar process is used to change the base Vulcan salute emoji into 
one of different skin tone.s

The ability to create combinations can be problematic. Most accented characters can 
be represented in two ways: with a single code point or a combined code point. 
Visually, both these situations look like the same glyph, but inside the string 
they are different: they aren't equal and even have different lengths.
"""

>>> goodbye = 'до свидáния'
>>> len(goodbye)
11
>>> departs = 'до свида́ния'
>>> len(departs)
12


>>> from points import hex_code_points
>>> hex_code_points(goodbye)
'0434 043e 0020 0441 0432 0438 0434 00e1 043d 0438 044f'
>>> hex_code_points(departs)
'0434 043e 0020 0441 0432 0438 0434 0430 0301 043d 0438 044f'
>>> '\u00e1'
'á'
>>> '\u0430\u0301'
'а́'

"""
Visually, both `goodbye` and `departs` appear to contain the same characters. 
The underlying representation is differnt though. The `departs` string uses 
two code points in a combined character to represent the accented "a". 
By contrast, the `goodbye` string uses a single code point accented "a". 
This difference can be dangerous and in DNS allows for the 
(IDN homgraph attack)[https://en.wikipedia.org/wiki/IDN_homograph_attack].
"""
