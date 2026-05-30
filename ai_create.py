import tkinter as tk
import random

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SPEED = 150


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("贪吃蛇")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            root,
            width=GRID_WIDTH * CELL_SIZE,
            height=GRID_HEIGHT * CELL_SIZE,
            bg="black",
        )
        self.canvas.pack()

        self.frame = tk.Frame(root)
        self.frame.pack(fill="x", padx=5, pady=5)

        self.score_label = tk.Label(self.frame, text="得分: 0", font=("Arial", 14))
        self.score_label.pack(side="left")

        self.status_label = tk.Label(self.frame, text="按空格开始", font=("Arial", 14))
        self.status_label.pack(side="right")

        self.root.bind("<KeyPress>", self.on_key)
        self.reset_game()
        self.draw()

    def reset_game(self):
        cx, cy = GRID_WIDTH // 2, GRID_HEIGHT // 2
        self.snake = [(cx, cy), (cx - 1, cy), (cx - 2, cy)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.food = self.spawn_food()
        self.score = 0
        self.running = False
        self.game_over = False
        self.score_label.config(text="得分: 0")
        self.status_label.config(text="按空格开始")

    def spawn_food(self):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if pos not in self.snake:
                return pos

    def on_key(self, event):
        key = event.keysym
        if key == "space":
            if self.game_over:
                self.reset_game()
                self.draw()
            elif not self.running:
                self.running = True
                self.status_label.config(text="游戏中")
                self.game_loop()
            return

        direction_map = {
            "Up": (0, -1),
            "Down": (0, 1),
            "Left": (-1, 0),
            "Right": (1, 0),
            "w": (0, -1),
            "s": (0, 1),
            "a": (-1, 0),
            "d": (1, 0),
        }
        if key in direction_map:
            new_dir = direction_map[key]
            if (new_dir[0] + self.direction[0], new_dir[1] + self.direction[1]) != (0, 0):
                self.next_direction = new_dir

    def game_loop(self):
        if not self.running:
            return
        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        if (
            new_head[0] < 0
            or new_head[0] >= GRID_WIDTH
            or new_head[1] < 0
            or new_head[1] >= GRID_HEIGHT
            or new_head in self.snake
        ):
            self.game_over = True
            self.running = False
            self.status_label.config(text="游戏结束! 按空格重新开始")
            self.draw()
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 10
            self.score_label.config(text=f"得分: {self.score}")
            self.food = self.spawn_food()
        else:
            self.snake.pop()

        self.draw()
        self.root.after(SPEED, self.game_loop)

    def draw(self):
        self.canvas.delete("all")
        # 食物
        fx, fy = self.food
        self.canvas.create_rectangle(
            fx * CELL_SIZE, fy * CELL_SIZE,
            (fx + 1) * CELL_SIZE, (fy + 1) * CELL_SIZE,
            fill="red",
        )
        # 蛇身
        for i, (x, y) in enumerate(self.snake):
            color = "#00ff00" if i == 0 else "#00cc00"
            self.canvas.create_rectangle(
                x * CELL_SIZE, y * CELL_SIZE,
                (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                fill=color,
            )
        if self.game_over:
            self.canvas.create_text(
                GRID_WIDTH * CELL_SIZE // 2,
                GRID_HEIGHT * CELL_SIZE // 2,
                text="GAME OVER",
                fill="white",
                font=("Arial", 36, "bold"),
            )


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
