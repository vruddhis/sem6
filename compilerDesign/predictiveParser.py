from typing import Dict, List, Set, Tuple

class Grammar:
    def __init__(self, rules: Dict[str, List[str]], terminals: List[str], start: str):
        self.rules = rules  
        self.terminals = set(terminals)  
        self.variables = set(rules.keys())  
        self.start = start  
        
        self.first: Dict[str, Set[str]] = {var: set() for var in self.variables}  
        self.follow: Dict[str, Set[str]] = {var: set() for var in self.variables}  
        self.LHS: Dict[str, List[Tuple[str, str]]] = {var: [] for var in self.variables}  
        
        self.parserTable: Dict[Tuple[str, str], List[str]] = {}  
        
        self._compute_first_sets()
        self._compute_follow_sets()
        self._build_parsing_table()
    
    def _compute_first_sets(self):
        for terminal in self.terminals:
            self.first[terminal] = {terminal}  

        for variable in self.variables:
            self._find_first(variable)

    def _find_first(self, var: str) -> Set[str]:
        if var in self.terminals:
            return {var}

        if self.first[var]:  
            return self.first[var]

        first_set = set()
        for rule in self.rules[var]:
            if rule == 'epsilon':
                first_set.add('epsilon')
                continue

            for symbol in rule:
                symbol_first = self._find_first(symbol)
                first_set.update(symbol_first - {'epsilon'})

                if 'epsilon' not in symbol_first:
                    break
            else:
                first_set.add('epsilon')

        self.first[var] = first_set
        return first_set
    
    def _compute_follow_sets(self):
        self.follow[self.start].add('$')  

        for variable in self.variables:
            self._find_follow(variable)

    def _find_follow(self, var: str) -> Set[str]:
        if self.follow[var]: 
            return self.follow[var]

        for lhs, rules in self.rules.items():
            for rule in rules:
                for i, symbol in enumerate(rule):
                    if symbol == var:
                        follow_set = set()
                        next_part = rule[i + 1:]
                        
                        if next_part:
                            first_next = set()
                            for char in next_part:
                                first_char = self._find_first(char)
                                first_next.update(first_char - {'epsilon'})
                                if 'epsilon' not in first_char:
                                    break
                            else:
                                follow_set.update(self._find_follow(lhs))
                            follow_set.update(first_next)
                        else:
                            follow_set.update(self._find_follow(lhs))
                        
                        self.follow[var].update(follow_set)
        
        return self.follow[var]
    
    def _build_parsing_table(self):
        for var in self.variables:
            for rule in self.rules[var]:
                first_rule = set()
                
                if rule == 'epsilon':
                    first_rule = self._find_follow(var)  
                else:
                    for symbol in rule:
                        first_symbol = self._find_first(symbol)
                        first_rule.update(first_symbol - {'epsilon'})
                        if 'epsilon' not in first_symbol:
                            break
                    else:
                        first_rule.update(self._find_follow(var))

                for terminal in first_rule:
                    if terminal != 'epsilon':
                        self.parserTable[(var, terminal)] = rule
                
                if 'epsilon' in first_rule:
                    for terminal in self._find_follow(var):
                        self.parserTable[(var, terminal)] = 'epsilon'

    def parse(self, input_string: str) -> bool:
        stack = [self.start, '$']
        input_buffer = list(input_string) + ['$']
        
        while stack:
            top = stack.pop(0)
            current_input = input_buffer[0]

            if top in self.terminals or top == '$':
                if top == current_input:
                    input_buffer.pop(0)
                else:
                    return False
            else:
                key = (top, current_input)
                if key in self.parserTable:
                    production = self.parserTable[key]
                    if production != 'epsilon':
                        stack = list(production) + stack
                else:
                    return False
        
        return not input_buffer



grammar =  Grammar({'S':['ACB', 'CbB', 'Ba'], 'B':['g', 'epsilon'], 'A' : ['da', 'BC'], 'C': ['h', 'epsilon']}, ['a','b', 'd', 'g', 'h'], 'S')

print("Parsing Table:", grammar.parserTable)
