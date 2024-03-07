# Subject Classifier built on Distilbert

## Table of Contents
- [Model Details](#model-details)
- [How to Get Started With the Model](#how-to-get-started-with-the-model)
- [Uses](#uses)
- [Risks, Limitations and Biases](#risks-limitations-and-biases)
- [Training](#training)
- [Evaluation](#evaluation)
- [Environmental Impact](#environmental-impact)

## Model Details

**Model Description:**  This is the [uncased DistilBERT model](https://huggingface.co/distilbert-base-uncased) fine-tuned on a custom dataset that is built on the [IITJEE NEET AIIMS Students Questions Data](https://www.kaggle.com/datasets/mrutyunjaybiswal/iitjee-neet-aims-students-questions-data?resource=download) for the subject classification task. 
- **Developed by:** The [Typeform](https://www.typeform.com/) team.
- **Model Type:** Text Classification
- **Language(s):** English
- **License:** GNU GENERAL PUBLIC LICENSE
- **Parent Model:** See the [distilbert base uncased model](https://huggingface.co/distilbert-base-uncased) for more information about the Distilled-BERT base model.


## Uses
This model can be used for text classification tasks.


## Risks, Limitations and Biases
**CONTENT WARNING: Readers should be aware this section contains content that is disturbing, offensive, and can propagate historical and current stereotypes.**

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).


## Training

Training is done on a [NVIDIA RTX 3070](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3070-3070ti/) [AMD Ryzen 7 5800](https://www.amd.com/en/products/cpu/amd-ryzen-7-5800) with the following hyperparameters:

```
$ training.ipynb \
    --model_name_or_path distilbert-base-uncased \
    --do_train \
    --do_eval \
    --max_seq_length 512 \
    --per_device_train_batch_size 4 \
    --learning_rate 1e-05 \
    --num_train_epochs 5 \
```

## Evaluation


#### Evaluation Results
When fine-tuned on downstream tasks, this model achieves the following results:

Epochs: 5 | Train Loss:  0.001                 | Train Accuracy:  0.989                 | Val Loss:  0.006                 | Val Accuracy:  0.950
CPU times: user 18h 19min 13s, sys: 1min 34s, total: 18h 20min 47s
Wall time: 18h 20min 7s
- **Epoch = ** 5.0
- **Evaluation Accuracy =**  0.950
- **Evaluation Loss =** 0.006
- **Training Accuracy =**  0.989
- **Training Loss =** 0.001

#### Testing Results

|                 | precision | recall | f1-score | support |
|-----------------|-----------|--------|----------|---------|
| biology         | 0.98      | 0.99   | 0.99     | 15988   |
| chemistry       | 1.00      | 0.99   | 0.99     | 20678   |
| computer        | 1.00      | 0.99   | 0.99     | 8754    |
| maths           | 1.00      | 1.00   | 1.00     | 26661   |
| physics         | 0.99      | 0.98   | 0.99     | 10306   |
| social sciences | 0.99      | 1.00   | 0.99     | 25695   |
|                 |           |        |          |         |
| accuracy        | 0.99      | 108082 |          |         |
| macro avg       | 0.99      | 0.99   | 0.99     | 108082  |
| weighted avg    | 0.99      | 0.99   | 0.99     | 108082  |


## Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700). We present the hardware type based on the [associated paper](https://arxiv.org/pdf/2105.09680.pdf).


**Hardware Type:** 1 NVIDIA RTX 3070 

**Hours used:**  18h 19min 13s

**Carbon Emitted:** (Power consumption x Time x Carbon produced based on location of power grid): Unknown


