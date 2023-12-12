class Depth_First_Search:
    def __init__(self):
        self.data = None
        self.visited = None
        self.component = None
        self.result = None

    def fit(self, data: dict, start: str):
        self.data = data
        self.visited = set()
        self._dfs(start)

    def _dfs(self, node):  # function for dfs
        if node not in self.visited:
            print(node)
            self.visited.add(node)
            for neighbour in self.data[node]:
                self._dfs(neighbour)
