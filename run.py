#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This calls the git Popen examples in different ways
    to show, what we need to test.
    We do need to test the Exceptions - see test_git.py """

import git
from git import GitCallException, GitErrorException
from pprint import pprint


print("-" * 30 + "Run git1 - successful:")
pprint(git.git1(['status', '-s']))

try:
    print("-" * 30 + "Run git1 - raise TypeError:")
    pprint(git.git1())
except TypeError as e:
    print e.message

try:
    print("-" * 30 + "Run git1 - raise GitCallException:")
    pprint(git.git1(''))
except GitCallException as e:
    print e.message

try:
    print("-" * 30 + "Run git1 - raise GitErrorException:")
    pprint(git.git1(['asdasdasd']))
except GitErrorException as e:
    print e.message


print("-" * 30 + "Run git2 - successful:")
pprint(git.git2(['status', '-s']))

try:
    print("-" * 30 + "Run git2 - raise TypeError:")
    pprint(git.git2())
except TypeError as e:
    print e.message

try:
    print("-" * 30 + "Run git2 - raise GitCallException:")
    pprint(git.git2(''))
except GitCallException as e:
    print e.message

try:
    print("-" * 30 + "Run git2 - raise GitErrorException:")
    pprint(git.git2(['asdasdasd']))
except GitErrorException as e:
    print e.message

