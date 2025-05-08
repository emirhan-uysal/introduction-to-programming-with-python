# encapsulated_test_case.py

class TestCase:
    def __init__(self, name, critical=False):
        self.__name = name              # Private attribute
        self._duration = 0.0            # Protected attribute (by convention)
        self.__result = None            # Private attribute
        self.critical = critical        # Public attribute

    # Public method to set result
    def set_result(self, passed, duration):
        self.__result = passed
        self._duration = duration

    # Public method to print report
    def report(self):
        status = "✅ PASS" if self.__result else "❌ FAIL"
        crit = " [CRITICAL]" if self.critical else ""
        print(f"{self.__name}{crit}: {status} in {self._duration:.2f}s")

    # === Getter for test name ===
    def get_name(self):
        return self.__name

    # === Setter for test name ===
    def set_name(self, new_name):
        if not new_name.strip():
            print("Name cannot be empty.")
            return
        self.__name = new_name

    # === Getter for result ===
    def is_successful(self):
        return self.__result is True


# === Using the encapsulated class ===
test = TestCase("Login Test", critical=True)

# Access public method
test.set_result(True, 1.45)
test.report()

# Try accessing private attribute directly (not recommended)
# print(test.__name)           # Will raise AttributeError

# Use getter and setter instead
print("\nCurrent name:", test.get_name())
test.set_name("Auth Test")
test.report()

test.set_name("   ")  # Will trigger validation
