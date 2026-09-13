---
title: "Kalite Kontrol Yenilik Dokümanı"
page_id: "50680029"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kalite Kontrol Yenilik Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kalite Kontrol Yenilik Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFjMWE1YjI5LWVmZWMtNDUwMy1iNjQ5LTIwYmEwYmE2MzA0NCZsaW5rPTYxZWFkNTI1LWZhNGUtNDRhZi1hMzA1LWYyZjU0MTlkZTNkNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1c1a5b29-efec-4503-b649-20ba0ba63044&link=61ead525-fa4e-44af-a305-f2f5419de3d4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kalite-kontrol-yenilik-dokumani_79167521_50680029.html"
source_version: "2022-11-03T09:40:16.383+03:00"
source_bytes: 566522
fetched_at: "2026-09-13T04:26:04+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kalite Kontrol Yenilik Dokümanı

Kalite Kontrol Yenilikleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| **Amaç** **ve** **Fayda** | Kalite Kontrol modülünde önemli kalite performans ölçümlerinden biri olan Parts Per Million (PPM) kullanımının desteklenmesine, işleyişin daha kontrollü, güvenli ve hızlı olabilmesine yönelik bazı iyileştirme çalışmaları yapılmıştır.<br>PPM, kalite performansını ölçmek için kullanılan yaygın bir ölçümdür. Özellikle otomotiv sektöründe kontrollerde kalite performans ölçümünde kullanılmaktadır. Satın alınan 1 milyon parça içerisinden 1 adet hatalı parça tespit edilirse PPM değeri 1 olarak belirtilecektir. 1 PPM değeri, bir milyon içerisinde 1 hata olduğunu ifade etmektedir. Formül olarak ifade edilirse PPM = (Hatalı Parça Sayısı / Toplam Parça Sayısı) \* 1.000.000 şeklindedir. Tedarikçi/Stok raporları PPM desteği ile daha işlevsel hale getirilmiştir. Tedarikçi/Stok durum takibini sağlayabilmek için kalite performans raporu oluşturulmuştur. Kalite performans raporu ile tedarikçi/stok bazında son 10 alış irsaliyesindeki sonuçlar tablo ve grafiksel gösterim ile kullanıma sunulmaktadır.<br>Kalite kontrol süreçlerinde PPM kalite performans ölçümünün izlenebilmesi, tedarikçi/stok durum takibinin sağlanması ile denetimsel, kurumsal kolaylık hedefleyen bu yenilik, Netsis 8.0 onaylı sürümü ile birlikte kullanılabilir olacaktır. |
| **Ürün Grubu** | \[X\] Netsis Enterprise<br>\[X\] Netsis Standard<br>\[X\] Netsis Entegre |
| **Modül** | \[X\] Kalite Kontrol |
| **Kategori** | \[X\] Yeni Fonksiyon |
| **Versiyon Önkoşulu** | 8.0.0 |
| **Uygulama** | ![](../_assets/ca0b503bfcd5952e4e5d.png) |

#### Kalite Kontrol Kayıtları

Kalite kontrol kayıtlarının kapanması esnasında ek kontroller oluşturularak kayıtların daha güvenli ve doğru oluşturulması hedeflenmiştir.

Bu kapsamda eklenen kontroller şunlardır:

- Ölçüm değerlerinin girişlerinin yapılmış olması.
- Hareket kayıtlarının durumlarının belirlenmiş olması.

![](../_assets/ac80713bc0c0757f9391.png)

Kalite kontrol kaydı kapandığında sistem tarafından tavsiye edilen durum (kabul, red) bilgisinin görüntülenmesi; sistemde kayıt altına alınması ve durum değişikliğinin kullanıcının seçimi ile yapılabilmesi sağlanmıştır.

#### Kalite Detayları

##### Veri Giriş Kullanım Yöntemleri

Kalite kontrol kalite detayları bölümünde veri giriş yöntemleri, hareket bazında kullanım (mevcut) veri girişi ve ölçüm bazında kullanım veri girişi olmak üzere desteklenmiştir.

![](../_assets/3f23fd0d7b8021264e49.png)

Bu sayede yapılan kalite ölçümleri bazında hareket kayıtları yapılabilecektir. Veri giriş yöntemleri arasında kullanım esnasında geçiş yapılabilecektir.

#### Grup Tanımlama

Grup tanımlama ekranında fare üzerinde sağ tuş seçiminde Stok Eşleştir işlemi ile ilgili grubun belirtilen stok kodu ile eşleştirilmesi desteklenmiştir.

![](../_assets/4c4c9ad562f18396bd24.png)

Seçim sonrasında açılan ekranda istenen stok kodu ve departman kodu bilgilerinin seçilmesi ile eşleştirme kaydı otomatik olarak sistem tarafından kaydedilir.
![](../_assets/9c35be11d7a6bf5fe33a.png)

#### Muayene Tanımlama

![](../_assets/8391cd56673c9cc55d2d.png)
Stok/Cari Muayene eşleştirme ekranında öngörülen PPM değerinin sisteme tanımlanabilmesi desteklenmiştir. Sisteme girilen değer sonrasında sistem raporlarında kullanılacaktır.

#### Kalite Kontrol Raporları

Satıcı performans raporunda stok detaylı/detaysız durumuna göre istenen PPM değerlerinin ve sistemde hesaplanan PPM değerlerinin görüntülenmesi desteklenmiştir.
![](../_assets/07bcee1c77f2f23f6b53.png)
Stok performans raporunda öngörülen PPM değerlerinin ve sistemde hesaplanan PPM değerlerinin görüntülenmesi de desteklenmiştir.
![](../_assets/380adedde05f2c39e789.png)

#### Kalite Kontrol Performans Raporu

Satıcıların veya stokların belirlenen tarih aralığında alış irsaliyelerine bağlı kalite kontrol kayıtlarının kontrol edilebilmesine yönelik oluşturulmuştur. Stok/Cari kısıtları ile son 10 irsaliye kaydının kalite kontrol kayıt sonuçlarının tablo ve grafiksel olarak gösterimi desteklenmiştir.
![](../_assets/312e3277da83fb02a9be.png)

Çalıştır işlemi sonrasında sonuçlar, ekrana üst bölümde tablo yapısında alt bölümde ise grafiksel olarak görüntülenmektedir.
![](../_assets/af1933912364ba1ec310.png)

Aktarım seçenekleri ile ilgili sonuçların dışarıya aktarımı sağlanabilecektir. Başlık bilgisi yazdırma seçeneği ile çıktı üzerinde görüntülenebilecektir.

![](../_assets/42de259adaed3138637e.png)
