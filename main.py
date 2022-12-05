import re
playing = True
player1_move = ''
player2_move = ''


def restart():
    global playing
    game_restart = input('Would you like to play again? (Y/N)\n')
    game_restart = game_restart.upper()
    if re.match('^[N]', game_restart):
        playing = False
        print('Thank you for playing!')


def check_win():
    if player1_move == 'R' and player2_move == 'R':
        print('it\'s a tie! Another round!')
    elif player1_move == 'R' and player2_move == 'S':
        print('Player one wins!')
        restart()
    elif player1_move == 'R' and player2_move == 'P':
        print('Player two wins!')
        restart()
    elif player1_move == 'P' and player2_move == 'R':
        print('Player one wins!')
        restart()
    elif player1_move == 'P' and player2_move == 'P':
        print('it\'s a tie! Another round!')
    elif player1_move == 'P' and player2_move == 'S':
        print('Player two wins!')
        restart()
    elif player1_move == 'S' and player2_move == 'R':
        print('Player two wins!')
        restart()
    elif player1_move == 'S' and player2_move == 'P':
        print('Player one wins!')
        restart()
    elif player1_move == 'S' and player2_move == 'S':
        print('it\'s a tie! Another round!')


while playing:
    player1_move = input(
        'Player one please choose - Rock(R), Paper(P) or Scissors(S)?\n')
    player1_move = player1_move.upper()
    if not re.match('^[RPS]$', player1_move):
        print('Please input either R, P or S')
    else:
        player2_move = input(
            'Player two please choose - Rock(R), Paper(P) or Scissors(S)?\n')
        player2_move = player2_move.upper()
        if not re.match('^[RPS]$', player2_move):
            print('Please input either R, P or S\n Game restarting')
        else:
            check_win()
