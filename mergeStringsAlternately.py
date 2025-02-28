class mergeStringsAlternately:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x : int = 0
        newWord : str = ""
        while(x < len(word1) or x < len(word2)):
            if(x < len(word1)):
                newWord += word1[x]
            if(x < len(word2)):
                newWord += word2[x]
            x += 1
        return newWord
            