from threading import Thread
from datetime import datetime
from network import connect, send

choices = {}


def check_win(dict):
    if 'R' in list(dict.values()) and 'S' in list(dict.values()):
        print(choices['R'])
        # restart()
    if 'R' in list(dict.values()) and 'P' in list(dict.values()):
        print(choices['P'])
        # restart()
    if 'P' in list(dict.values()) and 'S' in list(dict.values()):
        print(choices['R'])
        # restart()
    else:
        print('It\'s a tie')

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
    print(f'printar {choices[user]}')
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
        check_win(choices)
        # then empty the dictionary choices


user = input('Your name: ')
channel = input('Channel to join or create: ')
# connect to (or create) a channel, with a user name
connect(channel, user, react_on_messages)
# start non-blocking thread to input and send messages
Thread(target=send_message).start()
