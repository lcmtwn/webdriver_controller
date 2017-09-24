Webdriver Controller
===
[![PyPI](https://img.shields.io/pypi/v/webdriver_controller.svg?style=flat)](https://pypi.python.org/pypi/webdriver_controller)
[![PyPI](https://img.shields.io/pypi/status/webdriver_controller.svg?style=flat)](https://pypi.python.org/pypi/webdriver_controller)

**Working in progress**

A tool manages Selenium Webdriver local installation. It is inspired by Angular team's [webdriver-manager](https://github.com/angular/webdriver-manager) package.

Get Started
---
```
usage: webdriver_controller [-h] {download,cleanup,list,start} ...

Webdriver controller

positional arguments:
  {download,cleanup,list,start}
    download          download Selenium Webdriver binaries
    cleanup           remove downloaded Selenium Webdriver binaries
    list              list downloaded Selenium Webdriver version
    start             start Selenium binaries

optional arguments:
  -h, --help          show this help message and exit
```
Limitation
---
* Mac/Linux platform are supported.
 * only tested on Python 3.5+ and Mac OS
* Selenium standalone server, Gecko driver and Chrome driver are downloaded.
