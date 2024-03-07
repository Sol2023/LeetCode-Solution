class Solution:
    def compress(self, chars: List[str]) -> int:

        final_index = 0
        index = 0

        while index< len(chars):

            current_char = chars[index]
            count=0

            while index < len(chars) and current_char == chars[index]:
                index+=1
                count+=1
            
            chars[final_index]=current_char
            final_index+=1

            if count!=1:
                for s in str(count):
                    chars[final_index]=s
                    final_index+=1
        
        return final_index
        