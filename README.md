# Handwritten Digit Recognition

This project explores three machine learning models — Support Vector Classifier (SVC), Neural Networks (NN), and a biologically inspired model (`:v`) — to recognize handwritten digits from images. It was completed as part of the *Machine Learning and Computer Vision* module at Sheffield Hallam University.

---

## 📌 Objectives

- Train and evaluate different ML models on handwritten digit recognition
- Compare model accuracy, computational complexity, and robustness
- Analyze misclassifications and optimize preprocessing

---

## 🛠️ Tools & Libraries

- Python
- scikit-learn
- TensorFlow, Keras
- NumPy, Matplotlib

---

## 🧠 Models Used

1. **SVC (Support Vector Classifier)**  
   - Kernel: RBF  
   - Tuned parameters: C, Gamma

2. **Neural Network**  
   - Layers: Input → Hidden → Output  
   - Activation: ReLU  
   - Training: Backpropagation

3. **`:v` Model**  
   - Inspired by biological neuron behavior  
   - Combines supervised and unsupervised learning (sparse coding, lateral inhibition)

> The `:v` model is a conceptual experiment aiming to simulate more brain-like recognition mechanisms.

---

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 📂 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/handwritten-digit-recognition-mlcv.git
   cd handwritten-digit-recognition-mlcv

2. Install dependencies:
   pip install -r requirements.txt

3. Run the script:
   python src/mlcv_33085799.py
