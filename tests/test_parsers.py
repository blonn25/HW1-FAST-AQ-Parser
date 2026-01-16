# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/blank.fa
    """

    ##### assert that the test.fa loads and reads properly #####
    fa_file = 'data/test.fa'
    fa_parser = FastaParser(fa_file)
    seq_data = [data for data in fa_parser]
    
    # sequence copied form test.fa (zero indexed)
    seq_5 = 'TAAGTAGTGCACTCCTGCGCGTCTCTTCCCAGAATCGTACTCTCAGAGCTAGAGAGGCGCGTTTGCCGTTCTACTCACCCCAGCCTCTGAAGAGGGATGC'
    assert seq_data[5][0] == 'seq5' and seq_data[5][1] == seq_5, "data/test.fa not read in properly"

    ##### assert that the blank and bad fastas raise proper errors #####
    with pytest.raises(ValueError):
        blank_parser = FastaParser('tests/blank.fa')
        for _ in blank_parser:
            pass

    with pytest.raises(ValueError):
        bad_parser = FastaParser('tests/bad.fa')
        for _ in bad_parser:
            pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in. If a fastq file is
    read, the first item is None
    """
    
    ##### assert that FastaParser will not read fastq files #####
    fq_file = 'data/test.fq'
    fa_parser = FastaParser(fq_file)
    seq_data = [data for data in fa_parser]
    assert seq_data[0][0] == None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """

    ##### assert that the test.fq loads and reads properly #####
    fq_file = 'data/test.fq'
    fq_parser = FastqParser(fq_file)
    seq_data = [data for data in fq_parser]
    
    # sequence copied form test.fq (zero indexed)
    seq_5 = 'CGCGATGAAGAAGACCTATCCCAACTTGCTCTGGCTAGCCTCGCCAAGTATGATAGGATCCATCGTCTATCATGCATGCGTTAGACACTTGCTGGAGTAC'
    qual_5 = """:+;!5'&.";$+/2;!##<'!9+&4#3"2>,=*%)""<&=*2,$651/&01#*%.:=5-:&,:(%>/;0!0%#4/-807+5"6;&::>;&.9+((!5'&5"""
    assert seq_data[5][0] == 'seq5' and seq_data[5][1] == seq_5 and seq_data[5][2] == qual_5, "data/test.fq not read in properly"

    ##### assert that the blank and bad fastas raise proper errors #####
    with pytest.raises(ValueError):
        blank_parser = FastqParser('tests/blank.fq')    # bonus file added by Beau
        for _ in blank_parser:
            pass

    with pytest.raises(ValueError):
        bad_parser = FastqParser('tests/bad.fq')        # bonus file added by Beau
        for _ in bad_parser:
            pass


def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """

    ##### assert that FastaParser will not read fastq files #####
    fa_file = 'data/test.fa'
    fq_parser = FastqParser(fa_file)
    seq_data = [data for data in fq_parser]
    assert seq_data[0][0] == None