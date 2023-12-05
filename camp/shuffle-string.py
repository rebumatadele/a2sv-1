class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_str = [""]*len(indices)
        for i, value in enumerate(indices):
            shuffled_str[value]= s[i]
        shuffled_str = "".join(map(str,shuffled_str))
        return shuffled_str
