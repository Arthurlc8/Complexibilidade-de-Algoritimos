class AFDTerminaEm01:
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
                self.state = 'q1'
            else:  # char == '1'
                self.state = 'q0'

    def is_accepted(self, string):
        for char in string:
            if char not in {'0', '1'}:
                raise ValueError("A string deve conter apenas '0' e '1'.")
            self.transition(char)
        return self.state == 'q2'

afd = AFDTerminaEm01()
test_strings = ["01", "10", "001", "110", "0101", "1001", "000", "111"]

for s in test_strings:
    result = afd.is_accepted(s)
    print(f"A string '{s}' é aceita? {'Sim' if result else 'Não'}")