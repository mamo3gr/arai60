import collections


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        DFSによる解法。

        inspired from:
        https://github.com/Hiroto-Iizuka/coding_practice/pull/19
        """
        node_to_neighbors: dict[int, list[int]] = collections.defaultdict(list)
        for edge in edges:
            a, b = edge
            node_to_neighbors[a].append(b)
            node_to_neighbors[b].append(a)

        visited = set()
        num_components = 0

        def mark_neighbors_visited(i: int):
            for neighbor in node_to_neighbors[i]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                mark_neighbors_visited(neighbor)

        for i in range(n):
            if i in visited:
                continue

            visited.add(i)
            mark_neighbors_visited(i)
            num_components += 1

        return num_components
