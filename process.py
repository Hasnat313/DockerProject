# process.py
import json
import random
import uuid
from datetime import datetime

def generate_events(n=100):
    event_types = ["sensor_read", "motor_command", "status_update"]
    events = []
    for _ in range(n):
        events.append({
            "event_id": str(uuid.uuid4()),
            "event_type": random.choice(event_types),
            "value": round(random.uniform(0.0, 100.0), 2),
            "timestamp": datetime.utcnow().isoformat()
        })
    return events

def validate_events(events):
    valid = []
    for e in events:
        if e["value"] >= 0 and e["event_id"]:
            valid.append(e)
    invalid = len(events) - len(valid)
    return valid, invalid

def summarize(events):
    summary = {}
    for e in events:
        t = e["event_type"]
        if t not in summary:
            summary[t] = {"count": 0, "total_value": 0.0}
        summary[t]["count"] += 1
        summary[t]["total_value"] += e["value"]
    return summary

def main():
    print("Generating events...")
    events = generate_events(100)

    print("Validating...")
    valid, dropped = validate_events(events)
    print(f"Valid: {len(valid)}, Dropped: {dropped}")

    print("Summarizing...")
    summary = summarize(valid)
    for event_type, stats in summary.items():
        print(f"{event_type}: {stats['count']} events, "
              f"avg value: {stats['total_value']/stats['count']:.2f}")

    # save output
    with open("output/summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("Done — output/summary.json written")

if __name__ == "__main__":
    import os
    os.makedirs("output", exist_ok=True)
    main()