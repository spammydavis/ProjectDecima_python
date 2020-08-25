from uuid import UUID

from . import CoreDummy
from ...utils.byte_io_ds import ByteIODS


class CoreBoneData(CoreDummy):

    def __init__(self):
        super().__init__()
        self.bone_ids = []
        self.bone_matrices = []
        self.guid_0 = UUID(int=0)

    def parse(self, reader: ByteIODS, core_file):
        self.header.parse(reader,)
        self.guid = reader.read_guid()
        bone_count = reader.read_uint32()
        self.bone_ids = reader.read_fmt(f'{bone_count}H')
        matrix_count = reader.read_uint32()
        self.bone_matrices = [reader.read_fmt('16f') for _ in range(matrix_count)]
        self.guid_0 = reader.read_guid()
