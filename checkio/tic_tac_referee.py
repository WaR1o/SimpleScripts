# there is 3 different scenarios when players could win
# if all values in a row are equal (game_result[n][m] == game_result[n][m+1] == game_result[n][m+2])
# if all values in a column are equal (game_result[n][m] == game_result[n+1][m] == game_result[n+2][m])
# if all diagonal values are equal(game_result[0][0] == game_result[1][1] == game_result[2][2])
# or reverse diagonal values are equal(game_result[2][0] == game_result[1][1] == game_result[0][2])
 # check if player X wins

def checkio(game_result):
    if game_result[2][0] == game_result[1][1] == game_result[0][2]:
        if game_result[0][2] == 'X' or game_result[0][2] == 'O':
            return game_result[0][2]
    elif game_result[0][0] == game_result[1][1] == game_result[2][2]:
        if game_result[0][0] == 'X' or game_result[0][0] == 'O':
            return game_result[0][0]
    for m in range(3):
        if game_result[0][m] == game_result[1][m] == game_result[2][m]:
            if game_result[0][m] == 'X' or game_result[0][m] == 'O':
                return game_result[0][m]
    for n in range(3):
        if game_result[n][0] == game_result[n][1] == game_result[n][2]:
            if game_result[n][0] == 'X' or game_result[n][0] == 'O':
                return game_result[n][0]
    else:
        return "D"
    # check if player O wins
    # check if its a draw

print(checkio([
        "OOX",
        "XXO",
        "OXX"]))
