from os import path

class Main:
    def __init__(self, string):
        self.string = string
        self.polindrome = ''

    def main(self):
        s = self.string
        for i in range(1, len(s) - 1):
            if min(i, len(s) - i) * 2 + 1 <= len(self.polindrome):
                continue
            for odd in [1, 0]:
                if s[i + odd] != s[i - 1]:
                    continue
                halfSize = len(path.commonprefix([s[i + odd:], s[:i][::-1]]))
                if 2 * halfSize + odd > len(self.polindrome):
                    longest = s[i - halfSize:i + halfSize + odd]
                    break
        return longest

    def start(self):
        print(self.main())

nio = Main(input('Введіть текст: '))
nio.start()



