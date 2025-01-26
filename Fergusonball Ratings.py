playerAmount = int(input("Amount of players: "))
goldPlayers = 0
player = 1
while player <= playerAmount:
    playerPoints = int(input(f"P{player} points: "))
    playerFouls = int(input(f"P{player} fouls: "))
    if playerPoints * 5 - playerFouls * 3 > 40:
        goldPlayers += 1
    player += 1
goldTeam = None
if goldPlayers == playerAmount:
    goldTeam = "+"
print(f"{goldPlayers}{goldTeam}")