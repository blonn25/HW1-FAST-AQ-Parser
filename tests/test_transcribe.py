# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)

import pytest


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    seq = "GTTTCTTTGACCTTTTAACCGCTCTCTTAG"
    trans_seq = "CAAAGAAACUGGAAAAUUGGCGAGAGAAUC" # converted manually using (https://skaminsky115.github.io/nac/DNA-mRNA-Protein_Converter.html)
    assert trans_seq == transcribe(seq)

    with pytest.raises(ValueError):
        transcribe('GTTTCTTTGACCTTTTAACCGCTCTCTTAZG') # 'Z' is not an allowed nucleotide

    with pytest.raises(ValueError):
        transcribe(12345) # input is not a string


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    seq = 'GCTAGCATATTATCCTAAGGCGTTACCCCA'
    rev_trans_seq = 'UGGGGUAACGCCUUAGGAUAAUAUGCUAGC' # converted manually using (https://skaminsky115.github.io/nac/DNA-mRNA-Protein_Converter.html)
    assert rev_trans_seq == reverse_transcribe(seq)

    with pytest.raises(ValueError):
        reverse_transcribe('GTTTCTTTGACCTTTTAACCGCTCTCTTAZG') # 'Z' is not an allowed nucleotide

    with pytest.raises(ValueError):
        reverse_transcribe(12345) # input is not a string