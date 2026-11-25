"""Example module. Delete or replace it when you start a real project.

It exists so the test suite and CI have something real to check on day one.
"""


def gc_content(sequence: str) -> float:
    """Return the fraction of G and C bases in a DNA sequence.

    GC content = (count of G + count of C) / (length of the sequence)

    where G (guanine) and C (cytosine) are two of the four DNA bases.
    The result is a number between 0 and 1.

    Raises ValueError for an empty sequence or for characters other than A, C, G, T, N.
    N (unknown base) counts toward the length but not toward G or C.
    """
    seq = sequence.upper()
    if not seq:
        raise ValueError("sequence is empty")
    invalid = set(seq) - set("ACGTN")
    if invalid:
        raise ValueError(f"invalid characters in sequence: {sorted(invalid)}")
    return (seq.count("G") + seq.count("C")) / len(seq)
