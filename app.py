from flask import Flask, render_template, request

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

dic = {0: 'Centromere',
       1: 'Coarse Speckled',
       2: 'Cytoplasmatic',
       3: 'Fine Speckled',
       4: 'Homogen',
       5: 'Nucleolar'}

model = load_model('Cendekia-pest-97.24.h5')

def predict_label(img_path):
    i = image.load_img(img_path, target_size=(128, 128))  # Mengubah target_size menjadi (128, 128)
    i = image.img_to_array(i) / 255.0
    i = i.reshape(1, 128, 128, 3)  # Mengubah ukuran gambar yang dimuat
    p = model.predict(i)
    p = np.argmax(p, axis=1)
    return dic[p[0]]


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("classification.html")

@app.route("/submit", methods=['POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "static/" + img.filename
        img.save(img_path)

        p = predict_label(img_path)
        return render_template("classification.html", prediction=p, img_path=img_path)

if __name__ == '__main__':
    app.run(debug=True)
