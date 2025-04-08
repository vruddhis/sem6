def remove_whitespace(tac):
  tac = tac.split()
  tac = ''.join(tac)
  return tac


def tac_to_code(tac, reg, addr):
  tac = remove_whitespace(tac)
  if len(tac) == 5:
    res = tac[0]
    if tac[1] != '=':
      print("unvalid")
      return -1
    op1 = tac[2]
    op = tac[3]
    op2 = tac[4]
    operators = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}
    ans = ''
    cmd = ''
    ans += operators[op]
    if op1 in reg:
      ans += ' '
      ans += reg[op1]
    else:
      if reg[0] != -1:
        addr.append(reg[0])
        cmd += 'MOV ['+ str(len(addr)) + '], R0'
        inner_var[reg[0]] = '['+ str(len(addr)) + ']'
      reg[0] = op1
      if reg[0] in inner_var:
        cmd += 'MOV R0, ' + inner_var[reg[0]]
      else:
        cmd += 'MOV R0, ' + reg[0]
      ans += ' '
      ans += 'R0'
    ans += ', '
    if op2 in reg:
      ans += reg[op2]
    else:
      if op2 in inner_var:
        ans += inner_var[op2]
      else:
        ans += op2
    reg[0] = res
    inner_var[res] = reg[0]
    return cmd + '\n' +  ans, reg, addr

def code_block_to_tac(block):
  reg = [-1, -1]
  addr = []
  for line in block:
    print(tac_to_code(line, reg, addr))

code_block_to_tac(['x=a+b', 'y=c + d', 'z = x - y'])
