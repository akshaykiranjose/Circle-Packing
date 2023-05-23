import numpy as np
import tensorflow as tf
from tqdm import tqdm

from tensorflow.keras import Input, layers
from tensorflow.keras.layers import Layer, Dense, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.losses import CategoricalCrossentropy as CCE
from tensorflow.keras.optimizers import Adam, Nadam, SGD
from tensorflow.keras.constraints import MinMaxNorm
from tensorflow.keras.activations import tanh
from tensorflow.keras import backend as K
from tensorflow.keras import regularizers

def one_hot(a, num_classes):
    return tf.constant(np.eye(num_classes, num_classes)[a], dtype=tf.float32)

class Normalization(Layer):
    
    def __init__(self, maxnorm, **kwargs): # maximum possible norm for weights
        super(Normalization, self).__init__(**kwargs)
        self.maxnorm = maxnorm
            
    def build(self, input_shape):
        self.w = self.add_weight(name='w',
                                 shape = input_shape, 
                                 constraint = lambda x: tf.clip_by_norm(self.w, self.maxnorm, axes=1),
                                 trainable=True)
        
    def call(self, inputs):
        return tf.math.multiply(inputs, self.w)
    

class CircularNoiseLayer(Layer):

    def __init__(self, noise_radius):

        super(CircularNoiseLayer, self).__init__()
        self.noise_radius = noise_radius
        self.alpha = .5
        
    def spherical_gaussian(self, NumData):
        x = np.random.normal(size = [NumData, 2])
        u = np.random.uniform(size = [NumData, 1])
        norm = np.linalg.norm(x, axis = 1, keepdims=True, ord = 2)   
        noise = x*np.power(u, self.alpha)*self.noise_radius/norm
        return noise

    def call(self, inputs):
        noise = self.spherical_gaussian(inputs.shape[0])
        return inputs + noise


class Autoencoder(Model):
    
    def __init__(self, num_circles, larger_radius, smaller_radius, **kwargs):
        super(Autoencoder, self).__init__(**kwargs)
        
        self.main_dim = num_circles
        self.latent_dim = 2
        self.R = larger_radius
        self.r = smaller_radius
                
        self.normalize = Normalization(self.R - self.r)       
        self.noise = CircularNoiseLayer(self.r)
        
        self.encoder = tf.keras.Sequential([
            Input(shape=(self.main_dim)),
            Dense(self.main_dim, activation= 'selu'),
            Dense(self.main_dim, activation = 'selu'),
            Dense(self.main_dim//2, activation = 'selu'),
            Dense(self.main_dim//4, activation = 'selu'),
            Dense(self.latent_dim, activation = 'tanh')#, kernel_regularizer=regularizers.L1L2(l1=1e-2, l2=1e-1))
        ])       
        self.decoder = tf.keras.Sequential([
            Dense(self.main_dim//4, activation = 'relu'),
            Dense(self.main_dim//2, activation = 'relu'),
            Dense(self.main_dim, activation = 'relu'),
            Dense(self.main_dim, activation = 'relu'),
            Dense(self.main_dim, activation='softmax')
        ])
        
    def call(self, x):
        encoded = self.encoder(x)
        normed_encoded = self.normalize(encoded)
        noisy_encoded = self.noise(normed_encoded)
        decoded = self.decoder(noisy_encoded)
        return decoded

    def latent(self, x):
        return self.encoder(x)

    def centres(self, x):
        return self.normalize(self.encoder(x)).numpy()
    

