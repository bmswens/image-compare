# image-compare
A script for calculating and visualizing the amount of differences between two images.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

All Python requirements can be found in ```requirements.txt``` and can be installed with the following command.

```pip install -r requirements.txt```

### Installing

#### Direct Install (with venv)

##### Linux
```
git clone https://github.com/bmswens/image-compare.git
cd image-compare
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

##### Windows
```
git clone https://github.com/bmswens/image-compare.git
cd image-compare
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Usage

Supplying two images will return the number of clusters of pixel differences between the two images.
```
python compare.py /path/to/img1.jpg /path/to/img2.jpg
>>> 15
```
Supplying an output will create a greyscale image highlighting the clusters in red.
```
python compare.py --output /path/to/output.jpg /path/to/img1.jpg /path/to/img2.jpg
```

## Built With

* [Python](https://www.python.org/) - Primary language


## Authors

* **Brandon Swenson**- *Initial work* - [bmswens](https://github.com/bmswens)

## License

This project is licensed under the GNU GPLv3 - see the [LICENSE.md](LICENSE.md) file for details
