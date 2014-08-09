#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2007-2008  Brian G. Matherly
# Copyright (C) 2008       Gary Burton
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# $Id$

"""
Option class representing a color.
"""

#-------------------------------------------------------------------------
#
# gramps modules
#
#-------------------------------------------------------------------------
from . import Option

#-------------------------------------------------------------------------
#
# ColorOption class
#
#-------------------------------------------------------------------------
class ColorOption(Option):
    """
    This class describes an option that allows the selection of a color.
    """
    def __init__(self, label, value):
        """
        @param label: A friendly label to be applied to this option.
            Example: "Males"
        @type label: string
        @param value: An initial value for this option.
            Example: "#ff00a0"
        @type value: string
        @return: nothing
        """
        Option.__init__(self, label, value)
