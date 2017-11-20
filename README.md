# ALPR Project with Raspberry Pi

[TOC]

## Cahpter 0: Technology Stack

[Github Link for the project](https://github.com/jiinkwan/ALPR_Practice)

HW: Raspberry Pi 3+, picamera
SW: Raspbian Jessie, OpenCV, pytesseract, MariaDB, Python 3

Requirements
	1. Application must read the plate and return to the calling program the plate information (Minimum data: Country, State/Province, and license plate number)
	2. Minimum distance: 20 feet from the plate
	3. Human intervention is not required, however could optionally display results and allow them to be modified by the user
	4. Must support license plates of all varieties(truck, trailer, van, car, etc.) 
	5. Open source prgrams and libraries

Project Deadline: Dec 31, 2017

## Chapter 1: Setting up H/W

SSH Enable
	# sudo raspi-config
    
picamera setting
	# sudo apt-get install python3-picamera

## Chapter 2: Setting up S/W
### python 3

[Python3 Update](https://www.wyre-it.co.uk/blog/latestpython/)

    #!/bin/sh
    RELEASE=3.6.3

    # install dependencies
    sudo apt-get install libbz2-dev liblzma-dev libsqlite3-dev libncurses5-dev libgdbm-dev zlib1g-dev libreadline-dev libssl-dev tk-dev

    # download and build Python
    mkdir ~/python3
    cd ~/python3
    wget https://www.python.org/ftp/python/$RELEASE/Python-$RELEASE.tar.xz
    tar xvf Python-$RELEASE.tar.xz
    cd Python-$RELEASE
    ./configure
    make
    sudo make install
    sudo rm -rf ~/python3/Python-$RELEASE
    cd ~


    
### pytesseract
[pytesseract installtion](http://emaru.tistory.com/16)

	$ sudo apt-get install autoconf automake libtool libpng12-dev libtiff5-dev zlib1g-dev libicu-dev libpango1.0-dev libcairo2-dev
    $ sudo apt-get install libjpeg62-turbo-dev
    $ wget http://www.leptonica.org/source/leptonica-1.73.tar.gz
    $ tar -xvzf leptonica-1.73.tar.gz
    $ cd leptonica-1.73
    $ ./configure 
    $ make
    $ sudo apt-get install checkinstall
    $ sudo checkinstall
    $ checkinstall
    $ sudo ldconfig
    $ wget https://github.com/tesseract-ocr/tesseract/archive/3.04.01.tar.gz
    $ tar -xvzf 3.04.01.tar.gz
    $ cd tesseract-3.04.01
    $ ./autogen.sh
    $ ./configure
    $ make
    $ sudo make install
    $ sudo ldconfig
    $ sudo pip3.6 install pytesseract

### OpenCV

[OpenCV Installation](http://emaru.tistory.com/14)

    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
    $ sudo apt-get install libgtk2.0-dev
    $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
    $ sudo apt-get install libxvidcore-dev libx264-dev
    $ sudo apt-get install libatlas-base-dev gfortran
    $ sudo apt-get install python2.7-dev python3-dev
    $ sudo pip install numpy
    $ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
    $ unzip opencv.zip
    $ wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
    $ unzip opencv_contrib.zip
    $ cd opencv-3.1.0
    $ mkdir build
    $ cd build
    $ cmake –D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
    -D BUILD_EXAMPLES=ON ..
    $ make -j4
    $ sudo make install
    $ sudo ldconfig

????

	$ sudo pip3.6 install opencv-python

### MariaDB

	$ sudo apt-get install mariadb-server

출처: http://seodaeya.tistory.com/entry/Maria-DB-설치-in-Raspberry-Pi [티모스 실종사건]

## Chapter 3: Coding
[ALPR w/ TensorFlow](https://github.com/matthewearl/deep-anpr)
## Chpater 4: Test
## Chapter 4: Result and Conclusion
