# show.py
def code_points(message):
    for character in message:
        code_point = ord(character)
        print( f'{code_point:4} ', end='')

    print()