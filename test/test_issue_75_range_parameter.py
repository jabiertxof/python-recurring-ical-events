
"""This tests the range parameter for ics file.
see https://github.com/niccokunzmann/python-recurring-ical-events/issues/75
Description:  This parameter can be specified on a property that
    specifies a recurrence identifier.  The parameter specifies the
    effective range of recurrence instances that is specified by the
    property.  The effective range is from the recurrence identifier
    specified by the property.  If this parameter is not specified on
    an allowed property, then the default range is the single instance
    specified by the recurrence identifier value of the property.  The
    parameter value can only be "THISANDFUTURE" to indicate a range
    defined by the recurrence identifier and all subsequent instances.
    The value "THISANDPRIOR" is deprecated by this revision of
    iCalendar and MUST NOT be generated by applications.
"""

import pytest


@pytest.mark.parametrize(
    ("date", "summary"),
    [
        ("20240901", "ORGINAL EVENT"),
        ("20240911", "ORGINAL EVENT"),
        ("20240913", "MODIFIED EVENT"),
        ("20240915", "MODIFIED EVENT"),
        ("20240917", "MODIFIED EVENT"),
        ("20240919", "MODIFIED EVENT"),
        ("20240921", "MODIFIED EVENT"),
        ("20240923", "EDITED EVENT"),
        ("20240924", "EDITED EVENT"),  # RDATE
        ("20240925", "EDITED EVENT"),
    ],
)
def test_issue_75_RANGE_parameter(calendars, date, summary):
    events = calendars.issue_75_range_parameter.at(date)
    assert len(events) == 1, f"Expecting one event at {date}"
    event = events[0]
    assert event["SUMMARY"] == summary

# TODO: Test DTSTART and DTEND 
