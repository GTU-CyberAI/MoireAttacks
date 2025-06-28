# MoireAttacks

## Project Description

This project focuses on developing robust object detection systems against Moiré pattern attacks. The system consists of two main components: a generative network that creates synthetic images with Moiré patterns to build a comprehensive dataset, and an enhanced YOLO model with custom attention modules integrated into its backbone architecture. The goal is to train the YOLO model to be resilient against Moiré pattern-based adversarial attacks while maintaining high detection accuracy.

The project combines adversarial attack generation techniques with advanced deep learning architectures to create a more secure and reliable object detection system suitable for real-world applications where Moiré pattern attacks might be encountered.

## File Structure

- **src/Attack-main/image_transformer.py** - Image transformation utilities for generating Moiré patterns and applying various transformations to input images
- **src/Attack-main/Moire_Attack.py** - Main script for generating Moiré pattern attacks on images, implementing the core adversarial attack methodology
- **src/Attack-main/mosaicing_demosaicing_v2.py** - Advanced mosaicing and demosaicing algorithms for creating realistic Moiré effects
- **src/Attack-main/get_human_from_coco.py** - Utility script for extracting human detection annotations from COCO dataset for training purposes
- **src/YOLO-Attention/ultralytics** - Modified ultralytics YOLO implementation with integrated attention mechanisms
- **src/YOLO-Attention/predict.py** - Prediction script for the attention-enhanced YOLO model
- **src/YOLO-Attention/train.py** - Training script for the custom YOLO model with attention modules

## Installation Instructions

1. Clone the repository:
```bash
git clone https://github.com/GTU-CyberAI/MoireAttacks.git
```

2. Navigate to the project directory:
```bash
cd MoireAttacks
```

3. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install required dependencies:
```bash
pip install -r config/req-yolo.txt
pip install -r config/req-attack.txt
```

5. Run the YOLO prediction:
```bash
python src/YOLO-Attention/predict.py
```

6. Run the Moiré attack generation:
```bash
python src/Attack-main/Moire_Attack.py
```

## Troubleshooting

### Common Issues and Solutions

**Issue: ModuleNotFoundError when running scripts**
- Solution: Ensure you have activated the virtual environment and installed all requirements from both req-yolo.txt and req-attack.txt

**Issue: CUDA out of memory errors during training**
- Solution: Reduce batch size in the training configuration or use a smaller model variant

**Issue: Import errors with ultralytics**
- Solution: Make sure the modified ultralytics package is properly installed. You may need to install it in development mode: `pip install -e src/YOLO-Attention/ultralytics`

**Issue: File path errors**
- Solution: Ensure you're running scripts from the project root directory and all data paths are correctly configured


## Acknowledgments

This project was developed under the supervision of **Dr. Salih Sarp** at Gebze Technical University.

**Collaborators:**
- Alper Tavşanoğlu
- Hüseyin Koçak

We acknowledge the use of the COCO dataset and the ultralytics YOLO framework as foundational components of this research.
