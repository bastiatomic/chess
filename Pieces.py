class ChessPiece:
    def __init__(self, name, symbol, fen):
        self.name = name
        self.symbol = symbol
        self.fen = fen

chess_pieces = {
    "K": ChessPiece("WHITE_KING", "♔", "K"),
    "Q": ChessPiece("WHITE_QUEEN", "♕", "Q"),
    "R": ChessPiece("WHITE_ROOK", "♖", "R"),
    "B": ChessPiece("WHITE_BISHOP", "♗", "B"),
    "N": ChessPiece("WHITE_KNIGHT", "♘", "N"),
    "P": ChessPiece("WHITE_PAWN", "♙", "P"),
    "k": ChessPiece("BLACK_KING", "♚", "k"),
    "q": ChessPiece("BLACK_QUEEN", "♛", "q"),
    "r": ChessPiece("BLACK_ROOK", "♜", "r"),
    "b": ChessPiece("BLACK_BISHOP", "♝", "b"),
    "n": ChessPiece("BLACK_KNIGHT", "♞", "n"),
    "p": ChessPiece("BLACK_PAWN", "♟", "p")
}