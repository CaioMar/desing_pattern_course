
class Sentence:
    def __init__(self, plain_text):
        self.plain_text = plain_text.split()
        self._cap_index = {}

    class Token:
        def __init__(self, index, capitalize=False):
            self.index = index
            self.capitalize = capitalize


    def _get_token(self, index):
        for token in self._cap_index:
            if index == token.index:
                return token
        return

    def __getitem__(self, index):
        token = self._get_token(index)
        if not isinstance(token, self.Token):
            token = self.Token(index)
            self._cap_index[index] = token
        return token    

    def __str__(self):
        result = []
        for index, word in enumerate(self.plain_text):
            if index in self._cap_index.keys():
                if self._cap_index[index].capitalize:
                    word = word.upper()
            result.append(word)
        return ' '.join(result)

if __name__ == "__main__":
    
    sentence = Sentence("Hello world I'm an awesome Data Scientist")
    sentence[5].capitalize = True
    print(sentence)
