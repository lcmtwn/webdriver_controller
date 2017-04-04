Webdriver Controller
===

**Working in progress**

A tool manages Selenium Webdriver local installation. It is inspired by Angular team's [webdriver-manager](https://github.com/angular/webdriver-manager) package.

Get Started
---
```
usage: webdriver_controller [-h] {download,cleanup} ...

Webdriver controller

positional arguments:
  {download,cleanup}
    download          download Selenium Webdriver binaries
    cleanup           remove downloaded Selenium Webdriver binaries
    list              list downloaded Selenium Webdriver version

optional arguments:
  -h, --help          show this help message and exit
```
Limitation
---
* Mac/Linux platform are supported.
 * only tested on Python 3.5.x and Mac OS
* only selenium standalone jar and chrome driver are downloaded.
