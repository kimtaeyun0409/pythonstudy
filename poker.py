from collections import Counter
import random

grade2=''

def get_hand_rank(cards):
    # 카드의 값과 무늬 분리
    value_map = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    values = [card[:-1] for card in cards]  # 값 추출
    suits = [card[-1] for card in cards]     # 무늬 추출
   # print(values, suits)
    numeric_values = sorted([value_map[value] for value in values], reverse=True)
    value_counts = Counter(numeric_values)
    counts = sorted(value_counts.values(), reverse=True)

    is_flush = len(set(suits)) == 1
    is_straight = len(value_counts) == 5 and (max(numeric_values) - min(numeric_values) == 4)

    # 스트레이트에서 A-5의 경우도 처리
    if sorted(numeric_values) == [2, 3, 4, 5, 14]:  # A가 낮은 카드로 사용될 때
        is_straight = True

    # 족보 판별
    if is_straight and is_flush and max(numeric_values) == 14:
        return "로얄 플러시"
    elif is_straight and is_flush:
        return "스트레이트 플러시"
    elif counts == [4, 1]:
        return "포 카드"
    elif counts == [3, 2]:
        return "풀 하우스"
    elif is_flush:
        return "플러시"
    elif is_straight:
        return "스트레이트"
    elif counts == [3, 1, 1]:
        return "트리플"
    elif counts == [2, 2, 1]:
        return "투 페어"
    elif counts == [2, 1, 1, 1]:
        return "원페어"
    else:
        return "하이 카드"

def compare_hands(player1_cards, player2_cards):
    global grade2
    hand_ranks = {
        "하이 카드": 1,
        "원페어": 2,
        "투 페어": 3,
        "트리플": 4,
        "스트레이트": 5,
        "플러시": 6,
        "풀 하우스": 7,
        "포 카드": 8,
        "스트레이트 플러시": 9,
        "로얄 플러시": 10
    }

    player1_rank = get_hand_rank(player1_cards)
    player2_rank = get_hand_rank(player2_cards)
    print("당신의 카드족보는:",player1_rank)
    grade2 = player2_rank
    if hand_ranks[player1_rank] > hand_ranks[player2_rank]:
        return True
    elif hand_ranks[player1_rank] < hand_ranks[player2_rank]:
        return False
    else:
        return None

def main():
    # 사용자로부터 카드 입력받기
    num1 = random.randint(1,4)
    num2 = random.randint(1, 13)
    shape = ['','♠','♥','♦','♣']
    val = ['','A','2','3','4','5','6','7','8','9','10','J','Q','K']
    player1_cards = []
    player2_cards = []
    for i in range(5):
        num1 = random.randint(1,4)
        num2 = random.randint(1, 13)
        player1_cards.append(val[num2] + shape[num1])
    for i in range(5):
        num1 = random.randint(1,4)
        num2 = random.randint(1, 13)
        player2_cards.append(val[num2] + shape[num1])

    print("당신의 카드는",end=' ')
    for i in range(5):
        print(player1_cards[i], end = ' ')
    print()
    
   # print(player1_cards,player2_cards)
    result = compare_hands(player1_cards, player2_cards)

    judge = input("이길 것 같으면 win, 질 것 같으면 lose, 비길 것 같으면 draw: ")

    if judge == 'win':
        judge = True
    elif judge == "lose":
        judge = False
    elif judge == 'draw':
        judge = None
    if result == judge:
        print('맞추셨습니다. ㅊㅋㅊㅋ')
    else:
        print('안타까워요. 도박 근절!!')

    print(grade2)
if __name__ == "__main__":
    main()