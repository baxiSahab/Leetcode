class TimeMap:
    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass


# Test cases
if __name__ == "__main__":
    tm = TimeMap()

    # Test 1: Basic set and get
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))   # Expected: "bar"
    print(tm.get("foo", 3))   # Expected: "bar" (largest ts <= 3 is 1)

    # Test 2: Multiple values for same key
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))   # Expected: "bar2"
    print(tm.get("foo", 5))   # Expected: "bar2"

    # Test 3: Timestamp before any stored value
    print(tm.get("foo", 0))   # Expected: ""

    # Test 4: Key doesn't exist
    print(tm.get("unknown", 5))  # Expected: ""

    # Test 5: Multiple keys
    tm.set("love", "high", 10)
    tm.set("love", "low", 20)
    print(tm.get("love", 15))  # Expected: "high"
    print(tm.get("love", 20))  # Expected: "low"