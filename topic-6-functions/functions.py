# log_utils.py

from datetime import datetime

# === Basic function ===
def log_test_result(test_name, passed):
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"[{datetime.now()}] {test_name}: {status}")

# === Simulated overloading using default arguments ===
def log_test_result_with_details(test_name, passed, duration=None, critical=False):
    status = "✅ PASS" if passed else "❌ FAIL"
    line = f"[{datetime.now()}] {test_name}: {status}"
    
    if duration is not None:
        line += f" | Duration: {duration:.2f}s"
    if critical:
        line += " | ⚠️ Critical Test"
    
    print(line)

# === Simulated overloading using *args and **kwargs ===
def log(*args, **kwargs):
    """
    Generic logger that can handle flexible arguments.
    """
    if args:
        print(" - ".join(str(arg) for arg in args), end=" ")

    if kwargs:
        print("|", ", ".join(f"{k}={v}" for k, v in kwargs.items()))

    if not args and not kwargs:
        print("[LOG] No details provided")

# === Example usage ===

log_test_result("Login", True)
log_test_result_with_details("Purchase", False, duration=3.2, critical=True)
log_test_result_with_details("Search", True)

print("\nUsing generic logger:")
log("Cart", "FAILED", time="2.1s", retries=2)
log(message="Environment unstable", code=503)
log()
