#!/bin/bash

TEST_DIR="tests/test_*.py"

for test in `ls $TEST_DIR`; do
    echo "Running test $test"
    python3 -m unittest $test
done