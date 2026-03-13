import sqlite3 as sqlite

class Database:
    def __init__(self, source):
        self.source = source
        self.conn = sqlite.connect(source)