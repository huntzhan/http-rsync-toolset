# -*- coding: utf-8 -*-
from __future__ import (
    division, absolute_import, print_function, unicode_literals,
)
from builtins import *                  # noqa
from future.builtins.disabled import *  # noqa

from os import getcwd
from os.path import dirname, join
from cpl import replace


def entry_point():
    print("entry_point")
    return 42


def deploy():
    TARGET_NAME = 'rsync-playbook'
    src = join(
        dirname(__file__),
        TARGET_NAME,
    )
    dst = join(
        getcwd(),
        TARGET_NAME,
    )
    replace(src, dst)
