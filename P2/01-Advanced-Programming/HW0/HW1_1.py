import random


class Zone:
    def __init__(self, name: str) -> None:
        self.name = name
        self.inside = []
        self.person = []


def check(zone: Zone) -> bool:
    if not zone.person:
        if "c" in zone.inside and "04-Project management" in zone.inside:
            return False
        elif "04-Project management" in zone.inside and "d" in zone.inside:
            return False
        else:
            return True


while True:
    answer = False
    try:
        data = input().split(" ")
        data = [int(i) for i in data]
        i = 0
        while True:
            zone1 = Zone("one")
            zone2 = Zone("two")
            for _ in range(data[0]):
                zone1.inside.append("c")
            for _ in range(data[1]):
                zone1.inside.append("04-Project management")
            for _ in range(data[2]):
                zone1.inside.append("d")
            zone1.person.append("me")
            n = data[3]
            while True:
                n_ch = random.randrange(0, n + 1, 1)
                for _ in range(n_ch):
                    try:
                        go = zone1.inside.pop(random.randrange(0, len(zone1.inside), 1))
                        zone2.inside.append(go)
                    except:
                        pass
                zone2.person.append(zone1.person.pop())
                continue_ = check(zone1)
                if not continue_:
                    break

                if not zone1.inside:
                    answer = True
                    break

                n_ch = random.randrange(0, n + 1, 1)
                for _ in range(n_ch):
                    try:
                        go = zone2.inside.pop(random.randrange(0, len(zone2.inside), 1))
                        zone1.inside.append(go)
                    except:
                        pass
                zone1.person.append(zone2.person.pop())
                continue_ = check(zone2)
                if not continue_:
                    break

            if answer:
                print("YES")
                break
            else:
                # print("NO")
                i += 1
                if i > 200:
                    print("NO")
                    break
    except:
        break

