vraag = input('is de kaas geel? ')

if vraag == 'ja':
    vraag = input('Zitten er gaten in ')
    if vraag == 'ja':
        vraag = input('is de kaas belachelijk duur? ')
        if vraag == 'ja':
            print('Emmenthaler')
    elif vraag == 'no':
        vraag = input('is de kaas hard als steen ')
        if vraag == 'ja':
            print('Pamigiano reggiano')
        elif vraag == 'no':
            print('Goudse kaas')


if vraag == 'no':
    vraag = input('Heeft de kaas blauwe schimmel? ')
    if vraag == 'ja':
         vraag = input('Heeft de kaas een korts?')
         if vraag == 'ja':
             print('bleu de rochbaron')
         elif vraag == 'no':
             print('Foume d\'Ambert')
if vraag == 'no':
    vraag = input('Heeft de kaas een korst?')
    if vraag == 'yes':
        print('Camembert')
    elif vraag == 'no':
        print('Mozzarella')

