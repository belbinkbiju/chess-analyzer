import chess.pgn

print("Chess Game Analysis - My First Python Script")

pgn_file = open("data/lichess_belbinkbiju_2026-04-10.pgn")

your_username = "belbinkbiju"
total_games = 0

# Overall
your_wins = 0
your_losses = 0
draws = 0

# White stats
white_wins = 0
white_losses = 0
white_draws = 0

# Black stats
black_wins = 0
black_losses = 0
black_draws = 0

while True:
    game = chess.pgn.read_game(pgn_file)
    if game is None:
        break

    white = game.headers["White"]
    black = game.headers["Black"]
    result = game.headers["Result"]

    total_games += 1

    # You played as White
    if your_username == white:
        if result == "1-0":
            your_wins += 1
            white_wins += 1
        elif result == "0-1":
            your_losses += 1
            white_losses += 1
        else:
            draws += 1
            white_draws += 1

    # You played as Black
    elif your_username == black:
        if result == "0-1":
            your_wins += 1
            black_wins += 1
        elif result == "1-0":
            your_losses += 1
            black_losses += 1
        else:
            draws += 1
            black_draws += 1

# Output
print("\n--- Overall ---")
print("Total games:", total_games)
print("Your wins:", your_wins)
print("Your losses:", your_losses)
print("Draws:", draws)

print("\n--- As White ---")
print("Wins:", white_wins)
print("Losses:", white_losses)
print("Draws:", white_draws)

print("\n--- As Black ---")
print("Wins:", black_wins)
print("Losses:", black_losses)
print("Draws:", black_draws)