class AFNSubstring010:
    def _init_(self):
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0':
            if char == '0':
                self.state = 'q1'
            else:  # char == '1'
                self.state = 'q0'
        elif self.state == 'q1':
            if char == '0':
                self.state = 'q1'
            else:  # char == '1'
                self.state = 'q2'
        elif self.state == 'q2':
            if char == '0':
                self.state = 'q3'
            else:  # char == '1'
                self.state = 'q0'
        elif self.state == 'q3':
            self.state = 'q3'

    def is_accepted(self, string):
        for char in string:
            if char not in {'0', '1'}:
                raise ValueError("A string deve conter apenas '0' e '1'.")
            self.transition(char)
        return self.state == 'q3'

afd = AFNSubstring010()
test_strings = ["010", "0010", "1001", "110", "0101", "10010", "000", "111"]

for s in test_strings:
    result = afd.is_accepted(s)
    print(f"A string '{s}' é aceita? {'Sim' if result else 'Não'}")