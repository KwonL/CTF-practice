# Bad binary

python binary compiled with pyinstaller. Extract pyc with pyi-archive_viewer. 

Then add first 8-bytes(pyc header file) to extracted file. 

with uncompyle6, get source of binary.

input in python 2.7 has vuln.

`cbmctf{!nPuT_i5_baD_in_PYTHON2.X}`