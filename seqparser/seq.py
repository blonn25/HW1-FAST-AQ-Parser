# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """

    # check that the sequence is a string
    if not isinstance(seq, str):
        raise ValueError(f"The provided sequence, seq, must be of type string.")

    # clean up the sequence
    seq = ''.join(seq.strip().upper().split())

    # initialize new sequence variable, new_seq, and iterate through nucleotides in DNA seq
    new_seq = ''
    for nuc in seq:

        # check that current base is allowed based in the set of ALLOWED_NUC
        if nuc not in ALLOWED_NUC:
            raise ValueError(f"Unallowed nucleotide is present in the provided sequence. Allowed nucleotides are {ALLOWED_NUC}.")
        
        # append transcribed base to the new_seq (mRNA)
        new_seq += TRANSCRIPTION_MAPPING[nuc]

    # reverse the mRNA seq if applicable (reverse transcription)
    if reverse:
        new_seq = new_seq[::-1]
    
    return new_seq


def reverse_transcribe(seq: str) -> str:
    """"""
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    return transcribe(seq, reverse=True)