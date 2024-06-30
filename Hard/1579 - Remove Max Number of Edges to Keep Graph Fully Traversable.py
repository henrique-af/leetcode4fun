class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        # Classe UnionFind para gerenciar os componentes
        class UnionFind:
            def __init__(self, n):
                self.representative = [i for i in range(n + 1)]
                self.component_size = [1] * (n + 1)
                self.components = n

            def find_representative(self, x):
                if self.representative[x] != x:
                    self.representative[x] = self.find_representative(
                        self.representative[x]
                    )
                return self.representative[x]

            def perform_union(self, x, y):
                repr_x = self.find_representative(x)
                repr_y = self.find_representative(y)
                if repr_x == repr_y:
                    return 0
                if self.component_size[repr_x] > self.component_size[repr_y]:
                    self.component_size[repr_x] += self.component_size[repr_y]
                    self.representative[repr_y] = repr_x
                else:
                    self.component_size[repr_y] += self.component_size[repr_x]
                    self.representative[repr_x] = repr_y
                self.components -= 1
                return 1

            def is_connected(self):
                return self.components == 1

        alice = UnionFind(n)
        bob = UnionFind(n)

        edges_required = 0

        for edge in edges:
            if edge[0] == 3:
                edges_required += alice.perform_union(
                    edge[1], edge[2]
                ) | bob.perform_union(edge[1], edge[2])

        for edge in edges:
            if edge[0] == 1:
                edges_required += alice.perform_union(edge[1], edge[2])
            elif edge[0] == 2:
                edges_required += bob.perform_union(edge[1], edge[2])
        if alice.is_connected() and bob.is_connected():
            return len(edges) - edges_required

        return -1


# Exemplo de uso
n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
sol = Solution()
print(sol.maxNumEdgesToRemove(n, edges)) 
