# NAI 5
Neural Networks for Classification

Neural networks are computational systems inspired by the structure and function of the human brain.
They are comprised of interconnected nodes known as neurons, organized into layers.
Each neuron processes input data and transmits signals to neurons in the next layer.
Neural networks learn by adjusting connections between neurons based on example data.

## Table of Contents

- [Authors](#authors)
- [Datasets](#datasets)
- [Getting Started](#getting-started)
  - [Prerequisites and Installation](#prerequisites-and-installation)
  - [How to run the program](#how-to-run-the-program)
  - [Output](#output)
- [Program Output Examples](#program-output-examples)
  - [Wheat Seeds](#wheat-seeds-)
  - [Cifar-10](#cifar-10---animals)
  - [Fashion Mnist](#fashion-mnist---clothes)
  - [Chlorophyll](#chlorophyll)
- [Contributing](#contributing)

## Authors
- Alicja Szczypior
- Krzysztof Szczypior

## Datasets

1. wheat_seeds.csv - author`s file source
2. fashion_mnist from _**fashion_mnist.load_data()**_
3. Cifar-10 from _**cifar10.load_data()**_
4. Chlorophyll A and B levels in Chestnut and Chives from author`s file source: _**chlorophyll_a_b_levels.csv**_

## Getting Started

### Prerequisites and Installation

To run the program, install the following Python packages (if required):
TensorFlow with some packages which should be imported in the code:
- fashion_mnist dataset
- Flatten, Dense
- Sequential model
- seaborn package
- numpy package
- pyplot from matplotlib
- sklearn.metrics
- tensorflow

### How to run the program
Run just every .py file with script per project and used method or press the run button.

### Output

1. **wheat_seeds** displays prediction and accuracy.
2. **Cifar-10** (animals) displays predicted model + actual class with accuracy.
3. **Clothes** displays predicted image, model A & B, visualization of confusion matrix.
4. **chlorophyll** displays prediction and accuracy.

## Program Output Examples


### Wheat seeds 
1. Model:
![wheat_seed_dt_figure1.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/wheat_seed_2.png?raw=true)
2. Results:
![wheat_seed_dt_figure2.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/wheat_seed_1.png?raw=true)

### Cifar-10 - Animals

1. Model:
![cifar_1.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/cifar_3.png?raw=true)
2. Results:
![cifar_2.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/cifar_1.png?raw=true)
![cifar_3.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/cifar_2.png?raw=true)

### Fashion mnist - Clothes

1. Model A
![clothes_modelA.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/clothes_model_A.png?raw=true)
2. Model A result
![clothes_modelA_results.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/clothes_model_A_results.png?raw=true)
3. Model A confusion matrix 
![clothes_modelA_confusion_matrix.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/clothes_model_A_confusion_matrix.png?raw=true)
4. Model B 
![clothes_modelB.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/clothes_model_B.png?raw=true)
5. Model B result
![clothes_modelB_results.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/clothes_model_B_results.png?raw=true)
6. Model B Confusion matrix
![clothes_modelB_confusion_matrix](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/clothes_model_B_confusion_matrix.png?raw=true)
7. Model BN
![clothes_modelB_normalization.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/clothes_model_BN.png?raw=true)
8. Model BN result
![clothes_modelB_normalization_result.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/clothes_model_BN_results.png?raw=true)
9. Model BN Confusion matrix
![clothes_modelB_normalization_confusion_matrix.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/clothes_model_BN_confusion_matrix.png?raw=true)


### Chlorophyll

1. Chlorophyll model
![chlorophyll_model.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/chlorophyll_model.png?raw=true)

2. Chlorophyll result
![chlorophyll_result.png](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_5_Neural_Networks/assets/chlorophyll_result.png?raw=true)


## Contributing

If you would like to contribute to this project, please feel free to create issues, submit pull requests, or make suggestions. We welcome all contributions.

Enjoy!
