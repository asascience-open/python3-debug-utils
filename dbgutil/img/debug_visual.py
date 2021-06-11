# coding: UTF-8

import numpy as np
import PIL.Image as Image
import PIL.PngImagePlugin as Png
import txt.debug_text as dbg_txt
from imgcat import imgcat
from txt.debug_text import *

# Save a ref. to the text _repr method so we can still
# call it after replacing it with vis_repr below.
_nd_repr = dbg_txt._repr

def _vis_repr(varname_str, obj):
    '''
    Display certain objects type (images, etc.)
    in special ways, everything else just gets repr'd by
    the parent class. Shadows the base class method by
    the same name.
    '''

    _type = type(obj)
    if _type in (Image.Image, Png.PngImageFile):

        print()
        print(obj)

        print(bold(varname_str), '=')
        imgcat(np.asarray(obj))

        # green_background = Image.new('RGBA', obj.size, (0, 255, 0))
        # composite = Image.alpha_composite(green_background, obj)
        # imgcat(np.asarray(composite))

    else:
        _nd_repr(varname_str, obj)

## IMPORTANT - replace the text _repr method with _vis_repr for enhanced functionality
dbg_txt._repr = _vis_repr
