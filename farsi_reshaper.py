import reshaper

if __name__ == '__main__':
    reshaper.print_info()
    while True:
        try:
            text = input('Enter a line to reshape: ')
            reshaper.reshape(text)
            print('Reshaped and copied!')
        except (KeyboardInterrupt, EOFError):
            print('\nThanks for using :)')
            break
