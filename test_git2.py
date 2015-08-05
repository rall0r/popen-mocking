#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock
import git
from git import GitCallException, GitErrorException


class TestGit(unittest.TestCase):

    @mock.patch('subprocess.Popen.communicate', return_value=('foo1', 'bar1'))
    @mock.patch('subprocess.Popen.wait', return_value=0)
    def test_git_ok(self, mock_wait, mock_popen):
        self.assertEqual(('foo1', 'bar1', 0), git.git2(['log']))

    @mock.patch('subprocess.Popen.communicate', return_value=('foo2', 'bar2'))
    @mock.patch('subprocess.Popen.wait', return_value=0)
    def test_git_raise_typeerror(self, mock_wait, mock_popen):
        self.assertRaises(TypeError, git.git2)

    @mock.patch('subprocess.Popen.communicate', return_value=('foo3', 'bar3'))
    @mock.patch('subprocess.Popen.wait', return_value=0)
    def test_git_raise_gitcallexception(self, mock_wait, mock_popen):
        self.assertRaises(GitCallException, lambda: git.git2(''))

    @mock.patch('subprocess.Popen.communicate', return_value=('foo4', 'bar4'))
    @mock.patch('subprocess.Popen.wait', return_value=1)
    def test_git_raise_giterrorexception(self, mock_wait, mock_popen):
        self.assertRaises(GitErrorException, lambda: git.git2(['log']))
