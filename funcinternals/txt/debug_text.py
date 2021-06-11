from sys import _getframe
from os import sep

def bold(_str):
    ''' wrap string in bash terminal escape code for bold text '''

    return '\033[1m' + _str + '\033[0m'

def _repr(varname_str, obj):
    '''
    Display certain object types (HTTP reponses, numpy ndarrays, etc.)
    in special ways, everything else just gets repr'd.
    '''

    varname_str = bold(varname_str)
    _type = type(obj)

    if _type == dict:
        print()
        print(_type)
        print(varname_str, '=')

        for k in sorted(obj.keys()):
            print(str(k) + ':', obj[k])

    else:
        print()
        print(_type)

        print(varname_str, '=', repr(obj))

def debug(varname_str, frame=None, ignore_undefined=True):
    '''
    Print the variable name and value from the caller's local scope,
    or from the passed stack frame.
    '''

    if not frame:
        frame = _getframe(1)
    try:
        file = frame.f_code.co_filename.split(sep)[-1]

        method = frame.f_code.co_name
        line = frame.f_lineno

        obj = eval(varname_str, frame.f_globals, frame.f_locals)

        print()
        print('-' * 50, f"( debug called from: { method } @ { file }:{ line } )", '-' * 50)

        _repr(varname_str, obj)

    except NameError as e:
        if not ignore_undefined:

            print()
            print('(' + str(e) + ')')

        return
    finally:
        del frame



def inspect_caller_locals(suppress=[], ignore_undefined=True):
    '''
    Function decorator w/ arguments. Requires parens regardless of args, eg.:

    @inspect_caller_locals()
    def my_func(): ...

    Has access to the internal state of the *caller*. To access
    the decorated's internals, use debug('my_var') defined above (for a single var),
    or call inspect() defined below for all locals.

    To suppress output of large/verbose values that clutter up the terminal,
    add the quoted variable name strings to the suppress list. Eg.:

    @inspect_caller_locals(suppress = ['this_dict', 'that_list'])
    def my_func(): ...
    '''

    def decorator(function):

        def print_locals(*args, **kwargs):
            try:
                frame = _getframe(1)

                for arg in frame.f_code.co_varnames:
                    if arg not in suppress + ['_']:

                        debug(arg, frame=frame, ignore_undefined=ignore_undefined)
                    else:
                        print(f"(Supressed '{ arg }')")
            finally:
                del frame

            return function(*args, **kwargs)

        return print_locals

    return decorator

@inspect_caller_locals(suppress=[
    'downstream_response_body',
    'pixel_data',
])
def inspect():
    '''
    Call this at any point in a function definition
    to inspect its internal state at that time.
    Eg. to see state just prior to returning:

    def my_func():
        ...
        inspect()
        return

    Function body intentionally left blank. All work done in decorator and subroutines.
    '''

def compare_rgb_to_slots(rgb, slot_vals):

    debug('rgb')
    debug('slot_vals')