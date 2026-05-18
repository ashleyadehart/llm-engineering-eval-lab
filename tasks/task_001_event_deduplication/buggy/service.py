from tasks.task_001_event_deduplication.buggy.store import EventStore


class AnalyticsService:
    def __init__(self, store):
        self.store = store

    def ingest_event(self, event):
        self.store.add_event(event)

    def daily_summary(self):
        events = self.store.get_events()

        summary = {}

        for event in events:
            event_type = event["type"]

            if event_type not in summary:
                summary[event_type] = 0

            summary[event_type] += 1

        return summary