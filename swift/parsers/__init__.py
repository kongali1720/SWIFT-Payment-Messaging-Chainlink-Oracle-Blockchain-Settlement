from .field20 import Field20
from .field23b import Field23B
from .field32a import Field32A
from .field50k import Field50K
from .field59 import Field59
from .field71a import Field71A

FIELD_PARSERS = {
    "20": Field20(),
    "23B": Field23B(),
    "32A": Field32A(),
    "50K": Field50K(),
    "59": Field59(),
    "71A": Field71A(),
}
