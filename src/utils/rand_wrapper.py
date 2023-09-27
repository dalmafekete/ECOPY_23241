
import random

def random_from_list(input_list):
    random_num = random.choice(input_list)
    return random_num

def random_sublist_from_list(input_list, number_of_elements):
    return random.choices(input_list, number_of_elements)


def random_from_string(input_string):
    random_item = random.choice(input_string)
    return random_item

def hundred_small_random():
    new_list = []
    for n in range(100):
        new_list.append(random.random())
    return new_list

def hundred_large_random():
    large_list = []
    for n in range(100):
        large_list.append(random.randint(10,1000))
    return large_list

def random_reorder(input_list):
    return random.sample(input_list, len(input_list))

def five_random_number_div_three():
    div_list= []
    for n in range(5):
        random_num = random.randint(9,1000)
        while random_num % 3 != 0:
            random_num = random.randint(9,1000)
        div_list.append(random_num)
    return div_list

def uniform_one_to_five():
    num = random.uniform(1,6)
    return num