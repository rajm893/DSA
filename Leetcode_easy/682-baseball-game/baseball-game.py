class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for i in range(len(operations)):
            if operations[i] == "C":
                res.pop()

            elif operations[i] == "D":
                tmp = 2*res[-1]
                res.append(tmp)
    
            elif operations[i] == "+":
                tmp = res[-1]+res[-2]
                res.append(tmp)
            else:
                res.append(int(operations[i]))

        return sum(res)