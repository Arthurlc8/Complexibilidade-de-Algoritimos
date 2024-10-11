class AFNComprimentoPar:
    def _init_(self):
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0':
            self.state = 'q1'
        elif self.state == 'q1':
            self.state = 'q0'

    def is_accepted(self, string):
        for char in string:
            if char not in {'a', 'b'}:
                raise ValueError("A string deve conter apenas 'a' e 'b'.")
            self.transition(char)
        return self.state == 'q0'

afd = AFNComprimentoPar()
test_strings = ["", "a", "b", "ab", "ba", "aa", "bb", "aabb", "abab"]

for s in test_strings:
    result = afd.is_accepted(s)
    print(f"A string '{s}' é aceita? {'Sim' if result else 'Não'}")