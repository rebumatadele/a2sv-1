class Solution:
    def bestClosingTime(self, customers: str) -> int:
        current = total = customers.count('Y')
        res = 0
        for j in range(len(customers)):
            total += 1 if customers[j] == 'N' else -1 
            if total < current:
                current = total
                res = j + 1

        return res