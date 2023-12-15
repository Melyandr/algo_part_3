def read_from_file():
    with open("../test/input.txt", "r") as input_file:
        lines = input_file.readlines()

    list_with_words_from_file = []
    for line in lines:
        word = line.strip('\n')
        list_with_words_from_file.append(word)
    return list_with_words_from_file



def max_length(list_words):
    sorted_list_words = sorted(list_words, key=len)

    dict_for_length = {}
    for word in sorted_list_words:
        dict_for_length[word] = 1

    for i in sorted_list_words:
        for index_of_letter in range(len(i)):
            comparing_word = i[:index_of_letter] + i[index_of_letter + 1:]
            if comparing_word in dict_for_length and dict_for_length[comparing_word] + 1 > dict_for_length[i]:
                dict_for_length[i] = dict_for_length[comparing_word]+1

    return max(dict_for_length.values())


def record_in_file(number):
    with open("../test/output.txt", "w") as file:
        file.write(str(number))
        file.close()


if __name__ == '__main__':
    words = read_from_file()
    length = max_length(words)
    print(length)
    record_in_file(length)
