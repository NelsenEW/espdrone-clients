# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2011-2013 Bitcraze AB
#
#  Espdrone Nano Quadcopter Client
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License along with
#  this program; if not, write to the Free Software Foundation, Inc., 51
#  Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import os
from appdirs import AppDirs
import sys

# Path used all over the application
if not hasattr(sys, 'frozen'):
    module_path = os.path.dirname(__file__)
else:
    module_path = os.path.join(os.path.dirname(sys.executable),
                               'lib', 'edclient')
config_path = AppDirs("edclient", "Bitcraze").user_config_dir

# Locate the sdl2 lib on Windows (should be in edclient/thirst_party/)
if os.name == 'nt':
    os.environ["PYSDL2_DLL_PATH"] = os.path.join(module_path, "third_party")

if not hasattr(sys, 'frozen'):
    import pkg_resources
    try:
        VERSION = pkg_resources.require("edclient")[0].version
    except pkg_resources.DistributionNotFound:
        VERSION = "dev"
else:
    import json
    with open(os.path.join(module_path, "version.json")) as f:
        VERSION = json.load(f)['version']
