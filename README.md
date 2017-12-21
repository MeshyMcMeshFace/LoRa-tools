# LoRa-tools
Tools to help with the diagnostics of LoRa

## SDR tools

### Install required packages on Ubuntu
```
sudo apt-get install rtl-sdr gnuradio gr-osmosdr git autoconf python-numpy python-scipy swig fftw-dev libvolk1-dev cmake wx3.0-headers liblog4cpp5-dev libcppunit-dev
```

### Build and install liqid-dsp
```
git clone git://github.com/jgaeddert/liquid-dsp.git
cd liquid-dsp
./bootstrap.sh
./configure
make
sudo make install
cd ..
```
More information about liquid-dsp: https://github.com/jgaeddert/liquid-dsp

### Build and install gr-lora by rpp0
```
git clone https://github.com/rpp0/gr-lora.git
cd gr-lora
mkdir build
cd build
cmake ../
make
sudo make install
sudo ldconfig
cd ../..
```
More information about gr-lora by rpp0: https://github.com/rpp0/gr-lora

### Using the tools
```
git clone https://github.com/MeshyMcMeshFace/LoRa-tools.git
cd LoRa-tools/sdr
grcc -d . LoRaSenderUDP.grc
```
Run `LoRaSenderUDP.py`.

When LoRaSender UDP are running you can listen to the UDP ports 10541 and 10542.
Port 10541 get only the data sent by the LoRa device while 10542 also get the explicit header of 3 bytes.

While `LoRaSenderUDP.py` are running you can run a UDP reciever to decode packages, like `LoRaReceiverAscii.py`.

### Settings for LoRa transmitter
These settings are known to work:
+ Bandwidth: 125kHz
+ Spreading Factor: 8
+ Coding Rate: 4/5
+ Explicit mode
+ CRC disabled

