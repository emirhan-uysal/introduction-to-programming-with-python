# retry_loops.py

import random
import time

# Simulate a flaky function (e.g., service readiness check)
def is_service_ready():
    # Randomly return True or False (70% failure rate)
    return random.random() > 0.7

max_attempts = 5

# === WHILE Loop ===
print("🔁 WHILE loop: Retry until service is ready or attempts exhausted")

attempt = 0
ready = False

while attempt < max_attempts and not ready:
    attempt += 1
    print(f"Attempt {attempt}: Checking...")
    ready = is_service_ready()
    if not ready:
        print("Service not ready. Retrying...")
        time.sleep(0.2)

print("✅ Ready!" if ready else "❌ Gave up after max attempts.\n")

# === Simulated DO-WHILE Loop ===
print("🔁 Simulated DO-WHILE loop: Always attempt at least once")

attempt = 0
ready = False

while True:
    attempt += 1
    print(f"Attempt {attempt}: Checking...")
    ready = is_service_ready()
    if ready or attempt >= max_attempts:
        break
    print("Service not ready. Retrying...")
    time.sleep(0.2)

print("✅ Ready!" if ready else "❌ Gave up after max attempts.\n")

# === FOR Loop ===
print("🔁 FOR loop: Run flaky check across multiple test cases")

successful_runs = 0
total_runs = 10

for i in range(1, total_runs + 1):
    print(f"\nTest Case #{i}:")
    for attempt in range(1, max_attempts + 1):
        print(f"  Attempt {attempt}: Checking...")
        if is_service_ready():
            print(f"  ✅ Service ready on attempt {attempt}")
            successful_runs += 1
            break
        else:
            print("  Service not ready.")
            time.sleep(0.1)
    else:
        print("  ❌ Test case failed after max retries.")

print(f"\nSummary: {successful_runs}/{total_runs} test cases passed.")
