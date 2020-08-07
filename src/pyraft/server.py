import pickle


class AppendEntriesRequest:
    def __init__(self, *, term, prev_log_index, prev_log_term, entries):
        self.term = term
        self.prev_log_index = prev_log_index
        self.prev_log_term = prev_log_term
        self.entries = entries


class AppendEntriesResponse:
    def __init__(self, *, term, success, last_log_index):
        self.term = term
        self.success = success
        self.last_log_index = last_log_index
