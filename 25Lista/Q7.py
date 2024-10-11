class AFN01Inicio10Fim:
    def _init_(self):
        self.start_state = 'q0'
        self.accept_states = {'q3'}

    def is_accepted(self, string):
        current_states = {self.start_state}
        for char in string:
            if char not in {'0', '1'}:
                raise ValueError("A string deve conter apenas '0' e '1'.")
            next_states = set()
            for state in current_states:
                if state == 'q0' and char == '0':
                    next_states.add('q1')
                elif state == 'q1' and char == '1':
                    next_states.add('q2')
                elif state == 'q2':
                    next_states.add('q2')
                    if char == '1':
                        next_states.add('q3')
                elif state == 'q3':
                    next_states.add('q3')
            current_states = next_states
            if not current_states:
                break
        return not current_states.isdisjoint(self.accept_states)

afd = AFN01Inicio10Fim()
test_strings = ["0110", "01101", "1010", "010", "01", "0010", "01010"]

for s in test_strings:
    result = afd.is_accepted(s)
    print(f"A string '{s}' é aceita? {'Sim' if result else 'Não'}")
