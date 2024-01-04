import os
import webbrowser
from ContactBook import ContactBook
from Header import header
from NoteBook import NoteManager
from sort import FileSorter
from CryptoPrice import CryptoPriceFetcher

# ANSI escape codes for text coloring
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

def search_in_browser():
    query = input("Enter your search query: ")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def main():
    notebook = NoteManager()
    contacts = ContactBook()
    cryptoprice = CryptoPriceFetcher()

    while True:
        print("Choose a command:")
        print(f"{Colors.BLUE}1. ContactBook{Colors.RESET}")
        print(f"{Colors.GREEN}2. NoteBook{Colors.RESET}")
        print(f"{Colors.YELLOW}3. FileSorter{Colors.RESET}")
        print(f"{Colors.MAGENTA}4. CryptoPrice{Colors.RESET}")
        print(f"{Colors.CYAN}5. WebSearch{Colors.RESET}")
        print(f"{Colors.RED}6. Exit{Colors.RESET}")

        user_input = input("Enter command number: ")
        if user_input == '1':
            contacts.main()
        elif user_input == '2':
            notebook.main()
        elif user_input == '3':
            target_folder = input("Enter the folder path to sort: ")
            filesorter = FileSorter(target_folder)
            filesorter.run()
        elif user_input == '4':
            cryptoprice.display_crypto_prices()
        elif user_input == '5':
            search_in_browser()
        elif user_input == '6':
            print(f"{Colors.RED}Goodbye!{Colors.RESET}")
            break
        else:
            print(f"{Colors.RED}Wrong command. Enter a valid command.{Colors.RESET}")

if __name__ == '__main__':
    main()





