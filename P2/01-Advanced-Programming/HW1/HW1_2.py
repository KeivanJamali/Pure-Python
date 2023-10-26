import itertools


def find_permutations(l: map):
    """Returns all permutations of a list as a list."""
    return set(itertools.permutations(l))


class HW1_2:

    @staticmethod
    def max_power(lst: map) -> int:
        """
        Returns the maximum power calculated for a given list of items.

        Parameters:
            lst (list): A list of items.

        Returns:
            int: The maximum power calculated.
        """
        power = 0
        for item in find_permutations(lst):
            item_group = [[]]
            for i in item:
                if i == 0:
                    if item_group[-1]:
                        item_group.append([])
                else:
                    item_group[-1].append(i)
            if not item_group[-1]:
                item_group = item_group[:-1]
            new_power = HW1_2.max_calculator(item_group)
            if new_power > power:
                power = new_power
        return power

    @staticmethod
    def max_calculator(lst: list) -> int:
        """
        Calculates the maximum difference between the maximum and minimum value in each sublist of a given list.

        Args:
            lst (list): A list of sublists, where each sublist contains integers.

        Returns:
            int: The sum of all the maximum differences between the maximum and minimum value in each sublist.
        """
        total_sum = 0
        for item in lst:
            if len(item) > 1:
                total_sum += max(item) - min(item)
        return total_sum


def main(n: int, string: str) -> int:
    """
    Calculate the maximum power of a list of integers.

    Args:
        n (int): The length of the list.
        string (str): A space-separated string of integers.

    Returns:
        int: The maximum power of the list.

    """
    for _ in range(n - 1):
        string += " 0"
    lst = list(map(int, string.split()))
    return HW1_2.max_power(lst)


n = int(input())
string = input()
print(main(n, string))
