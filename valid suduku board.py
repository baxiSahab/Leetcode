def isValidSudoku(board):
    
    
    row_set = []
    for i in range(9):
        for j in range(9):
            item = board[i][j]
            if item in row_set: return False
            if item == '.': continue
            row_set.append(item)
        row_set = []
    
    col_set = []
    for j in range(9):
        for i in range(9):
            item = board[i][j]
            if item in col_set: return False
            if item == '.': continue
            col_set.append(item)
        col_set = []

    box_set = []

    for box_n in range(9):
        row_start = (box_n // 3 )*3
        col_start = (box_n %3)*3

        for i in range(row_start , row_start + 3):
            for j in range(col_start , col_start + 3):
                item = board[i][j]
                if item in box_set: return False
                if item == '.': continue
                box_set.append(item)
        box_set = []

    return True
    
    # ===== TEST CASES =====

def run_tests():
# Test Case 1: Valid Sudoku board
    board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
    result1 = isValidSudoku(board1)
    print(f"Test 1 - Valid board: {result1}")
    print(f"Expected: True\n")

    # Test Case 2: Invalid - duplicate in row
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    result2 = isValidSudoku(board2)
    print(f"Test 2 - Duplicate in first column (two 8's): {result2}")
    print(f"Expected: False\n")

    # Test Case 3: Invalid - duplicate in column
    board3 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    result3 = isValidSudoku(board3)
    print(f"Test 3 - Duplicate in column (two 5's in col 0): {result3}")
    print(f"Expected: False\n")

    # Test Case 4: Invalid - duplicate in 3x3 box
    board4 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        ["5","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    result4 = isValidSudoku(board4)
    print(f"Test 4 - Duplicate in first 3x3 box (two 5's): {result4}")
    print(f"Expected: False\n")

    # Test Case 5: Empty board (all dots)
    board5 = [
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",]
    ]
    result5 = isValidSudoku(board5)
    print(f"Test 5 - Empty board: {result5}")
    print(f"Expected: True\n")

    # Test Case 6: Single valid number
    board6 = [
        ["1",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",],
        [".",".",".",".",".",".",".",".",".",]
    ]
    result6 = isValidSudoku(board6)
    print(f"Test 6 - Single number: {result6}")
    print(f"Expected: True\n")


if __name__ == "__main__":
    run_tests()


    #  # TODO: Add your solution here
   
    # for i in range(9):
    #     row_set = set()
    #     for j in range(9):
    #         if board[i][j] == '.':
    #            continue 
    #         if board[i][j] in row_set:
    #             return False
    #         else:
    #             row_set.add(board[i][j])

    # col_set = ()

    # for i in range(9):
    #     col_set = set()
    #     for j in range(9):
    #         if board[j][i] == '.':
    #            continue 
    #         if board[j][i] in col_set:
    #             return False
    #         else: 
    #             col_set.add(board[j][i])

    # for box in range(9):
    #     box_set = set()

    #     row_start = (box // 3) * 3
    #     col_start = (box % 3) * 3

    #     for i in range(row_start, row_start+3):

    #         for j in range(col_start, col_start+3):

    #             if board[i][j] == '.':
    #                 continue
    #             if board[i][j] in box_set:
    #                 return False
    #             else:
    #                 box_set.add(board[i][j])


    # return True