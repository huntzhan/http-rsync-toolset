# -*- coding: utf-8 -*-
from __future__ import (
    division, absolute_import, print_function, unicode_literals,
)
from builtins import *                  # noqa
from future.builtins.disabled import *  # noqa

from os import getcwd
from os.path import dirname, join

from cpl import replace

from http_rsync_toolset.metadata import TARGET_NAME


def deploy():
    src = join(
        dirname(__file__),
        TARGET_NAME,
    )
    dst = join(
        getcwd(),
        TARGET_NAME,
    )
    replace(src, dst)
