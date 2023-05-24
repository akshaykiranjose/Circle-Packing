from model import *
from utils import *

#for this demo, we take 10 circles, each of radius 0.262258924 that we know will fit without overlap into the unit circle.
num_circles = 10
large_radius =  1.
small_radius = 0.262258924

BATCHES = 200
EPOCHS = 1000

eye = one_hot(np.arange(0, num_circles), num_circles)
Input = tf.reshape(tf.tile(eye, [BATCHES, 1]) ,[-1, num_circles, num_circles]) #for ease of implementation of training

loss = CCE()
optim = Adam(learning_rate = 0.0005)

autoencoder = EncoderDecoder(num_circles, large_radius, small_radius)

#training can be finished and satisfactory packing obtained way before 1000 epochs.
#thus we split training with batches of size 200.
#for early manual stopping
for epoch in tqdm(range(EPOCHS)): 
    
    for inputs in Input:           
            with tf.GradientTape() as tape:
                curr_loss = loss(autoencoder(inputs), inputs)
                grads = tape.gradient(curr_loss, autoencoder.trainable_variables)
            optim.apply_gradients(zip(grads, autoencoder.trainable_variables))

centres = autoencoder.centres(eye)
plot_circles(centres, large_radius, small_radius)
