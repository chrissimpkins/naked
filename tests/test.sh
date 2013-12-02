#!/bin/sh

NOSE_FLAGS="--verbosity=2"
TEST_COMMAND="nosetests"
COM_PARSE_TESTS="test_COMMAND_PARSE.py"
COM_ALL_COMMANDS="test_COMMANDS.py"
IO_TESTS="test_IO.py"

if [ "$1" = "all" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$COM_PARSE_TESTS" "$COM_ALL_COMMANDS" "$IO_TESTS"
elif [ "$1" = "commandparse" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$COM_PARSE_TESTS"
elif [ "$1" = "commands" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$COM_ALL_COMMANDS"
elif [ "$1" = "io" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$IO_TESTS"
else
	echo "Enter 'all' or a command suite to test."
	exit 1
fi
