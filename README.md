# CCSDS-CADU-Generator
This is a set of simple programs for packing your binary files into CCSDS CADU frames and mixing into one CADU file.

## Using
CADU-Genereator.exe
```sh
CADU-Generator.exe -i (--input) input_file.bin -o (--output) output_file.bin -v (--vcid (0 to F)) 1 -a (--asm) 1acffc1d
```

CADU-Mixer.exe
```sh
CADU-Mixer.exe -ip (--inputp) input_file1.bin -is (--inputs) input_file2.bin -o (--output) output_file.bin
```
