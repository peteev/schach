if piece_board[piecerow][piececolumn].farbe == "w":
        whitecount += 1
    if piece_board[piecerow][piececolumn].farbe == "b":
        blackcount += 1
    if whitecount < blackcount:
        blackcount -= 1
    if whitecount-2 >= blackcount:
        whitecount -= 1