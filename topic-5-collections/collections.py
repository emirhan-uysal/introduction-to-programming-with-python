# test_collections.py

# === Tuple: Immutable test configuration ===
test_config = ("API v2", "env=staging", "timeout=5s")
print("Test Config:", test_config)

# === List: Ordered collection of test case names ===
test_cases = ["Login", "Logout", "Purchase", "Search", "Cart", "Profile"]
print("\nTest Cases (list):", test_cases)

# Add a new test case
test_cases.append("Notifications")

# Remove one
test_cases.remove("Logout")

# === Dict: Map test names to pass/fail result ===
test_results = {
    "Login": True,
    "Purchase": False,
    "Search": True,
    "Cart": False,
    "Profile": True,
    "Notifications": True
}

print("\nTest Results (dict):")
for test, result in test_results.items():
    status = "✅ Pass" if result else "❌ Fail"
    print(f"  {test}: {status}")

# === Set: Unique error messages collected from failures ===
error_messages = set()

# Simulate collecting errors from failed tests
if not test_results["Purchase"]:
    error_messages.add("Payment gateway timeout")
if not test_results["Cart"]:
    error_messages.add("Cart service 500 error")
# Simulate a duplicate error
error_messages.add("Payment gateway timeout")

print("\nUnique Error Messages (set):")
for err in error_messages:
    print("  ⚠️", err)

# === Summary using all collections ===
print("\n📊 Summary:")
print("Total Test Cases:", len(test_cases))
print("Passed:", sum(1 for passed in test_results.values() if passed))
print("Failed:", sum(1 for passed in test_results.values() if not passed))
print("Unique Errors:", len(error_messages))
