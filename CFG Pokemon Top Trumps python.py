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
    response = requests.get(url)

#Checks for successful request 
    if response.status_code == 200:
        data = response.json()
        return{
            'name': data['name'],
            'id':data['id'],
            'height': data['height'],
            'weight': data['weight']
        }
    #If request fails
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

#Player chooses pokemon
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
#Initialises Scores

player_score = 0
opponent_score = 0

#Gameplay
def play_game(rounds):

    #Sets scores global so that they can be accessed outside function
    global player_score
    global opponent_score

    #Loops for set number of rounds
    for i in range(rounds):
        player_pokemon = choose_pokemon()
        opponent_pokemon = get_pokemon_data(get_random_pokemon_id())

        stat_choices = ['1. id', '2. height', '3. weight']
        print("\nChoose a stat to compare:")
        for i, stat in enumerate(stat_choices, start=1):
            print(f"{i}. {stat}")

        chosen_stat = None

        try:
            choice = int(input("Enter the number of your chosen stat: "))
            if 1 <= choice <= len(stat_choices):
                chosen_stat = stat_choices[choice - 1].split()[-1]
            else:
                print("Invalid input. Please enter a valid number.")
                continue

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        #Tuple unpacking return values of compare_stats function
        winner,winning_pokemon = compare_stats(
            player_pokemon,
            opponent_pokemon,
            player_pokemon[chosen_stat],
            opponent_pokemon[chosen_stat],
            chosen_stat,
            player_pokemon['name'],
            opponent_pokemon['name']
                            )
                
        #Player Scores
        if winner == 'player':
            player_score += 1
        elif winner == 'opponent':
            opponent_score += 1

        #Results
        print(f"\n{winning_pokemon} beat {opponent_pokemon['name']}." if winner == 'player' else f"{player_pokemon['name']} beat {winning_pokemon}.")
        print(f"The Winner is: {winner}")
        print(f"Current Scores - player: {player_score}, Opponent: {opponent_score}")
    
    #Game end 
    print('\nGame Over!')
    print(f"Final Scores - Player: {player_score}, Opponent: {opponent_score}")
    
    #Asks if player wants to play again and if so start the game again
    play_again = input("\nDo you want to play again? (yes/no): ".lower())
    if play_again.lower() == 'yes':
        rounds = int(input("Enter the number of rounds: "))
        play_game(rounds)


if __name__ == "__main__":
    rounds = int(input("Enter the number of rounds: "))
    play_game(rounds)