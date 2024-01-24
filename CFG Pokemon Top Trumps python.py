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
    
    #Checks for successful request
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return{
            'name': data['name'],
            'id':data['id'],
            'height': data['height'],
            'weight': data['weight']
        }
    #If request fails
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data for Pokemon with ID {pokemon_id}: {e}")
        return None
    
#Prints pokemon details
def print_pokemon_details(pokemon):
    print(f"{pokemon['name'].capitalize()} (ID: {pokemon['id']}) (height: {pokemon['height']}) (weight: {pokemon['weight']})")

#Player chooses pokemon
def choose_pokemon():
    pokemon_list = [get_pokemon_data(get_random_pokemon_id()) for _ in range(3)]

    print("Choose your pokemon:")
    for i, pokemon in enumerate(pokemon_list, start=1):
        print(f"{i}. ", end="")
        print_pokemon_details(pokemon)

    while True:
        try:
            choice = int(input("Enter the number of your chosen Pokemon: "))
            if 1 <= choice <= len(pokemon_list):
                return pokemon_list[choice - 1]
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


#Text
def print_stat_choices():
    stat_choices = ['id', 'height', 'weight']
    print("\nChoose a stat to compare:")
    for i, stat in enumerate(stat_choices, start=1):
        print(f"{i}. {stat.capitalize()}")
    return stat_choices

#If player chooses one round
def play_round(player_pokemon, opponent_pokemon, chosen_stat):
    player_stat = player_pokemon[chosen_stat]
    opponent_stat = opponent_pokemon[chosen_stat]

    if player_stat > opponent_stat:
        return 'player', player_pokemon['name']
    elif player_stat < opponent_stat:
        return 'opponent', opponent_pokemon['name']
    else:
        return 'tie', None
    
#Main game
def play_game(rounds):
    player_score = 0
    opponent_score = 0

    for _ in range(rounds):
        player_pokemon = choose_pokemon()
        opponent_pokemon = get_pokemon_data(get_random_pokemon_id())

        print_pokemon_details(player_pokemon)
        print_pokemon_details(opponent_pokemon)
        
        stat_choices = print_stat_choices()

        print_stat_choices()
        chosen_stat = None

        while chosen_stat is None:
            try:
                choice = int(input("Enter the number of your chosen stat: "))
                if 1 <= choice <= len(stat_choices):
                    chosen_stat = stat_choices[choice - 1]
                else:
                    print("Invalid input. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        winner, winning_pokemon = play_round(player_pokemon, opponent_pokemon, chosen_stat)

        if winner == 'player':
            player_score += 1
        elif winner == 'opponent':
            opponent_score += 1

        print(f"\n{winning_pokemon} beat {opponent_pokemon['name']}." if winner == 'player' else f"{player_pokemon['name']} beat {winning_pokemon}.")
        print(f"The Winner is: {winner}")
        print(f"Current Scores - player: {player_score}, Opponent: {opponent_score}")

    print('\nGame Over!')
    print(f"Final Scores - Player: {player_score}, Opponent: {opponent_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        rounds = int(input("Enter the number of rounds: "))
        play_game(rounds)

if __name__ == "__main__":
    rounds = int(input("Enter the number of rounds: "))
    play_game(rounds)