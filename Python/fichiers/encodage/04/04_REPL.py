>>> 'hello'.encode('utf-8')
b'hello'
>>> 'café'.encode('utf-8')
b'caf\xc3\xa9'
>>> 'é'.encode('utf-8')
b'\xc3\xa9'
>>> '€'.encode('utf-8')
b'\xe2\x82\xac'
>>> b'caf\xc3\xa9'.decode('utf-8')
'café'