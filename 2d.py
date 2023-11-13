def draw_board(player_1_pieced, player_2_pices):
    for i in range(0,8):
        for j in range(0,8):
            # condition
            print(f"({i},{j})", end="\t")
        print()

