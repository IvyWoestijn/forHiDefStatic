"""
Write the functions
`line`,
`rectangle`,
`parallelogram`, and
`triangle` such that all tests succeed.

*If the functionality you need already exists in
(a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.*

The focus in this exercise is to work with default parameters.
All functions expect the `size` as first parameters (1 or 2).
These are compulsive.

After the size you can decide to create a filled shape or an *hollow shape*.
The default is filled.
        ****             ****
        ****             *  *
Filled: ****     Hollow: ****

Then, you can optionally supply how far from the left margin the drawing
should be placed (indentation).
By default the drawing should be placed as close to the margin as possible.

Finally, it should be possible to change the default drawing char
from '*' to anything else.

For `parallelogram` you can also decide the slope
(integer, positive or negative).

For triangle we suggest the following signature:
triangle(width, fill=True, indentation=0, char='*',
         align_right=False, from_top_to_bottom=True)
"""
