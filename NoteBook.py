from abc import ABC, abstractmethod
from prettytable import PrettyTable
from colorama import Fore, Style
class UserInterface(ABC):
    @abstractmethod
    def display_message(self, message):
        pass
    @abstractmethod
    def get_user_input(self):
        pass
    @abstractmethod
    def display_notes(self, notes):
        pass
    @abstractmethod
    def show_menu(self, options):
        pass

class ConsoleUserInterface(UserInterface):
    def display_message(self, message):
        print(message)

    def get_user_input(self):
        return input(">>> ")

    def display_notes(self, notes):
        if notes:
            table = PrettyTable()
            table.field_names = ["Note", "Text", "Tags"]

            for i, note in enumerate(notes, 1):
                tags = ' '.join(tag for tag in note.tags if tag.startswith("#"))
                table.add_row([f"{i}", f"{note.text}", f"{tags}"])

            print(table)
        else:
            print("No notes found.")

    def show_menu(self, options):
        print("Choose an option:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        choice = input("Enter your choice (1/2/3/4/5/6): ")
        return choice


class NoteManager:
    def __init__(self, user_interface):
        self.notes = []
        self.user_interface = user_interface
    COMMANDS = {
        'add_note': 'add_note',
        'search_notes_by_tag': 'search_notes_by_tag',
        'search_notes_by_text': 'search_notes_by_text',
        'edit_note': 'edit_note',
        'delete_note': 'delete_note',
        'get_all_notes': 'get_all_notes',
        'no_command': None,
        'exit': ['exit', 'close', 'good bye'],
    }
    def command_handler(self, text):
        for kword, command in self.COMMANDS.items():
            if isinstance(command, str):
                if text.lower().startswith(command):
                    return getattr(self, f'{command}_command'), text.replace(command, '').strip().split()
            elif isinstance(command, list):
                if text.strip().lower() in command:
                    return getattr(self, f'{kword}_command'), []

    def main(self):
        while True:
            user_input = self.user_interface.get_user_input()
            command, data = self.command_handler(user_input)

            if command == self.exit_command:
                self.user_interface.display_message(command())
                break

            result = command(*data)
            if result:
                self.user_interface.display_message(result)
            else:
                self.user_interface.display_message("Command failed. Please try again.")
            if command == self.exit_command:
                break
if __name__ == '__main__':
    console_interface = ConsoleUserInterface()
    note_manager = NoteManager(console_interface)
    note_manager.main()
