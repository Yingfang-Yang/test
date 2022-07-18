import random

def find_target(target, n):
    # target = random.randint(1, n)
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        if guess(target) == -1:
            high = mid - 1
        elif guess(target) == 1:
            low  = mid + 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    pick = input(random.randint(1, 10))
    find_target(pick, 10)