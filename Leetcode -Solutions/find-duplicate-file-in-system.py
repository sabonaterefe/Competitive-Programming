from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)
        result = []
        
        for path in paths:
            directory, *files = path.split(' ')
            
            for file in files:
                file_name, content = file.split('(')
                content_map[content].append(directory + '/' + file_name)
        
        for paths in content_map.values():
            if len(paths) > 1:
                result.append(paths)
        
        return result