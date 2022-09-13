from run_address_book import run_address_book
from run_notebook import run_notebook

def main():
    while True:
        line = input("Enter your option: ")
        match line:
            case '1':
                run_notebook()
            case '2':
                run_address_book()
            case '3':
                print('RUN CLEANER')
            case '4':
                break
            case _:
                print('Wrong command')
                
main()