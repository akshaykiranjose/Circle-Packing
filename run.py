from model import *
from utils import *

num_circles = 10
large_radius =  1.
small_radius = 0.262258924

BATCHES = 200
EPOCHS = 1000

eye = one_hot(np.arange(0, num_circles), num_circles )
Input = tf.reshape(tf.tile(eye, [BATCHES, 1]) ,[-1, num_circles, num_circles])


loss = CCE()

autoencoder = Autoencoder(num_circles, large_radius, small_radius)

centres = autoencoder.centres(eye)

plot_circles(centres, large_radius, small_radius)
