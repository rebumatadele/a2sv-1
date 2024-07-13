class Solution:
    def groupAnagrams(self, strs):
        dic = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            dic[sorted_word].append(word)
        
        return list(dic.values())