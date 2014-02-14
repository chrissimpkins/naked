#!/usr/bin/env python
# encoding: utf-8

import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 7: # do not run with tox in non-2.7 versions (fails because not building the C files)

    import unittest
    import os
    from Naked.toolshed.c.shell import execute, execute_rb, execute_js, run, run_rb, run_js, muterun, muterun_rb, muterun_js
    from Naked.toolshed.types import NakedObject

    class NakedCShellTest(unittest.TestCase):

        def setUp(self):
            self.good_command = "echo 'test command'"   #zero exit status, good command
            self.bad_command = "bogusapp -help" #non-zero exit status, missing executable
            self.missing_option = "ls --random" #non-zero exit status from an executable that is present
            self.node_success_path = os.path.join('testfiles', 'keep', 'js', 'node_success.js')
            self.node_fail_path = os.path.join('testfiles', 'keep', 'js', 'node_error.js')
            self.ruby_success_path = os.path.join('testfiles', 'keep', 'rb', 'ruby_success.rb')
            self.ruby_fail_path = os.path.join('testfiles', 'keep', 'rb', 'ruby_error.rb')

        def tearDown(self):
            pass


        #------------------------------------------------------------------------------
        # execute() method tests
        #------------------------------------------------------------------------------
        def test_execute_good_command(self):
            self.assertTrue(execute(self.good_command))

        def test_execute_bad_command(self):
            self.assertFalse(execute(self.bad_command))

        def test_execute_missing_option(self):
            self.assertFalse(execute(self.missing_option))

        #------------------------------------------------------------------------------
        # run() method tests
        #------------------------------------------------------------------------------
        def test_run_good_command(self):
            self.assertEqual(b"test command\n", run(self.good_command))

        def test_run_good_command_suppress_stdout(self):
            self.assertEqual(b"test command\n", run(self.good_command, suppress_stdout=True)) # still receive return value when stout print suppressed

        def test_run_bad_command(self):
            self.assertEqual(False, run(self.bad_command))

        def test_run_bad_command_output(self):
            test_string = run(self.bad_command)
            self.assertEqual(False, run(self.bad_command))

        def test_run_bad_command_output(self):
            with self.assertRaises(SystemExit): # raises SystemExit when suppress_exit_status_call = False
                self.assertEqual(False, run(self.bad_command, suppress_exit_status_call=False))

        def test_run_missing_option(self):
            self.assertEqual(False, run(self.missing_option))


        #------------------------------------------------------------------------------
        # muterun() tests
        #------------------------------------------------------------------------------
        def test_muterun_good_command_return_type(self):
            self.assertEqual(type(NakedObject()), type(muterun(self.good_command))) # returns NakedObject on success

        def test_muterun_bad_command_return_type(self):
            self.assertEqual(type(NakedObject()), type(muterun(self.bad_command))) # returns NakedObject on error

        def test_muterun_good_command_exitcode(self):
            out = muterun(self.good_command)
            self.assertEqual(0, out.exitcode) # exit code = 0 = success

        def test_muterun_good_command_stdout(self):
            out = muterun(self.good_command)
            self.assertEqual(b"test command\n", out.stdout) # stdout string is correct

        def test_muterun_good_command_stderr(self):
            out = muterun(self.good_command)
            self.assertEqual(b"", out.stderr)  # stderr empty string when successful command

        def test_muterun_bad_command_exitcode(self):
            out = muterun(self.bad_command)
            self.assertEqual(127, out.exitcode) # returns 127 on absent executable

        def test_muterun_bad_command_stdout(self):
            out = muterun(self.bad_command)
            self.assertEqual(b"", out.stdout) # std out is empty string on failure

        def test_muterun_bad_command_stderr(self):
            out = muterun(self.bad_command)
            self.assertTrue(b'bogusapp: command not found' in out.stderr) # has std err message on failure

        def test_muterun_missing_option_exitcode(self):
            out = muterun(self.missing_option)
            self.assertEqual(1, out.exitcode) # returns 1 on missing option to ls

        def test_muterun_missing_option_stderr(self):
            out = muterun(self.missing_option)
            self.assertTrue(len(out.stderr) > 0) # there is a stderr message present

        def test_muterun_missing_option_stdout(self):
            out = muterun(self.missing_option)
            self.assertEqual(b"", out.stdout)  # std out is empty string on failure


        #------------------------------------------------------------------------------
        # Node.js script execution tests
        #------------------------------------------------------------------------------
        def test_execute_node_success(self):
            self.assertTrue(execute_js(self.node_success_path))

        def test_execute_node_fail(self):
            self.assertFalse(execute_js(self.node_fail_path))

        def test_muterun_node_success(self):
            out = muterun_js(self.node_success_path)
            self.assertEqual(b'success\n', out.stdout)
            self.assertEqual(0, out.exitcode)
            self.assertEqual(b'', out.stderr)

        def test_muterun_node_fail(self):
            out = muterun_js(self.node_fail_path)
            self.assertEqual(b'error\n', out.stderr)
            self.assertEqual(b'', out.stdout)
            self.assertEqual(1, out.exitcode)

        def test_run_node_success(self):
            out = run_js(self.node_success_path)
            self.assertEqual(b'success\n', out)

        def test_run_node_success_suppress_stdout(self):
            out = run_js(self.node_success_path, suppress_stdout=True)
            self.assertEqual(b'success\n', out) # still returns a value, does not print to std out

        def test_run_node_fail_suppress_stderr(self):
            out = run_js(self.node_fail_path, suppress_stderr=True)
            self.assertEqual(False, out)  # returns False

        def test_run_node_fail_suppress_exitstatus_false(self):
            with self.assertRaises(SystemExit):
                out = run_js(self.node_fail_path, suppress_exit_status_call=False) # when suppress_exit_status=True, Python script stopped prematurely

        def test_run_node_success_suppress_exitstatus_false(self):
            out = run_js(self.node_success_path, suppress_exit_status_call=False) # when command succeeds SystemExit is not raised
            self.assertEqual(b'success\n', out)

        #------------------------------------------------------------------------------
        # Ruby script execution tests
        #------------------------------------------------------------------------------
        def test_execute_rb_success(self):
            self.assertTrue(execute_rb(self.ruby_success_path))

        def test_execute_rb_fail(self):
            self.assertFalse(execute_rb(self.ruby_fail_path))

        def test_muterun_rb_success(self):
            out = muterun_rb(self.ruby_success_path)
            self.assertEqual(b'success\n', out.stdout)
            self.assertEqual(0, out.exitcode)
            self.assertEqual(b'', out.stderr)

        def test_muterun_rb_fail(self):
            out = muterun_rb(self.ruby_fail_path)
            self.assertEqual(b'error\n', out.stderr)
            self.assertEqual(b'', out.stdout)
            self.assertEqual(1, out.exitcode)

        def test_run_rb_success(self):
            out = run_rb(self.ruby_success_path)
            self.assertEqual(b'success\n', out)

        def test_run_rb_success_suppress_stdout(self):
            out = run_rb(self.ruby_success_path, suppress_stdout=True)
            self.assertEqual(b'success\n', out) # still returns a value, does not print to std out

        def test_run_rb_fail_suppress_stderr(self):
            out = run_rb(self.ruby_fail_path, suppress_stderr=True)
            self.assertEqual(False, out)  # returns False

        def test_run_rb_fail_suppress_exitstatus_false(self):
            with self.assertRaises(SystemExit):
                out = run_rb(self.ruby_fail_path, suppress_exit_status_call=False) # when suppress_exit_status=True, Python script stopped prematurely

        def test_run_rb_success_suppress_exitstatus_false(self):
            out = run_js(self.node_success_path, suppress_exit_status_call=False) # when command succeeds SystemExit is not raised
            self.assertEqual(b'success\n', out)


