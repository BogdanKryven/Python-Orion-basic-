

class Connection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return True
        elif exc_type is DBMergeConflict:
            return True
        elif exc_type is DBExce2:
            return True
        else:
            return False
