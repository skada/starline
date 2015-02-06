from starline.settings.base import *

try:
    from starline.settings.local import *
except ImportError as e:
    pass
