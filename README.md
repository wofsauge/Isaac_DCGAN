# DCGAN in TensorLayer

THIS PROJECT IS BASED ON https://github.com/tensorlayer/dcgan

This is the TensorLayer implementation of [Deep Convolutional Generative Adversarial Networks](http://arxiv.org/abs/1511.06434) usable for binding of isaac sprites.


## Prerequisites

- Python3.5 3.6
- TensorFlow==2.0.0a0  `pip3 install tensorflow-gpu==2.0.0a0`
- TensorLayer=2.1.0		`pip3 install tensorlayer==2.1.0`

## Usage

First, put the sprites you like to use into a `data` folder. 
Optional: Use the FileConverter to turn png files into jpeg files. (look into that for more informations)
    $ python fileConverter.py

Second, train the GAN:

    $ python train.py
	
This process will take a while (~1second per epoch)
Resulting images can be found in the "samples" folder.

Further configuration in the data.py file