def checkmate(board_str: str) -> None:
    if board_str is None:
        print("Error")
        return

    lines = board_str.splitlines()
    if len(lines) == 0:
        print("Error")
        return

    n = len(lines)
    for row in lines:
        if len(row) != n:
            print("Error")
            return

    board = [list(row) for row in lines]

    # หาตำแหน่ง King
    king_pos = None
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'K':
                if king_pos is not None:
                    print("Error")  # เจอ K ซ้ำ
                    return
                king_pos = (r, c)
    if king_pos is None:
        print("Error")  # ไม่มี K เลย
        return

    kr, kc = king_pos

    def in_bounds(r, c):
        return 0 <= r < n and 0 <= c < n

    # --- Pawn ---
    for dc in (-1, 1):
        pr, pc = kr + 1, kc + dc
        if in_bounds(pr, pc) and board[pr][pc] == 'P':
            print("Success")
            return

    # --- Rook / Queen (แนวตรง) ---
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        r, c = kr + dr, kc + dc
        while in_bounds(r, c):
            if board[r][c] != '.':
                if board[r][c] in ('R', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    # --- Bishop / Queen (แนวทแยง) ---
    for dr, dc in [(1,1), (1,-1), (-1,1), (-1,-1)]:
        r, c = kr + dr, kc + dc
        while in_bounds(r, c):
            if board[r][c] != '.':
                if board[r][c] in ('B', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    print("Fail")
