from main import *

run_cases = [
    ([1, 2, 3, 4, 4, 5, 6, 7, 7, 7], [1, 2, 3, 4, 5, 6, 7]),
    ([10, 10, 20, 30, 30, 30, 40, 50, 50], [10, 20, 30, 40, 50]),
]

submit_cases = run_cases + [
    (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ),
    ([], []),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 20, 30, 40, 50, 50, 40, 30, 20, 10], [10, 20, 30, 40, 50]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * nums: {input1}")
    print(f"Expecting: {expected_output}")
    result = remove_duplicates(input1)
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
