"""
# To Dutch
Write the function`to_dutch`, such that all tests succeed.

The key of this exercise is to start small: make your
function work for simple and small input.
E.G., make your to_dutch function first for digits,
than for 2digit numbers, etc. Just like in the previous exercises
the key is to reuse existing functions.

If the functionality you need already exists in
(a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.
"""

small = [
    'nul', 'een', 'twee', 'drie', 'vier',
    'vijf', 'zes', 'zeven', 'acht', 'negen',

    'tien', 'elf', 'twaalf', 'dertien', 'veertien',
    'vijftien', 'zestien', 'zeventien', 'achttien', 'negentien'
]

tens = ['nul', 'tien', 'twintig', 'dertig', 'veertig',
        'vijftig', 'zestig', 'zeventig', 'tachtig', 'negentig']

scales = ['een', 'tien', 'honderd', 'duizend ', ' miljoen ',
          ' miljard ', ' biljoen ', ' biljard ', ' triljoen ', ' triljard ']
