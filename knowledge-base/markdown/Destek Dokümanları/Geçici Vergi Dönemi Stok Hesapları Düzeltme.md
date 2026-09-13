---
title: "Geçici Vergi Dönemi Stok Hesapları Düzeltme"
page_id: "147554752"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Geçici Vergi Dönemi Stok Hesapları Düzeltme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Geçici Vergi Dönemi Stok Hesapları Düzeltme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTJlYjk0MDc0LTgxYWMtNGZhZi1hMzQyLWRhMTcxN2VkZDcwNSZsaW5rPWEyOWExZDFmLWIxNTMtNGI0ZS04OTFkLWFlNTRlMjdmOGRjNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=2eb94074-81ac-4faf-a342-da1717edd705&link=a29a1d1f-b153-4b4e-891d-ae54e27f8dc5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "gecici-vergi-donemi-stok-hesaplari-duzeltme_147554903_147554752.html"
source_version: "2024-08-13T15:45:59.200+03:00"
source_bytes: 386395
fetched_at: "2026-09-13T04:22:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# Geçici Vergi Dönemi Stok Hesapları Düzeltme

**Toplulaştırılmış** **Yöntemler** **ile Stok Hesapları** **Düzeltme**

Enflasyon düzeltmesinde esas yöntem düzeltme katsayısının hesaplanıp(gerçek yöntem), ilgili katsayısının düzeltmeye konu olacak bilanço kalemine uygulanması suretiyle düzeltme işleminin tamamlanmasıdır. Ancak tebliğde stoklara ilişkin düzeltmede toplulaştırılmış yöntemin kullanılması mükelleflerin tercihine bırakılmıştır.

**Stoklara İlişkin "Basit Ortalama Yöntemi" Düzeltme Katsayısı:**

Basit ortalama yönteminde düzeltme katsayısı, mali tabloların ait olduğu aya ilişkin fiyat endeksinin (Yİ-ÜFE), bu endeks ile bir önceki geçici vergi döneminin sonundaki fiyat endeksi (Yİ-ÜFE) toplamının ikiye bölünmesi sonucu bulunan endekse bölünmesiyle elde edilen katsayı olarak hesaplanır ve düzeltmeye esas tutar olarak da düzeltme işlemine tabi tutulan bilançoda yer alan stoklara ait değerler esas alınır.
30.06.2024 tarihli enflasyon düzeltmesinde kullanılacak basit ortalama yöntem düzeltme
katsayısı 1,03421 olarak hesap edilmektedir.
Bilançonun ait olduğu aya ait Yİ-ÜFE
Düzeltme Katsayısı= --------------------------------------------------------------------------------------------------------------------------------------------------------
(Bilançonun ait olduğu aya ait Yİ-ÜFE + Bilanço günü itibarıyla bir önceki geçici vergi döneminin sonundaki Yİ-ÜFE) / 2
Stok Hesapları Düzeltme işleminde "Tarih" 30.06.2024 , "Dönem Başlangıç Tarihi" 31.03.2024 olarak girilmeli ve "Dönem Son Ay İçin Düzeltme" parametresi işaretlenmelidir.
Örnek: 30/06/2024 tarihi itibariyle 153-01-002 hesabının bakiyesi 600.000TL'dir. İşletme ilgili hesabın enflasyon düzeltmesini gerçekleştirirken toplulaştırılmış yöntemlerden basit ortalama yöntemi seçmiştir.
![](../_assets/4ddcb6b2fea47d0711a7.png)
![](../_assets/632969894499ca58cd44.png) ![](../_assets/25c5addaedac60ce0192.png)
Baz endeksler aşağıdaki gibidir.
Mart Yİ-ÜFE = 3.252,79
Haziran 2024 Yİ-ÜFE=3.483,25
Dönem Ortalama Düzeltme Katsayısı = Haziran /((Haziran+2023Aralık)/2)
Dönem Ortalama Düzeltme Katsayısı = 3.483,25/ ((3.483,25+3.252,79) / 2) =1,034213
Enflasyon Farkı=Bilançonun ait olduğu ay itibari ile hesap bakiyesi \* Dönem ortalama düzeltme katsayısı
Enflasyon Farkı= 600.000,00-TL x 0,03421 =20.526,00-TL olarak hesaplanır.
İşlem sonucunda Mahsup tipli ve Açıklama 1 alanı "TOPLULAŞTIRILMIŞ YÖNTEM ENFLASYON DÜZELTMELERİ" olan yevmiye fişi oluşur. 153-01-002 hesabın kartında tanımlanmış olan enflasyon fark hesabı ile muhasebe parametrelerinde tanımlanmış olan enflasyon düzeltme hesabı karşılıklı olarak çalışır.
![](../_assets/4f44fbc0606c4c4e2d41.png)
