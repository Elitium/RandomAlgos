class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        tot = n + n
        def finalPar(past, count, tots):
            if len(past) == tot:
                res.append(past)
                return
            elif count == 0:
                finalPar(past + "(", 1, tots+1)
            else:
                if tots != n:
                    finalPar(past + "(", count+1, tots+1)
                finalPar(past + ")", count-1, tots)
        
        finalPar("(",1, 1)
        return res

