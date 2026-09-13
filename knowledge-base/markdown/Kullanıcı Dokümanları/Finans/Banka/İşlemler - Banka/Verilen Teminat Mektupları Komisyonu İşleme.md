---
title: "Verilen Teminat Mektupları Komisyonu İşleme"
page_id: "22806282"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Banka"
  - "İşlemler / Banka"
  - "Verilen Teminat Mektupları Komisyonu İşleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / İşlemler / Banka / Verilen Teminat Mektupları Komisyonu İşleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTVhM2M4ZTFiLTZkMWMtNDkyZC05OTliLTMyNzhmYTM3ZjhhYyZsaW5rPWI4NmZmOTQyLWI3ZWItNDRmYi1hNDMzLTE2NGRhNTYwMWUzMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5a3c8e1b-6d1c-492d-999b-3278fa37f8ac&link=b86ff942-b7eb-44fb-a433-164da5601e32&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "verilen-teminat-mektuplari-komisyonu-isleme_22806284_22806282.html"
source_version: "2022-04-04T15:22:05.350+03:00"
source_bytes: 60225
fetched_at: "2026-09-13T04:10:16+00:00"
generator: "netsis-scraper 1.0.0"
---
# Verilen Teminat Mektupları Komisyonu İşleme

Finans Bölümü'nde, "İşlemler/Banka" menüsünün altında yer alır. Verilen Teminat Mektupları Komisyonu İşleme, bankadan teminat karşılığı alınan "Teminat Mektubuna" ait tutar karşılığında bankanın aldığı rakamın (komisyonun) kaydedildiği bölümdür. "Damga" ile ilgili bilgiler, teminat mektubuna ait ilk defa kayıt yapılması halinde aktif hale gelir. Damga vergisi teminat tutarı üzerinden, BSMV ise damga vergisi ve komisyon üzerinden alınır. Daha sonra, her yıl üç aylık dönemlerle komisyon ve komisyon üzerinden BSMV alınır. Virman banka hesap kodunun "Vadesiz" veya "Rotatif" hesap olması gerekir.

Banka Hesap Hareketlerine aşağıdaki şekilde kayıt aktarılır:

```text
Komisyon                  Alacak
```

```text
Damga Vergisi          Alacak
```

```text
BSMV                       Alacak olacak şekilde kayıt aktarılır.
```

![](../../../../_assets/11b15bf56e8b350dad01.png)

Verilen Teminat Mektupları Komisyonu İşleme ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Verilen Teminat Mektupları Komisyonu İşleme Ekranı |  |
| --- | --- |
| Kayıt No | Teminat mektubu komisyonu işlemek için kayıt numarası girilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kayıtlı numaralar arasından seçim yapılır. |
| Dekont No | Yapılan işleme ait banka tarafından verilen işlem numarasının rapor amaçlı takibinin yapılması amacıyla dekont numarası girilen alandır. |
| Başlangıç Tarihi | Banka hareketindeki son kayda ait başlangıç tarihinin otomatik olarak aktarıldığı alandır. |
| Bitiş Tarihi | Banka hareketindeki son kayda ait bitiş tarihinin otomatik olarak aktarıldığı alandır. |
| İşlem Tarihi | Verilen teminat mektubu komisyonu işlem tarihinin girildiği alandır. |
| Komisyon Oranı | Verilen teminat mektubu komisyon oranının girildiği alandır. |
| Döviz Kuru | Hesabın dövizli olması durumunda aktif hale gelen alandır. Döviz kurunun girilmesini sağlar. |
| Yıl Günü | Komisyon hesaplanırken kullanılacak yıl gününün girildiği alandır. |
| ![](../../../../_assets/7bed9e17dfb93802c049.png) Komisyon Hesapla | Girilen bilgiler doğrultusunda komisyon hesaplamasının program tarafından otomatik olarak yapılması için kullanılan butondur. |
| Komisyon Muhasebe Kodu, Muhasebe Referans Kodu, Proje Kodu | Aktarılacak muhasebe hesap kodu, Banka → Kayıt → [Banka Genel Parametreleri](<../Kayıt - Banka/Banka Genel Parametreleri.md>) bölümünde tanımlanan bilgiler doğrultusunda otomatik olarak ekrana getirilir. Kullanıcı tarafından rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile, hesap kodları arasından farklı bir hesap seçilerek değişiklik yapılabilir. |
| Damga Muhasebe Kodu, Muhasebe Referans Kodu, Proje Kodu | Aktarılacak muhasebe hesap kodu, Banka → Kayıt → [Banka Genel Parametreleri](<../Kayıt - Banka/Banka Genel Parametreleri.md>) bölümünde tanımlanan bilgiler doğrultusunda otomatik olarak ekrana getirilir. Kullanıcı tarafından rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile, hesap kodları arasından farklı bir hesap seçilerek değişiklik yapılabilir. |
| BSMV Muhasebe Kodu, Muhasebe Referans Kodu, Proje Kodu | Aktarılacak muhasebe hesap kodu, Banka → Kayıt → [Banka Genel Parametreleri](<../Kayıt - Banka/Banka Genel Parametreleri.md>) bölümünde tanımlanan bilgiler doğrultusunda otomatik olarak ekrana getirilir. Kullanıcı tarafından rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile, hesap kodları arasından farklı bir hesap seçilerek değişiklik yapılabilir. |
| Tutar | Banka → Kayıt → [Banka Genel Parametreleri](<../Kayıt - Banka/Banka Genel Parametreleri.md>) bölümünde yapılan tanımlamalar baz alınarak hesaplanan tutarın aktarıldığı alandır. Kullanıcı tarafından hesaplanan tutar değiştirilebilir. |
| Virman Banka Hesap Kodu | Komisyon hesaplama sonucu bulunan tutarın aktarılacağı hesap kodunun otomatik olarak aktarıldığı alandır. Kullanıcı tarafından rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile, hesap kodları arasından farklı bir hesap seçilerek değişiklik yapılabilir. |

İlgili alanlara bilgi girişi yapıldıktan sonra "Kaydet" ![](../../../../_assets/865524a70e225c89c107.jpg) butonuna basılarak kayıt oluşturulur. Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
