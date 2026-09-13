---
title: "Gelen e-İrsaliyeden Alış İrsaliyesi Oluşturma"
page_id: "156369583"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Gelen e-İrsaliyeden Alış İrsaliyesi Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Gelen e-İrsaliyeden Alış İrsaliyesi Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA3MTZhZDY2LWVkZDUtNGIxNS04NTE0LTJmNzE0NDhkOWY4NiZsaW5rPTI2NGE1NjIxLTE4ZTUtNGFjOC1iYWI3LTlmYTZiOGRiMmVhZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0716ad66-edd5-4b15-8514-2f71448d9f86&link=264a5621-18e5-4ac8-bab7-9fa6b8db2ead&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "gelen-e-irsaliyeden-alis-irsaliyesi-olusturma_156369600_156369583.html"
source_version: "2024-12-10T08:08:27.147+03:00"
source_bytes: 2212406
fetched_at: "2026-09-13T04:22:32+00:00"
generator: "netsis-scraper 1.0.0"
---
# Gelen e-İrsaliyeden Alış İrsaliyesi Oluşturma

Gelen e-İrsaliyeden Alış İrsaliyesi oluşturulabilmesi 2 farklı yöntemle yapılabilmektedir.

1. İrsaliye Bazında Gelen e-İrsaliye ekranında ilgili e-İrsaliye kaydı üzerinde sağ tuş ile e-İrsaliyeden Alış İrsaliyesi Oluşturma seçeneği ile
2. Alış İrsaliyesi ekranında sağ tuş menüsüne eklenen E-Belge Eşleştir seçeneği ile

# İrsaliye Bazında Gelen e-İrsaliye Ekranından Alış İrsaliyesi Oluşturma

9.0.28 seti ile birlikte "**İrsaliye Bazında Gelen e-İrsaliye"** ekranının sağ tuş seçenek menüsüne eklenen **"e-İrsaliyeden** **Alış İrsaliyesi Oluşturma"** işlemi ile Gelen e-İrsaliyeden alış irsaliyesi oluşturulması desteklenmiştir.

Gelen e-İrsaliyeden alış irsaliyesi oluşturulabilmesi için Zarf bazında Gelen e-İrsaliye ekranında e-İrsaliye

zarf durumunun "1300", irsaliye durumunun "Kabul" olması gerekmektedir.

![](../_assets/9b0d3094a46fa0f41b7d.png)

**İrsaliye** **Bazında** **Gelen** **e-İrsaliye** ekranında ilgili kayıt üzerinde sağ klik e-İrsaliyeden Alış İrsaliyesi Oluşturma seçeneği ile alış irsaliyesi oluşturulabilmektedir.

![](../_assets/1fe1db8012fcb2d2c22e.png)

Oluşturulan alış irsaliyesi ADI00…38 olarak kaydedilmiştir. Gelen uyarı ekranında tamam seçeneğine tıklandığında oluşan alış irsaliyesi ekrana gelecektir. Eğer gelen e-İrsaliyenin xml'indeki vergi numarası Cari Hesap Kayıtları ekranında vergi numaralarından bulunamazsa uyarı verilip cari kartın açılması beklenmektedir.

Benzer şekilde Xml de fatura kalemlerinin Netsiste bulunup belgeleye getirilmesi adımında xml dosyada SellerssItemIdentification, BuyersItemIdentification ve ManufacturersItemIdentification tagleri ile gelen bilgiler için sırasıyla stokkodu, barkod bilgisi, üretici kodu, cari stok kodu ve Müşteri Satıcı Stok Kayıtları ekranındaki alanlar kontrol edilir. Eğer stok kodu bulunamazsa "EFATURA_STOK" şeklinde açılmış olan sabit bir stok kodu için kalemler oluşmaktadır. İlgili kalemler üzerinde kullanıcı gerçek stok kodları ile düzenleme yapmalıdır. Toplamlar sekmesinde tamam seçeneği ile Gelen e-İrsaliyeden Alış İrsaliyesi Oluşturma işlemi tamamlanır.

Üst Bilgiler, Kalemler ve Toplamlar sekmesi kontrol edilerek Toplamlar sekmesinde tamam seçeneği ile alış irsaliyesi oluşturma işlemi tamamlanır.

![](../_assets/5ccb68008d5cd9bb2e80.png)

![](../_assets/241ff58453bd97cc29bf.png)

İrsaliye Bazında Gelen e-İrsaliye ekranında**, "e-Belge Eşleştirme İptali"** işlemi ile de oluşturulan alış irsaliyesinin e-Belge bağlantısının koparılması sağlanır. Böylece yapılan işlemler geri alınabilir ve istenirse Alış İrsaliyesi ekranından eşleştirilen alış irsaliyesi silinebilir.

![](../_assets/3c4b34cdd9923d123b96.png)

# Alış İrsaliyesi Ekranında Sağ Tuş Menüsüne Eklenen E-Belge Eşleştir İşlemi

Alış irsaliyesi manuel oluşturularak **Alış** **İrsaliyesi** ekranında sağ klikte **"E-Belge** **Eşleştir"** seçeneği ile de gelen e-İrsaliye ile alış irsaliyesi eşleştirilebilmektedir.

![](../_assets/2a79a87cd8ac5b80ffd0.png)

![](../_assets/c52fa23e7fa6097da3fd.png)

2 yöntemin sonunda İrsaliye Bazında Gelen e-İrsaliye ekranında Netsis İrsaliye Numarası alanı dolmaktadır.

![](../_assets/28b8dfb73ae28fd6474b.png)

Benzer şekilde, **Alış İrsaliyesi** ekranının Üst Bilgiler sekmesinde sağ tuş menüsünde de **"e-Belge** **Eşleştirme İptali"** işlemiyle de alış irsaliyesinin e-Belge bağlantısının koparılması sağlanır ve istenirse belge silinebilir.

![](../_assets/f236d25eb3b828d9adb1.png)
