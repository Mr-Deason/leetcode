class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        off = [0]
        depth = 0
        length = 0
        ans = 0
        flag = 0
        input += '\n'
        for ch in input:
            if ch == '\n':
                if depth <= len(off):
                    off = off[:depth+1]
                if flag == 1:
                    ans = max(ans, off[-1]+depth+length)
                else:
                    off += [off[-1] + length]
                depth = length = flag = 0
            elif ch == '\t':
                depth += 1
            else:
                if ch == '.':
                    flag = 1
                length += 1
            #print off, depth
        return ans



def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            input = stringToString(line)

            ret = Solution().lengthLongestPath(input)

            out = str(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()