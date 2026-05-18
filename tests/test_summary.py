from tasks.task_001_event_deduplication.buggy.store import EventStore
from tasks.task_001_event_deduplication.buggy.service import AnalyticsService

def test_summary_counts_events():
    store = EventStore()
    service = AnalyticsService(store)

    service.ingest_event({
        "event_id": "1",
        "type": "click"
    })

    service.ingest_event({
        "event_id": "2",
        "type": "click"
    })

    assert service.daily_summary() == {
        "click": 2
    }

def test_duplicate_event_ids_are_ignored():
    store = EventStore()
    service = AnalyticsService(store)

    service.ingest_event({
        "event_id": "1",
        "type": "click"
    })

    service.ingest_event({
        "event_id": "1",
        "type": "click"
    })

    assert service.daily_summary() == {
        "click": 1
    }