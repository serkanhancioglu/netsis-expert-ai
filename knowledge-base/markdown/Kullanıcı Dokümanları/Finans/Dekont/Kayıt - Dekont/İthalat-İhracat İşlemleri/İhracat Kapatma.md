---
title: "İhracat Kapatma"
page_id: "22805914"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Dekont"
  - "Kayıt / Dekont"
  - "İthalat/İhracat İşlemleri"
  - "İhracat Kapatma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / İthalat/İhracat İşlemleri / İhracat Kapatma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTg1OTU0YzExLTBmMjYtNDQzMS05YTQyLTk3MTAyNjY2YjY4ZCZsaW5rPTQ2MmRmMGJkLTc2MmEtNGNkMi1hOWI1LWE1YTVmOGYyNzAxNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=85954c11-0f26-4431-9a42-97102666b68d&link=462df0bd-762a-4cd2-a9b5-a5a5f8f27017&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ihracat-kapatma_34231022_22805914.html"
source_version: "2022-12-01T09:00:16.577+03:00"
source_bytes: 195870
fetched_at: "2026-09-13T04:09:20+00:00"
generator: "netsis-scraper 1.0.0"
---
# İhracat Kapatma

İhracat Kapatma, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. İhracat Kapatma, ihracat kapatma işleminin yapıldığı bölümdür. İlk olarak, Fatura → [Satış İrsaliyesi](<../../../../Lojistik - Satış/Fatura/Kayıt - Fatura/Satış İrsaliyesi.md>) bölümünden "Tipi" alanı "İthalat/İhracat" olarak işaretlenen ve döviz tutarı girilen bir irsaliye kaydının oluşturulması gerekir. Oluşturulan irsaliye kaydı, proforma fatura niteliğindedir. İthalat/ihracat tipi olarak CIF seçildiğinde, ihracat kapatma sırasında navlun ve sigorta tutarları sorgulanır ve istendiğinde bu tutarlar cari hareketlere aktarılır. Girilen ihracat irsaliyesinin, Export Referans No (Dosya No) alanının boş bırakılmaması gerekir.

Yapılan ihracatın "Export (Dosya No) Numarası" ithalat irsaliyesinin kesilmesinden sonra belirleniyorsa, bu numaranın daha sonra da irsaliyeye girmesi veya Dekont Modülü → İthalat/İhracat İşlemleri → [İthalat/İhracat Referans No Atama](<İthalat-İhracat Referans No Atama.md>) bölümünden aktarılması mümkün.

Girilen ihracat irsaliyesi kaydındaki "Miktar" bilgisi normal şartlarda stok hareket kayıtlarında izlenmez. Bu bilgi başka bir alanda program tarafından tutulur. "İhracat Kapatma" işlemi gerçekleştiğinde, "Miktar" bilgisi stok hareket kayıtlarında izlenebilir. Ancak, Fatura → Kayıt → [Satış Parametreleri](<../../../../Lojistik - Satış/Fatura/Kayıt - Fatura/Satış Parametreleri.md>) → "İthalat/İhracat Miktarları Stoklara Geçsin" parametresi işaretlenirse, mal fiilen stoklara girmese bile miktar bilgisi stoklarda izlenir.

Yapılan ihracatla ilgili her türlü masraf tutarı kaydedilirken, seri numarası IH ve aynı referans numarası kullanılması gerekir. Böylece, daha sonra ilgili ihracata ait tüm bilgiler, ihracat raporu kullanılarak listelenir. "Genel Dekont Kaydı" bölümünden IH seri numarası ile kaydedilen bilgiler, ihracat kapatma işlemi sırasında dikkate alınmaz. Sadece raporlama amacı ile kullanılır.

![](../../../../../_assets/d491493674c99995ebe8.png)

İhracat Kapatma ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| İhracat Kapatma Ekranı |  |
| --- | --- |
| İhracat Referans No | İhracat kapatma için referans numarası girilen alandır. Girilen referans numarası ile kaydedilen irsaliyelerin listelenmesi sağlanır. Boş bırakıldığında ilgili cari koda ait tüm irsaliyeler listelenir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, referans numaraları arasından seçim yapılır. |
| Fiili İhracat Tarihi | İhracatın gerçekleştirildiği fiili tarihin girildiği alandır. Girilen tarih, oluşturulacak ihracat faturasının tarihi olarak kullanılır. |
| Fiili Kur | Fiili ihracat tarihindeki kur (kayıtlı ise) program tarafından otomatik olarak ekrana getirilir. Hesaplamalarda kullanılacak olan kur, istendiği zaman değiştirilebilir. İrsaliyede girilen döviz tutarı bu kur ile çarpılarak TL tutar hesaplanır. |
| İrsaliye No | "İhracat Referans No" alanında girilen referans numarasına ait irsaliye numarası program tarafından otomatik olarak ekrana getirilir. Kullanıcı müdahale edemez. |
| Cari Kodu | "İhracat Referans No" alanında girilen referans numarasına ait irsaliyenin kesildiği cari kod program tarafından otomatik olarak ekrana getirilir. Kullanıcı müdahale edemez. |
| İrsaliye Tutarı | "İhracat Referans No" alanında girilen referans numarasına sahip irsaliyenin döviz tutarı toplamını gösteren alandır. |
| Navlun Tutarı | Navlun tutarı, sadece ithalat/ihracat tipi CIF olarak kesilen irsaliyeler için sorgulanır. Diğer tiplerde kesilen irsaliyelerde bu alana erişilmez. İlgili ihracat için karşılanan bir navlun tutarı varsa ve bu tutarın ihracat faturasında izlenmesi isteniyorsa, navlun tutarının girilmesi gerekir. |
| Navlun Muhasebe Kodu | CIF tipiyle kesilen irsaliyelerde navlun tutarının muhasebeye aktarılması istendiğinde, ilgili muhasebe kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodları arasından seçim yapılır. |
| Navlun Eklensin | Girilen navlun tutarının cari hareketlere ve muhasebeye aktarılması için kullanılan seçenektir. İşaretlenmediğinde, navlun tutarı sadece bilgi amaçlı olarak ihracat faturalarındaki "Ek Maliyet-1" alanından izlenir. Muhasebeye ve cari hareketlere aktarılmaz. |
| Sigorta Tutarı | Sigorta tutarı sadece ithalat/ihracat tipi CIF olarak kesilen irsaliyeler için sorgulanır. Diğer tiplerde kesilen irsaliyelerde bu alana erişilmez. İlgili ihracat için karşılanan bir sigorta tutarı varsa ve bu tutarın ihracat faturasında izlenmesi isteniyorsa, sigorta tutarının girilmesi gerekir. |
| Sigorta Muhasebe Kodu | CIF tipiyle kesilen irsaliyelerde sigorta tutarının muhasebeye aktarılması istendiğinde, ilgili muhasebe kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodları arasından seçim yapılır. |
| Sigorta Eklensin | Girilen sigorta tutarının cari hareketlere ve muhasebeye aktarılması için kullanılan seçenektir. İşaretlenmediğinde, sigorta tutarı sadece bilgi amaçlı olarak ihracat faturalarındaki "Ek Maliyet-2" alanından izlenir. Muhasebeye ve cari hareketlere aktarılmaz. |
| Fatura No | Kapatılacak ihracat faturasının numarasının program tarafından otomatik aktarıldığı alandır. |
| GÇB No | İhracatın gümrük çıkış beyanname numarasının girildiği alandır. |
| GÇB Tarihi | İhracatın gümrük çıkış beyanname tarihinin girildiği alandır. |
| Entegrasyon Cari Açıklama | Yevmiye fişindeki cari hesap kodunun "Açıklama" alanına aktarılacak bilginin girildiği alandır. |
| Cari Hareket Açıklama | Cari harekete aktarılması istenen açıklamanın girildiği alandır. Otomatik aktarılan açıklama üzerinde değişiklik yapılabilir. |
| Entegrasyon Açıklama | "Entegrasyon Kayıtları" bölümündeki "Yevmiye Açıklama" alanına ve ihracat kapatma işlemi sonucu oluşan dekontun "Açıklama" alanına aktarılacak bilginin girildiği alandır. Otomatik aktarılan açıklama üzerinde değişiklik yapılabilir. |
| Resmi Fatura No | Kapatılacak ihracat için resmi fatura numarasının program tarafından otomatik aktarıldığı alandır. |
| Bedelsiz Kapatma Yapılsın | İhracat kapatma işleminin bedelsiz yapılması istendiğinde kullanılan seçenektir. İşaretlenerek kapatma yapıldığında cari hareketlere ve muhasebeye kayıt aktarılmaması sağlanır. Kapatılan belgenin genel toplamı 0 (sıfır) ve e-Faturası oluşturulmuşsa, bedelsiz kapatma seçeneği program tarafından otomatik olarak işaretli şekilde gelir. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İhracat kapatma işleminin gerçekleştirilmesi için kullanılan butondur. Kapatma işlemi yapılan irsaliye CIF tipinin dışında kesilmişse, ilgili irsaliyede girilen döviz tutarları "Fiili Kur" alanındaki kur ile çarpılarak TL rakam hesaplanır. Hesaplanan rakam, stok hareket ve cari hareket kayıtları ile entegrasyona aktarılır. İrsaliyenin tipi CIF ve navlun ile sigorta tutarları girilmişse, navlun ve sigorta tutarları cari hareketlere aktarılır. Stok harekete aktarılmaz ve entegrasyon kaydı yapılır. Bütün kapatma işlemlerinde, ithalat/ihracat tipi ne olursa olsun kapatma işlemi için "Genel Dekont Kaydı" bölümünde seri numarası IH olan bir dekont oluşur. |
| ![](../../../../../_assets/249197106fa4d90d9fe9.png) Çıkış | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
