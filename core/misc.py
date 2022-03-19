from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from random import choice

chars=ascii_letters+ascii_lowercase+ascii_uppercase+digits

def gen_token():
    t=''
    for a in range(15):
        t+=choice(chars)
    return  t
