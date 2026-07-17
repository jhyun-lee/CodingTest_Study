def solution(board):
    flat_board = "".join(board)
    o_cnt = flat_board.count("O")
    x_cnt = flat_board.count("X")

    if not (0 <= o_cnt - x_cnt <= 1):
        return 0

    cols = ["".join(col) for col in zip(*board)]
    diags = [
        board[0][0] + board[1][1] + board[2][2],
        board[0][2] + board[1][1] + board[2][0]
    ]
    all_lines = board + cols + diags  
    

    o_win = "OOO" in all_lines
    x_win = "XXX" in all_lines
    

    if o_win and o_cnt != x_cnt + 1:    
        return 0
    if x_win and o_cnt != x_cnt:       
        return 0
        
    return 1