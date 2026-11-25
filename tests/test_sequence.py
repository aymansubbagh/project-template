import pytest

from project_name import gc_content


def test_all_gc():
    assert gc_content("GGCC") == 1.0


def test_no_gc():
    assert gc_content("ATAT") == 0.0


def test_mixed_and_lowercase():
    assert gc_content("atgc") == 0.5


def test_n_counts_in_length_only():
    assert gc_content("GCNN") == 0.5


def test_empty_raises():
    with pytest.raises(ValueError):
        gc_content("")


def test_invalid_raises():
    with pytest.raises(ValueError):
        gc_content("ATGX")


@pytest.mark.validation
def test_against_biopython():
    """Scientific validation pattern: compare with a trusted reference implementation."""
    bio = pytest.importorskip("Bio.SeqUtils")
    seq = "ATGCGCGATTACAGGCTTAA"
    assert gc_content(seq) == pytest.approx(bio.gc_fraction(seq))
