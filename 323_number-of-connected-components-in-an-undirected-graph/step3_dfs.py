import collections


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        node_to_neighbors = collections.defaultdict(list)
        for a, b in edges:
            node_to_neighbors[a].append(b)
            node_to_neighbors[b].append(a)

        visited = set()
        num_components = 0

        def mark_connected_components(start: int) -> None:
            frontier = [start]
            while frontier:
                node = frontier.pop()
                if node in visited:
                    continue
                visited.add(node)
                frontier.extend(node_to_neighbors[node])

        for i in range(n):
            if i in visited:
                continue
            num_components += 1
            mark_connected_components(i)

        return num_components
