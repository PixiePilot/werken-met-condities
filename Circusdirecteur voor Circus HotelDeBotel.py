print(':----------------------------------------:')
print(':Circusdirecteur voor Circus HotelDeBotel:')
print(':              vacature                  :')
print(':----------------------------------------:')
#----------------------------------------------------
name = input('Wat is uw naam: ')
print('Perfect, de vragen beginnen nu.')
def praktijk():
    try:
         global a
         a = int((input)('Voer in hoeveel jaar u ervaring u heeft met dieren dresuur: '))
    except ValueError: # If user does not use INT value it will run the definition again.
        print('please input a value')
        praktijk()
praktijk()

if a < 4:
    print('Helaas, Je voeldoet niet aan de eisen')
    quit()
else:
    def praktijk2():
     try:    
            global b
            b = int((input)('Voer in hoeveel jaar u ervaring u heeft met jongleren?: '))
     except ValueError: # If user does not use INT value it will run the definition again.
        print('please input a value')
        praktijk2()
praktijk2()

if b < 5:
    print('Helaas, Je voeldoet niet aan de eisen')
    quit()
else:
    def praktijk3():
     try:    
            global c
            c = int((input)('Voer in hoeveel jaar u ervaring u heeft met praktijk acrobatiek?: '))
     except ValueError: # If user does not use INT value it will run the definition again.
        print('please input a value')
        praktijk3()
praktijk3()

if c < 3:
    print('Helaas, Je voeldoet niet aan de eisen')
    quit()
def mbo():
    global d
    d = input('bent u in bezit van een mbo4 diploma?: ')
    if d == 'nee':
        print('helaas je voldoet niet aan de eisen')
        quit()
    elif d == 'ja':
        print('')
    
    else:
        print('voer alstublieft ja of nee in')
        mbo()
    
mbo()

def vrachtwagen():
    global f
    f = input('bent u in bezit Vrachtwagen rijbewijs?: ')
    if f == 'nee':
        print('helaas je voldoet niet aan de eisen')
        quit()
    elif f == 'ja':
        print('')
    
    else:
        print('voer alstublieft ja of nee in')
        vrachtwagen()
vrachtwagen()

def hoed():
    global g
    g = input('bent u In bezit van een hoge hoed?: ')
    if g == 'nee':
        print('helaas je voldoet niet aan de eisen')
        quit()
    elif g == 'ja':
        print('')
    
    else:
        print('voer alstublieft ja of nee in')
        hoed()
hoed()

def Geenname():
    gender = input('ben u een man of vrouw?: ')
    if gender == 'man':
        print('man')

        snor = int((input) ('Hoe lang is uw snor als u er geen heeft voer 0 in: '))
        if snor < 10:
                print('helaas, u voldoet niet aan de eisen')
                
          
        elif snor > 10:
                global h # note to me, Remember !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                h = True


    elif gender == 'vrouw':
        antwoord = input('Heeft u rood krulhaar: ')
        if antwoord == 'ja':
            haar = int((input)('hoe lang is uw krulhaar?: '))
            if haar < 20:
                print('Helaas, U voldoet niet aan de eisen')
                quit()
            elif haar > 19:
                global t
                t = True #Note to me, Remember!!!!!!!!!!!!!!!!!!!!!!!!!!!
        elif antwoord == 'nee':
            print('u voldoet niet aan de eisen')
            quit()
        else:
            print('Voer alstublieft ja of nee in')
            Geenname()
Geenname()
def lengthdef():
    try:
        length = int((input)('Wat is je lengte?: '))
        if length < 150:
            print('Je voldoet niet aan de eisen.')
        
        elif length > 150:
            global r
            r = True
    except ValueError:
        print('Voer een nummer in alstublieft')
        lengthdef()
lengthdef() 
def weight():
    try:
        weightv = int((input)('Wat is je gewicht?: '))
        if weightv < 150:
            print('Je voldoet niet aan de eisen.')
        
        elif weightv > 150:
            global e
            e = True
    except ValueError:
        print('Voer een nummer in alstublieft')
        weight()
weight() 
ab = input('Wat is het raarste verhaal in uw leven?: ')
abc = input('Wat is het meeste beschaamde ding daat u heeft gedaan?: ')
abcd = input('Wat is het stouste als u als kind heeft gedaan?: ')
abcde = input('Waarom wilt u hier werken?: ')

