class Door:
    def __init__(self,closed):
        self.door = closed

    def open(self):
        return not self.door

    def close(self):
        return self.door

x = Door(False)
if x.open():
    print("Open")
else:
    print("Close")



# if self.door:
#     return print("Door is Already Open")
# else:
#     self.door = False
#     return print("Door is Open")

