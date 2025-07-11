class Door:

    def __init__(self, closed=True, locked=False):
        self._closed = closed
        self._locked = locked

    @property
    def opened(self):
        return not self._closed

    @opened.setter
    def opened(self, value):
        if value:  # trying to open
            if self.locked:
                print("Can't open: Door is locked")
            elif self.opened:
                print("Door already open")
            else:
                self._closed = False
                print("Opened door")
        else:  # trying to close
            if self.closed:
                print("Door already closed")
            else:
                self._closed = True
                print("Closed door")

    @property
    def closed(self):
        return self._closed

    @closed.setter
    def closed(self, value):
        # Redirect to opened setter so all logic lives in one place
        self.opened = not value

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        if value:  # trying to lock
            if not self.closed:
                print("Can't lock: Door is open")
            elif self.locked:
                print("Door already locked")
            else:
                self._locked = True
                print("Locked door")
        else:  # trying to unlock
            if not self.locked:
                print("Door already unlocked")
            else:
                self._locked = False
                print("Unlocked door")

    def open(self):
        self.opened = True

    def close(self):
        self.opened = False

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
