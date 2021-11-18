from .teams import TEAMS_INFO, TeamKeys
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl




csfont = {'fontname':'Comic Sans MS'}
hfont = {'fontname':'Helvetica'}




def count_number_of_goals(data_df, column='all_scored_goals'):
    ru_to_key = {team_info.russian_str: team_key for team_key, team_info in TEAMS_INFO.items()}
    return {ru_to_key[row['comands']]: row[column] for _, row in data_df.iterrows()}


def build_bar_plot_with_highlighted_two_teams(data_df, team1, team2, plot_name, outname, **kwargs):

    
    number_of_goals = count_number_of_goals(data_df, **kwargs)
    
    values_with_teams = list(number_of_goals.items())
    values_with_teams = sorted(values_with_teams, key=lambda x: x[1])
    values = [x[1] for x in values_with_teams]
    teams = [x[0] for x in values_with_teams]
    
    position = np.arange(len(values_with_teams))
    width = 0.9

#     fig = plt.figure(
    fig, ax = plt.subplots(figsize=(16, 9))
    bars = ax.barh(position, values, width, color='grey')
    for i, team in enumerate(teams):
        if team in (team1, team2):
            bars[i].set_color(TEAMS_INFO[team].color)
            
    labels = [TEAMS_INFO[team].russian_str for team in teams]
    ax.set_yticklabels(labels, fontname='roboto', fontsize=12)
    ax.set_yticks(position)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)   
    ax.spines['left'].set_color('#DDDDDD')
    ax.spines['bottom'].set_visible(False)
    ax.axes.xaxis.set_visible(False)

    ax.set_axisbelow(True)
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)


    for i, bar in enumerate(bars):
        bar_color = bar.get_facecolor()
        ax.text(
            # bar.get_x() + bar.get_width() / 2,
            # bar.get_height() + 0.3,
        
            values[i] + 0.3,
            bar.get_y() + bar.get_height() / 2,
            


            bar.get_width(),
            verticalalignment='center',
            horizontalalignment='left',
            color=bar_color,
            weight='bold',
            fontname='Roboto'
        )

    ax.set_title(plot_name, pad=0, color='#333333', weight='bold', fontname='roboto', fontsize=18)    

    fig.tight_layout()

    fig.savefig(outname)
    
    return fig, ax



def extract_plot_values(data_df_list, team1, team2, prefix): # под каруселью
    team1_values = list()
    team2_values = list()
    
    for df in data_df_list:
        line_1_2 = df[((df.home_team.str.upper() == team1.name) &
                       (df.away_team.str.upper()  == team2.name))]
        line_2_1 = df[((df.home_team.str.upper() == team2.name) &
                       (df.away_team.str.upper()  == team1.name))]
    
        if len(line_2_1) == 0 and len(line_1_2) == 0:
            team1_values.append(None)
            team2_values.append(None)
            continue
        
        team1_value = 0
        team2_value = 0
        if len(line_1_2) != 0:
            team1_value += line_1_2[f'{prefix}_h_t'].iloc[0]
            team2_value += line_1_2[f'{prefix}_a_t'].iloc[0]
            
        print(team1_value, team2_value)
        
        
        if len(line_2_1) != 0:
            team1_value += line_2_1[f'{prefix}_a_t'].iloc[0]
            team2_value += line_2_1[f'{prefix}_h_t'].iloc[0]
            
        team1_values.append(team1_value)
        team2_values.append(team2_value)
    
    return team1_values, team2_values

    df = pd.read_csv('stats/21_22.csv')

def aggregate_current_dataframe(df): #для карусели
    prefixes = sorted({col[:-4] for col in df.columns if col.endswith('_t')})
    teams_set = set(df.away_team) | set(df.home_team)
    teams_set = {TeamKeys[x.upper()] for x in teams_set}
    
    new_df_list = []
    
    
    for team in teams_set:
        new_df_line = dict()
        new_df_line['comands'] = TEAMS_INFO[team].russian_str
    
        for prefix in prefixes:        
            sum_value = df[df.home_team.str.upper() == team.name][f'{prefix}_h_t'].sum(0) 
            sum_value += df[df.away_team.str.upper() == team.name][f'{prefix}_a_t'].sum(0)
            count_value = ((df.home_team.str.upper() == team.name) |
                            (df.away_team.str.upper() == team.name)).sum(0)
    
            if prefix in ['yellow_cards', 'goal_score']:
                new_df_line[prefix] = round(sum_value)
            else:
                new_df_line[prefix] = round(sum_value / count_value, 1)
           
        new_df_list.append(new_df_line)
            

    return pd.DataFrame(new_df_list)

def build_bar_plot_two_teams(data_df_list, team1, team2, plot_name ,column):
    # number_of_goals = count_number_of_goals(data_df, **kwargs)
    # number_of_goals2 = count_number_of_goals(data_df2, **kwargs)    
    # values_with_teams = list(number_of_goals.items())
    # values_with_teams = sorted(values_with_teams, key=lambda x: x[1])
    # values = [x[1] for x in values_with_teams]
    # teams = [x[0] for x in values_with_teams]
    fig1, ax = plt.subplots(figsize=(16, 9))
    years = [1, 2, 3, 4, 5]
    team1_values, team2_values = extract_plot_values(data_df_list, team1, team2, column)
    grafs = ax.plot(years, team1_values, "o-", label=TEAMS_INFO[team1].russian_str, color=TEAMS_INFO[team1].color, markersize=15, linewidth=4)
    grafs1 = ax.plot(years, team2_values, "o-", label=TEAMS_INFO[team2].russian_str, color=TEAMS_INFO[team2].color, markersize=15, linewidth=4)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)   
    ax.spines['left'].set_color('#DDDDDD')
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.legend()
    ax.grid()
    years_list = ['2017-2018','2018-2019','2019-2020','2020-2021', '2021-2022'] 
    ax.set_xticklabels(years_list, fontname='roboto', fontsize=12)
    ax.set_xticks(years)
    max_value = max(list(filter(None, team1_values)) + list(filter(None, team2_values)))
    ax.set_yticklabels(list(range(max_value+1)),  fontname='roboto', fontsize=12) #просто проставить от нуля до максимального значения из списков (team_values) отсортировать исключая ну
    ax.set_yticks(list(range(max_value+1)))
    ax.set_xlim(0, 6)
    
   
    


    ax.set_title(plot_name, pad=0, color='#333333', weight='bold', fontname='roboto', fontsize=18)    
    return fig1, ax
