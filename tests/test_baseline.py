
import pytest
import baseline.tasks


@pytest.mark.req("BASELINE-04")
def test_first_missing():
    assert baseline.tasks.first_missing(["a", "b", "c"], ["a", "c"]) == "b"
    assert baseline.tasks.first_missing(["a", "b"], ["a", "b"]) is None