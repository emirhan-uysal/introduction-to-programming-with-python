# exception_handling.py

class TestError(Exception):
    """Custom exception for test-related failures."""
    def __init__(self, message):
        super().__init__(message)


def run_parallel_tests(total_steps, threads):
    try:
        if not isinstance(total_steps, int) or not isinstance(threads, int):
            raise TypeError("Inputs must be integers")

        if threads <= 0:
            raise ValueError("Number of threads must be greater than zero")

        steps_per_thread = total_steps / threads
        print(f"Each thread will handle {steps_per_thread:.2f} steps")

        if steps_per_thread > 10:
            raise TestError("Too many steps per thread! Might be unstable.")

    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero (no threads given)")

    except TypeError as e:
        print(f"❌ Type Error: {e}")

    except ValueError as e:
        print(f"❌ Value Error: {e}")

    except TestError as e:
        print(f"⚠️ Custom Test Error: {e}")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    else:
        print("✅ Test load balanced successfully")

    finally:
        print("🔚 Done attempting test distribution\n")


# === Run with different test cases ===
run_parallel_tests(50, 5)
run_parallel_tests(50, 0)         # Triggers ZeroDivisionError
run_parallel_tests(50, "four")    # Triggers TypeError
run_parallel_tests(50, 3)         # Triggers custom TestError

# with_and_exception_handling.py

def load_test_config(file_path):
    try:
        with open(file_path, 'r') as f:
            config = f.read()
            print("📄 Config Loaded:")
            print(config)
            return config

    except FileNotFoundError:
        print(f"❌ Error: File not found -> {file_path}")

    except IOError as e:
        print(f"❌ I/O Error while reading file: {e}")

    finally:
        print("🔚 Finished attempting to read configuration\n")


# === Try reading valid and invalid files ===
load_test_config("config.txt")         # Try this with a real file
load_test_config("missing_config.txt") # Should trigger FileNotFoundError
