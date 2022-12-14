# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SoiMapClipper
                                 A QGIS plugin
 This plugin clips the map area of Survey of India map sheets
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-03-30
        copyright            : (C) 2022 by Jack Tomaney
        email                : jat90@cam.ac.uk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Jack Tomaney'
__date__ = '2022-03-30'
__copyright__ = '(C) 2022 by Jack Tomaney'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SoiMapClipper class from file SoiMapClipper.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .SOI_map_clipper import SoiMapClipperPlugin
    return SoiMapClipperPlugin(iface)
