"""CPU functionality."""

import sys



class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.register = [0] * 8
        self.ram = [0] * 256
        self.pc = 0
        self.SP = 7
        self.ir = 0
        self.mar = 0
        self.mdr = 0
        self.fl = 0
        self.branch_table = {
            LDI: self.handle_LDI,
            PRA: self.handle_PRA,
            PRN: self.handle_PRN,
            HLT: self.handle_HLT,
            MUL: self.handle_MUL,
            DIV: self.handle_DIV,
            ADD: self.handle_ADD,
            SUB: self.handle_SUB,
            POP: self.handle_POP,
            PUSH: self.handle_PUSH,
        }

   