import time

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 3
move_pair = 30
# one_game = (my_compute_time + opponent_compute_time) * move_pair

def game(x):
    # start_game = time.perf_counter()
    # all_time = round(time.perf_counter() - start_game)
    # print(type(opponents))
    # for i in range(opponents):
    #     print(i)
    #     one_game = (my_compute_time + opponent_compute_time) * move_pair    
    #     time_take = opponents * move_pair
    #     print(one_game, 'time 1 game')
    #     print('time take', time_take)
    for j in range(opponents):
        print('board',j+1)
        for i in range(move_pair):
            time.sleep(my_compute_time)
            print(f'BOARD:{j+1} ROUND: {move_pair-i} My move')
            time.sleep(opponent_compute_time)
            print(f'BOARD:{j+1} ROUND:{move_pair-i} Oppenemt move')

if __name__ == "__main__":
    print("Start")
    start_game = time.perf_counter()
    # game(my_compute_time, opponent_compute_time, opponents, move_pair)
    game(3)
    elapsed = time.perf_counter() - start_game
    print(elapsed)