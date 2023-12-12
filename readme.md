# Data Statistics Code Challenge

This is a code challenge project that focuses on calculating statistics for a given set of integer data. It consists of two main components: `DataCapture` and `DataStatistics`. The project also includes test cases that can be run using `pytest` to ensure the correctness of the code.

## 1. Creating a python environment

To avoid installing different versions or unneeded version of libraries in your system I recommend you to create a virtua lenvironment for this project.

```bash
python -m venv .env
source .env/bin/activate
```

If `python` doen't work, try `python3` or the python's version installed in your system.


## 2. Installing the required dependencies
In order to pacefully run the project/test you might need to install the needed libraries inside the environment.
Once activated you environment (step 1), run:

```bash
pip install -r requiremenets.txt
```


## 3. Running Tests

To ensure the correctness of the code, you can run the provided tests using `pytest`. Make sure you have `pytest` installed (prior step), and then run the following command in your terminal:

```bash
pytest
```

For a more verbose answer:
```bash
pytest -vv
```

Enjoy the green ticks :)

# PERSONAL NOTES
This is just for me Don't worry about this.

``````
3,9,3,4,6
3,3,4,6,9

I =     0   1   2   3   4   5   6   7   8   9   10
        ------------------------------------------
D =     0   0   0   2   1   0   1   0   0   1   0

L =     0   0   0   0   2   3   3   4   3   3   5
G =     5   5   5   3   2   2   1   1   1   0   0
                   [             ]

3 -> 3
6 <- 3

G(6) = 1
L(3) = 0


L(0) - G(6) + L(3) :)
```