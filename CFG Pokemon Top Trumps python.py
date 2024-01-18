# CFG Pokemon Top Trumps python 

#Imported packages 
import random
import requests

#Generates random pokemon Id to select card
def get_random_pokemon_id():
    return random.randint(1,151)


#get pokemon info from API
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
def compare_stats(player_pokemon, opponent_pokemon, player_stat, opponent_stat, stat_name, player_name, opponent_name):
    #Player Wins
    if player_stat > opponent_stat:
        print(f"You Win! Your {stat_name} is higher.")
        return 'player',player_name
    #Computer wins
    elif player_stat < opponent_stat:
        print(f"You lose! Opponent's {stat_name} is higher.")
        return 'opponent',opponent_name
    #Tie
    else:
        print(f"It's a tie! Both have the same{stat_name}.")
        return 'tie',None

def choose_pokemon():
    pokemon_list = [get_pokemon_data(get_random_pokemon_id())for i in range(3)]

    print("Choose your pokemon:")
    for i, pokemon in enumerate(pokemon_list, start=1):
        print(f"{i}. {pokemon['name'].capitalize()} (ID: {pokemon['id']}) (height: {pokemon['height']}) (weight:{pokemon['weight']})")

    while True:
        try: 
            choice = int(input("Enter the number of your chosen Pokemon: "))
            if 1 <= choice <= len(pokemon_list):
                return pokemon_list[choice - 1]
            else: 
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Sets up game
def play_game():

    player_pokemon = choose_pokemon()
    opponent_pokemon = get_pokemon_data(get_random_pokemon_id())

    #Give Player/Computer ther card
    while True: 
            print(f"Your Pokemon: {player_pokemon['name']} (ID: {player_pokemon['id']}) (height: {player_pokemon['height']}) (weight:{player_pokemon['weight']})")

            #Player chooses stat
            stat_choices = ['id', 'height', 'weight']
            chosen_stat = input("Choose a stat to compare (id,height,or weight)").lower()


            if chosen_stat in stat_choices:
                winner,winning_pokemon = compare_stats(
                    player_pokemon,
                    opponent_pokemon,
                    player_pokemon[chosen_stat],
                    opponent_pokemon[chosen_stat],
                    chosen_stat,
                    player_pokemon['name'],
                    opponent_pokemon['name']
                    )
                print(f"\n{winning_pokemon} beat {opponent_pokemon['name']}." if winner == 'player' else f"{player_pokemon['name']} beat {winning_pokemon}.")
                print(f"The Winner is: {winner}")
            else:
                print("Invalid stat choice. Please choose id, height, or weight.")

            play_again = input("\nDo you want to play again? (yes/no): ")
            if play_again.lower() == 'yes':
                player_pokemon = choose_pokemon()
                opponent_pokemon = get_pokemon_data(get_random_pokemon_id())
            else:
                break

if __name__ == "__main__":
    play_game()
