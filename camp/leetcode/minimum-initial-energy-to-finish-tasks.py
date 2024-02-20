class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(reverse = True, key = lambda x: x[1]-x[0])

        min_energy = tasks[0][1]
        curr_energy = min_energy - tasks[0][0]

        for i in range(1,len(tasks)):
            if curr_energy < tasks[i][1]:
                min_energy += (tasks[i][1] - curr_energy)
                curr_energy = tasks[i][1]
            curr_energy -= tasks[i][0]

        return min_energy
