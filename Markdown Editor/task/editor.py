# write your code here
PROMT = 'Choose a formatter: '
INPUT_MSG = 'Text: '
LABEL_INPUT_MSG = 'Label: '
URL_INPUT_MSG = 'URL: '
ROWS_NUM_INPUT_MSG = 'Number of rows: '
ROWS_NUM_INPUT_ERR_MSG = 'The number of rows should be greater than zero'
HEADER_LEVEL_INPUT_MSG = 'Level: '
HEADER_LEVEL_INPUT_ERR_MSG = 'The level should be within the range of 1 to 6'
UNKNOWN_INPUT_MSG = 'Unknown formatting type or command.'


def create_list():
    try:
        rows_number = int(input(ROWS_NUM_INPUT_MSG))
        assert rows_number > 0
    except (ValueError, AssertionError):
        print(ROWS_NUM_INPUT_ERR_MSG)
        return create_list()
    return [input(f'Row #{i + 1}: ') for i in range(rows_number)]


def create_header():
    try:
        header_level = int(input(HEADER_LEVEL_INPUT_MSG))
        assert 1 <= header_level <= 6
    except (ValueError, AssertionError):
        print(HEADER_LEVEL_INPUT_ERR_MSG)
        return create_header()
    return f'{"#" * header_level} {input(INPUT_MSG)}\n'


formatters = {
    'plain': lambda: input(INPUT_MSG),
    'bold': lambda: f'**{input(INPUT_MSG)}**',
    'italic': lambda: f'*{input(INPUT_MSG)}*',
    'link': lambda: f'[{input(LABEL_INPUT_MSG)}]({input(URL_INPUT_MSG)})',
    'inline-code': lambda: f'`{input(INPUT_MSG)}`',
    'new-line': lambda: f'\n',
    'unordered-list': lambda: '\n'.join(f'* {item}' for item in create_list()) + '\n',
    'ordered-list': lambda: '\n'.join(f'{i}. {item}' for i, item in enumerate(create_list(), start=1)) + '\n',
    'header': lambda: create_header()
}


def main():
    result_markdown = ''

    while (user_input := input(PROMT)) != '!done':
        if user_input == '!help':
            print(f'Available formatters:', *formatters, '\nSpecial commands: !help !done')
        elif user_input in formatters:
            result_markdown += formatters[user_input]()
            print(result_markdown)
        else:
            print(UNKNOWN_INPUT_MSG)

    with open('output.md', 'w') as output_file:
        output_file.write(result_markdown)


if __name__ == '__main__':
    main()
