
class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.temp_dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add(self,n:Node):
        prev = self.tail.prev
        prev.next = n
        n.next = self.tail
        n.prev = prev
        self.tail.prev = n

    def _remove(self,n:Node):
        next = n.next
        prev = n.prev
        next.prev = prev
        prev.next = next
    
    def get(self,key) -> int:
        if key in self.temp_dict:
            n = self.temp_dict[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1
    
    def put(self, key, value):
        if key in self.temp_dict:
            self._remove(self.temp_dict[key])
        n = Node(key, value)
        self._add(n)
        self.temp_dict[key] = n
        if (len(self.temp_dict) > self.capacity):
            n = self.head.next
            self._remove(n)
            del self.temp_dict[n.key]



lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
print(lRUCache.get(1))    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))    # return -1 (not found)
print(lRUCache.get(3))    # return 3
print(lRUCache.get(4))    # return 4




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0,None)
        result_tail = result
        carry = 0

        while (l1 or l2 or carry):
            l1_val = (l1.val if l1.val else None)
            l2_val = (l2.val if l2.val else None)

            carry, out = divmod(l1_val + l2_val + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1.next else None)
            l2 = (l2.next if l2.next else None)

        return result.next

solution = Solution
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))
print(solution.addTwoNumbers(l1,l2))



from enum import Enum
from random import randint

class Suit(Enum):
    Heart = "Heart"
    Spade = "Spade"
    Club = "Club"
    Diamond = "Diamond"

class Card():
    
    def __init__(self, suit:Suit, value:int) -> None:
        self.suit = suit
        self.value = value
    def __str__(self):
        return str(self.value) + " " + str(self.suit)
class Deck():
    cards = None
    def __init__(self) -> None:
        self.cards = []
        for i in range(1,15):
            self.cards.append(Card(Suit.Heart, i))
            self.cards.append(Card(Suit.Spade, i))
            self.cards.append(Card(Suit.Club, i))
            self.cards.append(Card(Suit.Diamond, i))
        
    def __str__(self):
        ret_val = ""
        for card in self.cards:
            ret_val += str(card) + "\n"
        return ret_val

    def draw(self):
        self.cards.pop()
    
    def draw_random(self):
        rand_draw = range(0, len(self.cards)-1)
        card = self.cards[rand_draw]
        del self.cards[rand_draw]
        return card

    def add_to_top(self, card:Card):
        self.cards.append(card)

    def add_to_bottom(self, card:Card):
        self.cards.insert(0,card)
    
    def shuffle(self):
        ceil = len(self.cards) - 1
        for i in range(0, len(self.cards)):
            swap_index = randint(0, ceil)
            swap_card = self.cards[swap_index]
            self.cards[swap_index] = self.cards[i]
            self.cards[i] = swap_card


deck = Deck()

print(deck)
deck.shuffle()
print(deck)