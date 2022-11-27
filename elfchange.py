#-------------------------------------------------------------------------------
# elftools example: elf_relocations.py
#
# An example of obtaining a relocation section from an ELF file and examining
# the relocation entries it contains.
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
#-------------------------------------------------------------------------------
from __future__ import print_function
import sys
import os

# If pyelftools is not installed, the example can also run from the root or
# examples/ dir of the source distribution.
sys.path[0:0] = ['.', '..']

from elftools.elf.elffile import ELFFile
from elftools.elf.relocation import RelocationSection

def process_file(filename):
    print('Processing file:', filename)
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)

        # Read the .rela.dyn section from the file, by explicitly asking
        # ELFFile for this section
        # The section names are strings
        # reladyn_name = '.rela.dyn'
        reladyn_name = '.rela.text'
        reladyn = elffile.get_section_by_name(reladyn_name)

        sym_section = elffile.get_section_by_name('.symtab')
        str_section = elffile.get_section_by_name('.strtab')

        if not isinstance(reladyn, RelocationSection):
            print('  The file has no %s section' % reladyn_name)

        else:
            print('  %s section with %s relocations' % (reladyn_name, reladyn.num_relocations()))

        for sym in sym_section.iter_symbols():
	#	print(sym['st_info']['type'])
        #    	print(str_section.get_string(sym['st_name']))
                if(sym['st_info']['type'] == "STT_FUNC" or sym['st_info']['type'] == "STT_OBJECT" or sym['st_shndx'] == "SHN_UNDEF" and sym['st_info']['type'] == "STT_NOTYPE"):
                        sym = str_section.get_string(sym['st_name'])
                        os.system("riscv64-unknown-linux-gnu-objcopy  --redefine-sym " + sym + "=u" + sym + " " + filename)

if __name__ == '__main__':
    if sys.argv[1] == '--test':
        for filename in sys.argv[2:]:
            process_file(filename)
