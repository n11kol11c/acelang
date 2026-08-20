from __future__ import annotations


BYTE = 1
KILOBYTE = 1024
MEGABYTE = KILOBYTE * 1024
GIGABYTE = MEGABYTE * 1024
TERABYTE = GIGABYTE * 1024

BUFFER_SIZE = 512
MAX_FILENAME_LEN = 32
MIN_FILENAME_LEN = 1
MAX_FILE_SIZE = 4 * GIGABYTE
MAX_PACKET_SIZE = 1500
MAX_EVENT_SIZE = 256
MAX_NET_EVENT_SIZE = 65536
MAX_STATEBAG_SIZE = 1 << 20
MAX_ENTITY_OWNERS = 256
MAX_CLIENTS = 128
MAX_PLAYERS = 32
MAX_RESOURCE_NAME = 64
MAX_IP_LEN = 46
MAX_LICENSE_LEN = 40
MAX_DISCORD_LEN = 18
MAX_STEAM_LEN = 17
MAX_XBL_LEN = 36
MAX_COMMAND_LEN = 128
MAX_CHAT_LEN = 256
MAX_CONVAR_LEN = 512
MAX_HOSTNAME_LEN = 128
MAX_RESOURCE_PATH = 260
MAX_SCRIPT_PATH = 260
MAX_CFG_LINE = 1024
MAX_CFG_FILE = 4 * MEGABYTE


def to_bytes(n: int, unit: str = "B", /) -> int:
    units = {"B": BYTE, "KB": KILOBYTE, "MB": MEGABYTE, "GB": GIGABYTE, "TB": TERABYTE}
    return n * units.get(unit.upper(), BYTE)


def from_bytes(n: int, /) -> tuple[float, str]:
    for unit, size in [("TB", TERABYTE), ("GB", GIGABYTE), ("MB", MEGABYTE), ("KB", KILOBYTE)]:
        if n >= size:
            return (round(n / size, 2), unit)
    return (float(n), "B")


def fmt_size(n: int, /) -> str:
    value, unit = from_bytes(n)
    return f"{value} {unit}"


def fmt_bits(n: int, /) -> str:
    value, unit = from_bytes(n)
    return f"{value * 8} {unit.replace('B', 'b')}"


def fmt_bits_per_sec(n: int, /) -> str:
    value, unit = from_bytes(n)
    return f"{value * 8} {unit.replace('B', 'b')}/s"


def clamp(value: int, lo: int, hi: int, /) -> int:
    return max(lo, min(hi, value))


def in_range(value: int, lo: int, hi: int, /) -> bool:
    return lo <= value <= hi


def is_valid_buffer(n: int, /) -> bool:
    return n > 0 and n <= MAX_FILE_SIZE


def is_valid_filename(name: str, /) -> bool:
    return MIN_FILENAME_LEN <= len(name) <= MAX_FILENAME_LEN


def is_valid_cfg_line(line: str, /) -> bool:
    return len(line) <= MAX_CFG_LINE


def is_valid_cfg_size(size: int, /) -> bool:
    return size <= MAX_CFG_FILE


def is_valid_packet(n: int, /) -> bool:
    return 0 < n <= MAX_PACKET_SIZE


def is_valid_hostname(name: str, /) -> bool:
    return 0 < len(name) <= MAX_HOSTNAME_LEN


def is_valid_resource_name(name: str, /) -> bool:
    return 0 < len(name) <= MAX_RESOURCE_NAME


def is_valid_convar_value(value: str, /) -> bool:
    return len(value) <= MAX_CONVAR_LEN


def is_valid_command(cmd: str, /) -> bool:
    return 0 < len(cmd) <= MAX_COMMAND_LEN


def is_valid_chat_msg(msg: str, /) -> bool:
    return 0 < len(msg) <= MAX_CHAT_LEN


def chunks(data: bytes, size: int, /) -> list[bytes]:
    return [data[i:i + size] for i in range(0, len(data), size)]


def align(n: int, alignment: int = 4, /) -> int:
    return (n + alignment - 1) & ~(alignment - 1)


def log2_floor(n: int, /) -> int:
    if n <= 0:
        return 0
    result = 0
    while (1 << (result + 1)) <= n:
        result += 1
    return result


def log2_ceil(n: int, /) -> int:
    if n <= 0:
        return 0
    result = log2_floor(n)
    if (1 << result) < n:
        result += 1
    return result


def next_power_of_2(n: int, /) -> int:
    if n <= 0:
        return 1
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n + 1


def prev_power_of_2(n: int, /) -> int:
    if n <= 0:
        return 0
    result = next_power_of_2(n)
    if result > n:
        result >>= 1
    return result


def popcount(n: int, /) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


class Buffer:
    __slots__ = ("_data", "_pos", "_len")

    def __init__(self, data: bytes | bytearray | None = None, /) -> None:
        self._data = bytes(data) if data else b""
        self._pos = 0
        self._len = len(self._data)

    @property
    def size(self) -> int:
        return self._len

    @property
    def pos(self) -> int:
        return self._pos

    @property
    def remaining(self) -> int:
        return self._len - self._pos

    @property
    def empty(self) -> bool:
        return self._pos >= self._len

    def read(self, n: int = -1, /) -> bytes:
        if n < 0:
            data = self._data[self._pos:]
            self._pos = self._len
            return data
        end = min(self._pos + n, self._len)
        data = self._data[self._pos:end]
        self._pos = end
        return data

    def read_int(self, size: int = 4, /) -> int:
        return int.from_bytes(self.read(size), "little")

    def read_str(self, length: int = -1, /) -> str:
        data = self.read(length)
        return data.rstrip(b"\x00").decode("utf-8", errors="replace")

    def seek(self, pos: int, /) -> None:
        self._pos = clamp(pos, 0, self._len)

    def skip(self, n: int, /) -> None:
        self._pos = clamp(self._pos + n, 0, self._len)

    def reset(self) -> None:
        self._pos = 0

    def peek(self, n: int = 1, /) -> bytes:
        return self._data[self._pos:self._pos + n]

    def __len__(self) -> int:
        return self._len

    def __bool__(self) -> bool:
        return self._len > 0

    def __repr__(self) -> str:
        return f"Buffer(size={self._len}, pos={self._pos})"


class BufferConvert:
    __slots__ = ()

    # ── Bytes <-> String ──

    @staticmethod
    def bytes_to_str(data: bytes, encoding: str = "utf-8", errors: str = "replace", /) -> str:
        return data.decode(encoding, errors=errors)

    @staticmethod
    def str_to_bytes(s: str, encoding: str = "utf-8", /) -> bytes:
        return s.encode(encoding)

    @staticmethod
    def bytes_to_hex(data: bytes, sep: str = " ", /) -> str:
        return sep.join(f"{b:02x}" for b in data)

    @staticmethod
    def hex_to_bytes(hex_str: str, /) -> bytes:
        clean = hex_str.replace(" ", "").replace("\n", "")
        return bytes.fromhex(clean)

    @staticmethod
    def bytes_to_bin(data: bytes, sep: str = " ", /) -> str:
        return sep.join(f"{b:08b}" for b in data)

    @staticmethod
    def bin_to_bytes(bin_str: str, /) -> bytes:
        clean = bin_str.replace(" ", "").replace("\n", "")
        return bytes(int(clean[i:i + 8], 2) for i in range(0, len(clean), 8))

    # ── Int <-> Bytes ──

    @staticmethod
    def int_to_bytes(n: int, length: int = 4, byteorder: str = "little", /) -> bytes:
        return n.to_bytes(length, byteorder, signed=True)

    @staticmethod
    def bytes_to_int(data: bytes, byteorder: str = "little", /) -> int:
        return int.from_bytes(data, byteorder, signed=True)

    @staticmethod
    def int_to_uint_bytes(n: int, length: int = 4, byteorder: str = "little", /) -> bytes:
        return n.to_bytes(length, byteorder, signed=False)

    @staticmethod
    def bytes_to_uint(data: bytes, byteorder: str = "little", /) -> int:
        return int.from_bytes(data, byteorder, signed=False)

    @staticmethod
    def int16_to_bytes(n: int, /) -> bytes:
        return n.to_bytes(2, "little", signed=True)

    @staticmethod
    def bytes_to_int16(data: bytes, /) -> int:
        return int.from_bytes(data[:2], "little", signed=True)

    @staticmethod
    def int32_to_bytes(n: int, /) -> bytes:
        return n.to_bytes(4, "little", signed=True)

    @staticmethod
    def bytes_to_int32(data: bytes, /) -> int:
        return int.from_bytes(data[:4], "little", signed=True)

    @staticmethod
    def int64_to_bytes(n: int, /) -> bytes:
        return n.to_bytes(8, "little", signed=True)

    @staticmethod
    def bytes_to_int64(data: bytes, /) -> int:
        return int.from_bytes(data[:8], "little", signed=True)

    @staticmethod
    def uint16_to_bytes(n: int, /) -> bytes:
        return n.to_bytes(2, "little", signed=False)

    @staticmethod
    def bytes_to_uint16(data: bytes, /) -> int:
        return int.from_bytes(data[:2], "little", signed=False)

    @staticmethod
    def uint32_to_bytes(n: int, /) -> bytes:
        return n.to_bytes(4, "little", signed=False)

    @staticmethod
    def bytes_to_uint32(data: bytes, /) -> int:
        return int.from_bytes(data[:4], "little", signed=False)

    @staticmethod
    def uint64_to_bytes(n: int, /) -> bytes:
        return n.to_bytes(8, "little", signed=False)

    @staticmethod
    def bytes_to_uint64(data: bytes, /) -> int:
        return int.from_bytes(data[:8], "little", signed=False)

    # ── Float <-> Bytes ──

    @staticmethod
    def float32_to_bytes(f: float, /) -> bytes:
        import struct
        return struct.pack("<f", f)

    @staticmethod
    def bytes_to_float32(data: bytes, /) -> float:
        import struct
        return struct.unpack("<f", data[:4])[0]

    @staticmethod
    def float64_to_bytes(f: float, /) -> bytes:
        import struct
        return struct.pack("<d", f)

    @staticmethod
    def bytes_to_float64(data: bytes, /) -> float:
        import struct
        return struct.unpack("<d", data[:8])[0]

    # ── Bool <-> Bytes ──

    @staticmethod
    def bool_to_bytes(flag: bool, /) -> bytes:
        return b"\x01" if flag else b"\x00"

    @staticmethod
    def bytes_to_bool(data: bytes, /) -> bool:
        return data[0] != 0 if data else False

    # ── Str <-> Int ──

    @staticmethod
    def str_to_int(s: str, /) -> int:
        return int(s)

    @staticmethod
    def str_to_float(s: str, /) -> float:
        return float(s)

    @staticmethod
    def str_to_bool(s: str, /) -> bool:
        return s.lower() in ("true", "1", "yes", "on")

    # ── Network Order (Big Endian) ──

    @staticmethod
    def int_to_network(n: int, length: int = 4, /) -> bytes:
        return n.to_bytes(length, "big", signed=False)

    @staticmethod
    def network_to_int(data: bytes, /) -> int:
        return int.from_bytes(data, "big", signed=False)

    @staticmethod
    def ip_to_int(ip: str, /) -> int:
        parts = ip.split(".")
        return (int(parts[0]) << 24) | (int(parts[1]) << 16) | (int(parts[2]) << 8) | int(parts[3])

    @staticmethod
    def int_to_ip(n: int, /) -> str:
        return f"{(n >> 24) & 0xFF}.{(n >> 16) & 0xFF}.{(n >> 8) & 0xFF}.{n & 0xFF}"

    @staticmethod
    def mac_to_bytes(mac: str, /) -> bytes:
        return bytes.fromhex(mac.replace(":", "").replace("-", ""))

    @staticmethod
    def bytes_to_mac(data: bytes, /) -> str:
        return ":".join(f"{b:02x}" for b in data[:6])

    # ── JSON / Pickle ──

    @staticmethod
    def json_to_bytes(obj: object, /) -> bytes:
        import json
        return json.dumps(obj).encode("utf-8")

    @staticmethod
    def bytes_to_json(data: bytes, /) -> object:
        import json
        return json.loads(data.decode("utf-8"))

    @staticmethod
    def pickle_to_bytes(obj: object, /) -> bytes:
        import pickle
        return pickle.dumps(obj)

    @staticmethod
    def bytes_to_pickle(data: bytes, /) -> object:
        import pickle
        return pickle.loads(data)

    # ── Base64 ──

    @staticmethod
    def bytes_to_base64(data: bytes, /) -> str:
        import base64
        return base64.b64encode(data).decode("ascii")

    @staticmethod
    def base64_to_bytes(s: str, /) -> bytes:
        import base64
        return base64.b64decode(s)

    # ── Bitwise ──

    @staticmethod
    def bytes_to_bits(data: bytes, /) -> list[int]:
        result: list[int] = []
        for byte in data:
            for i in range(7, -1, -1):
                result.append((byte >> i) & 1)
        return result

    @staticmethod
    def bits_to_bytes(bits: list[int], /) -> bytes:
        result = bytearray()
        for i in range(0, len(bits), 8):
            byte = 0
            for j in range(8):
                if i + j < len(bits):
                    byte = (byte << 1) | (bits[i + j] & 1)
                else:
                    byte <<= 1
            result.append(byte)
        return bytes(result)

    @staticmethod
    def get_bit(data: bytes, index: int, /) -> int:
        byte_index = index >> 3
        bit_index = 7 - (index & 7)
        if byte_index >= len(data):
            return 0
        return (data[byte_index] >> bit_index) & 1

    @staticmethod
    def set_bit(data: bytearray, index: int, value: int, /) -> None:
        byte_index = index >> 3
        bit_index = 7 - (index & 7)
        if byte_index >= len(data):
            return
        if value:
            data[byte_index] |= 1 << bit_index
        else:
            data[byte_index] &= ~(1 << bit_index)

    # ── Buffer Class ──

    @staticmethod
    def buffer_to_bytes(buf: Buffer, /) -> bytes:
        return buf.read()

    @staticmethod
    def bytes_to_buffer(data: bytes, /) -> Buffer:
        return Buffer(data)

    @staticmethod
    def str_to_buffer(s: str, /) -> Buffer:
        return Buffer(s.encode("utf-8"))

    @staticmethod
    def buffer_to_str(buf: Buffer, encoding: str = "utf-8", /) -> str:
        return buf.read().decode(encoding, errors="replace")

    @staticmethod
    def int_to_buffer(n: int, size: int = 4, /) -> Buffer:
        return Buffer(n.to_bytes(size, "little", signed=True))

    @staticmethod
    def buffer_to_int(buf: Buffer, size: int = 4, /) -> int:
        return int.from_bytes(buf.read(size), "little", signed=True)
