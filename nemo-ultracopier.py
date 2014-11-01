#! /usr/bin/python
#  -*- coding: utf-8 -*-

# Nemo action: Nemo-UltraCopy
# Release Date: 09 May 2014
#
# Authors: Lester Carballo Pérez(https://github.com/lestcape).
#
#          Email: lestcape@gmail.com     Website: https://github.com/lestcape/Nemo-UltraCopy
#
# "This is an action for the Nemo browser, to paste files using ultracopier
# instead of the default nemo copier tool."
#
# This program is free software:
#
#    You can redistribute it and/or modify it under the terms of the
#    GNU General Public License as published by the Free Software
#    Foundation, either version 3 of the License, or (at your option)
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import mimetypes
import sys
import os
import urllib
from gi.repository import Gtk, Gdk

clipboard  = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
result = clipboard.wait_for_contents(Gdk.Atom.intern("x-special/gnome-copied-files", False))
if result is not None:
    info = result.get_data().splitlines()
    action = info[0]
    files = info[1:]
    fileList = ""
    for file in files:
        if file.index("file://") == 0:
            fileList += " '" + urllib.unquote(file[7:]) + "'"

    print fileList
    print sys.argv[1]
    if action == "copy":
        os.system("ultracopier cp %s '%s'" % (fileList, urllib.unquote(sys.argv[1])))
    elif action == "cut":
        os.system("ultracopier mv %s '%s'" % (fileList, urllib.unquote(sys.argv[1])))

