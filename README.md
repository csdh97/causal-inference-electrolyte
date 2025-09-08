# 
This is the official code of causal inference analysis for electrolyte in our work

## 1. Environment Setup
```bash
git clone https://github.com/Split-and-Merge-Proxy/causal-inference-electrolyte.git
cd causal-inference-electrolyte
conda create -n causal-inference-electrolyte python=3.8
conda activate causal-inference-electrolyte
pip install -r requirements.txt
```

## 2. Data Preparation
Our experiment analysis data has been in `./data/experiment_data.xlsx`. You can use your own data and put it in the same folder.

## 3. Inference
```bash
python main.py --mode custom --data_path ./data/experiment_data.xlsx --output_variable all
```

## Acknowledges
- [notears](https://github.com/xunzheng/notears)
- [dowhy](https://github.com/py-why/dowhy)

If you have any questions, please don't hesitate to contact me through [cs.dh97@gmail.com](cs.dh97@gmail.com)