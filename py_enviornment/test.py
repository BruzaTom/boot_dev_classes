from main import *

run_cases = [
    (200, 0.5, 1, 100),
    (200, 0.5, 2, 50),
    (200, 0.05, 3, 171),
]

submit_cases = run_cases + [
    (1000, 0.005, 2, 990),
    (1000, 0.05, 3, 857),
    (1200, 0.55, 8, 2),
    (1200, 0.09, 16, 265),
    (0, 0.5, 1, 0),
    (100, 0, 5, 100),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * intl_followers: {input1}")
    print(f" * fraction_lost_daily: {input2}")
    print(f" * days: {input3}")
    print(f"Expecting: {expected_output}")
    result = round(decayed_followers(input1, input2, input3))
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
