from tensorflow.keras.models import model_from_json
import cv2
import numpy as np

def overall(image):
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

    '''loaded_model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
    '''
    loaded_model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    print(image)
    img = cv2.imread(image)
    img = cv2.resize(img, (50,50))
    #print(img.shape)
    img = img.reshape(1, 50, 50, 3)

    p = loaded_model.predict(img)
    answer = p[0][0]

    if int(answer) == 0:
        return 'CAT'
    else:
        return 'DOG'
