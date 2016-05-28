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
import pmt

import sys
sys.path.append('/Users/marc/.virtualenvs/qc/lib/python2.7/site-packages')
from obspy.seedlink import SLClient


class seedlink_f(gr.sync_block, gr.tagged_stream_block):
    """
    Get seismological waveform from seedlink server
    It's a 'source' block.

    server_url = "rtserve.resif.fr:18000"
    channel = "FR_CHIF:HHZ"
    """
    def __init__(self, server, port, channel):
        gr.sync_block.__init__(self,
                               name="seedlink_f",
                               in_sig=None,
                               out_sig=[numpy.float32])

        # initialise seedlink client
        server_url = server + ":" + str(port)
        self._slClient = SLClient(loglevel='error')
        self._slClient.slconn.setSLAddress(server_url)
        self._slClient.multiselect = (channel)
        self._channel = channel
        self._slClient.initialize()
        self.nitems_written = 0

    def work(self, input_items, output_items):
        out = output_items[0]
        slpack = self._slClient.slconn.collect()
        try: 
            seqnum = slpack.getSequenceNumber()
            trace = slpack.getTrace()
        except:
            out[:] = []
            return 0

        # print "sending slpack(id:%d): %d samples, len(out)=%d" % \
        #     (seqnum, len(trace.data), len(out))
        out[:len(trace.data)] = numpy.float32(trace.data)

        # https://gnuradio.org/doc/doxygen/page_python_blocks.html
        # https://github.com/guruofquality/grextras/wiki/Blocks-Coding-Guide
        # add_item_tag(which_output, abs_offset, key, value, srcid)

        # add a packet length tag
        abs_offset = self.nitems_written + 0
        key = pmt.string_to_symbol("packet_len")
        value = pmt.from_long(len(trace.data))
        srcid = pmt.string_to_symbol(self._channel)
        self.add_item_tag(0, abs_offset, key, value, srcid)

        # add a tag to manage time
        abs_offset = self.nitems_written + 0
        key = pmt.string_to_symbol("rx_time")
        value = pmt.from_double(trace.stats['starttime'].timestamp)
        srcid = pmt.string_to_symbol(self._channel)
        self.add_item_tag(0, abs_offset, key, value, srcid)
        # print "starttime ", trace.stats['starttime'].timestamp

        # add a tag to manage sample rate change
        abs_offset = self.nitems_written + 0
        key = pmt.string_to_symbol("rx_rate")
        fech = 1./trace.stats['delta']
        value = pmt.from_double(fech)
        srcid = pmt.string_to_symbol(self._channel)
        self.add_item_tag(0, abs_offset, key, value, srcid)
        # print "fech ", 1./trace.stats['delta']

        self.samp_rate = fech
        self.nitems_written += len(trace.data)

        return len(trace.data)
