# Task 001 — Event Deduplication Retry Bug

## Scenario

The analytics ingestion service duplicates events whenever retry requests occur.

## Expected Behavior

Repeated ingestion attempts using the same `event_id`
should not create duplicate analytics records.

## Actual Behavior

Duplicate retries inflate summary counts.

## Constraints

- Do not change the public API
- Preserve existing functionality
- Maintain performance characteristics