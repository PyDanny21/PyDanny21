def cedis_to_dollars():
    print('Welcome to Py-Convertor')
    print('')
    cedis=eval(input('Enter amount in cedis:'))
    dollars=convert_to_dollars(cedis)
    print('This is','$',dollars)
    print('')

convert_to_dollars = lambda cedis: cedis/12.3

def dollars_to_cedis():
    print('Welcome to Py-Convertor')
    print('')
    dollars=eval(input('Enter amount in dollars:'))
    cedis=convert_to_cedis(dollars)
    print('This is','$',cedis)
    print('')

convert_to_cedis = lambda dollars: dollars*12.3


if __name__ == '__main__':
    while(True):
        currency=str(input('Enter Currency:'))
        if currency=='dollars to cedis':
            dollars_to_cedis()
        elif currency=='cedis to dollars':
            cedis_to_dollars()
