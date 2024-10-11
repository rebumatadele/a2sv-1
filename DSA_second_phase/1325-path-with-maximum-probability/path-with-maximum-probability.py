class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        graph = defaultdict(list)

        num_edges = len(edges)
        for i in range(num_edges):
            node1, node2, prob = edges[i][0], edges[i][1], succProb[i]
            graph[node1].append((prob, node2))
            graph[node2].append((prob, node1))

        priority_queue = [(-1.0, start)]

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        while priority_queue:
            current_prob, current_node = heapq.heappop(priority_queue)
            current_prob = -current_prob

            if current_node == end:
                return current_prob

            for neighbor_prob, neighbor_node in graph[current_node]:
                new_prob = neighbor_prob * current_prob

                if new_prob > max_prob[neighbor_node]:
                    max_prob[neighbor_node] = new_prob
                    heapq.heappush(priority_queue, (-new_prob, neighbor_node))

        return 0.0
