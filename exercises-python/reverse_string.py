import timeit

def reverse_string_1(word):
    rev_word = ''
    start_time = timeit.default_timer()
    for i in range(len(word)):
        rev_word += word[len(word) - 1 - i]
        time_diff = timeit.default_timer() - start_time
    return f'{rev_word} {time_diff * 10**6}'

# print(reverse_string("coolio"))
# print(timeit.Timer(reverse_string('coolio')).timeit(number=10000))

def reverse_string_2(word):
    rev_word = ''
    start_time = timeit.default_timer()
    rev_word = word[::-1]
    time_diff = timeit.default_timer() - start_time
    return f'{rev_word} {time_diff * 10**6}'

def reverse_string_3(word):
    rev_word = ''
    start_time = timeit.default_timer()
    rev_word = ''.join(reversed(word))
    time_diff = timeit.default_timer() - start_time
    return f'{rev_word} {time_diff * 10**6}'

for x in range(1,2):
    print(x, "\t", reverse_string_1('coolio_'))
    print(x+1, "\t", reverse_string_2('coolio_'))
    print(x+2, "\t", reverse_string_3('coolio_'))
