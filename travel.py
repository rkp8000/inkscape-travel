#!/usr/bin/env python
# coding: utf-8 

"""
singleshape.py
Simple inkscape extension for tutorial purposes.

Code by Rich Pang (2018).
"""

import inkex, simplestyle
import numpy as np

__version__ = '1.0'

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
            '', '--x', action='store', type='string', dest='x', default='', help='x')
        self.OptionParser.add_option(
            '', '--y', action='store', type='string', dest='y', default='', help='y')
        self.OptionParser.add_option(
            '', '--x_size', action='store', type='string', dest='x_size', default='', help='x size')
        self.OptionParser.add_option(
            '', '--y_size', action='store', type='string', dest='y_size', default='', help='y size')
        self.OptionParser.add_option(
            '', '--theta', action='store', type='string', dest='theta', default='', help='theta')
        self.OptionParser.add_option(
            '', '--active-tab', action='store', type='string', dest='active_tab', default='options', help='active tab')
        
    def effect(self):
        
        x_scale = self.options.x_scale
        y_scale = self.options.y_scale
        
        t_start = self.options.t_start
        t_end = self.options.t_end
        fps = self.options.fps
        dt = self.options.dt
        
        x = self.options.x
        y = self.options.y
        
        x_size = self.options.x_size
        y_size = self.options.y_size
        
        theta = self.options.theta
        
        rect_id, rect = self.selected.iteritems().next()
        
        w = rect.get('width')
        h = rect.get('height')
        
        x_rect = rect.get('x')
        y_rect = rect.get('y')
        
        # for educative purposes: write user params to file
        with open('travel.log', 'w') as f:
            
            f.write('USER PARAMS:\n\n')
            
            f.write('x_scale: {}\n'.format(x_scale))
            f.write('y_scale: {}\n\n'.format(y_scale))
            
            f.write('t_start: {}\n'.format(t_start))
            f.write('t_end: {}\n'.format(t_end))
            
            f.write('fps: {}\n'.format(fps))
            f.write('dt: {}\n\n'.format(dt))
            
            f.write('x(t): {}\n'.format(x))
            f.write('y(t): {}\n\n'.format(y))
            
            f.write('x_size: {}\n'.format(x_size))
            f.write('y_size: {}\n\n'.format(y_size))
            
            f.write('theta: {}\n\n'.format(theta))
            
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
        
        style = {
            'stroke'        : 'none',
            'stroke-width'  : '1',
            'fill'          : '#000000'
        }

        attribs = {
            'style'     : simplestyle.formatStyle(style),
            'height'    : str(50),
            'width'     : str(50),
            'x'         : str(0),
            'y'         : str(0)
        }
        rect = inkex.etree.SubElement(parent, inkex.addNS('rect','svg'), attribs )

        
if __name__ == '__main__':
    e = Travel()
    e.affect()

