#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.flags = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2}", end=' ')
            for x in range(self.width):
                if reveal:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    if self.flags[y][x]:
                        print('F', end=' ')
                    elif self.revealed[y][x]:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                    else:
                        print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if self.revealed[y][x]:
            print("Cell already revealed!")
            return True
        if self.flags[y][x]:
            print("Cell is flagged! Unflag before revealing.")
            return True

        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def toggle_flag(self, x, y):
        if self.revealed[y][x]:
            print("You cannot flag a revealed cell!")
        else:
            self.flags[y][x] = not self.flags[y][x]

    def is_won(self):
        for y in range(self.height):
            for x in range(self.width):
                if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                move = input("Enter move (R x y to reveal, F x y to flag): ").split()
                if len(move) != 3:
                    print("Invalid input. Use format: R x y or F x y")
                    continue

                action, x, y = move[0].upper(), int(move[1]), int(move[2])
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of range.")
                    continue

                if action == "R":
                    if not self.reveal(x, y):
                        self.print_board(reveal=True)
                        print("💥 Game Over! You hit a mine.")
                        break
                elif action == "F":
                    self.toggle_flag(x, y)
                else:
                    print("Invalid action. Use R (reveal) or F (flag).")

                if self.is_won():
                    self.print_board(reveal=True)
                    print("🎉 Congratulations! You cleared the field!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers for x and y.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
