def main(n: int, string: str) -> int:
    lst = list(map(int, string.split(" ")))
    lst = sorted(lst)
    n2 = n//2
    if n % 2 == 0:
        pre = sum(lst[:n2])
        post = sum(lst[n2:])
    else:
        pre = sum(lst[:n2])
        post = sum(lst[n2 + 1:])
    return post - pre


n = int(input())
string = input()
print(main(n, string))
