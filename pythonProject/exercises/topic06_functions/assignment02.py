"""
# Basic text functions
Write the functions
`is_digit`,
`to_upper`,
`to_lower`,
`is_alpha`,
`is_int`, and
`trim`.
All these functions should be written such that the tests succeed.
The goal of this exercise is to create a lot of
small helper functions and to re-use them.

If the functionality you need already exists in
(a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.
You can make use of `ord()` and `chr()`
that respectively turn a character into an integer, and vice versa.
Hence, it is not necessary to implement `ord()` and `chr()` yourself.

First play with these two functions until you understand how they work.
Then try to write a function `is_between` this function can be used
to make extreme simple implementations of ``is_digit` and `is_alpha`.
"""


def is_whitespace(ch):  # given
    return ch == ' ' or ch == '\t' or ch == '\r' or ch == '\n'
