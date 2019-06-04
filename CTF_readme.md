# List of tools

## Forensic
- to extract file, use binwalk with -e option, or foremost
- File system forensic: sleuthkit
- steg: zsteg or stegsolver.jar
-

## Binary
- To play with provided glibc, you can use patchelf --set-rpath, --set-interpreter instead of just using LD_PRELOAD, which will cause segfault due to inproper ld version
