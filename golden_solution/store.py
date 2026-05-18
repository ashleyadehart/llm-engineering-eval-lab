class EventStore:
    def __init__(self):
        self.events = []
        self.event_ids = set()

    def add_event(self, event):
        event_id = event["event_id"]

        if event_id in self.event_ids:
            return

        self.events.append(event)
        self.event_ids.add(event_id)

    def get_events(self):
        return self.events