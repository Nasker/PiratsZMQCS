#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2020'
__date__ = '23/07/2020'
__credits__ = ['Otger Ballester', ]
__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

from simplecssys.config import ConfObject


class ServerPortsConfig(ConfObject):
    cmd_port = 56485
    async_port = 56486


# Example of how to define a Configuration with childs
class SubChapterConfig(ConfObject):
    field1 = None
    field2 = None


class ChapterConfig(ConfObject):
    chfield = True
    subchapter = SubChapterConfig()


class FullConfig(ConfObject):
    server_ports = ServerPortsConfig()
    exampleconf = ChapterConfig()


if __name__ == "__main__":

    fc = FullConfig()
    # to use it
    print(fc.as_dict())

    # to load a yaml into the config
    # fc.load_yaml(yaml_path)
    # to save a yaml so a user can edit



