class AFNZeroSeguidoDeUm:
    def _init_(self):
        self.start_state = 'q0'
        self.accept_states = {'q2'}

    def is_accepted(self, string):
        current_state = self.start_state
        for char in string:
            if char not in {'0', '1'}:
                raise ValueError("A string deve conter apenas '0' e '1'.")
            if current_state == 'q0':
                if char == '0':
                    current_state = 'q1'
                elif char == '1':
                    current_state = 'q0'
            elif current_state == 'q1':
                if char == '0':
                    current_state = 'q1'
                elif char == '1':
                    current_state = 'q2'
            elif current_state == 'q2':
                current_state = 'q2'
        return current_state in self.accept_states

afd = AFNZeroSeguidoDeUm()
test_strings = ["01", "001", "10", "111", "000", "0101", "1001", "1"]

for s in test_strings:
    result = afd.is_accepted(s)
    print(f"A string '{s}' é aceita? {'Sim' if result else 'Não'}")
