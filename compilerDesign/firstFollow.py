
class Grammar:
    #assume every variable has exactly one rule. everything is either terminal or variable
    def __init__(self, rules, terminals, start):
        self.first = {}
        self.terminals = set(terminals)
        self.rules = rules
        self.follow = {}
        self.LHS = {}
        self.start = start
        
    
        
    def findFirst(self, input: chr): 
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

    def findLHS(self):
        variables = self.rules.keys()
        for variable in variables:
            self.LHS[variable] = {}
        for variable in variables:
            for rule in self.rules[variable]:
                if rule == 'epsilon':
                    continue
                for char in rule:
                    if char not in self.terminals:
                        if variable not in self.LHS[char]:
                            self.LHS[char][variable] =  rule
        
        
        
    def findFollow(self, input):
        ans = set()
        if input == self.start:
            ans.add('$')
        relevantRules = self.LHS[input]
        for parent in relevantRules: #index in that dictionary
            ansRule = set()
            string = relevantRules[parent]
            i = string.index(input)
            next = string[i+1:]
            print(parent, string, next)
            if next == '':
                #go to parent
                if parent not in self.follow:
                    self.findFollow(parent)
                ansRule.union(self.follow[parent])
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
                    
                
        

g = Grammar({'S':['ACB', 'CbB', 'Ba'], 'B':['g', 'epsilon'], 'A' : ['da', 'BC'], 'C': ['h', 'epsilon']}, ['a','b', 'd', 'g', 'h'], 'S')
g.findLHS()
print(g.LHS)
print(g.findFollow('C'))



