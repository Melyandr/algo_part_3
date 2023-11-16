def couples_for_wedding(graph):
    first_tribe = set()
    second_tribe = set()
    for person in graph[1]:
        first_tribe.add(person)

    for person_first_tribe in graph[1]:
        for sublist in graph[2:]:
            if person_first_tribe in sublist:
                for new_person in sublist:
                    if new_person not in graph[1]:
                        first_tribe.add(new_person)
                        graph[1].append(new_person)
                        sublist_for_removing = sublist
                graph.remove(sublist_for_removing)

    second_tribe.update(graph[2])

    odd_numbers = set()
    paired_numbers = set()

    for person in graph[1]:
        if person % 2 == 0:
            paired_numbers.add(person)
        else:
            odd_numbers.add(person)

    set_output = set()

    for boy_first_tribe in odd_numbers:
        for person_second_tribe in graph[2]:
            if (boy_first_tribe + person_second_tribe) % 2 != 0:
                set_output.add(f"{boy_first_tribe}/" f"{person_second_tribe}")

    for girl_first_tribe in paired_numbers:
        for person_second_tribe in graph[2]:
            if (girl_first_tribe + person_second_tribe) % 2 != 0:
                set_output.add(f"{girl_first_tribe}/" f"{person_second_tribe}")

    return set_output


def read_from_file():
    with open("../tests/input.txt", "r") as input_file:
        lines = input_file.readlines()

    graph = []
    for line in lines:
        part = list(map(int, line.split(" ")))
        graph.append(part)
    return graph


def write_to_file(couples, count):
    with open("../tests/output.txt", "w") as output_file:
        if couples:
            output_file.write(f"Можливі комбінації пар: {count} (")
            output_file.write((", ".join(couples)))

        output_file.write(")")

        output_file.close()


if __name__ == "__main__":
    graph = read_from_file()
    combinations = couples_for_wedding(graph)
    count_couples = len(combinations)
    write_to_file(combinations, count_couples)
