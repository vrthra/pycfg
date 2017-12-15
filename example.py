#!/usr/bin/env python3
# This is the CGI decode function as shown in the course

hex_values = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

def cgi_decode(s):
    t = ""
    i = 0
    while i < len(s):
        c = s[i]
        if c == '+':
            t = t + ' '
        elif c == '%':
            digit_high = s[i + 1]
            digit_low  = s[i + 2]
            i = i + 2
            if digit_high in hex_values and digit_low in hex_values:
                v = hex_values[digit_high] * 16 + hex_values[digit_low]
                t = t + chr(v)
            else:
                return None
        else:
            t = t + c
        i = i + 1
    return t

def dots(var):
    return var

def triangle(a, b, c):
    if a == b:
        if b == c:
            return 'Equilateral'
        else:
            return 'Isosceless'
    else:
        if b == c:
            return "Isosceles"
        else:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"

def main(var):
    r = cgi_decode(var)
    v = r.split(' ')
    x = dots(var) + triangle(int(v[0]), int(v[1]), int(v[2]))
    print(x)

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
