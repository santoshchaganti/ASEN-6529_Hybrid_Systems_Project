import heapq
import imageio
import io
class AStar:
    def __init__(self, automaton, start, goal):
        self.automaton = automaton
        self.start = start
        self.goal = goal

    def heuristic(self, state):
        return abs(state[0][0] - self.goal[0][0]) + abs(state[0][1] - self.goal[0][1])

    def search(self):
        frontier = []
        heapq.heappush(frontier, (0, self.start))
        came_from = {self.start: None}
        cost_so_far = {self.start: 0}

        while frontier:
            _, current = heapq.heappop(frontier)

            if current == self.goal:
                break

            for next in self.automaton.transitions.get(current, []):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(next)
                    heapq.heappush(frontier, (priority, next))
                    came_from[next] = current

       
        if self.goal not in came_from:
            return None

        return self.reconstruct_path(came_from, self.start, self.goal)

    def reconstruct_path(self, came_from, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path
    
    def create_path_gif(self):
        path_to_key = self.astar(self.robot_position, self.key_position)
        path_to_letter = self.astar(path_to_key[-1], self.letter_position)
        path_to_delivery = self.astar(path_to_letter[-1], self.deliver_position)
        complete_path = path_to_key + path_to_letter[1:] + path_to_delivery[1:]

        frames = []
        for i in range(len(complete_path)):
            fig = self.draw_grid(complete_path[:i+1])
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)
            frame = imageio.imread(buf)
            frames.append(frame)
            buf.close()

        imageio.mimsave('path_animation.gif', frames, duration=0.5)


def run_a_star(automaton, start, goal):
    a_star = AStar(automaton, start, goal)
    return a_star.search()


