class AFNSequenciasAB:
    def _init_(self):
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0':
            if char == 'a':
                self.state = 'q1'
            elif char == 'b':
                self.state = 'q_invalid'
        elif self.state == 'q1':
            if char == 'a':
                self.state = 'q1'
            elif char == 'b':
                self.state = 'q1'  # continua aceitando b
        elif self.state == 'q_invalid':
            self.state = 'q_invalid'

    def is_accepted(self, string):
        for char in string:
            if char not in {'a', 'b'}:
                raise ValueError("A string deve conter apenas 'a' e 'b'.")
            self.transition(char)
        return self.state in {'q0', 'q1'}

afd = AFNSequenciasAB()
test_strings = ["", "a", "b", "ab", "aa", "ba", "aab", "bba", "aaab", "abab"]

for s in test_strings:
    result = afd.is_accepted(s)
    print(f"A string '{s}' é aceita? {'Sim' if result else 'Não'}")