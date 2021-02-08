# points.py
def hex_code_points(message):
    return " ".join([f'{ord(letter):04x}' for letter in message])