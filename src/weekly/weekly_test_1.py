def evens_from_list(input_list):
    even_numbers = [y for x,y in enumerate(input_list) if x%2 != 0]
    return even_numbers

def every_element_is_odd(input_list):
    odd_count = 0
    for num in input_list:
        if num % 2 == 1:
            odd_count += 1
    if odd_count == len(input_list):
         return True
    else:
        return False



def kth_largest_in_list(input_list, kth_largest):
    input_list.sort()
    return input_list[-kth_largest]


def cumavg_list(input_list):
    import numpy as np
    z = np.cumsum(input_list) / range(1, len(input_list) + 1)
    return z


def element_wise_multiplication(input_list1, input_list2):
    multiplied_list = []
    if len(input_list1) > len(input_list2):
        reference_list = input_list2
    else:
        reference_list = input_list1
    for i in range(len(reference_list)):
        multiplied_list.append(input_list1[i] * input_list2[i])
    return multiplied_list

def merge_lists(*lists):
    merged_list = []
    for l in lists:
        merged_list.extend(l)
    return merged_list

def squared_odds(input_list):
    odd_numbers = []
    for i in input_list:
        if i %2 ==1:
            odd_numbers.append(i)
    squared_list = []
    for num in odd_numbers:
        squared_list.append(num*num)
    return squared_list

def reverse_sort_by_key(input_dict):
    keys = list(input_dict.keys())
    keys.sort(reverse=True)
    sorted_dict = {i:input_dict[i] for i in keys}
    return sorted_dict


def sort_list_by_divisibility(input_list):
    list_2 = []
    list_5 = []
    list_25 = []
    list_none = []
    for i in input_list:
        if i % 2 == 0:
            list_2.append(i)
            if i % 5 == 0:
                list_25.append(i)
        elif i % 5 == 0:
            list_5.append(i)
        if i % 2 != 0:
            if i % 5 != 0:
                list_none.append(i)

    div_dict = {'by_two': list_2, "by_five": list_5, "by_two_and_five": list_25, "by_none": list_none}
    return div_dict