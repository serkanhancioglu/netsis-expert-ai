---
title: "Faiz İşleme - Kapatma"
page_id: "22806280"
product: "netsis-3-enterprise"
depth: 5
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Banka"
  - "İşlemler / Banka"
  - "Faiz İşleme - Kapatma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / İşlemler / Banka / Faiz İşleme - Kapatma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ0MjhiOTY0LWIzMDMtNDIyNy04MWMxLWMzY2E3ZmI2ODA2NiZsaW5rPWE2MzMwNTZhLTRhMjMtNDAzYS1iY2FlLThiMzI4Y2RkMjMxZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d428b964-b303-4227-81c1-c3ca7fb68066&link=a633056a-4a23-403a-bcae-8b328cdd231e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "faiz-isleme-kapatma_34221841_22806280.html"
source_version: "2022-12-05T08:56:40.137+03:00"
source_bytes: 501842
fetched_at: "2026-09-13T04:10:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# Faiz İşleme - Kapatma

Finans Bölümü'nde, "İşlemler/Banka" menüsünün altında yer alır. Faiz İşleme-Kapatma bölümünde; Vadesiz, Vadeli, Rotatif ve Spot Hesaplar için faiz hesaplatarak işleme ve kapatma ile ilgili işlemlerin yapılmasını sağlar. Faiz İşleme-Kapatma, Ön Sorgulama ve Faiz Bilgileri sekmelerinden oluşur. Spot, Repo ve Vadeli hesaplar için; Faiz Tutarı=(Gün\*Anapara\*Faiz Oran)/(Yıl günü\*100) faiz, rotatif ve vadesiz mevduatta bakiye üzerinden alınır. Aşağıdaki örnekte belirtildiği gibi gün hesaplanıp, her gün faiz formülünden geçirilerek toplam faiz tutarı hesaplanır.

**Örneğin**

Banka Hesap Hareketlerinde (Transfer Hesap Kodu) Vadesiz Hesap ise:

|  | Borç | Alacak | Tip | Açıklama |
| --- | --- | --- | --- | --- |
| Faiz Gelir | 100 |  | faiz | Faiz Gelir |
| MSIGV |  | 10 | masraf | MSIGV |
| SSDF |  | 1 | masraf | SSDF |

Rotatif Hesap ise, Banka Hesap Hareketlerinde (Transfer Hesap Kodu):

|  | Borç | Alacak |
| --- | --- | --- |
| Faiz Gider |  | 100 |
| Komisyon |  | 10 |
| KKDF |  | 3 |
| BSMV |  | 5 |

Vadeli Hesap ise, vadeli hesapta hesap kapanır ve faizi ile birlikte para vadesiz hesaba aktarılır. Kullanıcı, isterse daha sonra hesap açma bölümünden tekrar kendisi vadeli hesap açabilir.

Banka Hesap Hareketlerinde (Vadeli Hesap Kodu), hesap açıldığında vadeli hesapta borç, aynı tutar kadar vadesiz hesapta alacak kaydı oluşur.

```text
Spot Hesap ise, spot kredi açıldığında spot hesaba alacak, aynı tutar kadar vadesiz hesapta borç kaydı oluşur.
```

|  | Borç | Alacak |
| --- | --- | --- |
| Hesap Açılışı |  | 100.000.000 |
| Hesap Kapanışı | 100.000.000 |  |

Banka Hesap Hareketlerinde, Transfer-Vadesiz Hesap Kodu aşağıdaki şekilde oluşur:

|  | Tutar |
| --- | --- |
| Komisyon | 100.000 |
| KKDF | 83.333 |
| BSMV | 41.667 |
| Hesap Kapama | 100.833.333 |

Repo Hesap ise; repo hesapta hesap kapanır ve faizi ile birlikte para vadesiz hesaba aktarılır. Kullanıcı, isterse daha sonra hesap açma bölümünden tekrar kendisi repo hesap açabilir.

Banka Hesap Hareketlerinde (Repo Hesap kodu), hesap açıldığında repo hesabına borç, aynı tutar kadar vadesiz hesapta alacak kaydı oluşur.

Faiz işleme kapatmada borç ve alacak kaydı aşağıdaki şekilde oluşur:

|  | Borç | Alacak |
| --- | --- | --- |
| Ana Para | 10.000.000 (hesap açılışı ile var olan kayıt) |  |
| Hesap Kapanışı |  | 10.000.000 |

**Ön Sorgulama**

Faiz İşleme-Kapatma ekranındaki Ön sorgulama sekmesinin alanları ve içerdiği bilgiler aşağıdaki şekildedir:

![](../../../../../_assets/8ca1becdd786ddb39e14.png)

| Faiz İşleme (Kapatma) Ekranı |  |
| --- | --- |
| Banka Hesap Kodu | Faiz işleme/kapatma yapılacak banka hesap kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, banka hesapları arasından seçim yapılır. |
| ![](../../../../../_assets/c102c4379c4bac16132c.png) Diğer Sayfa | "Faiz Bilgileri" sekmesine geçmek için kullanılan butondur. |

**Faiz Bilgileri**

![](../../../../../_assets/52c2df68ee399ef1a787.png)

Faiz İşleme-Kapatma ekranındaki Faiz Bilgileri sekmesinin alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Faiz İşleme/Kapatma Ekranı |  |
| --- | --- |
| Referans No | Faiz işlemek için 15 karakterden oluşan alfa numerik takip numarası girilen alandır. |
| Oran | Faiz kapatması yapılacak hesabın "Vadeli", "Uzun Vadeli" veya "Taksitli Kredi" olması durumunda aktif hale gelen alandır. Faiz oranının girilmesini sağlar. |
| Dövizli Anapara | Faiz kapatması yapılacak hesabın "Vadeli", "Uzun Vadeli" veya "Taksitli Kredi" olması durumunda aktif hale gelen alandır. Dövizli anaparanın izlenmesini sağlar. |
| Anapara | Faiz kapatması yapılacak hesabın "Vadeli", "Uzun Vadeli" veya "Taksitli Kredi" olması durumunda aktif hale gelen alandır. Anaparanın izlenmesini sağlar. |
| Dekont No | Yapılan işleme ait banka tarafından verilen işlem numarasının rapor amaçlı takibinin yapılması amacıyla dekont numarası girilen alandır. |
| Başlangıç Tarihi | "Vadeli" ve "Spot" hesaplarda, banka hareketindeki son kayda ait tarihin otomatik olarak aktarıldığı alandır. Kullanıcı, tarih üzerinde değişiklik yapabilir. |
| Kapanış Tarihi | "Vadeli" ve "Spot" hesaplarda, banka hareketindeki son kayda ait vade tarihinin otomatik olarak aktarıldığı alandır. Kullanıcı, tarih üzerinde değişiklik yapabilir. |
| Döviz Kuru | Hesabın dövizli olması durumunda aktif hale gelen alandır. Döviz kurunun girilmesini sağlar. |
| Yıl Günü | Faiz hesaplanırken kullanılacak yıl gününün girildiği alandır. |
| İhracat Taahhütlü | Kredi faizinin ihracat taahhütlü olması durumunda kullanılan seçenektir. |
| Vadeye 1 Gün Eklensin | Kredi faiz vadesine bir (1) gün eklenmesi için kullanılan seçenektir. |
| Firma Takvimi Dikkate Alınsın | Kredi faizi işlerken firma takviminin dikkate alınması için kullanılan seçenektir. |
| Kredi Erken Kapansın | Kredinin erken kapatılması istendiğinde kullanılan seçenektir. |
| Erken Kapama Ceza Oranı | "Kredi Erken Kapansın" parametresinin işaretlenmesi ile aktif hale gelen seçenektir. Kredinin erken kapatılmasına bağlı olarak bankanın uyguladığı ceza oranının girilmesini sağlar. |
| Ara Ödeme | Rotatif kredilerde faiz ödeme tarihinden önce ara ödeme yapılması için kullanılan seçenektir. |
| ![](../../../../../_assets/6c1700bcc924fb61e85b.png) Faiz Hesapla | Girilen bilgiler doğrultusunda faiz hesaplamasının program tarafından otomatik olarak yapılması için kullanılan butondur. |
| Faiz Geliri/Gideri, Muhasebe Kodu, Muhasebe Referans Kodu, Proje Kodu | "Vadeli" ve "Vadesiz" Hesapta faiz geliri, diğerlerinde faiz gideri olarak aktarılacak muhasebe hesap kodunun, Banka → Kayıt → Banka Şube Bazında Parametreler bölümünde tanımlanan bilgiler doğrultusunda otomatik olarak ekrana getirildiği alandır. Kullanıcı tarafından rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile, hesap kodları arasından farklı bir hesap seçilerek değişiklik yapılabilir. |
| MSIGV Muhasebe Kodu, Muhasebe Referans Kodu, Proje Kodu | Kapatma yapılan hesap tipinin "Vadeli" ve "Vadesiz" olduğu durumlarda aktif hale gelen alandır. Hesaplanan tutarın matrahını "Faiz Tutarı" oluşturur. Aktarılacak muhasebe hesap kodu, Banka → Kayıt → [Banka Şube Bazında Parametreler](<../../Kayıt - Banka/Banka Şube Bazında Parametreler.md>) bölümünde tanımlanan bilgiler doğrultusunda otomatik olarak ekrana getirilir. Kullanıcı tarafından rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile, hesap kodları arasından farklı bir hesap seçilerek değişiklik yapılabilir. |
| SSDF Muhasebe Kodu, Muhasebe Referans Kodu, Proje Kodu | Kapatma yapılan hesap tipinin "Vadeli" ve "Vadesiz" olduğu durumlarda aktif hale gelen alandır. Hesaplanan tutarın matrahını "MSIGV" oluşturur. Aktarılacak muhasebe hesap kodu, Banka → Kayıt → [Banka Şube Bazında Parametreler](<http://Banka Şube Bazında Parametreler>) bölümünde tanımlanan bilgiler doğrultusunda otomatik olarak ekrana getirilir. Kullanıcı tarafından rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile, hesap kodları arasından farklı bir hesap seçilerek değişiklik yapılabilir. |
| KKDF Muhasebe Kodu, Muhasebe Referans Kodu, Proje Kodu | Kapatma yapılan hesap tipinin "Spot" ve "Rotatif" olduğu durumlarda aktif hale gelen alandır. Aktarılacak muhasebe hesap kodu, Banka → Kayıt → [Banka Şube Bazında Parametreler](<../../Kayıt - Banka/Banka Şube Bazında Parametreler.md>) bölümünde tanımlanan bilgiler doğrultusunda otomatik olarak ekrana getirilir. Kullanıcı tarafından rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile, hesap kodları arasından farklı bir hesap seçilerek değişiklik yapılabilir. Faiz tutarı üzerinden alınır. |
| BSMV Muhasebe Kodu, Muhasebe Referans Kodu, Proje Kodu | Kapatma yapılan hesap tipinin "Spot" ve "Rotatif" olduğu durumlarda aktif hale gelen alandır. Aktarılacak muhasebe hesap kodu, Banka → Kayıt → [Banka Şube Bazında Parametreler](<../../Kayıt - Banka/Banka Şube Bazında Parametreler.md>) bölümünde tanımlanan bilgiler doğrultusunda otomatik olarak ekrana getirilir. Kullanıcı tarafından rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile, hesap kodları arasından farklı bir hesap seçilerek değişiklik yapılabilir. Faiz tutarı üzerinden alınır. |
| Komisyon Muhasebe Kodu, Muhasebe Referans Kodu, Proje Kodu | Kapatma yapılan hesap tipinin "Spot" ve "Rotatif" olduğu durumlarda aktif hale gelen alandır. Aktarılacak muhasebe hesap kodu, Banka → Kayıt → [Banka Şube Bazında Parametreler](<../../Kayıt - Banka/Banka Şube Bazında Parametreler.md>) bölümünde tanımlanan bilgiler doğrultusunda otomatik olarak ekrana getirilir. Kullanıcı tarafından rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile, hesap kodları arasından farklı bir hesap seçilerek değişiklik yapılabilir. Faiz tutarı üzerinden alınır. |
| Stopaj Muhasebe Kodu, Muhasebe Referans Kodu, Proje kodu | Kapatma yapılan hesap tipinin "Vadeli" olduğu durumlarda aktif hale gelen alandır. Aktarılacak muhasebe hesap kodu, Banka → Kayıt → [Banka Genel Parametreleri](<../../Kayıt - Banka/Banka Genel Parametreleri.md>) bölümünde tanımlanan bilgiler doğrultusunda otomatik olarak ekrana getirilir. Kullanıcı tarafından rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile, hesap kodları arasından farklı bir hesap seçilerek değişiklik yapılabilir. Faiz tutarı üzerinden alınır. |
| Ceza Muhasebe Kodu, Muhasebe Referans Kodu, Proje Kodu | Kapatma yapılan hesap tipinin "Taksitli" ve "Uzun/Orta Vadeli" olduğu durumlarda ekrana gelen alandır. "Kredi Erken Kapansın" parametresinin işaretlenmesi ile aktif hale gelir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodları arasından seçim yapılır. |
| Tutar | Banka → Kayıt → [Banka Genel Parametreleri](<../../Kayıt - Banka/Banka Genel Parametreleri.md>) bölümünde yapılan tanımlamalar baz alınarak hesaplanan tutarın aktarıldığı alandır. Kullanıcı tarafından hesaplanan tutar değiştirilebilir. |
| Net Faiz Geliri/Gideri | "Vadesiz" ve "Vadeli" hesaplar için faiz tutarından MSIGV ve SSDF tutarı çıkarılarak hesaplanır. Spot ve Rotatif hesaplarda hesaplama yapılırken, faiz tutarına Komisyon, KKDF ve BSMV eklenir. |
| Kapanacak Taksit | Kapanacak taksit sayısının girildiği alandır. |
| Taksit Anapara | Faiz hesaplama işlemi yapıldıktan sonra kalan taksit anaparanın izlendiği alandır. |
| Tüm Taksitler Tek Seferde Kapatılsın | Taksitlerin tek seferde kapatılması için kullanılan seçenektir. |
| Transfer Banka Hesap Kodu | Faiz kapatma sonucu hesaplanan faiz tutarının aktarılacağı hesap kodunun girildiği alandır. Seçilen hesap tipi "Vadesiz" hesap ise "Ön Sorgulama" sekmesinde seçilen banka hesabına, "Vadeli", "Rotatif" veya "Spot" hesap ise başka bir vadesiz banka hesap koduna aktarılır. |

İlgili alanlara bilgi girişi yapıldıktan sonra "Kaydet" ![](../../../../../_assets/865524a70e225c89c107.jpg) butonuna basılarak kayıt oluşturulur. Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
