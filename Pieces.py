class ChessPiece:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

WHITE_KING = ChessPiece("WHITE_KING", "♔")
WHITE_QUEEN = ChessPiece("WHITE_QUEEN", "♕")
WHITE_ROOK = ChessPiece("WHITE_ROOK", "♖")
WHITE_BISHOP = ChessPiece("WHITE_BISHOP", "♗")
WHITE_KNIGHT = ChessPiece("WHITE_KNIGHT", "♘")
WHITE_PAWN = ChessPiece("WHITE_PAWN", "♙")
BLACK_KING = ChessPiece("BLACK_KING", "♚")
BLACK_QUEEN = ChessPiece("BLACK_QUEEN", "♛")
BLACK_ROOK = ChessPiece("BLACK_ROOK", "♜")
BLACK_BISHOP = ChessPiece("BLACK_BISHOP", "♝")
BLACK_KNIGHT = ChessPiece("BLACK_KNIGHT", "♞")
BLACK_PAWN = ChessPiece("BLACK_PAWN", "♟")