#! /usr/bin/env python3

import sys
from IPython.nbformat import read, write, NO_CONVERT

nb = read(sys.stdin, NO_CONVERT)

for cell in nb.cells:
	if cell.cell_type == 'code':
		cell.outputs = []
		cell.execution_count = None

write(nb, sys.stdout, NO_CONVERT)