#!/usr/bin/env python
# Copyright (C) 2016 Canonical
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from setuptools import setup

INSTALL_REQUIRES = [
    "gunicorn",
    "redis",
    "flask",
]

TEST_REQUIRES = [
    "fakeredis",
    "mock",
]

setup(
    name='testflinger',
    version='1.0',
    long_description=__doc__,
    packages=['testflinger'],
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
    tests_require=TEST_REQUIRES,
    test_suite='testflinger.tests',
)
