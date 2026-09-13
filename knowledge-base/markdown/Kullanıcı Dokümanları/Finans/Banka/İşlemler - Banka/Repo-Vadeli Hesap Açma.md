---
title: "Repo/Vadeli Hesap Açma"
page_id: "22806268"
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
  - "Repo/Vadeli Hesap Açma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / İşlemler / Banka / Repo/Vadeli Hesap Açma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc5NTkwNjBiLTNmODgtNDNiMS1hN2YzLTMyNTNlZjY1NWEwYSZsaW5rPThiNmIzMjJhLWQwMWMtNDc0Zi05YjEwLWM0Mjc1MjljMjczOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7959060b-3f88-43b1-a7f3-3253ef655a0a&link=8b6b322a-d01c-474f-9b10-c427529c2738&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "repo-vadeli-hesap-acma_34221752_22806268.html"
source_version: "2022-04-04T13:20:30.633+03:00"
source_bytes: 235100
fetched_at: "2026-09-13T04:10:10+00:00"
generator: "netsis-scraper 1.0.0"
---
# Repo/Vadeli Hesap Açma

Finans Bölümü'nde, "İşlemler/Banka" menüsünün altında yer alır. Repo/Vadeli Hesap Açma, Repo/Vadeli Hesap açma işlemi yapılmasını sağlayan bölümdür.

![](../../../../_assets/c1d361b516d2d4043ddd.png)

Repo/Vadeli Hesap Açma ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Repo/Vadeli Hesap Açma Ekranı |  |
| --- | --- |
| Referans No | Repo/Vadeli Hesap Açma işlemi için 15 karakterden oluşan alfa numerik takip numarası girilen alandır. |
| Vadeli Banka Hesap Kodu | Repo/Vadeli Hesap kaydı yapıldığı zaman "Banka Hesap Hareketleri" bölümüne, Vadeli Banka Hesap Kodu tipi "Hesap Açılışı" olan borç hareketi aktarılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, banka hesap kodları arasından seçim yapılır. |
| Virman Banka Hesap Kodu | Repo/Vadeli Hesap kaydı yapıldığı zaman "Banka Hesap Hareketleri" bölümüne, Virman Banka Hesap Kodu tipi "Virman" olan alacak hareketi aktarılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, banka hesap kodları arasından seçim yapılır. |
| İşlem Tarihi | Yapılan işleme ait tarihin girildiği alandır. Program tarafından günün tarihi otomatik olarak ekrana gelir. |
| Dekont No | Yapılan işleme ait banka tarafından verilen işlem numarasının rapor amaçlı takibinin yapılması amacıyla dekont numarası girilen alandır. |
| Vade Tarihi/Efektif Tarihi | Açılışı yapılan hesaba ait vade/efektif tarihinin girildiği alandır. |
| Libor Oranı | Dünyanın önde gelen kredibilitesi yüksek bankaların kısa vadeli borçlanma için birbirlerine uyguladıkları faiz oranına "Libor Oranı" denir. Yapılan işleme ait "Libor Oranı" girilerek faiz oranının hesaplanması sağlanır.. |
| Spread Oranı | Döviz kurunun alış fiyatı ile satış fiyatı arasındaki farkın girildiği alandır. |
| Faiz Oranı | İlgili hesabın faiz oranının hesaplandığı alandır. Libor Oranı + Spread Oranı, faiz oranını belirler. |
| Döviz Tutar/Tutar | Hesaba ait "Dövizli" yada "TL" tutarın girildiği alandır. |
| Muhasebe Referans Kod | Muhasebe → Kayıt → Muhasebe Parametreleri → Yevmiye → “Fişlerde referans kodu sorulsun” parametresinin aktif olduğu durumlarda, seçilen hesap tiplerine göre referans kodu sorgulanır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, referans kodları arasından seçim yapılır. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → “Proje Uygulaması Var" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. İlgili proje kodu, rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile seçilerek girilir. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. İlgili plasiyer kodu, rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile seçilerek girilir. |
| Devir Kaydı | "Devir Kaydı" seçeneği aktif halde iken hesap açma işlemi yapıldığında, sadece "Vadeli Banka Hesap Kodu" alanında yazılan banka hesabının hareketlerine borç kaydı aktarılır. Virman banka hesap kodu hareketlerine ve entegrasyona kayıt aktarılmaz. Bu işlem, vadesiz mevduattan vadeli mevduata virman işlemi yapılması istenmediğinde fakat vadeli hesap ile ilgili faiz hesaplatılması istendiğinde kullanılabilir. |
| İhracat Taahhütlü | Bu seçenek işaretlenerek açılan kredi hesaplarının kapanışı sırasında BSMV hesaplanmaz. Ayrıca, hesap açılışı sırasında hesaplanan bileşik faiz oranı ve taksit tutarı da BSMV dikkate alınmadan hesaplanır. |

İlgili alanlara bilgi girişi yapıldıktan sonra "Kaydet" ![](../../../../_assets/865524a70e225c89c107.jpg) butonuna basılarak kayıt oluşturulur. Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
