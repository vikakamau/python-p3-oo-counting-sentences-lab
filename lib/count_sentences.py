class MyString:
    def __init__(self, value=""):
        self._value = value

    def get_string(self):
        return self._value

    def set_string(self, value):
        if type(value) is not str:
            print("The value must be a string.")
        else:
            self._value = value

    value = property(get_string, set_string)

    def is_sentence(self):
        return self._value.endswith('.') if self._value else False
    def is_question(self):
        return self._value.endswith('?') if self._value else False
    def is_exclamation(self):
        return self._value.endswith('!') if self._value else False
    def count_sentences(self):
      value = self.value.replace('!', '.').replace('?', '.')
      sentences = [s for s in value.split('.') if s]
      return len(sentences)

    @classmethod
    def from_string(cls, value):
        return cls(value)
