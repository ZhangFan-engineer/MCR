# Auther:zhangfan, 72510130,ZhangFan-engineer
# Reviewer:yanxi jiang, 72510210, pawsey0319
# Reviewer:chaijingyue,72510928,winderEmail
# Reviewer:殷浩然, 72510941, chuisan

def is_win(game):
    """判断是否有玩家获胜"""
    win = False
    
    # 检查所有行
    if game[2][0] == game[2][1] == game[2][2] and game[2][0] in ('X', 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and game[1][0] in ('X', 'O'):
        win = True
    if game[0][0] == game[0][1] == game[0][2] and game[0][0] in ('X', 'O'):
        win = True
    
    # 检查所有列
    if game[0][1] == game[1][1] == game[2][1] and game[0][1] in ('X', 'O'):
        win = True
    if game[0][0] == game[1][0] == game[2][0] and game[0][0] in ('X', 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and game[0][2] in ('X', 'O'):
        win = True
    
    # 检查两条对角线
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] in ('X', 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] in ('X', 'O'):
        win = True
    
    return win

def print_board(game):
    """打印当前棋盘状态"""
    for row in game:
        print(" ".join(row))
    print()

def main():
    # 初始化3x3棋盘
    game = [[' ' for _ in range(3)] for _ in range(3)]
    player1 = 'X'
    player2 = 'O'
    turn = False  # False为玩家1回合，True为玩家2回合，玩家1先行
    
    print("X = Player 1")
    print("O = Player 2\n")
    
    # 游戏主循环，最多9个回合
    for n in range(9):
        # 提示当前玩家输入
        if not turn:
            coords = input("Player 1: Which cell to mark? i:[1..3], j:[1..3 ]: ")
        else:
            coords = input("Player 2: Which cell to mark? i:[1..3], j:[1..3 ]: ")
        
        # 解析输入坐标
        i, j = map(int, coords.split())
        
        # 坐标转换：将1-3转换为0-2，避免列表越界
        i -= 1
        j -= 1
        
        # 根据当前回合放置相应棋子
        if not turn:
            game[i][j] = player1
        else:
            game[i][j] = player2
        
        # 检查是否有玩家获胜
        if is_win(game):
            print(f"Player {2 if turn else 1} Wins!")
            print("Final Board:")
            print_board(game)
            return
        
        # 输出当前棋盘状态
        print("Current Board:")
        print_board(game)
        
        # 切换回合
        turn = not turn
    
    # 如果所有回合结束仍无胜者，则为平局
    print("Tie!")
    print("Final Board:")
    print_board(game)

if __name__ == "__main__":
    main()
