# 05_REPL.py

>>> from points import hex_code_points
>>> place = 'café'
>>> hex_code_points(place)
'0063 0061 0066 00e9'
>>> place = 'caf\u00E9'
>>> place
'café'
>>> hex_code_points(place)
'0063 0061 0066 00e9'
>>> letter = '\u00E9'
>>> letter
'é'
>>> letter.encode('utf-8')
b'\xc3\xa9'
>>> hex_code_points('‡')
'2021'
>>> '\u2021'
'‡'
>>> '‡'.encode('utf-8')
b'\xe2\x80\xa1'
>>> hex_code_points('🐍')
'1f40d'
>>> '\U0001F40D'
'🐍'
>>> '🐍'.encode('utf-8')
b'\xf0\x9f\x90\x8d'