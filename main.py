piles_of_bananas = [3, 6, 7, 11]
bypass_time = 8


# piles_of_bananas = [30, 11, 23, 4, 20]
# bypass_time = 5


# piles_of_bananas = [30, 11, 23, 4, 20]
# bypass_time = 6


# answer for first ex is 4
# answer for second ex is 30
# answer for thir ex is 23
def binary_search(lst, hour):
    check_condition(lst, hour)
    high = max(lst)
    low = 1
    while low <= high:
        middle = (low + high) // 2
        guess = count_hour(lst, middle)
        if guess == hour:
            return middle
        if guess < hour:
            high = middle - 1
        else:
            low = middle + 1


def count_hour(lst, middle):
    total_hour = 0
    for i in lst:

        whole_num = i // middle
        if i % middle != 0:
            whole_num = whole_num + 1
        total_hour = total_hour + whole_num
    return total_hour


def check_condition(lst, time):
    if lst.__len__() < 1 or lst.__len__() > 10 ** 4:
        raise ValueError("Your list is out of bounds")

    if time < len(lst) or time > 10 ** 9:
        raise ValueError("Your time is out of bounds")

    for i in lst:
        if i < 1 or i > 10 ** 9:
            raise ValueError("Check piles in list")


result = binary_search(piles_of_bananas, bypass_time)
print(result)
