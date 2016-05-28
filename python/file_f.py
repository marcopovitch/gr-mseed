#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 Marc Grunberg (marc.grunberg@unistra.fr)
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

import sys
sys.path.append('/Users/marc/.virtualenvs/qc/lib/python2.7/site-packages')
from obspy.core import read


class file_f(gr.sync_block):
    """
    docstring for block file_f
    """
    def __init__(self, filename):
        gr.sync_block.__init__(self,
                               name="file_f",
                               in_sig=None,
                               out_sig=[numpy.float32])

        print "Reading MSEED file %s" % filename
        st = read(filename)
        tr = st[0]
        self.data = tr.data
        self.samp_rate = 1./tr.stats['delta']
        print "setting sampling rate to %f" % self.samp_rate
        self.begin = 0

    def work(self, input_items, output_items):
        out = output_items[0]
        block_size = len(out)
        print "block_size = %d" % block_size
        end = self.begin + block_size
        print "[%d, %d]" % (self.begin, end)

        blk = self.data[self.begin:end]
        out[:len(blk)] = blk
        if len(blk) == 0:
            print "Work done !"
            return -1  # WORK_DONE
        self.begin += block_size

        return len(blk)

