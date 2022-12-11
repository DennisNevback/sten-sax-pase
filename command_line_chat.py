from threading import Thread
from datetime import datetime
from network import connect, send

choices = {}


def check_win(player1_move, player2_move):
    if player1_move == 'R' and player2_move == 'R':
        print('it\'s a tie! Another round!')
    elif player1_move == 'R' and player2_move == 'S':
        print('Player one wins!')
        # restart()
    elif player1_move == 'R' and player2_move == 'P':
        print('Player two wins!')
        # restart()
    elif player1_move == 'P' and player2_move == 'R':
        print('Player one wins!')
        # restart()
    elif player1_move == 'P' and player2_move == 'P':
        print('it\'s a tie! Another round!')
    elif player1_move == 'P' and player2_move == 'S':
        print('Player two wins!')
        # restart()
    elif player1_move == 'S' and player2_move == 'R':
        print('Player two wins!')
        # restart()
    elif player1_move == 'S' and player2_move == 'P':
        print('Player one wins!')
        # restart()
    elif player1_move == 'S' and player2_move == 'S':
        print('it\'s a tie! Another round!')

# convert timestamp to iso date time format


def timestamp_to_iso(timestamp):
    return datetime.fromtimestamp(timestamp / 1000)\
        .isoformat().replace('T', ' ').split('.')[0]


def send_message():
    while True:
        send(input())


def react_on_messages(timestamp, user, message):
    global choices
    time = timestamp_to_iso(timestamp)
    print(f'\n{time} {user}\n{message}\n')
    if message == 'P':
        choices[user] = message
    if message == 'R':
        choices[user] = message
    if message == 'S':
        choices[user] = message
    print(f'printar {choices}')
    # print(choices[user])
    # print(choices.values())
    #print(f'testing choice{choices[0]}')
    # print(choices[1])
    print("Choose rock(R), paper(P) or scissors(S) (just write one alternative)")
    print("or just wait for the other player if you have made your choice")

    # both players have chosen
    if len(choices) >= 2:
        # check who has won
        print('win method')
        check_win(choices[user], choices[user])
        # then empty the dictionary choices


user = input('Your name: ')
channel = input('Channel to join or create: ')
# connect to (or create) a channel, with a user name
connect(channel, user, react_on_messages)
# start non-blocking thread to input and send messages
Thread(target=send_message).start()
