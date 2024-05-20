from collections import deque

n = int(input())
Deck = list(range(1,n+1))
Deck = deque(Deck)
while len(Deck) != 1:
    Deck.popleft()
    Deck.rotate(-1)
print(Deck[0])

#시발 deque 라는 좋은게있었네