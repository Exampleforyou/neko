from py3pin.Pinterest import Pinterest
import json
import nekos
import random

def lox():
    pinterest = Pinterest(email='xnoving@gmail.com', password='Adgjl1357', username='xnoving', cred_root='logs/')

    search_batch = pinterest.search(query='neko chan', scope='pins')
    print(search_batch)

    neko = nekos.img(target='neko')
    print(neko)
def sak_suck():
    print('da')
