import re
import datetime
from colorama import Fore, Style, init
import json

init(autoreset=True)
def save_contacts_to_file(contacts, file_path='contacts.json'):
    with open(file_path, 'w') as file:
        json.dump(contacts, file, indent=4)

def load_contacts_from_file():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
class ContactBook:
    def __init__(self):
        self.contacts = []

    def input_error(self, func):
        def inner(*args):
            try:
                return func(*args)
            except KeyError:
                return Fore.RED + '\nEnter a user name, please.\n' + Style.RESET_ALL
            except ValueError:
                return Fore.RED + '\nSecond argument must be a number.\n' + Style.RESET_ALL
            except IndexError:
                return Fore.RED + '\nPlease provide name, phone, email, address, and birthday.\n' + Style.RESET_ALL

        return inner

    def is_valid_phone_number(self, number):
        return re.match(r'^380\d{9}$', number)

    def add_contact(self):
        number = input(Fore.GREEN + 'Enter phone number (e.g., 380123456789): ' + Style.RESET_ALL)
        name = input(Fore.GREEN + 'Enter name: ' + Style.RESET_ALL)
        email = input(Fore.GREEN + 'Enter email: ' + Style.RESET_ALL)
        address = input(Fore.GREEN + 'Enter address: ' + Style.RESET_ALL)
        birthday = input(Fore.GREEN + 'Enter birthday (YYYY-MM-DD): ' + Style.RESET_ALL)

        if not self.is_valid_phone_number(number):
            return Fore.RED + 'Phone number is not valid. It should be in the format 380XXXXXXXXX.\n'

        self.contacts.append({
            "number": number,
            "name": name,
            "email": email,
            "address": address,
            "birthday": birthday
        })

        return Fore.GREEN + 'Contact added successfully.\n'

    def change_contact(self):
        name = input(Fore.CYAN + 'Enter the name of the contact you want to change: ' + Style.RESET_ALL)
        contact = self.find_contact_by_name(name)
        if contact:
            print(Fore.CYAN + f'Contact found: {contact}\n')
            print(Fore.MAGENTA + 'Choose the information to change:')
            print('1. Phone number')
            print('2. Email')
            print('3. Address')
            print('4. Birthday')
            choice = input(Fore.MAGENTA + 'Enter your choice (1/2/3/4): ' + Style.RESET_ALL)
            if choice == '1':
                new_number = input(Fore.CYAN + 'Enter the new phone number: ' + Style.RESET_ALL)
                contact['number'] = new_number
            elif choice == '2':
                new_email = input(Fore.CYAN + 'Enter the new email: ' + Style.RESET_ALL)
                contact['email'] = new_email
            elif choice == '3':
                new_address = input(Fore.CYAN + 'Enter the new address: ' + Style.RESET_ALL)
                contact['address'] = new_address
            elif choice == '4':
                new_birthday = input(Fore.CYAN + 'Enter the new birthday (YYYY-MM-DD): ' + Style.RESET_ALL)
                contact['birthday'] = new_birthday
            else:
                return Fore.RED + 'Invalid choice.\n'
            return Fore.GREEN + 'Contact updated successfully.\n'
        else:
            return Fore.RED + 'Contact not found.\n'

    def delete_contact(self):
        name = input(Fore.RED + 'Enter the name of the contact you want to delete: ' + Style.RESET_ALL)
        contact = self.find_contact_by_name(name)
        if contact:
            self.contacts.remove(contact)
            return Fore.GREEN + 'Contact deleted successfully.\n'
        else:
            return Fore.RED + 'Contact not found.\n'

    def find_contact_by_name(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                birthday = datetime.datetime.strptime(contact['birthday'], '%Y-%m-%d').date()
                days_until_bday = self.days_until_birthday(birthday)

                return {**contact, "days_until_birthday": days_until_bday}
        return None

    def show_all_contacts(self):
        if not self.contacts:
            return Fore.YELLOW + 'No contacts found.\n'

        today = datetime.date.today()

        for contact in self.contacts:
            birthday = datetime.datetime.strptime(contact['birthday'], '%Y-%m-%d').date()
            days_until_bday = self.days_until_birthday(birthday)

            print(Fore.YELLOW + f'Name: {contact["name"]}')
            print(f'Phone: {contact["number"]}')
            print(f'Email: {contact["email"]}')
            print(f'Address: {contact["address"]}')
            print(f'Birthday: {contact["birthday"]}')
            print(f'Days until birthday: {days_until_bday} days\n')

        return ''

    def days_until_birthday(self, birthday):
        today = datetime.date.today()
        next_birthday = datetime.date(today.year, birthday.month, birthday.day)
        if today > next_birthday:
            next_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)
        return (next_birthday - today).days

    def upcoming_birthday_contact(self):
        if not self.contacts:
            return Fore.YELLOW + 'No contacts found.\n'

        today = datetime.date.today()
        min_days_until_birthday = float('inf')
        upcoming_contact = None

        for contact in self.contacts:
            birthday = datetime.datetime.strptime(contact['birthday'], '%Y-%m-%d').date()
            days_until_bday = self.days_until_birthday(birthday)

            if days_until_bday < min_days_until_birthday:
                min_days_until_birthday = days_until_bday
                upcoming_contact = contact

        if upcoming_contact:
            return Fore.GREEN + f'The contact with the upcoming birthday is: {upcoming_contact["name"]}\n'
        else:
            return Fore.YELLOW + 'No upcoming birthdays found.\n'

    def main(self):
        contact_book = ContactBook()
        contact_book.contacts = load_contacts_from_file()
        while True:
            print(Fore.BLUE + 'Choose an option:')
            print('1. Add contact')
            print('2. Change contact')
            print('3. Delete contact')
            print('4. Show all contacts')
            print('5. Upcoming birthday contact')
            print('6. Exit\n')

            choice = input(Fore.BLUE + 'Enter your choice (1/2/3/4/5/6): ' + Style.RESET_ALL)

            if choice == '1':
                print(self.add_contact())
            elif choice == '2':
                print(self.change_contact())
            elif choice == '3':
                print(self.delete_contact())
            elif choice == '4':
                print(self.show_all_contacts())
            elif choice == '5':
                print(self.upcoming_birthday_contact())
            elif choice == '6':
                print(Fore.GREEN + 'Goodbye!\n')
                save_contacts_to_file(contact_book.contacts)
                break
            else:
                print(Fore.RED + 'Invalid choice. Please try again.\n')

if __name__ == '__main__':
    contact_book = ContactBook()
    contact_book.main()

