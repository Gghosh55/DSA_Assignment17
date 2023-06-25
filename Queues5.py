def find_the_winner(n, k):
    friends = list(range(1, n + 1))
    current = 0

    while len(friends) > 1:
        current = (current + k - 1) % len(friends)
        friends.pop(current)
        n -= 1
        if current == len(friends):
            current = 0

    return friends[0]
n = 5
k = 2
print(find_the_winner(n, k))

n = 6
k = 5
print(find_the_winner(n, k))
