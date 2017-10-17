class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        cur = 0
        for d in data:
            s = bin(d)[2:]
            s = s[-8:]
            if len(s) < 8:
                s = '0'*(8-len(s)) + s
            if cur > 0:
                if s[0:2] != '10':
                    return False
                cur -= 1
            else:
                for ch in s:
                    cur += int(ch)
                    if ch == '0':
                        break
                if cur == 1 or cur > 4:
                    return False
                cur = max(0, cur-1)
        return cur == 0




def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return []
    return [int(number) for number in input.split(",")]


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            data = stringToIntegerList(line)

            ret = Solution().validUtf8(data)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()