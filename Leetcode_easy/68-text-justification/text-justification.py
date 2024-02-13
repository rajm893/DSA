class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        line, length = [], 0
        i = 0
        res = []
        while i < len(words):
            if (length + len(line) + len(words[i])) > maxWidth:
                total_spaces   = maxWidth - length
                between_spaces = total_spaces // max(1,len(line)-1)
                remainder = total_spaces % max(1,len(line)-1)

                for j in range(max(1,len(line)-1)):
                    line[j] += " "*between_spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                line, length = [], 0

            line.append(words[i])
            length += len(words[i])
            i += 1
    # handling last line
        lastline = " ".join(line)
        trail_spaces = maxWidth - len(lastline)
        res.append(lastline+" "*trail_spaces)
        return res
