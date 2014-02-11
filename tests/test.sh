#!/bin/sh

NOSE_FLAGS="--verbosity=2"
TEST_COMMAND="nosetests"

CAST_TESTS="test_CASTS.py"
COM_PARSE_TESTS="test_COMMAND_PARSE.py"
COM_ALL_COMMANDS="test_COMMANDS.py"
IO_TESTS="test_IO.py"
NETWORK_TESTS="test_NETWORK.py"
NETWORK_TESTS_C="test_NETWORK_c.py"
PYTHON_TESTS="test_PYTHON.py"
PYTHON_TESTS_C="test_PYTHON_c.py"
STATE_TESTS="test_STATE.py"
STATE_TESTS_C="test_STATE_c.py"
SYS_TESTS="test_SYSTEM.py"
TEMPLATE_TESTS="test_INK_TEMPLATE.py"
TEMPLATE_TESTS_C="test_INK_TEMPLATE_c.py"


if [ "$1" = "all" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$CAST_TESTS" "$COM_PARSE_TESTS" "$COM_ALL_COMMANDS" "$IO_TESTS" "$NETWORK_TESTS" "$NETWORK_TESTS_C" "$PYTHON_TESTS" "$STATE_TESTS" "$STATE_TESTS_C" "$SYS_TESTS" "$TEMPLATE_TESTS" "$TEMPLATE_TESTS_C"
elif [ "$1" = "casts" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$CAST_TESTS"
elif [ "$1" = "commands" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$COM_ALL_COMMANDS"
elif [ "$1" = "io" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$IO_TESTS"
elif [ "$1" = "net" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$NETWORK_TESTS" "$NETWORK_TESTS_C"
elif [ "$1" = "parse" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$COM_PARSE_TESTS"
elif [ "$1" = "python" ]; then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$PYTHON_TESTS" "$PYTHON_TESTS_C"
elif [ "$1" = "state" ]; then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$STATE_TESTS" "$STATE_TESTS_C"
elif [ "$1" = "sys" ]; then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$SYS_TESTS"
elif [ "$1" = "template" ]; then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$TEMPLATE_TESTS" "$TEMPLATE_TESTS_C"
else
	echo "Enter 'all' or a command suite to test."
	exit 1
fi
