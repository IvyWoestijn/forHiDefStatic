"""
Given is a list of friends, which we represent in Python as
a dictionary with a `name` and an `age`.
We know that these lists are always sorted by name (alphabetically),
the ages are random.

Write the following three functions a **efficient** as possible:
`find_by_name(a_list, a_name)`,
`get_age(a_list, a_name)`, and
`get_oldest(a_list)`.

`find_by_name(a_list, a_name)` tries to find **a friend** (a `person`)
in the list with the given name.
Give an appropriate answer when no such friend exists in the list.
Note that the list is sorted by name.

`get_age(a_list, a_name)` tries to find **the age** of the friend
with the given name in a list.
Give an appropriate answer when no such friend exists in the list(
§Note that the list is sorted by name.)


`get_oldest(a_list)` searches for the oldest **friend** in a list.
It is possible that more than one such friend exists,
hence you should return the **all**.
Make sure they are (still) ordered alphabetically.

"""
