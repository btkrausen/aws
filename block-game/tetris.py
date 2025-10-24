#!/usr/bin/env python3
"""
Simple Tetris game implementation
"""
import random
import sys

# Game constants
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
]


class Tetris:
    def __init__(self):
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.score = 0
        self.game_over = False

    def new_piece(self):
        """Generate a new random tetromino piece"""
        self.current_piece = random.choice(SHAPES)
        self.current_x = BOARD_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_y = 0
        
        if self.check_collision(self.current_piece, self.current_x, self.current_y):
            self.game_over = True

    def check_collision(self, piece, offset_x, offset_y):
        """Check if piece collides with board boundaries or other pieces"""
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell:
                    new_x = offset_x + x
                    new_y = offset_y + y
                    if (new_x < 0 or new_x >= BOARD_WIDTH or 
                        new_y >= BOARD_HEIGHT or
                        (new_y >= 0 and self.board[new_y][new_x])):
                        return True
        return False

    def merge_piece(self):
        """Merge current piece into the board"""
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_y + y][self.current_x + x] = 1

    def clear_lines(self):
        """Clear completed lines and update score"""
        lines_cleared = 0
        y = BOARD_HEIGHT - 1
        while y >= 0:
            if all(self.board[y]):
                del self.board[y]
                self.board.insert(0, [0 for _ in range(BOARD_WIDTH)])
                lines_cleared += 1
            else:
                y -= 1
        self.score += lines_cleared * 100

    def rotate_piece(self):
        """Rotate current piece 90 degrees clockwise"""
        rotated = [[self.current_piece[y][x] 
                    for y in range(len(self.current_piece) - 1, -1, -1)]
                   for x in range(len(self.current_piece[0]))]
        
        if not self.check_collision(rotated, self.current_x, self.current_y):
            self.current_piece = rotated

    def move(self, dx, dy):
        """Move current piece by dx, dy if possible"""
        new_x = self.current_x + dx
        new_y = self.current_y + dy
        
        if not self.check_collision(self.current_piece, new_x, new_y):
            self.current_x = new_x
            self.current_y = new_y
            return True
        return False

    def drop(self):
        """Drop piece one step down"""
        if not self.move(0, 1):
            self.merge_piece()
            self.clear_lines()
            self.new_piece()

    def display(self):
        """Display the current game state"""
        # Create a copy of the board
        display_board = [row[:] for row in self.board]
        
        # Add current piece to display
        if self.current_piece:
            for y, row in enumerate(self.current_piece):
                for x, cell in enumerate(row):
                    if cell and self.current_y + y >= 0:
                        display_board[self.current_y + y][self.current_x + x] = 2
        
        # Print the board
        print("\n" * 50)  # Clear screen (simple method)
        print("=" * (BOARD_WIDTH * 2 + 2))
        print(f"Score: {self.score}")
        print("=" * (BOARD_WIDTH * 2 + 2))
        
        for row in display_board:
            print("|" + "".join("██" if cell else "  " for cell in row) + "|")
        
        print("=" * (BOARD_WIDTH * 2 + 2))
        print("Commands: a=left, d=right, s=down, w=rotate, q=quit")


def main():
    """Main game loop"""
    print("Welcome to Tetris!")
    print("This is a simple demo version.")
    print("Press Enter to start...")
    input()
    
    game = Tetris()
    game.new_piece()
    
    print("\nNote: This is a simplified version for demonstration.")
    print("Use commands: a (left), d (right), s (down), w (rotate), q (quit)")
    print("Press Enter after each command.\n")
    
    while not game.game_over:
        game.display()
        
        try:
            command = input("Command: ").strip().lower()
            
            if command == 'q':
                print("Thanks for playing!")
                break
            elif command == 'a':
                game.move(-1, 0)
            elif command == 'd':
                game.move(1, 0)
            elif command == 's':
                game.drop()
            elif command == 'w':
                game.rotate_piece()
            else:
                game.drop()  # Auto-drop on any other input
                
        except KeyboardInterrupt:
            print("\nGame interrupted. Thanks for playing!")
            break
    
    if game.game_over:
        game.display()
        print("\nGame Over!")
        print(f"Final Score: {game.score}")


if __name__ == "__main__":
    main()
