from requests import get
from json import loads
from trello import TrelloClient
import random
import os

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
board_id = os.getenv('BOARD_ID')

client = TrelloClient(
    api_key=api_key,
    api_secret=api_secret
)

board = client.get_board(board_id)


def generate_cards(cards, random_card):
    random_card['name'] = random.choice(daily_random_tasks)
    return cards + [random_card]

def create_all_lists(lists, board):
    list_details = []
    for li, detail in lists.items():
        list_detail = board.add_list(
            name=detail['name'],
            pos=detail['pos']
        )
        list_details.append(list_detail)
    return list_details

def remove_all_lists(board):
    lists = board.get_lists([])
    for li in lists:
        li.close()

def create_cards(list_details, cards):
    card_details = []
    for li in list_details:
        list_name = li.name
        for card in cards:
            if list_name in card['list']:
                card_detail = li.add_card(
                    name=card['name'],
                    position=card.get('pos')
                )
                card_description = card.get('description')
                if card_description:
                    card_detail.set_description(card_description)
                card_details.append(card_detail)
    return card_details

def reset(list_details):
    morning_todo_list = list_details[0]
    morning_done_list = list_details[1]
    evening_todo_list = list_details[2]
    evening_done_list = list_details[3]
    morning_done_list.move_all_cards(morning_todo_list)
    evening_done_list.move_all_cards(evening_todo_list)

def get_random_quote():
    response = get(
        'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
    )
    return '{quoteText} - {quoteAuthor}'.format(**loads(response.text))


lists = {
    'morning_routine_todo': {
        'name': 'Morning Routine - ToDo',
        'code': 'morning_routine_todo',
        'section': 'morning',
        'status': 'todo',
        'pos': 1
    },
    'morning_routine_done': {
        'name': 'Morning Routine - Done',
        'code': 'morning_routine_done',
        'section': 'morning',
        'status': 'done',
        'pos': 2
    },
    'evening_routine_todo': {
        'name': 'Evening Routine - ToDo',
        'code': 'evening_routine_todo',
        'section': 'evening',
        'status': 'todo',
        'pos': 3
    },
    'evening_routine_done': {
        'name': 'Evening Routine - Done',
        'code': 'evening_routine_done',
        'section': 'evening',
        'status': 'done',
        'pos': 4
    },
}

daily_random_tasks = [
    'Hug Mom',
    'Kiss Ross',
    'Call Papa',
    'Gratitude Journal',
    'Gratitude Journal',
    'Gratitude Journal',
    '5 Push Ups',
    'High-five Dad',
    '10 push ups',
    'Pet dogs for 30 seconds',
    'Fitness'
]

random_card = {
    'section': 'morning',
    'code': '',
    'list': [lists['morning_routine_todo']['name']],
    'description': '',
}

cards = [
    {
        'name': 'Eat Breakfast',
        'section': 'morning',
        'cadence': 1,
        'code': 'eat_breakfast',
        'list': [lists['morning_routine_todo']['name']],
        'description': None,
        'pos': 1
    },
    {
        'name': 'Brush Teeth',
        'section': ['morning', 'evening'],
        'cadence': 1,
        'code': 'brush_teeth',
        'list': [
            lists['morning_routine_todo']['name'],
            lists['evening_routine_todo']['name']
        ],
        'description': None,
        'pos': 2
    },
    {
        'name': 'Brush Hair',
        'section': ['morning', 'evening'],
        'cadence': 1,
        'code': 'brush_hair',
        'list': [
            lists['morning_routine_todo']['name'],
            lists['evening_routine_todo']['name']
        ],
        'description': None,
        'pos': 3
    },
    {
        'name': 'Get Dressed',
        'section': 'morning',
        'cadence': 1,
        'code': 'get_dressed',
        'list': [lists['morning_routine_todo']['name']],
        'description': None,
        'pos': 4
    },
    {
        'name': 'Walk Dogs',
        'section': ['morning', 'evening'],
        'cadence': 1,
        'code': 'walk_dogs',
        'list': [
            lists['morning_routine_todo']['name'],
            lists['evening_routine_todo']['name']
        ],
        'description': None,
        'pos': 5
    },
    {
        'name': 'Ready School',
        'section': ['morning'],
        'cadence': 1,
        'code': 'ready_school',
        'list': [lists['morning_routine_todo']['name']],
        'description': None,
        'pos': 6
    },
    {
        'name': 'Take Shower',
        'section': ['evening'],
        'cadence': 1,
        'code': 'take_shower',
        'list': [lists['evening_routine_todo']['name']],
        'description': None,
        'pos': 7
    },
    {
        'name': 'Read Quote',
        'section': ['morning'],
        'cadence': 1,
        'code': 'read_quote',
        'list': [lists['morning_routine_todo']['name']],
        'description': get_random_quote(),
        'pos': 8
    }
]

if __name__ == '__main__':
    list_details = create_all_lists(lists, board)
    all_cards = generate_cards(cards, random_card)
    card_details = create_cards(list_details, all_cards)
