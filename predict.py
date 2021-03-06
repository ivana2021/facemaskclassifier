from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

loaded_model = load_model('vgg19model.h5')    # load the previouly saved model

def predict_result(full_path):
    img = image.load_img(full_path, target_size = (32, 32, 3))
    img = np.expand_dims(img, axis=0)
    img = img.astype('float')/255

    result = loaded_model.predict(img)
    result = result.item()

    if result > 0.5:
        return round(result*100, 2), 'nomask'
    else:
        return round((1-result)*100, 2), 'mask'