#!/usr/bin/env python
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
#  this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""
This class provides a spin box with IP address
"""

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QAbstractSpinBox
from ipaddress import IPv4Address, AddressValueError

__author__ = "Bitcraze AB"
__all__ = ["IpSpinBox"]

DEFAULT_ADDR = "192.168.43.42"

class IpSpinBox(QAbstractSpinBox):
    def __init__(self, *args):
        QAbstractSpinBox.__init__(self, *args)
        regexp = QtCore.QRegExp("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        self.validator = QtGui.QRegExpValidator(regexp)
        self._value = None

    def validate(self, text, pos):
        return self.validator.validate(text, pos)

    def textFromValue(self, value):
        return str(value)

    def setValue(self, value):
        self._value = IPv4Address(value)
        self.lineEdit().setText(self.textFromValue(value))

    def value(self):
        try:
            self._value = IPv4Address(self.lineEdit().text())
            return str(self._value)
        except AddressValueError:
            if self.lineEdit().text():
                return str(-1)
            return None
        

    def stepBy(self, steps):
        if self._value is None:
            self._value = IPv4Address(DEFAULT_ADDR)
        self.setValue(self._value + steps)

    def stepEnabled(self):
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled
