---
title: Python download
tags: 崑山科大
lang: zh-tw
---
# 下載python & pip
- Win10
    - [python_download_link](https://www.python.org/downloads/)
    - 點擊紅色框框中的Download Python
        ![](https://i.imgur.com/95Frerg.png)
    - 到cmd或powershell用底下的指令查看有沒有下載pip
    	```shell=
    	pip help
    	```
    - [pip_download_link](https://bootstrap.pypa.io/get-pip.py)
- Linux
    - Ubuntu 20.04
        ```shell=
        sudo apt update
        sudo apt install python3
        sudo apt install python3-pip
        ```
    - 查看版本
        ```shell=
        pip3 --version
        ```
# 下載pycrypto、PyCryptodome and cryptography
- install pycrypto
- install PyCryptodome
    - Win10 or Linux
        ```shell=
        pip install PyCryptodome
        ```
    - Google Colab
        ```shell=
        !pip install PyCryptodome
        ```
- install cryptography
    - Win10 or linux
        ```shell=
        pip install cryptography
        ```
    - Google Colab
        ```shell=
        !pip install cryptography
        ```