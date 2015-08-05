#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Building a simple prototype for working with
   Popen, especialy mocking Popen'''

from subprocess import PIPE, Popen


class GitCallException(Exception):
    pass


class GitErrorException(Exception):
    pass


# Hard to test because of Popen.returncode.
# How can we mock Popen.returncode?
# See corresponding unittests (test_git1.py) for ways that won't work.
def git1(args):
    if not args:
        raise GitCallException('args must be provided')

    p = Popen(['git'] + args, stdin=PIPE, stdout=PIPE)
    out, err = p.communicate()
    # look here:
    rc = p.returncode

    if rc != 0:
        raise GitErrorException('git returncode: {0}'.format(rc))

    return out, err, rc


# Look at Popen.wait()
# That is easy to mock.
# See unittest test_git2.py
def git2(args):
    if not args:
        raise GitCallException('args must be provided')

    p = Popen(['git'] + args, stdin=PIPE, stdout=PIPE)
    out, err = p.communicate()
    # look here
    rc = p.wait()

    if rc != 0:
        raise GitErrorException('git returncode: {0}'.format(rc))

    return out, err, rc
