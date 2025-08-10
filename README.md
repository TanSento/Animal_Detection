# 🦁 Animal Detection System

An automated wildlife detection system using deep learning and IoT sensors, designed for real-time animal classification in natural habitats.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Keras](https://img.shields.io/badge/Keras-2.x-red.svg)](https://keras.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Overview

This project implements a complete wildlife monitoring solution that combines:
- **PIR Motion Detection** - Triggers camera capture when animals are detected
- **Real-time Image Classification** - Identifies 12 different wildlife species
- **Edge Computing** - Runs on NVIDIA Jetson Nano for field deployment
- **Multiple CNN Architectures** - Comprehensive comparison of deep learning models

### Supported Animal Classes
- Buffalo, Cheetah, Elephant, Gazelle, Giraffe, Hartebeest
- Lion (female & cub), Lion (male), Ostrich, Secretary Bird, Wildebeest, Zebra

## 🚀 Quick Start

### For Deployment (Jetson Nano)
```bash
cd deployment/
python3 predict.py
```

### For Training/Development
```bash
cd training/
jupyter notebook
# Open desired training notebook
```

## 📁 Project Structure

```
Animal_Detection/
├── deployment/                 # Production deployment code
│   ├── predict.py             # Main prediction script
│   ├── cam_PIR.py             # PIR sensor + camera integration
│   ├── camera.py              # Basic camera functionality
│   ├── jetcam/                # Jetson camera library
│   └── requirements.txt       # Deployment dependencies
├── training/                   # Model development & training
│   ├── notebooks/             # Jupyter training notebooks
│   │   ├── AlexNet_12_classes.ipynb
│   │   ├── Transfer_Learning_ResNet50.ipynb
│   │   ├── Transfer_Learning_InceptionV3.ipynb
│   │   ├── Transfer_Learning_InceptionResnet.ipynb
│   │   └── data_conversion/   # Data preprocessing notebooks
│   ├── CapsNet-Keras/         # Capsule Network implementation
│   └── requirements.txt       # Training dependencies
├── models/                     # Trained model files (download separately)
├── evaluation/                 # Model comparison & TensorBoard logs
├── docs/                       # Documentation & setup guides
└── README.md
```

## 🛠️ Hardware Requirements

### For Deployment
- **NVIDIA Jetson Nano** (4GB recommended)
- **CSI Camera** (720x720 resolution)
- **PIR Motion Sensor**
- **MicroSD Card** (64GB+ Class 10)
- External monitor (HDMI)

### For Training
- **GPU Required**: NVIDIA RTX 2070 or equivalent
- **RAM**: 16GB+ recommended
- **Storage**: 50GB+ for datasets and models

## ⚙️ Installation

### 1. Jetson Nano Setup (Deployment)

```bash
# Clone repository
git clone https://github.com/TanSento/Animal_Detection.git
cd Animal_Detection

# Install JetCam (camera interface)
cd deployment/jetcam
sudo python3 setup.py install
cd ../..

# Install dependencies
pip3 install -r deployment/requirements.txt

# Download pre-trained model
# Place TransferLearning-AlexNet-new.h5 in deployment/ directory
```

### 2. Training Environment Setup

```bash
# Install Anaconda (recommended)
wget https://www.anaconda.com/distribution/

# Create environment
conda create -n animal_detection python=3.7
conda activate animal_detection

# Install dependencies
pip install -r training/requirements.txt

# Start Jupyter
cd training/
jupyter notebook
```

## 🎯 Usage

### Automated Detection System

1. **Connect Hardware**:
   - PIR sensor to GPIO pin 12
   - CSI camera to Jetson Nano
   - External monitor via HDMI

2. **Run Detection**:
   ```bash
   cd deployment/
   python3 predict.py
   ```

3. **System Operation**:
   - PIR sensor detects motion
   - Camera captures image automatically
   - AI model classifies the animal
   - Results displayed in terminal
   - Process repeats every 5 seconds

### Model Training

1. **Data Preparation**:
   ```bash
   # Run data conversion notebooks
   jupyter notebook training/notebooks/data_conversion/
   ```

2. **Train Models**:
   ```bash
   # Choose your architecture
   jupyter notebook training/notebooks/AlexNet_12_classes.ipynb
   # or other model notebooks
   ```

3. **Monitor Training**:
   ```bash
   tensorboard --logdir=evaluation/tensorboard_logs --host localhost --port 7000
   ```

## 🧠 Model Architectures

This project compares 5 different deep learning architectures:

| Model | Input Size | Parameters | Transfer Learning | Custom Implementation |
|-------|------------|------------|-------------------|---------------------|
| **AlexNet** | 227×227 | ~60M | ✅ | - |
| **ResNet50** | 224×224 | ~25M | ✅ | - |
| **InceptionV3** | 224×224 | ~24M | ✅ | - |
| **InceptionResNet** | 224×224 | ~55M | ✅ | - |
| **CapsNet** | 128×128 | ~8M | - | ✅ |

**Selected Model**: AlexNet showed optimal balance of accuracy and inference speed for edge deployment.

## 📊 Performance

- **Accuracy**: 92%+ on test dataset
- **Inference Time**: ~200ms per image (Jetson Nano)
- **Classes**: 12 wildlife species
- **Real-time Performance**: ✅ Suitable for continuous monitoring

## 🔧 Configuration

### Camera Settings
```python
# In cam_PIR.py
WIDTH = 720
HEIGHT = 720
img_path = "/path/to/save/images"
```

### Detection Sensitivity
```python
# PIR sensor GPIO pin
input_pin = 12

# Detection interval
time.sleep(5)  # 5 seconds between detections
```

## 📈 TensorBoard Visualization

View training metrics and model comparisons:

```bash
cd evaluation/
tensorboard --logdir="tensorboard_logs" --host localhost --port 7000
```

Access at: `http://localhost:7000`

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Thesis Project** - Curtin University, Mechanical Engineering (2019)
- **NVIDIA Jetson Community** - For excellent edge AI hardware
- **Keras/TensorFlow** - Deep learning frameworks
- **OpenCV** - Computer vision library

## 📧 Contact

**Tan Bui** - [GitHub](https://github.com/TanSento)

Project Link: [https://github.com/TanSento/Animal_Detection](https://github.com/TanSento/Animal_Detection)

---

⭐ **Star this repository if you find it helpful!**