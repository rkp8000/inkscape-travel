#!/usr/bin/env python
# coding: utf-8 

"""
Copyright (C) 2018 Rich Pang, rpang.contact@gmail.com.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

from __future__ import division

import inkex, simplestyle
import numpy as np

__version__ = '0.1'

inkex.localize()


class Travel(inkex.Effect):
    
    def __init__(self):
        
        # initialize parent class
        inkex.Effect.__init__(self)
        
        # get params entered by user
        self.OptionParser.add_option(
            '', '--x_scale', action='store', type='float', dest='x_scale', default=0, help='x scale')
        self.OptionParser.add_option(
            '', '--y_scale', action='store', type='float', dest='y_scale', default=0, help='y scale')
        self.OptionParser.add_option(
            '', '--t_start', action='store', type='float', dest='t_start', default=0, help='t start')
        self.OptionParser.add_option(
            '', '--t_end', action='store', type='float', dest='t_end', default=1, help='t_end')
        self.OptionParser.add_option(
            '', '--fps', action='store', type='float', dest='fps', default=30, help='fps')
        self.OptionParser.add_option(
            '', '--dt', action='store', type='float', dest='dt', default=0.1, help='dt')
        self.OptionParser.add_option(
            '', '--x_eqn', action='store', type='string', dest='x_eqn', default='', help='x')
        self.OptionParser.add_option(
            '', '--y_eqn', action='store', type='string', dest='y_eqn', default='', help='y')
        self.OptionParser.add_option(
            '', '--x_size_eqn', action='store', type='string', dest='x_size_eqn', default='', help='x size')
        self.OptionParser.add_option(
            '', '--y_size_eqn', action='store', type='string', dest='y_size_eqn', default='', help='y size')
        self.OptionParser.add_option(
            '', '--theta_eqn', action='store', type='string', dest='theta_eqn', default='', help='theta')
        self.OptionParser.add_option(
            '', '--active-tab', action='store', type='string', dest='active_tab', default='options', help='active tab')
        
    def effect(self):

        # make sure rectangle is included in selection
        # if ... raise ...

        # get user-entered params

        x_scale = self.options.x_scale
        y_scale = self.options.y_scale
        
        t_start = self.options.t_start
        t_end = self.options.t_end
        fps = self.options.fps
        dt = self.options.dt
        
        x_eqn = self.options.x_eqn
        y_eqn = self.options.y_eqn
        
        x_size_eqn = self.options.x_size_eqn
        y_size_eqn = self.options.y_size_eqn
        
        theta_eqn = self.options.theta_eqn
        
        # get selected rect params

        rect_id, rect = self.selected.iteritems().next()
        
        w = float(rect.get('width'))
        h = float(rect.get('height'))
        
        x_rect = float(rect.get('x'))
        y_rect = float(rect.get('y'))

        x_0 = x_rect
        y_0 = y_rect + h

        # get selected object params
        # ... 
        
        # get common numpy operations
        abs = np.abs
        sin = np.sin
        cos = np.cos
        tan = np.tan
        exp = np.exp

        # compute dt
        if dt == 0:
            dt = 1./fps

        ts = np.arange(t_start, t_end, dt)

        # compute xs, ys, stretches, and rotations in arbitrary coordinates
        xs = np.nan * np.zeros(len(ts))
        ys = np.nan * np.zeros(len(ts))
        x_sizes = np.nan * np.zeros(len(ts))
        y_sizes = np.nan * np.zeros(len(ts))
        thetas = np.nan * np.zeros(len(ts))
        
        for ctr, t in enumerate(ts):
            xs[ctr] = eval(x_eqn)
            ys[ctr] = eval(y_eqn)
            x_sizes[ctr] = eval(x_size_eqn)
            y_sizes[ctr] = eval(y_size_eqn)
            thetas[ctr] = eval(theta_eqn)

        # ensure no Infs
        # ...

        # convert to screen coordinates
        xs *= (w/x_scale)
        xs += x_0

        ys *= (-h/y_scale)  # neg sign to invert y for inkscape screen
        ys += y_0

        x_sizes *= (w/x_scale)
        y_sizes *= (h/y_scale)

        # for educative purposes: write user params to file
        with open('travel.log', 'w') as f:
            
            f.write('t: {}\n\n'.format(t))

            f.write('x(t) = {}\n'.format(x_eqn))
            f.write('x: {}\n\n'.format(xs))
            f.write('y(t) = {}\n'.format(y_eqn))
            f.write('y: {}\n\n'.format(ys))

            f.write('x_size(t) = {}\n'.format(x_size_eqn))
            f.write('x_sizes: {}\n\n'.format(x_sizes))
            f.write('y_size(t) = {}\n'.format(y_size_eqn))
            f.write('y_sizes: {}\n\n'.format(y_sizes))

            f.write('theta(t) = {}\n'.format(theta_eqn))
            f.write('thetas: {}\n\n'.format(thetas))

            f.write('USER PARAMS:\n\n')
            
            f.write('x_scale: {}\n'.format(x_scale))
            f.write('y_scale: {}\n\n'.format(y_scale))
            
            f.write('t_start: {}\n'.format(t_start))
            f.write('t_end: {}\n'.format(t_end))
            
            f.write('fps: {}\n'.format(fps))
            f.write('dt: {}\n\n'.format(dt))
            
            f.write('x_eqn: {}\n'.format(x_eqn))
            f.write('y_eqn: {}\n\n'.format(y_eqn))
            
            f.write('x_size_eqn: {}\n'.format(x_size_eqn))
            f.write('y_size_eqn: {}\n\n'.format(y_size_eqn))
            
            f.write('theta_eqn: {}\n\n'.format(theta_eqn))
            
            f.write('RECT PROPERTIES:\n\n')
            
            f.write('width: {}\n'.format(w))
            f.write('height: {}\n'.format(h))
            f.write('x: {}\n'.format(x_rect))
            f.write('y: {}\n'.format(y_rect))
            
            f.write('SELECTED:\n\n')
            
            for a, b in self.selected.iteritems():
                f.write('{}:\n{}\n\n'.format(a, list(b.items())))
                
            f.write('np: {}\n'.format(np))
            
        parent = self.current_layer

        for x, y in zip(xs, ys):
            style = {
                'stroke': 'none',
                'stroke-width': '1',
                'fill': '#000000'
            }

            attribs = {
                'style': simplestyle.formatStyle(style),
                'r': str(2),
                'cx': str(x),
                'cy': str(y)
            }
            circle = inkex.etree.SubElement(parent, inkex.addNS('circle','svg'), attribs )

        
if __name__ == '__main__':
    e = Travel()
    e.affect()

