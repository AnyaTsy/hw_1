import art
from prettytable import PrettyTable


def header_text():
    attention = '******* achtung attention увага ********'.upper()
    text_GPA = art.text2art(" GPA", font='lean', chr_ignore=True, space=1)
    text_full = '***** Your Genius Personal Assistant ******'.upper()

    print(f'{attention:^110}\n', text_GPA, f'{text_full:^105}\n')


def inf_table():
    app_table = PrettyTable()

    app_table.field_names = ['№', 'Назва', 'Інформація', 'Запуск']
    app_table.add_row(['1', 'ContactBook',
                       'Книга контактів для зберігання телефонів, емейлів, днів народження та іншої корисної інформації',
                       'Для початку роботи натисніть 1'], divider=True)
    app_table.add_row(['2', 'NoteBook',
                       'Ззаписник в який можна додавати необхідні повсякденні записи',
                       'Для початку роботи натисніть 2'], divider=True)
    app_table.add_row(['3', 'FileSorter',
                       'Дозволяє відсортувати будь-яку теку з файлами', 'Для початку роботи натисніть 3'],
                      divider=True)
    app_table.add_row(['4', 'GPT навігатор',
                       'Допомагає витягти будь яку інформацію збережену в AddressBook чи NoteBook.bin',
                       'Для початку роботи натисніть 4'], divider=True)
    app_table.add_row(['5', 'help',
                       'Інформація по роботі з додатком', 'Для початку роботи натисніть 5'])

    app_table.max_width['Інформація'] = 60

    print("\033[36m{}\033[0m".format(app_table))


def help():
    help_table = PrettyTable()

    help_table.field_names = ['Назва застосунку', 'Список команд та їх фунуціонал']
    help_table.add_row(['ContactBook', 'add : додає контакт до списку контактів\n'
                                       'change : змінє контак зі списку\n'
                                       'delete : видяляє контак зі списку\n'
                                       'show : показує список контактів'
                                       'close : закриває книгу контактів'], divider=True)
    help_table.add_row(['NoteBook.bin', 'add : додає апис до записника\n'
                                    'change : змінє зінює запис в записнику\n'
                                    'delete : видяляє запис зі списку записів\n'
                                    'show : показує список всіх записів'
                                    'close : закриває записник'], divider=True)
    help_table.add_row(['FileSorter', 'close : сортувальник файлів'], divider=True)


    help_table.align['Список команд та їх фунуціонал'] = 'l'
    print("\033[33m{}\033[0m".format(help_table))

def header():
    header_text()
    inf_table()
    help()

header()