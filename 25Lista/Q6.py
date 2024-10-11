class AFNPeloMenosUmZero:
    def _init_(self):
        self.states = {'q0', 'q1'}
        self.start_state = 'q0'
        self.accept_states = {'q1'}

    def is_accepted(self, string):
        current_states = {self.start_state}
        for char in string:
            if char not in {'0', '1'}:
                raise ValueError("A string deve conter apenas '0' e '1'.")
            next_states = set()
            for state in current_states:
                if state == 'q0':
                    if char == '0':
                        next_states.add('q1')
                    next_states.add('q0')
                elif state == 'q1':
                    next_states.add('q1')
            current_states = next_states
        return not current_states.isdisjoint(self.accept_states)

afd = AFNPeloMenosUmZero()
test_strings = ["1", "0", "01", "10", "11", "001", "111"]

for s in test_strings:
    result = afd.is_accepted(s)
    print(f"A string '{s}' é aceita? {'Sim' if result else 'Não'}")
