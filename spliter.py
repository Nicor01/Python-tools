#!/usr/bin/env python3
import sys

def split(filename):
    chunk_size = 100000  # lines

    def write_chunk(part, lines):
        with open(filename+ str(part) +'.csv', 'w') as f_out:
            f_out.write(header)
            f_out.writelines(lines)

    with open(filename, 'r') as f:
        count = 0
        header = f.readline()
        lines = []
        for line in f:
            count += 1
            lines.append(line)
            if count % chunk_size == 0:
                write_chunk(count // chunk_size, lines)
                lines = []
        # write remainder
        if len(lines) > 0:
            write_chunk((count // chunk_size) + 1, lines)

if len(sys.argv) > 1:
    f1 = str(sys.argv[1])
    split(f1)

else:
    raise Exception("No input file specified")