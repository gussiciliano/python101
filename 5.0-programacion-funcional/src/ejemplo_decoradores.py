#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import sys

def accepts(*types, **kw):
    '''Function decorator. Checks decorated function's arguments are
    of the expected types.

    Parameters:
    types -- The expected types of the inputs to the decorated function.
             Must specify type for each parameter.
    kw    -- Optional specification of 'debug' level (this is the only valid
             keyword argument, no other should be given).
             debug = ( 0 | 1 | 2 )

    '''
    if not kw:
        # default level: MEDIUM
        debug = 1
    else:
        debug = kw['debug']
    try:
        def decorator(f):
            def newf(*args):
                if debug is 0:
                    return f(*args)
                assert len(args) == len(types)
                argtypes = tuple(map(type, args))
                if argtypes != types:
                    msg = info(f.__name__, types, argtypes, 0)
                    if debug is 1:
                        print >> sys.stderr, 'TypeWarning: ', msg
                    elif debug is 2:
                        raise (TypeError, msg)
                return f(*args)
            newf.__name__ = f.__name__
            return newf
        return decorator
    except (KeyError, key):
        raise (KeyError, key + "is not a valid keyword argument")
    except (TypeError, msg):
        raise (TypeError, msg)


def returns(ret_type, **kw):
    '''Function decorator. Checks decorated function's return value
    is of the expected type.

    Parameters:
    ret_type -- The expected type of the decorated function's return value.
                Must specify type for each parameter.
    kw       -- Optional specification of 'debug' level (this is the only valid
                keyword argument, no other should be given).
                debug=(0 | 1 | 2)
    '''
    try:
        if not kw:
            # default level: MEDIUM
            debug = 1
        else:
            debug = kw['debug']
        def decorator(f):
            def newf(*args):
                result = f(*args)
                if debug is 0:
                    return result
                res_type = type(result)
                if res_type != ret_type:
                    msg = info(f.__name__, (ret_type,), (res_type,), 1)
                    if debug is 1:
                        print >> sys.stderr, 'TypeWarning: ', msg
                    elif debug is 2:
                        raise (TypeError, msg)
                return result
            newf.__name__ = f.__name__
            return newf
        return decorator
    except (KeyError, key):
        raise (KeyError, key + "is not a valid keyword argument")
    except (TypeError, msg):
        raise (TypeError, msg)

def info(fname, expected, actual, flag):
    '''Convenience function returns nicely formatted error/warning msg.'''
    format = lambda types: ', '.join([str(t).split("'")[1] for t in types])
    expected, actual = format(expected), format(actual)
    msg = "'{}' method ".format( fname )\
          + ("accepts", "returns")[flag] + " ({}), but ".format(expected)\
          + ("was given", "result is")[flag] + " ({})".format(actual)
    return msg


def say_hello(enfasis):
    def decorator(f):
        def say_hello_func():
            value = f()
            if enfasis is True:
                value += "!!!"

            print(value)

        return say_hello_func

    return decorator

@say_hello(True)
def wellcome():
    return "hello"

@say_hello(False)
def saludar():
    return "hola"

@accepts(int)
@returns(int)
def add(x, y):
    return x + y

@accepts(int)
@returns(int)
def sub(x, y):
    return x - y

def apply(func, x, y): # 1
    return func(x, y) # 2

if __name__ == '__main__':
    wellcome()
    saludar()

    add("holis", "chauchis")
    add(3.4, 4.5)
    sub(3,5)
