from os import getcwd

from ggshield.dev_scan import cd


def test_cd_context_manager():
    prev = getcwd()
    with cd("/tmp"):  # nosec
        assert getcwd() == "/tmp"  # nosec
    assert getcwd() == prev
