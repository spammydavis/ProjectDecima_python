from ProjectDecima.byte_io_ds import ByteIODS
from uuid import UUID


class CoreHeader:

    def __init__(self):
        self.magic = 0
        self.size = 0
        self.guid = UUID(int=0)

    def parse(self, reader: ByteIODS):
        self.magic = reader.read_uint64()
        self.size = reader.read_uint32()
        self.guid = reader.read_guid()


