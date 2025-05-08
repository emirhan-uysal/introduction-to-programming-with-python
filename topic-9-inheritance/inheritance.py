# inheritance_polymorphism.py

class TestCase:
    def __init__(self, name):
        self.name = name
        self.result = None
        self.duration = 0.0

    def run(self):
        print(f"Running generic test: {self.name}")

    def report(self):
        status = "✅ PASS" if self.result else "❌ FAIL"
        print(f"{self.name}: {status} in {self.duration:.2f}s")


# === Subclass for API Tests ===
class ApiTestCase(TestCase):
    def __init__(self, name, endpoint):
        super().__init__(name)
        self.endpoint = endpoint

    def run(self):
        print(f"Calling API: {self.endpoint}")
        # Simulate API test result
        self.result = True
        self.duration = 1.1

    def report(self):
        print(f"[API] {self.name} -> {self.endpoint}")
        super().report()


# === Subclass for UI Tests ===
class UiTestCase(TestCase):
    def __init__(self, name, screen):
        super().__init__(name)
        self.screen = screen

    def run(self):
        print(f"Opening screen: {self.screen}")
        # Simulate UI test result
        self.result = False
        self.duration = 2.3

    def report(self):
        print(f"[UI] {self.name} on {self.screen}")
        super().report()


# === Demonstrate polymorphism ===

# All treated as TestCase type
test_cases = [
    ApiTestCase("Login API Test", "/api/login"),
    UiTestCase("Login Page Test", "LoginScreen")
]

for test in test_cases:
    test.run()
    test.report()
