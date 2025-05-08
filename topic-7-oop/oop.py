# test_case.py

class TestCase:
    def __init__(self, name, critical=False):
        self.name = name                  # Instance variable
        self.critical = critical          # Instance variable
        self.result = None                # Will be set later
        self.duration = 0.0

    def set_result(self, passed, duration):
        self.result = passed
        self.duration = duration

    def is_successful(self):
        return self.result is True

    def report(self):
        status = "✅ PASS" if self.result else "❌ FAIL"
        critical_tag = " [CRITICAL]" if self.critical else ""
        print(f"{self.name}{critical_tag}: {status} in {self.duration:.2f}s")


# === Using the class ===
test1 = TestCase("Login Test")
test2 = TestCase("Payment Test", critical=True)

# Simulate running the tests
test1.set_result(True, 1.2)
test2.set_result(False, 2.5)

# Print reports
test1.report()
test2.report()

# Check if all tests passed
print("\nAll tests passed?", test1.is_successful() and test2.is_successful())
