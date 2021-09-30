---
title: Python download
tags: 崑山科大
lang: zh-tw
---

{%hackmd theme-dark %}

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
# 將pip加到path
- Windows設定 => 「系統」 => 「關於」 => 「進階系統設定」 => 「環境變數」 => 「系統變數的Path」
- 再複製pip儲存的位置到Path中
    ![](https://i.imgur.com/iDpTyeD.png)
    ![](https://i.imgur.com/QLIwHia.png)
    ![](https://i.imgur.com/Ge6okIg.png)
    ![](https://i.imgur.com/D75zjrA.png)

- Linux
    - Ubuntu 20.04
        ```shell=
        sudo apt update
        sudo apt install python3
        sudo apt install python3-pip
        ```
    - 查看pip版本
        ```shell=
        pip3 --version
        ```
        
# 建立Python Virtual Env
- 

# 下載pycrypto、PyCryptodome and cryptography
- install pycrypto
    - Google Colab
        ```shell=
        !pip install pycrypto
        ```
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

# 下載gmpy2
- Ubuntu
    - 下載 libgmp-dev libmpfr-dev libmpc-dev
        ```shell=
        sudo apt install libgmp-dev libmpfr-dev libmpc-dev
        ```
    - 下載 gmpy2
        ```shell=
        sudo pip3 install gmpy2
        ```
- Google Colab
    ```shell=
    !apt install libmpc-dev
    !pip3 install --user gmpy2==2.1.0a2
    ```
        
- Win10
    - 先檢查有沒有wheel
        ```shell=
        wheel -h
        ```
        - 如果沒有
            ```shell=
            pip install wheel
            ```
    - 安裝gmpy2所需要的whl檔案
        - whl檔案包要和你所安裝的Python3版本一致
            ![](https://i.imgur.com/HLtMmep.png)
            - Python查看版本
                ```shell=
                python --version
                ```
        - [whl_download_link](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
        > 建議這個檔案下載後放到python檔案目錄下
    - 安裝剛剛載的whl檔案
        ```shell=
        pip install [whl檔案的絕對路徑]
        ```
    - 下載gmpy2
        ```shell=
        pip install gmpy2
        ```

# PyCryptodome 用法

# cryptography 用法