# gr-mseed


An Out-of-Tree (OOT) module for **gnuradio** to handle **seismological waveform** (mseed).

*It was just a Christmas project to have fun*. At least, it's possible 
to connect to a [seedlink](http://ds.iris.edu/ds/nodes/dmc/services/seedlink/) server or open a [mseed](https://ds.iris.edu/ds/nodes/dmc/data/formats/) file (seismological data standard) to plot spectrogram, waterfall, *etc.* using existing gnuradio modules. If you find it useful, please let me know.



## Dependencies

* [gnuradio](http://gnuradio.org) 
* [obspy](https://github.com/obspy/obspy/wiki)


## Installation
Go to the gr-mseed folder, then :
<pre>
mkdir build
cd build
cmake ../
make install
</pre>

## Usage

## links
* [Out Of Tree Module Tutorial](http://gnuradio.org/redmine/projects/gnuradio/wiki/OutOfTreeModules)