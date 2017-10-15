from timeline.timelines import Timeline, TimelineElement
from what_are_we_waiting_for.models import LabTest, Imaging, SpecialistReview


class WhatAreWeWaitingForTimeline(Timeline):
    slug = "what_are_we_waiting_for_timeline"

    elements = (
        TimelineElement(
            subrecord=LabTest,
            group_by="requested_timestamp",
            template="timeline/lab_test_requested.html",
            aggregate_template="timeline/aggregate_template.html"
        ),
        TimelineElement(
            subrecord=LabTest,
            group_by="reviewed_timestamp",
            template="timeline/lab_test_reviewed.html",
            aggregate_template="timeline/aggregate_template.html"
        ),
        TimelineElement(
            subrecord=Imaging,
            group_by="requested_timestamp",
            template="timeline/imaging_requested.html",
            aggregate_template="timeline/aggregate_template.html"
        ),
        TimelineElement(
            subrecord=Imaging,
            group_by="reviewed_timestamp",
            template="timeline/imaging_reviewed.html",
            aggregate_template="timeline/aggregate_template.html"
        ),
        TimelineElement(
            subrecord=SpecialistReview,
            group_by="requested_timestamp",
            template="timeline/speciality_type_requested.html",
            aggregate_template="timeline/aggregate_template.html"
        ),
        TimelineElement(
            subrecord=SpecialistReview,
            group_by="reviewed_timestamp",
            template="timeline/speciality_type_reviewed.html",
            aggregate_template="timeline/aggregate_template.html"
        ),
    )
