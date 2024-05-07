import numpy as np
import matplotlib.pyplot as plt

class GridWorld:
    def __init__(self):
        self.grid = np.array([
            ["Robot", "", "", ""],
            ["", "Fire", "", ""],
            ["Key", "", "", "Deliver"],
            ["", "", "Letter", ""]
        ])
        self.robot_position = (0, 0)
        self.fig, self.ax = plt.subplots(figsize=(8, 8))  
        self.texts = []
        self.initialize_plot()

    def initialize_plot(self):
        self.ax.set_xlim(-0.5, len(self.grid[0]) - 0.5)
        self.ax.set_ylim(-0.5, len(self.grid) - 0.5)

        for x in range(len(self.grid[0]) + 1):
            self.ax.axvline(x - 0.5, color='black', linewidth=2)
        for y in range(len(self.grid) + 1):
            self.ax.axhline(y - 0.5, color='black', linewidth=2)

        self.ax.set_xticks([])
        self.ax.set_yticks([])

        for i in range(len(self.grid)):
            row_texts = []
            for j in range(len(self.grid[i])):
                text = self.ax.text(j, i, self.grid[i][j], va='center', ha='center', fontsize=10)
                row_texts.append(text)
            self.texts.append(row_texts)

    def update_robot_position(self, new_position):
        old_position = self.robot_position
        self.texts[old_position[0]][old_position[1]].set_text('')
        self.robot_position = new_position
        self.texts[new_position[0]][new_position[1]].set_text('Robot')
        self.fig.canvas.draw()

    def show(self):
        plt.show() 


if __name__ == "__main__":
    env = GridWorld()
    env.show()  
