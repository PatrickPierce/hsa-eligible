# hsa-eligible
> Search if product is eligible for purchase with Health Saving Account (HSA)

Search by
* Account type and product name to return eligiblility status
	* hsa.py -a hsa -p aspirin
* Account type and status to return all products that match
	* hsa.py -a hsa -s eligible
* Product to return eligiblity status for all account types
	* hsa.py -p aspirin

## Installation

### Requirements

Python 3 and Firefox
*Tested with Python 3.8.2 and Firefox 75 on Fedora 32*

#### pip requirements
```
fuzzywuzzy==0.18.0
python-Levenshtein==0.12.0
selenium==3.141.0
urllib3==1.25.9
```

## Usage example

```
python3 hsa.py

Usage:
	hsa.py <account>, <product>
		hsa.py -a hsa, -p aspirin
	hsa.py <account>, <status>
		hsa.py -a hsa, -s eligible
	hsa.py <product>
		hsa.py -p aspirin
	
Options:
	-a Account type ["HSA", "HFSA", "LFSA", "DFSA", "HRA"]
	-p Product name
	-s Status ["Eligible", "Eligible with RX", "Eligible with LMN", "Not Eligible"]
```


## Release History

* 0.0.1 (5/4/2020)
    * Initial release

## Meta

Distributed under the GNU General Public License v3.0 license.
See ``LICENSE`` for more information.

[https://github.com/patrickpierce/hsa-eligible](https://github.com/patrickpierce/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request