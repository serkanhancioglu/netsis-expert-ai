---
title: "Spot Kredi Açma"
page_id: "22806271"
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
  - "Spot Kredi Açma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / İşlemler / Banka / Spot Kredi Açma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWNhMzE2YmY1LTkwNDItNDkwZS1hNzQzLTFlMmRmNTFkZjczNiZsaW5rPTNhMmJmOGY1LTYzMTAtNDViOS1iOGRhLTQyM2U0MGEyZmMxMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ca316bf5-9042-490e-a743-1e2df51df736&link=3a2bf8f5-6310-45b9-b8da-423e40a2fc13&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "spot-kredi-acma_34221766_22806271.html"
source_version: "2022-04-04T13:22:23.490+03:00"
source_bytes: 68134
fetched_at: "2026-09-13T04:10:11+00:00"
generator: "netsis-scraper 1.0.0"
---
# Spot Kredi Açma

Finans Bölümü'nde, "İşlemler/Banka" menüsünün altında yer alır. "Spot Kredi Açma" işleminin yapıldığı bölümdür. Daha önceden açılmış bir hesap olmaması için Spot Kredi Banka Hesap Kodu alanında girilen hesabın bakiyesinin sıfır olması gerekir. Virman Hesap Kodu alanına girilen hesabın (paranın aktarılacağı hesap) vadesiz hesap olması gerekir.

![](../../../../_assets/53b33f4a81701f7e9a29.png)

Spot Kredi Açma ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Spot Kredi Açma Ekranı |  |
| --- | --- |
| Referans No | "Spot Kredi Açma" işlemi için 15 karakterden oluşan alfa numerik takip numarası girilen alandır. |
| Devir Kaydı | "Devir Kaydı" seçeneği işaretlenerek işlem yapıldığı zaman sadece "Spot Kredi Banka Hesap Kodu" hareketlerine alacak kaydı aktarılır. Entegrasyon ve "Virman Banka Hesap Kodu" hareketine kayıt aktarılmaz. |
| Spot Kredi Banka Hesap Kodu | Banka Hesap Hareketlerine; "Spot Kredi Banka Hesap Kodu" alanına, tipi "Hesap açılışı" olan alacak hareketi aktarılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, banka hesap kodlarına ulaşılır. |
| Virman Banka Hesap Kodu | Banka Hesap Hareketlerine; "Virman Hesap Kodu" alanına, tipi "Virman" olan borç hareketi kaydedilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, banka hesap kodlarına ulaşılır. |
| İşlem Tarihi | Yapılan işleme ait tarihin girildiği alandır. Program tarafından günün tarihi otomatik olarak ekrana gelir. |
| Dekont No | Yapılan işleme ait banka tarafından verilen işlem numarasının rapor amaçlı takibinin yapılması amacıyla dekont numarası girilen alandır. |
| Vade Tarihi/Efektif Tarihi | Açılışı yapılan hesaba ait vade/efektif tarihinin girildiği alandır. |
| Faize Vergi Dahil | "Spot Kredi Açma" işleminde faize vergi dahil edilmesi istendiğinde kullanılan seçenektir. |
| Libor Oranı | Dünyanın önde gelen kredibilitesi yüksek bankaların kısa vadeli borçlanma için birbirlerine uyguladıkları faiz oranına "Libor Oranı" denir. Yapılan işleme ait "Libor Oranı" girilerek faiz oranının hesaplanması sağlanır. |
| Spread Oranı | Döviz kurunun alış fiyatı ile satış fiyatı arasındaki farkın girildiği alandır. |
| Faiz Oranı | İlgili hesabın faiz oranının hesaplandığı alandır. Libor Oranı + Spread Oranı, faiz oranını belirler. |
| Döviz Tutar/Tutar | Hesaba ait "Dövizli" yada "TL" tutarın girildiği alandır. |
| Muhasebe Referans Kod | Muhasebe → Kayıt → Muhasebe Parametreleri → Yevmiye → “Fişlerde referans kodu sorulsun” parametresinin aktif olduğu durumlarda, seçilen hesap tiplerine göre referans kodu sorgulanır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, referans kodları arasından seçim yapılır. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → “Proje Uygulaması Var" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. İlgili proje kodu, rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile seçilerek girilir. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. İlgili plasiyer kodu, rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile seçilerek girilir. |

İlgili alanlara bilgi girişi yapıldıktan sonra "Kaydet" ![](../../../../_assets/865524a70e225c89c107.jpg) butonuna basılarak kayıt oluşturulur. Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
