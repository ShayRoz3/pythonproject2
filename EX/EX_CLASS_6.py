#func to accecept a str and count the character within him
def most_frequenr(string):
    s = dict()
    for key in string:
        if key not in s:
            s[key] = 1
        else:
            s[key] += 1
    return s
print(most_frequenr('gosss dammss'))
print(most_frequenr("the quick brown fox jump over the lazy dog"))

print(most_frequenr("the quick brown fox jump over the lazy dog"))

#learn hpow to order the dict so it will be alphabetically



# they're selution- shecode
# def char_frequency(given_string):
#     abc_frequency = {}
#     abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
#            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
#            'x', 'y', 'z']
#
#     for i in range(0, len(abc)):
#         if given_string.find(abc[i]) != -1:
#             abc_frequency[abc[i]] = given_string.count(abc[i])
#
#     return abc_frequency
#
#
# print(char_frequency('abzz'))
