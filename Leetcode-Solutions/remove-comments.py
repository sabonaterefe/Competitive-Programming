class Solution:
    def removeComments(self, source:List[str])->List[str]:
        result = []
        in_block_comment = False
        new_line = ""
        
        for line in source:
            i = 0
            while i < len(line):
                if line[i:i+2] == "//" and not in_block_comment:
                    break
                elif line[i:i+2] == "/*" and not in_block_comment:
                    in_block_comment = True
                    i += 1
                elif line[i:i+2] == "*/" and in_block_comment:
                    in_block_comment = False
                    i += 1
                elif not in_block_comment:
                    new_line += line[i]
                i += 1
            
            if new_line and not in_block_comment:
                result.append(new_line)
                new_line = ""
        
        return result
