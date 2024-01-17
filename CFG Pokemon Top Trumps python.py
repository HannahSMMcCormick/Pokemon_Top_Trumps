# CFG Pokemon Top Trumps python 

#Imported packages 
import random
import requests

#Generates random pokemon Id to select card
def get_random_pokemon_id():
    return random.randint(1,151)


#get pokemon info
def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    responce = requests.get(url)

#Checks for successful request 
    if responce.status_code == 200:
        data = responce.json()
        return{
            'name': data['name'],
            'id':data['id'],
            'height': data['height'],
            'weight': data['weight']
        }
    #else fails
    else:
        print(f"Failed to retrieve data for Pokemon with ID {pokemon_id}")
        return None
#Who wins   
def compare_stats(player_stat, opponent_stat, stat_name):
    #Player Wins
    if player_stat > opponent_stat:
        print(f"You lose! Opponent's {stat_name} is higher.")
        return 'player'
    #Computer wins
    elif player_stat < opponent_stat:
        return 'opponent'
    #Tie
    else:
        print(f"It's a tie! Both have the same{stat_name}.")
        return 'tie'

#Sets up game
def play_game():

    #Give Player/Computer ther card
    player_pokemon_id = get_random_pokemon_id()
    opponent_pokemon_id = get_random_pokemon_id()

    #Fetches data for card
    player_pokemon = get_pokemon_data(player_pokemon_id)
    opponent_pokemon = get_pokemon_data(opponent_pokemon_id)

    #If both player and pokemon have card
    if player_pokemon and opponent_pokemon:

        #
        print(f"Your Pokemon: {player_pokemon['name']} (ID: {player_pokemon['id']})")
        print(f"Opponent's Pokemon: {opponent_pokemon['name']} (ID:{opponent_pokemon['id']})")

        stat_choices = ['id', 'height', 'weight']
        chosen_stat = input("Choose a stat to compare (id,height,or weight)")

        if chosen_stat in stat_choices:
            winner = compare_stats(player_pokemon[chosen_stat],opponent_pokemon[chosen_stat],chosen_stat)
            return winner
        else:
            print("Invalid stat choice. Please choose id, height, or weight")
            return None
        
Winner = play_game()
if Winner:
    print(f"The Winner is: {Winner}")