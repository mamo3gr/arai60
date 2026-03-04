class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parents = [i for i in range(n)]
        num_components = n

        for edge in edges:
            a, b = edge
            if parents[a] == parents[b]:
                continue

            parents_from = parents[b]
            parents_to = parents[a]
            for i in range(n):
                if parents[i] == parents_from:
                    parents[i] = parents_to
            num_components -= 1

        return num_components
