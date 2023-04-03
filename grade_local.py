#!/usr/bin/env python3

"""
Do a local practice grading.
The score you recieve here is not an actual score,
but gives you an idea on how prepared you are to submit to the autograder.
"""

import os
import sys
import types

import cse40.question
import cse40.assignment
import cse40.style
import cse40.utils

class T1A(cse40.question.Question):
    def score_question(self, submission):
        # We cal call your code using the submission object.
        result = submission.my_function()

        # Does the function return NotImplemented?
        if (self.check_not_implemented(result)):
            return

        # Does the function return a boolean?
        if (not isinstance(result, bool)):
            self.fail("Function must return a boolean value.")
            return

        # Add your code here.

        self.full_credit()

class T2A(cse40.question.Question):
    def score_question(self, submission):
        try:
            submission.test_my_function_value(4)
            self.fail("Function did not raise an exception on a bad value (4).")
        except Exception:
            self.full_credit()

class T2B(cse40.question.Question):
    def score_question(self, submission):
        question = submission.TestMyFunction("Test my_function()", 100)

        def my_bad_function():
            return False

        test_submission = types.SimpleNamespace(my_function = my_bad_function)
        question.score_question(test_submission)

        if (question.score == 100):
            self.fail("Test class passed a function that returned a bad value (False).")
            return

        self.full_credit()

def grade(path):
    submission = cse40.utils.prepare_submission(path)

    questions = [
        T1A("Task 1.A (my_function)", 40),
        T2A("Task 2.A (test_my_function_value)", 30),
        T2B("Task 2.B (TestMyFunction)", 30),
        cse40.style.Style(path, max_points = 0),
    ]

    assignment = cse40.assignment.Assignment('Practice Grading for Hands-On 0', questions)
    assignment.grade(submission)

    return assignment

def main(path):
    assignment = grade(path)
    print(assignment.report())

def _load_args(args):
    exe = args.pop(0)
    if (len(args) != 1 or ({'h', 'help'} & {arg.lower().strip().replace('-', '') for arg in args})):
        print("USAGE: python3 %s <submission path (.py or .ipynb)>" % (exe), file = sys.stderr)
        sys.exit(1)

    path = os.path.abspath(args.pop(0))

    return path

if (__name__ == '__main__'):
    main(_load_args(list(sys.argv)))
