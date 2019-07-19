#!/usr/bin/env python3

import regex

NUM_WITH_SUFF = regex.compile('(\p{N}*)([^\p{N}]+)')

def strip(token):
    """If token includes a numeric prefix, omit it and return the suffix."""
    m = NUM_WITH_SUFF.match(token)
    return m.group(2)
