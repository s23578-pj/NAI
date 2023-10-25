# NAI 2
Narzędzia Sztucznej Inteligencji
# Fuzzy Logic

Fuzzy logic is a many-valued logic system where variable truth values can range between 0 and 1, allowing for the representation of partial truth between complete true and complete false. In contrast, Boolean logic restricts variable truth values to integers 0 or 1.

## Table of Contents

- [Project Topis](#project-topic)
- [Authors](#authors)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How To Use It](#how-to-use-it)
- [Output](#output)
- [Contributing](#contributing)

## Project topic

Fuzzy Control Systems: The Cash Allowance System

## Authors

- Alicja Szczypior
- Krzysztof Szczypior

## Getting Started


### Prerequisites

To run Fuzzy Control Systems: The Cash Allowance System, you need to have Python 3 installed on your system. If you don't have it, you can download it from the official [Python website](https://www.python.org/downloads/).

### Installation

To install the required library, you can use `pip`:

```bash
pip3 install scikit-fuzzy
pip3 install matplotlib
```
### How To Use It

Your will find in file main.py section `CHECK EMPLOYEE'S CASH ALLOWANCE SECTION` with three variables to be filled with inputs like:

`position experience` - How many years of experience on current position has an employee, on a scale of 0 to 10?
_Fuzzy set: poor, average, good_

`seniority in company` - How many years have the employee worked in our company, on a scale of 0 to 10?
_Fuzzy set: poor, average, good_

`efficiency` - How many tasks has been done (per month), on a scale of 0 to 120?
_Fuzzy set: poor, mediocre, average, decent, good_

### Output

`cash allowance` - How much should we appreciate our employee, how high should be cash allowance, on a scale of 0% to 50%?
_Fuzzy set: very low, low, medium, high, very high_

### Contributing

If you would like to contribute to this project, please feel free to create issues, submit pull requests, or make suggestions. We welcome all contributions.

Enjoy using The Cash Allowance System !
