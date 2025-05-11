import numpy as np
import os
from copy import deepcopy
import time
from bfs import Best_First_Search
from astar import AStart_Search

''' TIME OUT FOR ALL ALGORITHM: 30 MIN ~ 1800 SECONDS '''
TIME_OUT = 1800

''' GET THE TESTCASES AND CHECKPOINTS PATH FOLDERS '''
path_board = os.getcwd() + '\\..\\Testcases'
path_checkpoint = os.getcwd() + '\\..\\Checkpoints'

''' TRAVERSE TESTCASE FILES AND RETURN A SET OF BOARD '''
def get_boards(specific_maps=None):
    os.chdir(path_board)
    list_boards = []
    if specific_maps:
        # Only include specified map files
        list_file = [file for file in specific_maps if file.endswith(".txt") and os.path.isfile(os.path.join(path_board, file))]
    else:
        # Include all .txt files with numeric names
        list_file = [file for file in os.listdir() if file.endswith(".txt") and file.split('.')[0].isdigit()]
    list_file.sort(key=lambda x: int(x.split('.')[0]))
    for file in list_file:
        file_path = os.path.join(path_board, file)
        board = get_board(file_path)
        list_boards.append((file, board))  # Store tuple of (filename, board)
    return list_boards

''' TRAVERSE CHECKPOINT FILES AND RETURN A SET OF CHECKPOINT '''
def get_check_points(specific_maps=None):
    os.chdir(path_checkpoint)
    list_check_point = []
    if specific_maps:
        # Only include specified checkpoint files
        list_file = [file for file in specific_maps if file.endswith(".txt") and os.path.isfile(os.path.join(path_checkpoint, file))]
    else:
        # Include all .txt files with numeric names
        list_file = [file for file in os.listdir() if file.endswith(".txt") and file.split('.')[0].isdigit()]
    list_file.sort(key=lambda x: int(x.split('.')[0]))
    for file in list_file:
        file_path = os.path.join(path_checkpoint, file)
        check_point = get_pair(file_path)
        list_check_point.append((file, check_point))  # Store tuple of (filename, checkpoint)
    return list_check_point

''' FORMAT THE INPUT TESTCASE TXT FILE '''
def format_row(row):
    for i in range(len(row)):
        if row[i] == '1':
            row[i] = '#'
        elif row[i] == 'p':
            row[i] = '@'
        elif row[i] == 'b':
            row[i] = '$'
        elif row[i] == 'c':
            row[i] = '%'

''' FORMAT THE INPUT CHECKPOINT TXT FILE '''
def format_check_points(check_points):
    result = []
    for check_point in check_points:
        result.append([check_point[0], check_point[1]])
    return result

''' READ A SINGLE TESTCASE TXT FILE '''
def get_board(path):
    result = np.loadtxt(f"{path}", dtype=str, delimiter=',')
    for row in result:
        format_row(row)
    return result

''' READ A SINGLE CHECKPOINT TXT FILE '''
def get_pair(path):
    result = np.loadtxt(f"{path}", dtype=int, delimiter=',')
    return result

''' PRINT BOARD STATE '''
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

''' SOKOBAN SOLVE FUNCTION '''
def sokoban_solve(maps, check_points):
    for algorithm in ["Best First Search"]:  # Added A* Search for completeness
        header = f"\n==== Testing Algorithm: {algorithm} ====\n\n"
        print(header.strip()) 
        for map_index, (filename, board) in enumerate(maps):
            board = deepcopy(board)  # Create a copy to avoid modifying original
            # Find matching checkpoint by filename
            checkpoint = None
            for cp_filename, cp in check_points:
                if cp_filename == filename:
                    checkpoint = cp
                    break
            if checkpoint is None:
                print(f"No checkpoint found for {filename}, skipping...")
                continue

            map_title = f"Map {filename}:"
            print(map_title)  # Print to console

            # Print initial board state
            # print("Initial Board:")
            # print_board(board)
            print(f"Checkpoints: {checkpoint}")

            start_time = time.time()

            if algorithm == "Best First Search":
                result = Best_First_Search(board, checkpoint)
            else:
                result = AStart_Search(board, checkpoint)

            end_time = time.time()
            duration = end_time - start_time

            if result:
                steps = len(result[0])
                states_explored = result[1]
                result_text = f"Solution found ({steps} steps, {states_explored} states explored)."

            else:
                result_text = "No solution found."

            time_text = f"Execution time: {duration:.3f} seconds\n"

            print(result_text) 
            print(time_text.strip()) 

''' RUN SOKOBAN FOR SPECIFIC MAPS '''
def sokoban(specific_maps=None):
    maps = get_boards(specific_maps)
    check_points = get_check_points(specific_maps)
    if not maps:
        print("No valid map files found.")
        return
    sokoban_solve(maps, check_points)

if __name__ == "__main__":
    for i in range(1, 3):
        specific_maps = [f"{i}.txt"]
        sokoban(specific_maps)