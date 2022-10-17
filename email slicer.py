def main():
    print('Welcome to Email slicer')
    print('')
    email=input('Email:')

    (username, domain)=email.split('@')
    (domain, extension)=domain.split('.')
    print('username :',username)
    print('domain :',domain)
    print('extension :',extension)
if __name__ == '__main__':
    main()