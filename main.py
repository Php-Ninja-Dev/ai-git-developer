# main.py

import pyperclip

def paste_from_clipboard():
    content = pyperclip.paste()
    print('Content pasted from clipboard:')
    print(content)


def main():
    print('Welcome to the improved pasting utility!')
    paste_from_clipboard()


if __name__ == '__main__':
    main()
