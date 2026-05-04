class TimeMap:

    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass


# --- Test Harness ---
tm = TimeMap()
tm.set("foo", "bar", 1)
print(tm.get("foo", 1))   # Expected: "bar"
print(tm.get("foo", 3))   # Expected: "bar"

tm.set("foo", "baz", 4)
print(tm.get("foo", 4))   # Expected: "baz"
print(tm.get("foo", 5))   # Expected: "baz"
print(tm.get("foo", 0))   # Expected: ""