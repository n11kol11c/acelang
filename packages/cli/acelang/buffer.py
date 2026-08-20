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
