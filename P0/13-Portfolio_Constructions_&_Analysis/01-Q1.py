import jovian
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

# we can save our code this way:
# import jovian
# jovian.commit(project='python binary search')

tests = []

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
tests.append(test)
# query occurs in the middle
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})
# query is the first Element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})
# query is the last Element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
# cards contain just one element
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})
# query dose not contain in cards
tests.append({
    'input': {
        'cards': [5, 4, 3, 1, 0],
        'query': 2
    },
    'output': -1
})
# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': -12
    },
    'output': -1
})
# numbers can repeat
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})
# numbers can repeat 2
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})
List = [5,4,3]
query = 4



def locate_card_leanier(cards: list, query: int) -> int:
    position = 0
    while position != len(cards):
        if query == cards[position]:
            return position
        position += 1
    return -1

def locate_card(cards: list, query: int) -> int:
    lo, hi = 0, len(cards)-1
    while lo <= hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid+1
    return -1



answer = locate_card(test['input']['cards'], test['input']['query'])
# print(test['output'] == locate_card(**test['input']))
evaluate_test_cases(locate_card, tests)