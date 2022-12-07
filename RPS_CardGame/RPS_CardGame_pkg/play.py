import random as rd
import time
class RPS_CardGame:
    cards = ['Rock', 'Paper', 'Scissors']*3

    def __init__(self, palyer):
        self.palyer = palyer
        self.deck = []
    
    def Build_Deck(self, com):
        Shuffle_cards = rd.sample(RPS_CardGame.cards, 8)
        self.deck = Shuffle_cards[:4]
        com.deck = Shuffle_cards[4:]
        print('덱이 만들어졌습니다. \n플레이어의 덱:', self.deck)
        return self.deck

    @classmethod
    def Hand(cls, hand):
        cls.hand = hand
        return cls.hand
    
    def Hand_remove(self, hand):    
        self.deck.remove(hand)
    
    def random_hand(self):
        self.hand = self.deck.pop()

    @staticmethod
    def is_valid_hand(hand):
        return hand in RPS_CardGame.cards
    
    @classmethod
    def play(cls):
        my = RPS_CardGame('my')
        com = RPS_CardGame('com')
        my.Build_Deck(com)

        stack=0
        score=0
        while True:    
            select_hand = input('카드 하나를 선택하세요.')
            if my.is_valid_hand(select_hand):
                myhand = RPS_CardGame.Hand(select_hand)
                my.Hand_remove(myhand)
            else:
                print('다시 입력해주세요.')
                continue

            com.random_hand()
            print('상대의 카드는...')
            time.sleep(2)
            print(com.hand+'!')
            time.sleep(1)
            if myhand == 'Rock':
                if com.hand == 'Rock':
                    print('<<draw!>>')

                if com.hand == 'Scissors':
                    print('<<win!>>')
                    score += 1
                if com.hand == 'Paper': 
                    print('<<lose!>>')   
                    score -= 1

            if myhand == 'Scissors':
                if com.hand == 'Rock':
                    print('<<lose!>>')
                    score -= 1
                if com.hand == 'Scissors':
                    print('<<draw!>>')

                if com.hand == 'Paper':    
                    print('<<win!>>')  
                    score += 1

            if myhand == 'Paper':
                if com.hand == 'Rock':
                    print('<<win!>>')
                    score += 1
                if com.hand == 'Scissors':
                    print('<<lose!>>')
                    score -= 1
                if com.hand == 'Paper':  
                    print('<<draw!>>')  
      
            stack += 1
            if stack == 3:
                break
    
            print('\n플레이어의 덱: {}'.format(my.deck))  
        time.sleep(1)
        judge(score)

class NotZeroMultipleError(Exception):
    def __init__(self):
        super().__init__('무승부입니다.')
 
def judge(x):
    try:
        if x == 0:                 
            raise NotZeroMultipleError   
        if x > 0:
            print('\n최종승리!!')
        else:
            print('\n최종패배...') 
    except Exception as e:
        print('\n승패가 정해지지 않았습니다.', e)
        print('\n다시 승부합니다.\n')
        RPS_CardGame.play()