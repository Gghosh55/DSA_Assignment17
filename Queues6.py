def deckRevealedIncreasing(deck):
    deck.sort(reverse=True)
    result = []

    for card in deck:
        if result:
            result.insert(0, result.pop())

        result.insert(0, card)

    return result
deck = [17, 13, 11, 2, 3, 5, 7]
print(deckRevealedIncreasing(deck))
