import collections
import sys

sys.path.append("src")

import pyraft


def test_vanilla_init():
    log = pyraft.MemoryLog()
    assert "Memory" == log.get_name()
    assert log.get_log_start_index() == 1
    assert log.get_last_log_index() == 0
    assert len(log) == 0


def test_custom_start_index_init():
    log = pyraft.MemoryLog(start_index=0)
    assert log.get_log_start_index() == 0
    assert log.get_last_log_index() == -1
    assert len(log) == 0


def test_append_one_entry():
    log = pyraft.MemoryLog()
    log.append(["X"])
    assert log.get_log_start_index() == 1
    assert log.get_last_log_index() == 1
    assert len(log) == 1
    assert log[1] == "X"


def test_truncate_prefix():
    log = pyraft.MemoryLog()
    log.append(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
    log.truncate_prefix(6)
    assert log.get_log_start_index() == 6
    assert log.get_last_log_index() == 10
    assert len(log) == 5
    assert log[6] == "F"


def test_truncate_suffix():
    log = pyraft.MemoryLog()
    log.append(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
    log.truncate_suffix(5)
    assert log.get_log_start_index() == 1
    assert log.get_last_log_index() == 5
    assert len(log) == 5
    assert log[1] == "A"


def test_get_size_bytes():
    log = pyraft.MemoryLog()
    log.append(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
    charsize = sys.getsizeof("X")
    dequesize = sys.getsizeof(collections.deque())
    assert log.get_size_bytes() >= charsize + dequesize


def test_update_metadata():
    log = pyraft.MemoryLog()
    assert log.update_metadata() == None
