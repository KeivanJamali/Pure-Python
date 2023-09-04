from random import Random


def make_sets(n: int) -> list:
    a = 0
    main_list = make_first_sets(n)
    while True:
        a += 1
        rand = Random().randrange(2, 4)
        s1 = set(Random().sample(list(range(1, n + 1)), rand))
        main_list.append(s1)
        # print(main_list)
        if len(main_list) > 2:
            result = check_list(main_list)
            if result == 3:
                main_list.pop()
            elif result == 1:
                main_list.pop()
            elif result == 5:
                # print("yeahhhhhh")
                return main_list
        if a % 20 == 0:
            main_list = make_first_sets(n)


def make_first_sets(n) -> list:
    while True:
        rand = Random().randrange(2, 4)
        try:
            if rand == 2:
                a, b = Random().randrange(3, n - 1, 2), Random().randrange(3, n - 1, 2)
            elif rand == 3:
                a, b = Random().randrange(4, n - 2, 3), Random().randrange(4, n - 2, 3)
            return [set(Random().sample(list(range(1, a)), rand)), set(Random().sample(list(range(a, b)), rand)),
                set(Random().sample(list(range(b, n + 1)), rand))]
        except:
            pass


def check_list(big_list: list) -> bool:
    """there are 3 things to check:
    1-no set should have intersect with more than 2 sets.
    2-at least one number should exist in three sets.
    3-there are no two sets to have more than one intersections.
    4-three sets have no intersections.
    5- all good!"""
    sharing = []
    b = 0

    # ________________________________________________________________
    for i in range(len(big_list)):
        if_a_list_share_more_than_3 = []
        non_sharing = []
        for j in range(len(big_list)):
            if i != j:
                inters = big_list[i] & (big_list[j])
                inters = list(inters)
                if len(inters) > 1:
                    # print("3")
                    return 3
                if len(inters) == 0:
                    non_sharing.append("empty")
                else:
                    sharing.append(inters[0])
                    if_a_list_share_more_than_3.append("sharing")
        if len(if_a_list_share_more_than_3) > 2:
            # print("1")
            return 1
        # if len(non_sharing) < 2:
        #     b += 1
    # ________________________________________________________________
    # if b >= len(big_list):
    #     return 4
    # ________________________________________________________________
    a = 0
    for i in sharing:
        if sharing.count(i) > 5:
            break
        a += 1
    if a == len(sharing):
        # print("2")
        return 2
    # ________________________________________________________________
    return 5


n = int(input())
answer = make_sets(n)
print(answer)
