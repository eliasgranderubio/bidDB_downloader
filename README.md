# bidDB_downloader
**bidDB_downloader** is a tool for downloading the BugTraq Ids database from the `http://www.securityfocus.com/` pages.

To fulfill its mission, each BugTraq Id and its info is parsed from the HTML and exported in a JSON way.

## Requirements
Before **bidDB_downloader** usage, you must have installed Python >= 3.4.5 and the requirements:

* Python3.4.5 or later
* Pip3
  * Joblib
  * Requests

The requirements can be installed with pip:
```
    sudo pip3 install -r requirements.txt
```

## Usage

Below, the help when you type `python3 bidDB_downloader.py --help` is shown:

```
    usage: bidDB_downloader.py [-h] [-w WORKERS] [-f FIRST] [-l LAST] [-v]

    BugTraq database downloader.

    optional arguments:
      -h, --help            show this help message and exit
      -w WORKERS, --workers WORKERS
                            number of workers for execution. By default, the
                            workers number is set to 100
      -f FIRST, --first FIRST
                            your download will start from this BugTraq Id. By
                            default, the first BugTraq Id is set to 1
      -l LAST, --last LAST  your download will finish in this last BugTraq Id. By
                            default, the last BugTraq Id is set to 100000
      -v, --version         show the version message and exit
```

Fulfilling with the described usage, a usage example would be the next one:
```
	python3 bidDB_downloader.py --workers 1 --first 1 --last 4
```

The expected output is shown below:
```
{"bugtraq_id": 1, "title": "Berkeley Sendmail DEBUG Vulnerability", "class": "Configuration Error", "cve": [], "local": "yes", "remote": "yes", "vuln_products": ["Eric Allman Sendmail 5.58"]}
{"bugtraq_id": 2, "title": "BSD fingerd buffer overflow Vulnerability", "class": "Boundary Condition Error", "cve": [], "local": "no", "remote": "yes", "vuln_products": ["BSD BSD 4.2"]}
{"bugtraq_id": 3, "title": "SunOS restore Vulnerability", "class": "Unknown", "cve": [], "local": "yes", "remote": "no", "vuln_products": ["Sun SunOS 4.0.3", "Sun SunOS 4.0.1", "Sun SunOS 4.0"]}
{"bugtraq_id": 4, "title": "BSD passwd buffer overflow Vulnerability", "class": "Boundary Condition Error", "cve": ["CVE-1999-1471"], "local": "no", "remote": "no", "vuln_products": ["BSD BSD 4.3", "BSD BSD 4.2"]}
```

## Bonus Track

You have available the BugTraq Ids database downloaded on 05/07/2017 in the **bonus_track** directory of this repository.

**IMPORTANT TO NOTE:** The BugTraq Ids database downloaded on 11/18/2016 which is included in the **20161118_sf_db.json.gz** file has deprecated info and it will be deleted soon.

## Bugs and Feedback
For bugs, questions and discussions please use the [Github Issues](https://github.com/eliasgranderubio/bidDB_downloader/issues) or ping me on Twitter (@3grander).
