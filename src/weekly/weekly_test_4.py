import random

import pandas
import pandas as pd
from typing import List, Dict
import matplotlib
import matplotlib.pyplot as plt

def csv_to_df(input_csv):
    euro12 = pd.read_csv(input_csv)
    return  euro12

csv_file = csv_to_df("/Users/feketedalma/Documents/GitHub/ECOPY_23241/data/Euro_2012_stats_TEAM.csv")

csv_to_df("/Users/feketedalma/Documents/GitHub/ECOPY_23241/data/Euro_2012_stats_TEAM.csv")


def number_of_participants(input_df):
    euro12 = input_df.copy()
    teams = euro12["Team"].count()
    return teams

number_of_participants(csv_file)

def goals(input_df):
    euro12 = input_df.copy()
    goals_euro = euro12[["Team", "Goals"]]
    return goals_euro

goals(csv_file)

def sorted_by_goal(input_df):
    return input_df.sort_values("Goals", ascending=False)

sorted_by_goal(goals(csv_file))

def avg_goal(input_df):
    euro12 = input_df.copy()
    df_average_scores = euro12["Goals"].mean()
    return df_average_scores

avg_goal(csv_file)

def countries_over_five(input_df):
    euro12 = input_df.copy()
    cv = euro12[["Team", "Goals"]]
    filtered_df = cv[cv['Goals'] >= 6]
    new_cv = pd.DataFrame(filtered_df['Team'])
    return new_cv

countries_over_five(csv_file)

def countries_starting_with_g(input_df):
    euro12 = input_df.copy()
    filtered_df = euro12[euro12['Team'].str.startswith('G')]
    return filtered_df['Team']

countries_starting_with_g(csv_file)

def first_seven_columns(input_df):
    euro12 = input_df.copy()
    if len(euro12.columns) >= 7:
        return euro12.iloc[:, :7]
    else:
        return euro12

first_seven_columns(csv_file)

def every_column_except_last_three(input_df):
    euro12 = input_df.copy()
    if len(euro12.columns) >= 3:
        return euro12.iloc[:, :-3]
    else:
        return euro12

every_column_except_last_three(csv_file)

def sliced_view(input_df, columns_to_keep, column_to_filter, rows_to_keep):
    euro12 = input_df.copy()
    szurt_adatok = euro12[euro12[column_to_filter].isin(rows_to_keep)]
    kivalasztott_oszlopok = szurt_adatok[columns_to_keep]

    return kivalasztott_oszlopok

def generate_quartile(input_df):
    quartile_list = []
    for i in input_df['Goals']:
        if i < 3:
            quartile_list.append(4)
        elif 2 < i < 5:
            quartile_list.append(3)
        elif i == 5:
            quartile_list.append(2)
        elif 5 < i < 13:
            quartile_list.append(1)
    input_df['Quartile'] = quartile_list
    return input_df

generate_quartile(csv_file)

def average_yellow_in_quartiles(input_df):
    euro12 = input_df.copy()
    avg_goals = euro12.groupby("Quartile")["Passes"].mean()
    return avg_goals

average_yellow_in_quartiles(csv_file)

def minmax_block_in_quartile(input_df):
    euro12 = input_df.copy()
    blocks = euro12.groupby("Quartile")["Blocks"].agg(['min', 'max'])
    return blocks

minmax_block_in_quartile(csv_file)

def scatter_goals_shots(input_df):
    euro12 = input_df.copy()
    plt.figure(figsize=(8, 6))
    plt.scatter(euro12['Goals'], euro12['Shots on target'])
    plt.title('Goals and Shot on target')
    plt.xlabel("Goals")
    plt.ylabel("Shots on target")
    plt.grid(True)
    plt.show()

scatter_goals_shots(csv_file)


class ParetoDistribution:
    def __init__(self, rand, shape, scale):
        self.rand = rand
        self.shape = shape
        self.scale = scale


    def ppf(self, p):
        ppf_one = -1 / self.shape
        ppf2 = self.scale * (1 - p) ** ppf_one
        return ppf2

    def gen_rand(self):
        p_value = random.random()
        ppf_one = -1/self.shape
        pareto_random = self.scale * (1 - p_value) ** ppf_one
        return pareto_random

def gen_pareto_mean_trajectories(pareto_distribution, number_of_trajectories, length_of_trajectory):
    random.seed(42)
    main_list = []
    for x in range(number_of_trajectories):
        inner_list = []
        for n in range(length_of_trajectory):
            rand = pareto_distribution.gen_rand()
            inner_list.append(rand)

        cum_list = []
        for i in range(number_of_trajectories):
            window = inner_list[0:i + 1]
            average = sum(window) / (i + 1)
            cum_list.append(average)
        main_list.append(cum_list)

    return main_list

gen_pareto_mean_trajectories(ParetoDistribution(random,1,1), 2, 20)