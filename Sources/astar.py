import support_function as spf 
import time
from queue import PriorityQueue


def AStart_Search(board, list_check_point):
    start_time = time.time()
    ''' A* SEARCH SOLUTION '''
    if spf.check_win(board,list_check_point):
        print("Found win")
        return [board]
    start_state = spf.state(board, None, list_check_point,1)
    list_state = [start_state]

    heuristic_queue = PriorityQueue()
    heuristic_queue.put(start_state)

    while not heuristic_queue.empty():
        now_state = heuristic_queue.get()
        cur_pos = spf.find_position_player(now_state.board)
        list_can_move = spf.get_next_pos(now_state.board, cur_pos)
        for next_pos in list_can_move:
            new_board = spf.move(now_state.board, next_pos, cur_pos, list_check_point)
            if spf.is_board_exist(new_board, list_state):
                continue
            if spf.is_board_can_not_win(new_board, list_check_point):
                continue
            if spf.is_all_boxes_stuck(new_board, list_check_point):
                continue
            new_state = spf.state(new_board, now_state, list_check_point,1)
            if spf.check_win(new_board, list_check_point):
                print("Found win")
                timesolve = time.time() - start_time
                print(f"Time solve = {timesolve}" )
                return (new_state.get_line(), len(list_state))
            list_state.append(new_state)
            heuristic_queue.put(new_state)
            end_time = time.time()
            if end_time - start_time > spf.TIME_OUT:
                return []
        end_time = time.time()
        if end_time - start_time > spf.TIME_OUT:
            return []
    print("Not Found")
    return []