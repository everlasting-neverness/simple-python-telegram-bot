import requests
# import json
from misc import token, proxies
from yobit import get_btc
from time import sleep

global last_update_id
last_update_id = 0

URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url, proxies=proxies)
    print(r.json())
    return r.json()

def get_message():
    data = get_updates()
    last_result = data['result'][-1]
    update_id = last_result['update_id']
    global last_update_id
    if update_id == last_update_id:
        return None;
    last_update_id = update_id
    chat_id = last_result['message']['chat']['id']
    message_text = last_result['message']['text']
    message = { 'chat_id': chat_id, 'message_text': message_text }
    return message

def send_message(chat_id, text="test"):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url, proxies=proxies)

def get_answer_text(message):
    if 'hello' in message:
        return 'hello there!'
    elif message == '/btc':
        return get_btc()
    else:
        return 'Hello!'

def main():
    # dict = get_updates()

    # with open('updates.json', 'w') as file:
    #     json.dump(dict, file, indent=2, ensure_ascii=False)
    while True:
        message = get_message()
        if message is None:
            print('old request')
            continue
        else:
            answer = get_answer_text(message['message_text'])
            # send_message(message['chat_id'], message['message_text'])
            send_message(message['chat_id'], answer)
        sleep(2)


if __name__ == '__main__':
    main()