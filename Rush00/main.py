# main.py
from checkmate import checkmate

def main():
    board = """\
R...
....
..P.
..K."""
    # ตัวอย่างบอร์ดเดียว: Rook ยิงตรงได้, Pawn ก็อยู่ใกล้ K ด้วย
    checkmate(board)  # expected: Success

if __name__ == "__main__":
    main()
