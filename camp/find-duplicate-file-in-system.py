class Solution(object):
    def findDuplicate(self, paths):
        my_dict = defaultdict(list)
        
        for path in paths:
            files = path.split(" ")
            directory = files[0]
            
            for file in files[1:]:
                name, content = file.split("(")
                my_dict[content[:-1]].append(directory + "/" + name)
                
        
        return [my_dict[content] for content in my_dict if len(my_dict[content]) > 1]
        