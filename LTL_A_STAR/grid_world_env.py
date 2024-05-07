import numpy as np
import matplotlib.pyplot as plt

class GridWorld:
    def __init__(self):
       
        self.grid = np.array([
            ["Robot", "", "", ""],
            ["", "Fire", "", "Letter"],
            ["", "", "", ""],
            ["Key", "", "", "Deliver"]
        ])

    def show(self):
        
        fig, ax = plt.subplots(figsize=(8, 8))  
        ax.set_xlim(-0.5, len(self.grid[0]) - 0.5)
        ax.set_ylim(-0.5, len(self.grid) - 0.5)

    
        for x in range(len(self.grid[0]) + 1):
            ax.axvline(x - 0.5, color='black', linewidth=2)
        for y in range(len(self.grid) + 1):
            ax.axhline(y - 0.5, color='black', linewidth=2)

       
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]:
                    ax.text(j, i, self.grid[i][j], va='center', ha='center', fontsize=12)

        plt.show()

if __name__ == "__main__":
    env = GridWorld()
    env.show()
