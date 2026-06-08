class Solution:
    def addBinary(self, a: str, b: str):
        result = []
        carry = 0 

        i, j = len(a)-1, len(b) -1

        while (i >= 0 or j >= 0 or carry ):

            total = carry

            if i >= 0 :
                total = total + int(a[i])
                i -=1
            if j >= 0 :
                total = total + int(b[j])
                j -=1
                
            result.append(str(total % 2))
            carry = total // 2
            
        return ''.join(reversed(result))
        
        
s = Solution()
print(s.addBinary("1011", "1101")) # expected output: "11000"
