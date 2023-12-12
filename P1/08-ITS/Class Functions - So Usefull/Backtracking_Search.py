class Backtracking_search:
    def __init__(self):
        self.data = None
        self.path = None
        self.visited = None

    def fit(self, data: dict, start: str, end: str, approach: str = "R"):
        """
        param:
            data: dictionary: key = starting point, value = list of ending points
            start: string: starting point
            end: string: ending point
            approach: string: "R" for recursive method or "NR" for not recursive method. default "R".

        return:
            None. but you can use self.path for seeing the path for reaching the end point from start point.
        """
        self.data = data
        if approach == "R":
            path = self._R_solve_maze(start, end, path=[start], visited=[start])
            self.path = path
        elif approach == "NR":
            self.path = self._NR_solve_maze(start, end)

    def _NR_solve_maze(self, start: str, end: str):
        """Source: https://www.youtube.com/watch?v=gBC_Fd8EE8A"""
        path = [start]
        current_point = start
        visited = [start]
        while current_point != end and path != []:
            for next_point in self.data[current_point]:
                if next_point not in visited:
                    visited.append(next_point)
                    path.append(current_point)
                    current_point = next_point
                    break
            else:
                current_point = path.pop()
        if current_point == end:
            path.append(current_point)
            path.pop(0)
        return path

    def _R_solve_maze(self, start: str, end: str, path: list, visited: list):
        """Source: https://www.youtube.com/watch?v=gBC_Fd8EE8A"""
        if start == end:
            return path
        for next_point in self.data[start]:
            if next_point not in visited:
                path.append(next_point)
                visited.append(next_point)
                path_new = self._R_solve_maze(next_point, end, path, visited)
                if path_new:
                    path = path_new
                    return path
                else:
                    path.pop()
        return []
