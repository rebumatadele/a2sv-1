class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        print(processorTime)
        p = len(processorTime)
        total = 0
        for i in range(len(processorTime)):
    
            total =max(processorTime[i] + max(tasks[i*4:(i*4)+4]), total) 
        print(total)
        return total