
# Supervisionado

import tensorflow as tf

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

 

# Dados de exemplo

X_train = tf.constant([[1.0], [2.0], [3.0], [4.0]])

y_train = tf.constant([[2.0], [4.0], [6.0], [8.0]])

 

# Modelo de Regressão Linear Simples

model = Sequential()

model.add(Dense(units=1, input_shape=(1,)))

model.compile(optimizer='sgd', loss='mean_squared_error')

 

# Treinamento do modelo

model.fit(X_train, y_train, epochs=1000, verbose=0)

 

# Previsão

X_new = tf.constant([[5.0]])

prediction = model.predict(X_new)

print(“Predição:”, prediction[0][0])

plt.ylabel('Notas')

plt.show()


# Não supervisionado

import tensorflow as tf

from tensorflow.keras.layers import Input, Dense

from tensorflow.keras.models import Model

 

# Dados de exemplo

X_unsupervised = tf.constant([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]])

 

# Modelo Autoencoder Simples

input_layer = Input(shape=(2,))

encoded = Dense(units=1)(input_layer)

decoded = Dense(units=2)(encoded)

 

autoencoder = Model(inputs=input_layer, outputs=decoded)

autoencoder.compile(optimizer='adam', loss='mean_squared_error')

 

# Treinamento do modelo não supervisionado

autoencoder.fit(X_unsupervised, X_unsupervised, epochs=1000, verbose=0)

 

# Previsão

prediction_unsupervised = autoencoder.predict(X_unsupervised)

print(“Predição Não Supervisionada:”, prediction_unsupervised)
