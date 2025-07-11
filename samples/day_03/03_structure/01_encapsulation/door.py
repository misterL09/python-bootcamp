class Door:

    def __init__(self, closed=True):
        self.closed = closed

    @property
    def opened(self):
        return not self.closed

    def open(self):
        if self.opened:
            print("Door already open")
        else:
            print("Opened door")

    def close(self):
        if self.closed:
            print("Door already closed")
        else:
            print("Closed door")