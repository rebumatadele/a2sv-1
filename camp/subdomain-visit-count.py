class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import defaultdict
        my_dict = defaultdict(int)
        for values in cpdomains:
           lst = values.split()
           count = int(lst[0])
           lst2 = lst[1].split(".")
           for i in range(len(lst2)):
               subdomain = ".".join(lst2[i:])
               my_dict[subdomain] +=count
            
        result = [f"{count} {subdomain}" for subdomain, count in my_dict.items()]
        return(result)     
