# Football Match Scraping
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/jonatasemidio/multilanguage-readme-pattern/blob/master/README.md)
[![tr](https://img.shields.io/badge/lang-tr--tr-green.svg)](https://github.com/dorukyy/multilanguage-readme-pattern/blob/master/README.tr.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-blue.svg)

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-3.141.0-blue.svg)](https://pypi.org/project/selenium/)
[![sqlite](https://img.shields.io/badge/sqlite-3.36.0-blue.svg)](https://www.sqlite.org/index.html)

[EN](#en)

[TR](#tr)

## EN
# Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Output](#output)
5. [License](#license)
6. [Contributing](#contributing)

### Introduction
This project is about scraping football match data from the website [https://www.spordb.com](https://www.spordb.com). The data is scraped using the Selenium library in Python. The website used is Turkish so, league names will be Turkish.

### Requirements
- Python 3.6 or higher
- Selenium
- Firefox Web Browser
- Geckodriver

### Installation
- Install Python 3.6 or higher from [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```
- Download the Geckodriver from [https://sourceforge.net/projects/geckodriver.mirror/](https://sourceforge.net/projects/geckodriver.mirror/)
- Extract the downloaded file and add the path to the extracted file to the system environment variable PATH.
- Edit config.ini file
- Run the script using the following command:

```bash
python main.py
```

### Output
The output of the script is a sqlite database file. The database contains the following tables:
- matches
- weeks

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

____________________________________________________________________________________________________________________________________________________________________________________

# TR
## İçindekiler
1. [Giriş](#giriş)
2. [Gereksinimler](#gereksinimler)
3. [Kurulum](#kurulum)
4. [Çıktı](#çıktı)
5. [Lisans](#lisans)
6. [Katkıda Bulunma](#katkıda-bulunma)

### Giriş
Bu proje, [https://www.spordb.com](https://www.spordb.com) web sitesinden futbol maçı verilerini çekmek için yazılmıştır. Veriler, Python'daki Selenium kütüphanesi kullanılarak çekilir.

### Gereksinimler
- Python 3.6 veya daha yüksek
- Selenium
- Firefox Web Tarayıcısı
- Geckodriver

### Kurulum
- [https://www.python.org/downloads/](https://www.python.org/downloads/) adresinden Python 3.6 veya daha yüksek sürümünü yükleyin.
- Aşağıdaki komutu kullanarak gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```
- Geckodriver'ı [https://sourceforge.net/projects/geckodriver.mirror/](https://sourceforge.net/projects/geckodriver.mirror/) adresinden indirin.
- İndirilen dosyayı çıkarın ve çıkarılan dosyanın yolunu sistem ortam değişkeni PATH'e ekleyin.
- config.ini dosyasını düzenleyin ve kendi bilgilerinizi yazın.
- Aşağıdaki komutu kullanarak çalıştırın:
```bash
python main.py
```

### Çıktı
Projenin çıktısı bir sqlite veritabanı dosyasıdır. Veritabanı aşağıdaki tabloları içerir:
- maçlar
- haftalar

### Lisans
Bu proje, ayrıntılar için [LICENSE](LICENSE) dosyasına bakın MIT Lisansı altında lisanslanmıştır.

## Katkıda Bulunma
Pull istekleri bekliyoruz. Büyük değişiklikler için lütfen önce neyi değiştirmek istediğinizi tartışmak üzere bir "issue" açın.