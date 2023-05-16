class StringUtility():
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def vowels(self):
        vows = ["a","e","i","o","u","y"]
        count = 0
        for i in self.string:
            if (i in vows):
                count += 1
        if (count < 5):
            return str(count)
        else:
            return "many"

    def bothEnds(self):
        bEnds = ""
        if (len(self.string) > 2):
            return self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
        else:
            return ""

    def fixStart(self):
        if len(self.string) > 1:
            first = self.string[0]
            build = first
            count = 0
            for i in range(1, len(self.string)):
                if self.string[i] == first:
                    build += "*"
                    count += 1
                else:
                    build += self.string[i]            
            return build
        else:
            return self.string

    def asciiSum(self):
        ascSum = 0
        for i in self.string:
            ascSum += ord(i)
        return ascSum

    def cipher(self):
        build = ""
        inc = len(self.string)
        asc = 0
        for i in self.string:
            if (ord(i) >= ord("A")) and (ord(i) <= ord("Z")) or (ord(i) >= ord("a")) and (ord(i) <= ord("z")):
                if (ord(i) >= ord("A")) and (ord(i) <= ord("Z")):
                    isCap = True
                else:
                    isCap = False
                asc = ord(i) + inc
                if (asc > ord("z")) and (not isCap):
                    diff = (ord("z") - ord(i)) + 1
                    thresh = ord("z") - (ord(i))
                    if inc-diff > thresh:
                        asc = ord("a") + ((inc-diff) - thresh) - (ord(i) - ord("a") + 1)
                    else:
                        asc = ord("a") + (inc-diff)
                elif (asc > ord("Z")) and isCap:
                    diff = (ord("Z") - ord(i)) + 1
                    thresh = ord("Z") - (ord(i))
                    if inc-diff > thresh:
                        asc = ord("A") + ((inc-diff) - thresh) - (ord(i) - ord("A") + 1)
                    else:
                        asc = ord("A") + (inc-diff)
                char = chr(asc)
                build += char
            else:
                build += i
        return build


    
