def find_common_names(players1, players2):
    players1_hash = {}
    common_players = []

    for p in players1:
        name = f"{p['first_name']} {p['last_name']}"
        players1_hash[name] = True

    for p in players2:
        name = f"{p['first_name']} {p['last_name']}"
        if players1_hash.get(name):
            common_players.append(name)

    return common_players


basketball_players = [
    {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
    {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
    {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
    {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"},
]

football_players = [
    {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
    {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
    {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
    {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"},
]

print(find_common_names(basketball_players, football_players))
