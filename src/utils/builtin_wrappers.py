def evens_from_list(input_list):
    even_numbers = [y for x,y in enumerate(input_list) if x%2 != 0]
    return even_numbers

def element_wise_sum(input_list1, input_list2):
    all_devices = []
    if len(input_list1) > len(input_list2):
        reference_list = input_list2
    else:
        reference_list = input_list1
    for i in range(len(reference_list)):
        all_devices.append(input_list1[i] + input_list2[i])
    return all_devices

def contains_value(input_list, element):
    result = any(element in input_list for item in input_list)
    return result

def remove_every_element_from_list(input_list):
    input_list.clear()
    print(input_list)


def reverse_list(input_list):
    reversed_l = list(reversed(input_list))
    return reversed_l

def number_of_odds_in_list(input_list):
    odd_count = 0
    for num in input_list:
        if num % 2 == 1:
            odd_count += 1
    return odd_count

def second_largest_in_list(input_list):
    input_list.sort()
    return input_list[-2]


def subset_of_list(input_list, start_index, end_index):
    return input_list[start_index:end_index+1]


def every_nth(input_list, step_size):
    return input_list[::step_size]




