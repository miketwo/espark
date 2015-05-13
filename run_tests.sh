#!/bin/bash -e

echo "Running unit tests..."
python espark/tests/test_espark.py

echo
echo "Running integration tests..."
diff=$(bin/esparkify data/domain_order.csv data/student_tests.csv | diff data/sample_solution.csv - || true)
if [ ${#diff} -gt 0 ]
then
    echo "Solutions are different!"
    echo "$diff"
    exit -1
else
    echo "All good."
fi

diff=$(bin/esparkify data/domain_order.csv data/edgecases.csv | diff data/edgecases_solution.csv - || true)
if [ ${#diff} -gt 0 ]
then
    echo "Solutions are different!"
    echo "$diff"
    exit -1
else
    echo "All good."
fi
