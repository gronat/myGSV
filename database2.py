import Queue


class Database:
    def __init__(self):
        self.q = Queue.Queue()
        self.d = dict()
        self.s = set()
        self.size_q = 0
        self.processing = 0


    def enqueue(self, key):
        if key not in self.s:
            self.s.add(key)
            self.q.put(key)
            self.size_q += 1


    def dequeue(self):
        self.size_q -= 1
        with self.q.mutex:
            self.processing += 1
        return self.q.get()

    def add(self, key, val):
        self.d[key] = val

    def has(self, key):
        return key in self.s

    def dsize(self):
        return len(self.d)

    def qsize(self):
        return self.size_q

    def task_done(self):
        self.q.task_done()
        with self.q.mutex:
            self.processing -= 1
    
    def processing(self):
        return self.processing