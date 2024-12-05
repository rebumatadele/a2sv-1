class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            amount = int(amount)
            time = int(time)
            if amount > 1000:
                invalid.append(transaction)
                continue
            for j, transaction2 in enumerate(transactions):
                if i != j:
                    name2, time2, amount2, city2 = transaction2.split(",")
                    time2 = int(time2)
                        
                    if name == name2 and city != city2 and abs(time - time2) <= 60:
                        invalid.append(transaction)
                        break
        return invalid



