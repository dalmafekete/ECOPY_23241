import random

import pandas
import pandas as pd
from typing import List, Dict
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

def csv_to_df(input_csv):
    food = pd.read_csv(input_csv, sep='\t')
    return food

def change_price_to_float(input_df):
    input_df['item_price'] = input_df['item_price'].str.replace('$', '').astype(float)
    return input_df

def number_of_observations(input_df):
    food = input_df.copy()
    szam = food.shape[0]
    return szam

def items_and_prices(input_df):
    food = input_df.copy()
    price_items = food[["item_name", "item_price"]]
    return price_items

def sorted_by_price(input_df):
    food = input_df.copy()
    sorted_df = food.sort_values(by="item_price", ascending=False)
    return sorted_df

def avg_price(input_df):
    food = input_df.copy()
    average = food["item_price"].mean()
    return average


def unique_items_over_ten_dollars(input_df):
    food = input_df.copy()
    draga_termekek = food[food["item_price"] > 10]
    egyedi_draga_termekek = draga_termekek.drop_duplicates(subset=["item_name", "item_price", "choice_description"])

    return egyedi_draga_termekek[["item_name", "choice_description","item_price"]]

def items_starting_with_s(input_df):
    food= input_df.copy()
    filtered_df = food[food['item_name'].str.startswith('S')]
    return filtered_df['item_name'].drop_duplicates()

def first_three_columns(input_df):
    food2 = input_df.copy()
    return food2.iloc[:, :3]


def every_column_except_last_two(input_df):
    food2 = input_df.copy()
    return food2.iloc[:, :-2]


def sliced_view(input_df,columns_to_keep, column_to_filter, rows_to_keep):
    food = input_df.copy()
    szurt_adatok = food[food[column_to_filter].isin(rows_to_keep)]
    kivalasztott_oszlopok = szurt_adatok[columns_to_keep]

    return kivalasztott_oszlopok

def generate_quartile(input_df):
    food = input_df.copy()
    quartile_list = []
    for i in food['item_price']:
        if i < 9.99:
            quartile_list.append('low-cost')
        elif 10 < i < 19.99:
            quartile_list.append('medium-cost')
        elif 20 < i < 29.99:
            quartile_list.append('high-cost')
        elif 30 <= i:
            quartile_list.append('premium')
    food['Quartile'] = quartile_list
    return food

def average_price_in_quartiles(input_df):
    food = input_df.copy()
    avg_goals = food.groupby("Quartile")["item_price"].mean()
    return avg_goals

def minmaxmean_price_in_quartile(input_df):
    food = input_df.copy()
    blocks = food.groupby("Quartile")["item_price"].agg(['min', 'max', 'mean'])
    return blocks


def gen_uniform_mean_trajectories(distribution, number_of_trajectories, length_of_trajectory):
    random.seed(42)
    main_list = []
    for x in range(number_of_trajectories):
        inner_list = []
        for n in range(length_of_trajectory):
            rand = distribution.gen_rand()
            inner_list.append(rand)

        cum_list = []
        for i in range(len(inner_list)):
            window = inner_list[0:i + 1]
            average = sum(window) / (i + 1)
            cum_list.append(average)
        main_list.append(cum_list)

    return main_list

def gen_logistic_mean_trajectories(distribution, number_of_trajectories, length_of_trajectory):
    random.seed(42)
    main_list = []
    for x in range(number_of_trajectories):
        inner_list = []
        for n in range(length_of_trajectory):
            rand = distribution.gen_rand()
            inner_list.append(rand)

        cum_list = []
        for i in range(len(inner_list)):
            window = inner_list[0:i + 1]
            average = sum(window) / (i + 1)
            cum_list.append(average)
        main_list.append(cum_list)

    return main_list

def gen_laplace_mean_trajectories(distribution, number_of_trajectories, length_of_trajectory):
    random.seed(42)
    main_list = []
    for x in range(number_of_trajectories):
        inner_list = []
        for n in range(length_of_trajectory):
            rand = distribution.gen_rand()
            inner_list.append(rand)

        cum_list = []
        for i in range(len(inner_list)):
            window = inner_list[0:i + 1]
            average = sum(window) / (i + 1)
            cum_list.append(average)
        main_list.append(cum_list)

    return main_list

def gen_cauchy_mean_trajectories(distribution, number_of_trajectories, length_of_trajectory):
    random.seed(42)
    main_list = []
    for x in range(number_of_trajectories):
        inner_list = []
        for n in range(length_of_trajectory):
            rand = distribution.gen_rand()
            inner_list.append(rand)

        cum_list = []
        for i in range(len(inner_list)):
            window = inner_list[0:i + 1]
            average = sum(window) / (i + 1)
            cum_list.append(average)
        main_list.append(cum_list)

    return main_list

def gen_chi2_mean_trajectories(distribution, number_of_trajectories, length_of_trajectory):
    random.seed(42)
    main_list = []
    for x in range(number_of_trajectories):
        inner_list = []
        for n in range(length_of_trajectory):
            rand = distribution.gen_rand()
            inner_list.append(rand)

        cum_list = []
        for i in range(len(inner_list)):
            window = inner_list[0:i + 1]
            average = sum(window) / (i + 1)
            cum_list.append(average)
        main_list.append(cum_list)

    return main_list