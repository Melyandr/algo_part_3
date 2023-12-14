def read_from_file():
    with open("../test/input.txt", "r") as input_file:
        lines = input_file.readlines()

    list_with_words_from_file = []
    for line in lines:
        word = line.strip("\n")
        list_with_words_from_file.append(word)
    return list_with_words_from_file


visited = []


def find_sub_words(
    list_with_word, current_word, index_of_word_input_list, list_counter
):
    for letter in current_word:
        index_of_letter = current_word.index(letter)
        comparing_word = (
            current_word[:index_of_letter] + current_word[index_of_letter + 1 :]
        )
        if comparing_word in list_with_word and comparing_word not in visited:
            visited.append(comparing_word)
            list_counter[index_of_word_input_list].append(1)
            find_sub_words(
                list_with_word, comparing_word, index_of_word_input_list, list_counter
            )


def find_derived_word(list_with_word):
    list_counter = []
    for i in range(len(list_with_word)):
        list_counter.append([])

    for word in list_with_word:
        index_of_word_input_list = list_with_word.index(word)

        for letter in word:
            index_of_letter = word.index(letter)
            comparing_word = word[:index_of_letter] + word[index_of_letter + 1 :]
            if comparing_word in list_with_word:
                list_counter[index_of_word_input_list].append(1)
                find_sub_words(
                    list_with_word,
                    comparing_word,
                    index_of_word_input_list,
                    list_counter,
                )

    return list_counter


def find_max_length(list_counter) -> int:
    max_length_of_sub_list = 0
    for array in list_counter:
        if len(array) > max_length_of_sub_list:
            max_length_of_sub_list = len(array)
    return max_length_of_sub_list


def record_in_file(number):
    with open("../test/output.txt", "w") as file:
        file.write(str(number))
        file.close()


if __name__ == "__main__":
    list_with_words = read_from_file()
    list_of_chains = find_derived_word(list_with_words)
    print(list_of_chains)
    max_length = find_max_length(list_of_chains)
    record_in_file(max_length)

#
