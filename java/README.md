# Taurus

Taurus is a Command-Line program written in Java which facilitates the analysis and creation of cryptocurrency trading data.

## Description

The program works by querying the [Binance RESTful API](https://binance-docs.github.io/apidocs/spot/en/) for financial information
such as exchange information containing details about currently-trading trade pairs such as ETHBTC, 24-hour price change statistics
and dated recent trade details including trade prices, quantities and quotes. Thereafter, this data is either output to the terminal
or used to create additional data such as establishing all trade paths between two given assets. Moreover, users are able to
save data retrieved from the API to JSON files and load the very same data into ```Taurus``` for later analysis.

## Getting Started

### Installation

1. Download the ```taurus-master``` archive by downloading [```taurus-master.zip```](https://github.com/tanakachitete/taurus/archive/master.zip)
2. Open a new terminal window in the directory where the archive was downloaded
3. Unzip the archive using the following command to obtain the ```taurus-master``` directory:
```
unzip taurus-master.zip
```
4. Delete ```taurus-master.zip``` using the following command:
```
rm taurus-master.zip
```
5. Change into the ```taurus-master/java``` directory by executing the following command:
```
cd taurus-master/java
```

### Compilation

* To compile ```Taurus.java```, enter the following:
```
javac -cp .:json-20200518.jar Taurus.java
```

### Execution
#### Interactive Mode

* To execute ```Taurus.java``` in Interactive Mode, execute the following:
```
java -cp .:json-20200518.jar Taurus -i
```

#### Report Mode

* To execute ```Taurus.java``` in Report Mode, execute the following:
```
java -cp .:json-20200518.jar Taurus -r <asset filename>.json <trade filename>.json
```

where ```<asset filename>``` and ```<trade filename>``` are both JSON files containing exchange information and trade details regarding
a particular trade pair, respectively. These files can be obtained from running ```Taurus.java``` in Interactive Mode.

## Author

Tanaka Chitete
* [Linkedin](https://www.linkedin.com/in/tanaka-chitete/)

## Acknowledgments

* Thank you to [DomPizzie](https://github.com/DomPizzie) for the [template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
