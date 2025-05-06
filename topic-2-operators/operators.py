total_tests = 12
passed_tests = 10
failed_tests = total_tests - passed_tests
duration_seconds = 55.3
critical_failures = 1
is_release_candidate = True

# Arithmetic Operators
pass_rate = passed_tests / total_tests * 100  # Division and multiplication
avg_time_per_test = duration_seconds / total_tests  # Simple division

# Comparison Operators
enough_tests_run = total_tests >= 10
high_pass_rate = pass_rate > 90
acceptable_duration = avg_time_per_test <= 10
no_critical_failures = critical_failures == 0

# Logical Operators
meets_quality_gate = (
    enough_tests_run and
    high_pass_rate and
    acceptable_duration and
    no_critical_failures
)

results = {
    "total_tests": total_tests,
    "passed_tests": passed_tests,
    "failed_tests": passed_tests,
    "duration_seconds": duration_seconds,
    "critical_failures": critical_failures,
    "is_release_candidate": is_release_candidate,
    "pass_rate": pass_rate,
    "avg_time_per_test": avg_time_per_test,
    "enough_tests_run": enough_tests_run,
    "high_pass_rate": high_pass_rate,
    "acceptable_duration": acceptable_duration,
    "no_critical_failures": no_critical_failures,
}

import helper

helper.generate_html_report_from_result(results)