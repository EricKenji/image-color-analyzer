
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)


def analyze_colors(path, number_of_colors=10):
    # opens image from static/uploads path
    img = Image.open(path)
    # converts into RGB image
    img = img.convert('RGB')
    # converts img into 2d num py array
    numpy_array = np.array(img)
    pixels = numpy_array.reshape(-1, 3)

    # Kmeans find clusters of similar colors in RGB space
    kmeans = KMeans(n_clusters=number_of_colors)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)
    #  converts RGB colors to HEX
    return [f'#{r:02x}{g:02x}{b:02x}' for r, g, b in colors]


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            path = 'static/uploads/' + file.filename
            file.save(path)
            colors = analyze_colors(path)
            return render_template('result.html', colors=colors, filename=file.filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)