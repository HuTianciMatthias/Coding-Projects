import random

def singing_songs():
    song = input("What song do you want to sing:")
    singer = input("Who will sing the song:")
    volume = input("At what volume will the song be sung(low/meduim/high):")
    return f"{singer} sings '{song}' at a {volume} volume."

def play_games():
    game = input("What game do you want to play:")
    number_of_players = input("How many players:")
    return f"Play '{game}' with {number_of_players} players."

def cut_cake():
    flavor = input("What flavor is the cake:")
    size = input("What size is the cake(small/medium/large):")
    return f"Cut the {size} {flavor} cake."

def main():
    activities = ['1','2','3']
    random.shuffle(activities)

    activity_results = []

    for activity in activities:
        if activity == "1":
            result = singing_songs()
            print("\n")
        elif activity == "2":
            result = play_games()
            print("\n")
        elif activity == "3":
            result = cut_cake()
            print("\n")

        activity_results.append(result)
        
    print("\n")
    print("This will be your birthday party's activity order:")

    count = 1
    for result in activity_results:
        print(f"{count}. {result}")
        count += 1

main()
