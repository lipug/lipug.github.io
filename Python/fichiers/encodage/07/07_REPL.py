# 07_REPL.py

>>> # ascii() -- repr() compatible string representation 
>>> ascii('abcd')
"'abcd'"
>>> ascii('café')
"'caf\\xe9'"
>>> ascii(0xE6)
'230'
>>> # bin() -- string representation of binary number
>>> bin(0)
'0b0'
>>> bin(9)
'0b1001'
>>> bin(0xE6)
'0b11100110'
>>> # bytes() -- -- returns raw byte data
>>> # input can be iterable, string, or integer
>>> bytes((104, 101, 108, 108, 111))
b'hello'
>>> bytes(range(97, 123))
b'abcdefghijklmnopqrstuvwxyz'
>>> bytes('Real 🐍', 'utf-8')
b'Real \xf0\x9f\x90\x8d'
>>> bytes(5)
b'\x00\x00\x00\x00\x00'
>>> bytes.fromhex('c0 ff ee')
b'\xc0\xff\xee'
>>> bytes.fromhex('68 65 6C 6C 6F')
b'hello'
>>> # chr() -- converts integer code point to Unicode character
>>> chr(97)
'a'
>>> chr(7048)
'ᮈ'
>>> chr(128013)
'🐍'
>>> chr(0x1F40D)
'🐍'
>>> chr(0b01100001)
'a'
>>> # hex() -- string representation of hexadecimal number 
>>> hex(104)
'0x68'
>>> # int() -- returns int, can specify the base of the input
>>> int(11)
11
>>> int(11.1)
11
>>> int('11')
11
>>> int('11', base=2)
3
>>> int('11', base=8)
9
>>> int('11', base=16)
17
>>> int(0x1F40E - 1)
128013
>>> int.from_bytes(b'\x00\x10', byteorder='big')
16
>>> int.from_bytes(b'\x00\x10', byteorder='little')
4096
>>> # ord() -- converts Unicode character to integer code point
>>> ord('a')
97
>>> ord('🐍')
128013
>>> # str() -- converts input to string
>>> str('text is fun')
'text is fun'
>>> str(5)
'5'
>>> str(0xE6)
'230'
>>> str(b'caf\xC3\xA9', 'utf-8')
'café'