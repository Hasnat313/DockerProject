# test_process.py
from process import generate_events, validate_events, summarize

def test_generate_events():
    events = generate_events(10)
    assert len(events) == 10
    assert all("event_id" in e for e in events)
    assert all("value" in e for e in events)

def test_validate_events():
    events = generate_events(50)
    valid, dropped = validate_events(events)
    assert len(valid) + dropped == len(events)

def test_summarize():
    events = generate_events(30)
    valid, _ = validate_events(events)
    summary = summarize(valid)
    assert len(summary) > 0
    assert all("count" in v for v in summary.values())

if __name__ == "__main__":
    test_generate_events()
    test_validate_events()
    test_summarize()
    print("All tests passed")