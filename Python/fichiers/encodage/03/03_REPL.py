# 03_REPL.py

>>> number = 539
>>> f'{number}'
'539'
>>> f'{number:0b}'
'1000011011'
>>> f'{number:0o}'
'1033'
>>> f'{number:0x}'
'21b'
>>> f'{number:0X}'
'21B'
>>> int('539')
539
>>> int('539', base=16)
1337
>>> int('539', base=2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 2: '539'
>>> int('11', base=2)
3
>>> 0x21B
539
>>> 0o1033
539
>>> 0b01000011011
539
>>> " ".join(f'{ord(digit):08b}' for digit in str(number))
'00110101 00110011 00111001'
