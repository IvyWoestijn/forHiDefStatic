"""
Implements the functions
`is_leap_year`,
`number_of_days_in_month`,
`number_of_days_in_year`,
`number_of_day` (compute the number of days until this day in a year), and
`date_diff_in_days`
such that all tests succeed.

If the functionality you need already exists in
(a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.
"""

number_of_days_in_month_data = {
    True: [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],  # leap year
    False: [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # non leap year
}
