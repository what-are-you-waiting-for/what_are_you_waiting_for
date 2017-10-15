from timeline.timelines import Timeline, TimelineElement
from what_are_we_waiting_for.models import LabTest


class WhatAreWeWaitingForTimeline(Timeline):
    slug = "what_are_we_waiting_for_timeline"

    elements = (
        TimelineElement(subrecord=LabTest, when="requested"),
    )
