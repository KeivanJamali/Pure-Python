from itertools import permutations


def find_permutations(l: list):
    """Returns all permutations of a list as a list."""
    return set(permutations(l))


def color_add(price: int, color: list):
    # print(color)
    if color:
        for i in range(len(color)):
            # print("SS")
            # print(color[i])
            color_2 = color.copy()
            color_2.pop(i)
            # print(color_2)
            results.append(price + color[i])
            # print(price + color[i])
            # print("EE")
            code = hash((price+color[i], tuple(color_2)))
            if code in cash:
                pass
            else:
                cash.append(code)
                return color_add(price + color[i], color_2)
    else:
        # print("AAAAAAAAAAAAAAAAAAAAAAAAA")
        pass

cash = []
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
m_list2 = m_list + m_list.copy()
purpose = int(input())
results = []
b = False

for engine in n_list:
    if b:
        break
    for color in m_list2:
        color_add(engine, list(color))
        if purpose in results:
            print(purpose)
            b = True
            break

new = []
if not b:
    for i in results:
        new.append(abs(i - purpose))
    print(purpose - min(new))

import tqdm