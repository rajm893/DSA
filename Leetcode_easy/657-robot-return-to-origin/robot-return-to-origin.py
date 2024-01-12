class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        steps = {'U':[0,1],
                'D': [0,-1],
                'L': [1,-1],
                'R': [1,1]}

        origin = [0,0]
        for move in moves:
            dir, diff = steps[move]
            origin[dir] += diff
        return origin[0] == origin[1] == 0