# Futbol Maçı Veri Çekme
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/jonatasemidio/multilanguage-readme-pattern/blob/master/README.md)
[![tr](https://img.shields.io/badge/lang-tr--tr-green.svg)](https://github.com/jonatasemidio/multilanguage-readme-pattern/blob/master/README.pt-br.md)

# İçindekiler
1. [Giriş](#giriş)
2. [Gereksinimler](#gereksinimler)
3. [Kurulum](#kurulum)
4. [Çıktı](#çıktı)
5. [Lisans](#lisans)
6. [Katkıda Bulunma](#katkıda-bulunma)

## Giriş
Bu proje, [https://www.spordb.com](https://www.spordb.com) web sitesinden futbol maçı verilerini çekmek için yazılmıştır. Veriler, Python'daki Selenium kütüphanesi kullanılarak çekilir.

## Gereksinimler
- Python 3.6 veya daha yüksek
- Selenium
- Firefox Web Tarayıcısı
- Geckodriver

## Kurulum
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

## Çıktı
Projenin çıktısı bir sqlite veritabanı dosyasıdır. Veritabanı aşağıdaki tabloları içerir:
- maçlar
- haftalar

## Lisans
Bu proje, ayrıntılar için [LICENSE](LICENSE) dosyasına bakın MIT Lisansı altında lisanslanmıştır.

## Katkıda Bulunma
Pull istekleri bekliyoruz. Büyük değişiklikler için lütfen önce neyi değiştirmek istediğinizi tartışmak üzere bir sorun açın.