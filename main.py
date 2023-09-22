def quick_sort(lst, k):
    if len(lst) == 0:
        return "your list is empty"
    elif len(lst) == 1:
        return lst[0], 0
    elif len(lst) >= k:
        quick_sort_helper(lst, 0, len(lst) - 1, k)
        return f"The number is  {lst[-k]}, The index is  {len(lst) - k}"
    else:
        return "k is greater than the length of the list"


def quick_sort_helper(lst, low, high, k):
    if low < high:
        split_point = partition(lst, low, high)
        if split_point == len(lst) - k:
            return lst[split_point], split_point
        elif split_point < len(lst) - k:
            return quick_sort_helper(lst, split_point + 1, high, k)
        else:
            return quick_sort_helper(lst, low, split_point - 1, k)


def partition(lst, low, high):
    pivot_value = lst[low]
    left_mark = low + 1
    right_mark = high
    done = False

    while not done:
        while left_mark <= right_mark and lst[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark >= left_mark and lst[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            lst[left_mark], lst[right_mark] = lst[right_mark], lst[left_mark]

    lst[low], lst[right_mark] = lst[right_mark], lst[low]
    return right_mark


# lst = [19, 2, 45, 31, 6, 11, 121, 27]  # 2,6,11,19,27,31,45,121
lst = [19, 2, 45, 10, 6, 11, 121, 5, 33, 27]  # 2,5,6,10,11,19,27,33,45,121
print(quick_sort(lst, 5))
