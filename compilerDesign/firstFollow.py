from typing import Dict, List, Set, Tuple

class Grammar:
    #assume every variable has exactly one rule. everything is either terminal or variable
    def __init__(self, rules, terminals, start):
        self.first : Dict[str, Set[str]]= {}  #Dict[str, Tuple[Set[str], Dict[str, List[str]]]
        self.terminals : Set[str]= set(terminals)
        self.variables: Set[str]
        self.rules : Dict[str, List[str]]= rules
        self.follow :  Dict[str, Set[str]]= {}
        self.LHS : Dict[str, List[Tuple[str, str]]] = {}
        self.start: str = start
        self.parserTable: Dict[Tuple[str, str], List[str]]
        
    
        
    def findFirst(self, input: str) -> Set[str]: 
        if input in self.terminals:
            self.first[input] = set(input)
            return [input]
        ans = set()
        for rule in self.rules[input]:#this gives a string
            ansRule = set()
            if rule == 'epsilon':
                ansRule.add('epsilon')
            else:    
                stopped = 0
                for char in rule:
                    
                    if char not in self.first:
                        self.findFirst(char)
                    if 'epsilon' in self.first[char]:
                        
                        ansRule = ansRule.union(self.first[char])
                        ansRule.remove('epsilon')
                    else:
                        
                        ansRule = ansRule.union(self.first[char])
                        
                        stopped = 1
                        break
                if stopped == 0:
                    ansRule.add('epsilon')
            ans = ans.union(ansRule)
            
        self.first[input] = ans
        return ans 

    def findLHS(self) -> None:
        variables = self.rules.keys()
        self.variables = variables
        for variable in variables:
            self.LHS[variable] = []
        for variable in variables:
            for rule in self.rules[variable]:
                if rule == 'epsilon':
                    continue
                for char in rule:
                    if char not in self.terminals:
                        
                            self.LHS[char].append([variable, rule])
        
        
        
    def findFollow(self, input: str) -> Set[str]:
        ans = set()
        if input == self.start:
            ans.add('$')
        relevantRules = self.LHS[input]
        
        for rule in relevantRules: #index in that dictionary
            ansRule = set()
            parent = rule[0]
            string = rule[1]
            
            i = string.index(input)
            next = string[i+1:]
            
            if next == '':
                #go to parent
                if parent not in self.follow:
                    self.findFollow(parent)
                
                ansRule = ansRule.union(self.follow[parent])
                
            else:
                stopped = 0
                for char in next:
                    
                    if char not in self.first:
                        self.findFirst(char)
                    
                    if 'epsilon' in self.first[char]:
                        
                        ansRule = ansRule.union(self.first[char])
                        ansRule.remove('epsilon')
                    else:
                        
                        ansRule = ansRule.union(self.first[char])
                        
                        stopped = 1
                        break
                if stopped == 0:
                    if parent not in self.follow:
                        self.findFollow(parent)
                    
                    ansRule = ansRule.union(self.follow[parent])
                    
                
            ans = ans.union(ansRule)
        self.follow[input] = ans
        return ans
    
    def findParserTable(self) -> Dict[Tuple[str, str], List[str]]:
        self.findLHS()
        for variable in self.variables:
            self.findFirst(variable)
            self.findFollow(variable)
        for variable in self.variables:

        
                    
                
        

g = Grammar({'S':['ACB', 'CbB', 'Ba'], 'B':['g', 'epsilon'], 'A' : ['da', 'BC'], 'C': ['h', 'epsilon']}, ['a','b', 'd', 'g', 'h'], 'S')
g.findLHS()
print(g.findFollow('A'))
print(g.findFollow('B'))
print(g.findFollow('C'))
print(g.findFollow('S'))


"i need to take care of deadlocks. if some function recursively ccalls itself break. do the source now. later whatever is causing the split will "
"i have to keep the rules somewhere that give to first and follow"
