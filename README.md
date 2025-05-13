# 🖼️ Image Color Analyzer

A simple Flask web application that lets users upload an image and returns the **top 10 most common colors** in that image using KMeans clustering.

---

## 📸 Features

- Upload any .jpg, .png, or other standard image formats
- Automatically processes the image and finds dominant colors
- Displays a visual color palette with hex codes
- Uses Flask for backend, Bootstrap for styling, and NumPy + scikit-learn for image analysis

---

## 🧰 Tech Stack

- Python 3.12
- Flask
- NumPy
- Pillow (PIL)
- scikit-learn
- Bootstrap 5

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/EricKenji/image-color-analyzer.git
cd image-color-analyzer
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  
```

### 3. Install Dependencies
```bash
pip install flask numpy pillow scikit-learn
```

### 4. Run the app
```bash
python app.py
```

Then open your browser and visit:
http://127.0.0.1:5000