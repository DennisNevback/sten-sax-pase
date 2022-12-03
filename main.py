playing = True


def restart():
    global playing
    game_state = input('Would you like to play again? (Y/N)')
    if game_state == 'N':
        playing = False


while playing:
    player1_move = input(
        'Player one please choose - Rock(R), Paper(P) or Scissor(S)?')
    player2_move = input(
        'Player two please choose - Rock(R), Paper(P) or Scissor(S)?')
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
