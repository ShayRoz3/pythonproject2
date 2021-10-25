# she_code seluttion for lesson  8
def print_first_and_last_chars_equal_strings(given_strings):
    result = []
    for i in range(len(given_strings)):
        if len(given_strings[i]) >= 2:
            current_string = given_strings[i]
            if current_string[0] == current_string[-1]:
                result.append(given_strings[i])
    print(result)


print_first_and_last_chars_equal_strings(['aba', 'xyz', 'aa', 'x', 'bbb'])
print_first_and_last_chars_equal_strings(['', 'x', 'xy', 'xyx', 'xx'])
