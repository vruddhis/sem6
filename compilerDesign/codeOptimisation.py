#shamelessly plagiarised from https://github.com/sampsyo/bril/blob/main/examples/tdce.py so the input is Bril IR in json format
import sys
import json

def trivial_dce_basic_block(func):
    changed = True

    while changed:
        changed = False
        used = set()
        for instr in func['instrs']:
            used.update(instr.get('args', []))

        new_instrs = []
        for instr in func['instrs']:
            if 'dest' not in instr:
                new_instrs.append(instr)
            elif instr['dest'] in used:
                new_instrs.append(instr)
            else:
                changed = True

        func['instrs'] = new_instrs

def localopt():
    bril = json.load(sys.stdin)
    for func in bril['functions']:
        trivial_dce_basic_block(func)
    json.dump(bril, sys.stdout, indent=2)

if __name__ == '__main__':
    localopt()
