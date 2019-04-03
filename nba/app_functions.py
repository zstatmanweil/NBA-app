from nba.player import Player
from nba.choice import Choice
import pandas as pd

#converts players created from the Player class into a list of players
def convert_to_players(raw_data):
    players = []
    for player in raw_data:
        player = Player(
                player['firstName'],
                player['lastName'],
                player['draft']['seasonYear'],
                player['draft']['pickNum'],
                player['draft']['roundNum']
                )
        players.append(player)
    return players

#creates a table showing each year a player was drafted and how many players
#were drafted that year
def display_table(players_list):
    draft_years = []
    draft_years_count = []
    
    for player in players_list:
        draft_year = player.draft_year
        
        if draft_year != '':
            draft_year = int(draft_year)
        else:
            draft_year = 0
        
        if draft_year not in draft_years:
            draft_years_count.append(1)
            draft_years.append(draft_year)
        else:
            i = list(draft_years).index(draft_year)
            draft_years_count[i] += 1     
    
    #creating and organizing data table
    data = {'No. of Players' : draft_years_count}
    sum_table = pd.DataFrame(data, draft_years)
    sum_table_sorted = sum_table.sort_index(ascending=True)
    total_players = sum_table_sorted["No. of Players"].sum()
    players_no_data = sum_table_sorted.loc[0, "No. of Players"]
    sum_table_clean = sum_table_sorted.drop(0, axis=0)
            
#     result = f"""\nHere are the number of players still in the league \
# from each draft year as of 2017. Note: there wasn't draft data for \
# {players_no_data} of the {total_players} players. It is possible these players \
# weren't drafted. \n"""

    return sum_table_clean

#creates a dictionary for each year a player was drafted and all players 
#drafted that year        
def players_by_year(players_list):
    draft_years_players = {}

    for player in players_list:
        draft_year = player.draft_year
    
        if draft_year != '':
            draft_year = int(draft_year)
        else:
            draft_year = 0
        
        if draft_year in draft_years_players:
            draft_years_players[draft_year].append(player)
        else:
            draft_years_players[draft_year] = [player]

    return draft_years_players

# finds the user's player within the player list, if it exists    
def find_player_by_name(players_list, user_submitted_name):
        for player in players_list:
            if user_submitted_name.lower() == player.search_name():
                return player
        return False


def users_choice(players_list, user_choice):
    choice = Choice(user_choice)
    result = ''
    if choice.is_NBA_year():
        players = players_by_year(players_list).get(int(choice.user_choice))
        if players:
            result = "\n" + ", ".join(map(lambda p: p.full_name(), players))
        else:
            result = f"\nNo one drafted in {choice.user_choice} was in the NBA as of 2019"

    elif choice.is_year_prior_NBA():
        result = "\nThat is prior to the NBA's existance"

    elif choice.is_name():
        player = find_player_by_name(players_list, choice.user_choice)
        if player:
            result = player.draft_info()
        else:
            result = f"\n{choice.user_choice.title()} wasn't active in the NBA in 2019."

    else:
        result = "Try again!"

    return result