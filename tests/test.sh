#!/bin/sh

NOSE_FLAGS="--verbosity=3"
TEST_COMMAND="nosetests"
CL_TESTS="test_COMMAND.py"

if [ "$1" = "all" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$CL_TESTS"
elif [ "$1" = "commandline" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$CL_TESTS"
else
	echo "Enter 'all' or a command suite to test."
	exit 1
fi
