# NAI 3
Machine learning with K-means algorithm application.

# Movie and Series Recommendations Engine based on Machine Learning

## Table of Contents

- [Authors](#authors)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How To Use The Engine](#how-to-use-the-engine)
  - [Output](#output)
  - [Program Examples](#program-examples)
- [DataFormat](#data-format)
- [Contributing](#contributing)

## Authors
- Alicja Szczypior
- Krzysztof Szczypior

## Getting Started

### Prerequisites
To run the Movies and Series Recommendations Engine you need to have Python 3 installed on your system. If you don't have it, you can download it from the [official Python website](https://www.python.org/).

### Installation
To install the required libraries, you can use pip:

```bash
pip3 install numpy
pip3 install argparse
```

## How To Use The Engine
Your will find in the main.py file where all logic starts. In the program three distance metrics are implemented, so you can choose which one you want to use or even compare results between all those distance metrics. 

To run the program use the command line to provide user and score type:

**python3 main.py --user <username> --score-type <score_type>**

**--user:** Input user, as a String.

**--score-type:** Choose between Euclidean, Pearson, or MSE distance metrics, as a String.


### Output
The program will display movies/series recommendations for the specified user based on the selected score type. The recommendations are split to the 5 most recommended and to the 5 most not recommended.


### Program Examples

#### For Paweł Czapiewski
* Pearson distance measure
![Pearson](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_3_Movies_recommendation/assets/PC_Pearson.png?raw=true)

* Euclidean distance measure
![Euclidean](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_3_Movies_recommendation/assets/PC_Euclidean.png?raw=true)

* MSE distance measure
![MSE](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_3_Movies_recommendation/assets/PC_MSE.png?raw=true)

#### For Alicja Szczypior
* Pearson distance measure
![Pearson](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_3_Movies_recommendation/assets/AS_Pearson.png?raw=true)

* Euclidean distance measure
![Euclidean](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_3_Movies_recommendation/assets/AS_Euclidean.png?raw=true)

* MSE distance measure
![MSE](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_3_Movies_recommendation/assets/AS_MSE.png?raw=true)

#### For Krzysztof Szczypior
* Pearson distance measure
![Pearson](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_3_Movies_recommendation/assets/KS_Pearson.png?raw=true)

* Euclidean distance measure
![Euclidean](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_3_Movies_recommendation/assets/KS_Euclidean.png?raw=true)

* MSE distance measure
![MSE](https://github.com/s23577/NAI_ZJAZD1/blob/main/ZJAZD_3_Movies_recommendation/assets/KS_MSE.png?raw=true)


## Data Format
Ensure your movie ratings data is in JSON format and follows the structure outlined below:

```
{
  "user1": {"movie1": 5, "movie2": 3, ...},
  "user2": {"movie1": 4, "movie3": 1, ...},
  ...
}
```

## Contributing

If you would like to contribute to this project, please feel free to create issues, submit pull requests, or make suggestions. We welcome all contributions.

Enjoy using The Movie and Series Recommendation Engine!

