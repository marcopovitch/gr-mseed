# gr-mseed


An Out-of-Tree (OOT) module for **gnuradio** to handle **seismological waveform** (mseed).

*It was just a Christmas project to have fun*. At least, it's possible 
to connect to a [seedlink](http://ds.iris.edu/ds/nodes/dmc/services/seedlink/) server or open a [mseed](https://ds.iris.edu/ds/nodes/dmc/data/formats/) file (seismological data standard) to plot spectrogram, waterfall, *etc.* using existing gnuradio modules. If you find it useful, please let me know.

![gnuradio interface with gr-mseed](https://cloud.githubusercontent.com/assets/4367036/15627672/9311e104-24eb-11e6-8907-6a3a7fe34a00.png)

![spectro&waterfall](https://cloud.githubusercontent.com/assets/4367036/15627689/2f4e555c-24ec-11e6-949c-a82a51027778.png)


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

### Demo

* The gnuradio-compagnon grc file is localted in the `examples` directory. To start the demo :

	<pre>gnuradio-compagnon waterfall.grc</pre>

* To try the standalone python app in the `examples` directory:
	<pre>./top_block.py</pre>

## Links
* [Out Of Tree Module Tutorial](https://wiki.gnuradio.org/index.php/OutOfTreeModules)
