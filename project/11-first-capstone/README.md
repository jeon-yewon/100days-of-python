# First Capstone Project - Blackjack game
## Rule
- 참가자와 딜러(컴퓨터)는 최초 2개의 패를 전달받는다.
- 딜러의 카드는 게임 종료시까지 1장만 오픈된다.
- 참가자는 카드를 더 뽑을 지 선택할 수 있다.
- 이 게임에서 J, Q, K의 score는 모두 10으로 처리한다.
- 이 게임에서 A의 score는 11로 처리한다.
- 게임이 완료되었을 때 21에 가까운 수를 가지고 있는 사람이 승리한다.

## Flowchart
<img width="500" alt="스크린샷 2022-09-21 오후 1 05 31" src="https://user-images.githubusercontent.com/52244210/191420833-cdbc314f-3ebf-44f9-bea9-122b2d8429f5.png">

## Functions
- `pop_cards` : card_list에서 참가자 또는 딜러 카드 리스트로 n개를 가져옴
- `print_cards` : 참가자 또는 딜러 카드 정보를 출력
- `calc_score` : 참가자 또는 딜러 카드의 score를 계산, `sum_score`를 return
- `check_result` : 게임 승/패를 결정하는 로직. `status`를 return
- `print_result` : `check_result` 함수에서 return한 결과값(`status`)를 통해 출력문을 결정
