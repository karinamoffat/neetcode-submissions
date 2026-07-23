class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            # first we check if adding the new word goes over the limit
            if len(words[i]) + length + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            # if no, add word
            else:
                totalSpaces = maxWidth - length
                basePad = totalSpaces//(max(1, len(line) - 1))
                extraSpaces = totalSpaces % (max(1, len(line) - 1))

                for j in range(max(1, len(line) -1)):
                    line[j] = line[j]+(" " * basePad)
                    if extraSpaces > 0:
                        line[j]= line[j]+(" ")
                        extraSpaces -= 1
                res.append("".join(line))
                line = []
                length = 0
        line = " ".join(line)
        totalSpaces = maxWidth - len(line)
        line = line + " " * totalSpaces
        res.append(line)

        return res
