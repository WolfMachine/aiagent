# flags.py
from enum import Enum

class Flags(Enum):
    VERBOSE = 1

flag_map = {
        '-v': Flags.VERBOSE,
        '--verbose': Flags.VERBOSE,
}

def normalize_flag(flag_str):
    # Leading hyphens stripped for consistency in mapping, but not critical for comparison
    if flag_str.startswith('--'):
        # For word flags, normalize to lowercase
        return flag_str.lower()
    # For single-char flags (like -m or -M), preserve case
    return flag_str

