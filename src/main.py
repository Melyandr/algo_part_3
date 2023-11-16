def couples_for_wedding(graph):
    if len(graph) == 0 | len(graph) == 1:
        return set()

    tribes = [set() for _ in range(len(graph))]
    i = 1
    while i < len(graph):
        for person in graph[i]:
            tribes[i].add(person)
            j = i + 1
            while j < len(graph):
                if person in graph[j]:
                    for new_person in graph[j]:
                        if new_person not in graph[i]:
                            tribes[i].add(new_person)
                            graph[i].append(new_person)
                    graph.remove(graph[j])
                else:
                    j += 1
        i += 1

    set_output = set()

    for i in range(len(tribes)):
        odd_numbers = {person for person in tribes[i] if person % 2 != 0}
        paired_numbers = {person for person in tribes[i] if person % 2 == 0}
        for j in range(i + 1, len(tribes)):
            for boy in odd_numbers:
                for person in tribes[j]:
                    if (boy + person) % 2 != 0:
                        set_output.add(f"{boy}/{person}")
            for girl in paired_numbers:
                for person in tribes[j]:
                    if (girl + person) % 2 != 0:
                        set_output.add(f"{girl}/{person}")

    return set_output


def read_from_file():
    with open("../test/input2.txt", "r") as input_file:
        lines = input_file.readlines()

    graph = []
    for line in lines:
        if line.strip():
            part = list(map(int, line.split(" ")))
            graph.append(part)
    return graph


def write_to_file(couples, count):
    with open("../test/output.txt", "w") as output_file:
        if couples:
            output_file.write(f"Можливі комбінації пар: {count} (")
            output_file.write((", ".join(couples)))

        output_file.write(")")

        output_file.close()


if __name__ == "__main__":
    graph = read_from_file()

    combinations = couples_for_wedding(graph)
    count_couples = len(combinations)
    print(count_couples)
    print(combinations)
    write_to_file(combinations, count_couples)
