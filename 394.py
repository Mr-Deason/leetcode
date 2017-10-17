class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [[1, '']]
        cnt = 0
        scnt = ''
        for ch in s:
            if ch.isdigit():
                scnt += ch
            elif ch.isalpha():
                stack[-1][1] += ch
            elif ch == '[':
                cnt = int(scnt)
                scnt = ''
                stack += [[cnt, '']]
            else:
                stack[-2][1] += stack[-1][0]*stack[-1][1]
                stack.pop()
            #print stack

        return stack[0][1]



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
            s = stringToString(line)

            ret = Solution().decodeString(s)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()