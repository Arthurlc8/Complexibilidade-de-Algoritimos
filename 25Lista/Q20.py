class AFDSequenciaAbUmaVez:
    def _init_(self):
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0':
            if char == 'a':
                self.state = 'q1'
            else:  # char == 'b'
                self.state = 'q0'
        elif self.state == 'q1':
            if char == 'a':
                self.state = 'q1'
            elif char == 'b':
                self.state = 'q2'
        elif self.state == 'q2':
            if char == 'a':
                self.state = 'q1'
            elif char == 'b':
                self.state = 'q3'
        elif self.state == 'q3':
            self.state = 'q3'  # permanece no estado não aceito

    def is_accepted(self, string):
        for char in string:
            if char not in {'a', 'b'}:
                raise ValueError("A string deve conter apenas 'a' e 'b'.")
            self.transition(char)
        return self.state == 'q2'

afd = AFDSequenciaAbUmaVez()
test_strings = ["ab", "aab", "abab", "bba", "ba", "abb", "aaab", "aaaab", "abbbbb", "b"]

for s in test_strings:
    result = afd.is_accepted(s)
    print(f"A string '{s}' é aceita? {'Sim' if result else 'Não'}")
