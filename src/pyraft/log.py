import collections
import sys

from . import utils


class LogEntry:
    def __init__(self, term, index, data):
        self.term = term
        self.index = index
        self.data = data


class MemoryLog:
    def __init__(self, *, start_index=1, entries=None):
        self.start_index = start_index
        self.entries = (
            entries if isinstance(entries, collections.deque) else collections.deque()
        )

    def __len__(self):
        return len(self.entries)

    def __getitem__(self, key):
        return self.entries[key - self.start_index]

    def append(self, new_entries):
        first_index = self.start_index + len(self.entries)
        last_index = first_index + len(new_entries) - 1
        for entry in new_entries:
            self.entries.append(entry)
        return first_index, last_index

    def get_log_start_index(self):
        return self.start_index

    def get_last_log_index(self):
        return self.start_index + len(self.entries) - 1

    def get_name(self):
        return "Memory"

    def get_size_bytes(self):
        return utils.total_size(self.entries)

    def truncate_prefix(self, first_index):
        if first_index > self.start_index:
            for _ in range(min(first_index - self.start_index, len(self.entries))):
                self.entries.popleft()
            self.start_index = first_index

    def truncate_suffix(self, last_index):
        if last_index < self.start_index:
            self.entries.clear()
        elif last_index < self.start_index - 1 + len(self.entries):
            for _ in range(self.start_index - 1 + len(self.entries) - last_index):
                self.entries.pop()

    def update_metadata(self):
        return
