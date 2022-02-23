class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         def get_key(log):
#             _id, rest = log.split(" ", maxsplit=1)
#             return (0, rest, _id) if rest[0].isalpha() else (1, )

#         return sorted(logs, key=get_key)
        
        
        digits = []
        letters = []
	
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key = lambda x: x.split()[0])
        letters.sort(key = lambda x: x.split()[1:])           
        result = letters + digits                                       
        
        return result