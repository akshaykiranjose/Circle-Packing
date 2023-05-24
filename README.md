# An Encoder-Decoder Approach for Packing Circles.

> :warning: **It could take a while to show all 5 .gif files in this readme**

A ```.gif``` file as below was made by saving the centres returned by the encoder every 200 epochs till we obtain a satisfactory packing layout. The total number of epochs 
of training goes as high as 20,000.

The values of ```r```: radius of smaller circle and ```R```: radius of the larger circle are chosen such that a packing arrangement without significant overlap can be found.

Here are two different instances of packing 14 circles in a unit circle.\
<img src="https://github.com/akshaykiranjose/Circle-Packing/blob/master/figures/14_0.gif" width="400" height="400" /> <img src="https://github.com/akshaykiranjose/Circle-Packing/blob/master/figures/14_1.gif" width="400" height="400" />


Here is one $\text{\color{red}Failed}$ attempt to pack 14 circles for the same values of ```r``` and ```R``` as above.\
<img src="https://github.com/akshaykiranjose/Circle-Packing/blob/master/figures/14_f.gif" width="400" height="400" /> 

Towards the end of training, the circles exhibit minor movement if and only if they don't have significant overlap with another circle.\

<img src="https://github.com/akshaykiranjose/Circle-Packing/blob/master/figures/13_0_run_long.gif" width="400" height="400" /> <img src="https://github.com/akshaykiranjose/Circle-Packing/blob/master/figures/15_0.gif" width="400" height="400" /> 

Packing 13 and 15 circles respectively.

<img src="https://github.com/akshaykiranjose/Circle-Packing/blob/master/figures/18_0.gif" width="400" height="400" /> <img src="https://github.com/akshaykiranjose/Circle-Packing/blob/master/figures/19_0.gif" width="400" height="400" /> 

Packing 18 and 19 circles respectively.

But trying to pack a larger number of circles by training a similar model does not give a satisfactory packing.\
<img src="https://github.com/akshaykiranjose/Circle-Packing/blob/master/figures/27_0.gif" width="400" height="400" /> <img src="https://github.com/akshaykiranjose/Circle-Packing/blob/master/figures/33_0.gif" width="400" height="400" />

Packing 27 and 33 circles respectively.
