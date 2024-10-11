class AFDUmZero:
    def _init_(self):
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0':
            if char == '0':
                self.state = 'q1'
            elif char == '1':
                self.state = 'q0'
        elif self.state == 'q1':
            if char == '0':
                self.state = 'q1'
            elif char == '1':
                self.state = 'q1'

    def is_accepted(self, string):
        for char in string:
            if char not in {'0', '1'}:
                raise ValueError("A string deve conter apenas '0' e '1'.")
            self.transition(char)
        return self.state == 'q1'

afd = AFDUmZero()
test_strings = ["1", "0", "01", "10", "11", "001", "111"]

for s in test_strings:
    result = afd.is_accepted(s)
    print(f"A string '{s}' é aceita? {'Sim' if result else 'Não'}")
    afd.state = 'q0'