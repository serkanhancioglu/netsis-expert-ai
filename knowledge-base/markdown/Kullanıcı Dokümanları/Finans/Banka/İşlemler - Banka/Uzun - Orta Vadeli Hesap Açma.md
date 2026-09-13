---
title: "Uzun - Orta Vadeli Hesap Açma"
page_id: "22806275"
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
  - "Uzun - Orta Vadeli Hesap Açma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / İşlemler / Banka / Uzun - Orta Vadeli Hesap Açma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFiYzRmYjkyLWI4ZGYtNDczOC04ZWIyLWFmOWViYTdkNWZkNiZsaW5rPTlhZDM4MjE4LTM1MmUtNGNhNS1hYjM3LWY3Y2MxNzIyMTRmMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1bc4fb92-b8df-4738-8eb2-af9eba7d5fd6&link=9ad38218-352e-4ca5-ab37-f7cc172214f1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "uzun-orta-vadeli-hesap-acma_34221778_22806275.html"
source_version: "2022-04-04T13:24:10.333+03:00"
source_bytes: 273305
fetched_at: "2026-09-13T04:10:12+00:00"
generator: "netsis-scraper 1.0.0"
---
# Uzun - Orta Vadeli Hesap Açma

Finans Bölümü'nde, "İşlemler/Banka" menüsünün altında yer alır. Uzun - Orta Vadeli Hesap Açma, Uzun-Orta Vadeli Hesap açma işlemi yapılmasını sağlayan bölümdür.

![](../../../../_assets/a15aba71aeca116d0c3e.png)

Uzun - Orta Vadeli Hesap Açma ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Uzun/Orta Vadeli Hesap Açma Ekranı |  |
| --- | --- |
| Referans No | "Uzun/Orta Vadeli Hesap Açma" işlemi için 15 karakterden oluşan alfa numerik takip numarası girilen alandır. |
| Uzun/Orta Vadeli Kredi Banka Hesap Kodu | Hesap tipi Uzun/Orta Vadeli Kredi olan hesabın girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile hesap kodları arasından seçim yapılır. Açılışı yapılacak olan kredi hesabının bakiye vermemesi gerekir. Açılış kaydının oluşturulması ile birlikte bu alana girilen hesap, kredi tutarı kadar alacaklı hale gelir. |
| Virman Banka Hesap Kodu | Kredi tutarının hangi vadesiz mevduat hesabına virman yapılacağının belirlendiği alandır. Kredi açılışı ile birlikte, söz konusu alana girilen hesap kredi tutarı kadar borçlu hale gelir. |
| İşlem Tarihi | Yapılan işleme ait tarihin girildiği alandır. Program tarafından günün tarihi otomatik olarak ekrana gelir. |
| Dekont No | Yapılan işleme ait banka tarafından verilen işlem numarasının rapor amaçlı takibinin yapılması amacıyla dekont numarası girilen alandır. |
| Efektif Tarihi | Açılışı yapılan hesaba ait efektif tarihin girildiği alandır. |
| Anapara Ödeme Tarihi | Açılışı yapılan hesaba ait anapara ödeme tarihinin girildiği alandır. Uzun/orta vadeli kredilerde ana paranın taksitler halinde, tamamının son taksitte ya da tamamının son taksitten sonraki bir tarihte kapatılması mümkündür. Açılış işlemi sırasında sorgulanan “Anapara Taksitlendirilsin Mi?” seçeneği işaretlenmezse, anaparanın tamamı son taksit ile birlikte kapatılabilir. Ancak, son taksitte de anapara kapanışı yapılmadığında, ödeme bu alanda belirlenen tarihte gerçekleşir. |
| Ödeme Planı | Yapılan işleme ait ödeme planı durumu seçilen alandır. Ödeme Planı Kullanılmasın, Ödeme Planı Kullanılsın ve Ödeme Planı Oluşturulsun seçenekleri arasından tercih yapılır. |
| Taksit Sayısı | Yapılan işleme ait taksit sayısının girildiği alandır. |
| Dönem | "Uzun/Orta Vadeli Hesap Açma" işlemi için dönem belirlenen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, 1 ay, 2 ay, 3 ay, ...12 ay seçenekleri arasından tercih yapılır. |
| Anapara Taksitlendirilsin Mi? | Anaparanın taksitlendirilmesi için kullanılan seçenektir. Anaparanın taksitlendirilerek kapatılacak olması halinde işaretlenmesi gereken seçenektir. Bu seçenek işaretlendiğinde, "Anapara Ödeme Tarihi" alanı pasif kalarak, bunun yerine "Taksit Başlangıcı" değeri sorgulanır. |
| Taksit Başlangıcı | "Anapara Taksitlendirilsin Mi?" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Taksit başlangıcı girilerek işleme devam edilir. Ana paranın kaçıncı taksitten itibaren ödenmeye başlanacağı bu alanda belirlenir. Örneğin; 36 ay vadeli alınan kredinin ilk 12 ayında sadece faiz ödemesi yapılacak ve 13. taksitten itibaren anapara ödemesine de başlanacak ise, 13 değerinin girilmesi gerekir. Böylece, ana para tutarı, kalan taksit sayısına bölünür ve toplam giderlere bu tutar eklenerek taksit tutarı hesaplanır. |
| Libor Oranı | Dünyanın önde gelen kredibilitesi yüksek bankaların kısa vadeli borçlanma için birbirlerine uyguladıkları faiz oranına "Libor Oranı" denir. Yapılan işleme ait "Libor Oranı" girilerek faiz oranının hesaplanması sağlanır. |
| Spread Oranı | Döviz kurunun alış fiyatı ile satış fiyatı arasındaki farkın girildiği alandır. |
| Faiz Oranı | İlgili hesabın faiz oranının hesaplandığı alandır. Libor Oranı + Spread Oranı, faiz oranını belirler. |
| Bileşik Faiz Oranı | Taksit tutarının hesaplaması sırasında kullanılacak faiz oranıdır. Hesap açılışında verilen faiz oranı ve Banka → Kayıt → Genel Parametreler bölümünde verilen BSMV ve KKDF oranları dikkate alınarak hesaplanır.<br>Bileşik Faiz Oranı= Faiz Oranı+(Faiz Oranı\*(BSMV Oranı+KKDF Oranı))<br>Taksitli kredi açılışında verilen faiz oranı %10, BSMV %5 ve KKDF %5 olduğunda bileşik faiz oranı aşağıdaki şekilde hesaplanır. Bileşik Faiz Oranı=10+(10\*(0,05+0,05))=11 Kredi açılışı “İhracat Taahhütlü” seçeneği işaretlenerek yapıldığında ise, yukarıdaki formülde BSMV oranı dikkate alınmaz. Bu durumda aynı örnek için bileşik faiz oranı 10,5 olarak hesaplanır. |
| Döviz Tutar/Tutar | Hesaba ait "Dövizli" yada "TL" tutarın girildiği alandır. |
| Muhasebe Referans Kod | Muhasebe → Kayıt → Muhasebe Parametreleri → Yevmiye → “Fişlerde referans kodu sorulsun” parametresinin aktif olduğu durumlarda, seçilen hesap tiplerine göre referans kodu sorgulanır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, referans kodları arasından seçim yapılır. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → “Proje Uygulaması Var" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. İlgili proje kodu, rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile seçilerek girilir. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. İlgili plasiyer kodu, rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile seçilerek girilir. |

İlgili alanlara bilgi girişi yapıldıktan sonra "Kaydet" ![](../../../../_assets/865524a70e225c89c107.jpg) butonuna basılarak kayıt oluşturulur. Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
