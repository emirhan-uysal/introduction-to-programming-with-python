###############################################################
# 
#  Primitive types --> int float bool str
#
###############################################################

total_tests = 10                # int
passed_tests = 7                # int
failed_tests = total_tests - passed_tests  # int
test_duration_seconds = 45.8    # float
all_passed = failed_tests == 0  # bool
report_title = "Test Summary"   # str

# Type casting
pass_percentage = (passed_tests / total_tests) * 100        # pass_percentage type will be float
pass_percentage_as_string = str(round(pass_percentage, 2)) + "%"  # changes the type from float to string


###############################################################
# 
#  Non-Primitive types --> everything execpt int float bool str
#
###############################################################

test_results = [True, True, False, True, False, True, True, True, True, True]  # List of bools
test_names = ["Login", "Logout", "Purchase", "Search", "Cart", "Profile", "Settings", "Help", "Signup", "Checkout"] # List of string

# Dictionary
summary = {
    "title": report_title,
    "total": total_tests,
    "passed": passed_tests,
    "failed": failed_tests,
    "duration_seconds": test_duration_seconds,
    "pass_percentage": pass_percentage,
    "all_passed": all_passed,
}

import helper

helper.generate_html_report(summary)