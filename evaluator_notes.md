# Evaluator Notes

## Purpose

This task evaluates whether a model understands
idempotent event ingestion behavior.

## Skills Tested

- state management
- reasoning about identity
- architectural consistency
- edge-case handling

## Common Incorrect Solutions

### Incorrect:
Deduplicating entire dictionaries

Why it fails:
Metadata changes can bypass equality checks.

### Incorrect:
Deduplicating in `daily_summary`

Why it fails:
Duplicates still pollute storage.