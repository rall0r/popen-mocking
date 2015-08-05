#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' These tests will all fail. They are here just for demonstrating the
    problem. '''

import unittest
import mock
import git


class TestGit(unittest.TestCase):

    # not working!
    # It fails because Popen.returncode is always None, followed by
    # the function under test raising an Exception.
    @mock.patch('subprocess.Popen.communicate', return_value=('foo', 'bar'))
    def test_git_mock_communicate(self, mock_popen):
        self.assertEqual(('foo', 'bar', 1), git.git1(['log']))

    # also not working!
    # Same as above.
    # We try to mock Popen.returncode, but that fails, because Popen.returncode
    # is no attribute of Popen.
    @mock.patch('subprocess.Popen.communicate', return_value=('foo', 'bar'))
    @mock.patch('subprocess.Popen.returncode', return_value=1)
    def test_git_mock_returncode(self, mock_popen, mock_2):
        self.assertEqual(('foo', 'bar', 1), git.git1(['log']))
