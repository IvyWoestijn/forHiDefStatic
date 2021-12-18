"""
# Symptoms (exam 2020-2021)
This whole assignment is about log books of patients, in which
one can see whether or not the patient showed symptoms on any give date.

`{"date": "2021/12/31", "symptoms": False}` implies that the patient
did not show any symptoms on the thirty-first of December.

`{"date": "2021/12/31", "symptoms": True}` implies that the patient
did show symptoms on the thirty-first of December.

One such piece of information is what we call an entry
(pl.: entries) in this assignment.

You can assume that the entries in these log books are **always sorted
by date** and that the log books are complete. Here, complete means
that you will find one entry for every day between the start date
and the and date. In other words, the dates in these entries do not
show any holes or jumps.

Using such a log book with the history of symptoms, we can partition
the entries in three periods: incubation, sickness, and recovered.
If you do not understand, we can show you an example table that
visualizes this exactly.

===

Write the function `get_incubation_days(patient_logbook)`
which returns the list of entries before the first symptom presented itself.
Make sure the order of entries does not change.

Write the function `get_sickness_days(patient_logbook)`
which returns the list of entries between the first symptom
and the last symptom presented themselves.
Make sure the order of entries does not change.

Write the function `get_recovered_days(patient_logbook)`
which returns the list of entries after the last symptom presented itself.
Make sure the order of entries does not change.

## Remark:
Keep the general guidelines into account
(only use studied techniques and mind your coding style).
"""
