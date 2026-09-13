---
title: "Fiş Oluşturma"
page_id: "22803962"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "Fiş Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / Fiş Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk5MjRhOTZkLWQ2YmEtNGVjMy05ZGZjLTA2OGU3N2Y1YTgyMiZsaW5rPTBmODUzN2RjLWFkNGQtNDNhNi05ODU3LWY1YjBjZGU3ZWM5ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9924a96d-d6ba-4ec3-9dfc-068e77f5a822&link=0f8537dc-ad4d-43a6-9857-f5b0cde7ec9e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "fis-olusturma_22804977_22803962.html"
source_version: "2022-10-24T11:37:46.240+03:00"
source_bytes: 36058
fetched_at: "2026-09-13T04:01:47+00:00"
generator: "netsis-scraper 1.0.0"
---
# Fiş Oluşturma

Fiş Oluşturma, oluşturulan yükleme emirlerinden irsaliye ya da fatura kaydı oluşturulması için kullanılan bölümdür. Fiş Oluşturma; Ön Sorgu ve Yükleme Emri Listesi sekmelerinden oluşur.

**Ön Sorgu**

Seçilen yükleme emirleri satış irsaliyeleri/faturaları oluşturulurken Ön Sorgu sekmesindeki kısıtlar dikkate alınır.

Fiş Oluşturma ekranı Ön Sorgu sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yükleme Emirlerinden Fiş Oluşturma Ekranı |  |
| --- | --- |
| Tarih | İrsaliye/fatura kaydı oluşturulacak yükleme emri tarihinin girildiği alandır. Verilen tarih aralığındaki yükleme emirleri için irsaliye/fatura kayıtları oluşturulur. |
| Yükleme Emri No | İrsaliye/fatura kaydı oluşturulacak yükleme emri numarasının girildiği alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber tuşu yardımı ile girilen numara aralığındaki yükleme emirleri için, irsaliye/fatura kayıtları oluşturulur. |
| Cari Kodu | İrsaliye/fatura kaydı oluşturulacak yükleme emirleri için cari kod kısıdı verilmesi istendiğinde kullanılan alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber tuşu yardımı ile herhangi bir cari kod aralığı girildiğinde, bu kod aralığındaki yükleme emirleri için irsaliye/fatura kayıtları oluşturulmuş olur. |
| Kamyon No | Girilen kamyon numaralarına göre yükleme emirlerinin listelenmesi için kullanılan alandır.![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber tuşu yardımı ile herhangi bir kamyon numarası aralığı girildiğinde, bu kamyon numaraları ile kaydedilmiş yükleme emirleri için irsaliyeler/faturalar oluşturulur. |
| Kod-1/Kod-2 | Kod-1/ Kod-2 bilgilerine göre yükleme emirlerinin listelenmesi için kullanılan alandır. |
| Açıklama 1, 2, 3 | Açıklama 1, 2, 3 bilgilerine göre yükleme emirlerinin listelenebilmesi için kullanılan alanlardır. |
| ![](../../../../_assets/e1aa2732c9793caadbb8.jpg) İleri Butonu | Ön sorgulama bilgilerinin girilmesinden sonra, bu bilgilere uygun yükleme emirlerinin listelendiği ekrana geçilmesini sağlayan butondur. |

**Yükleme Emri Listesi**

Yükleme emirlerinden fiş oluştururken, yükleme emri listesi ekranındaki alanlara verilen kısıtlar dikkate alınır.

Fiş Oluşturma ekranı Yükleme Emri Listesi sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yükleme Emirlerinden Fiş Oluşturma Ekranı |  |
| --- | --- |
| Belge Tipi | Yükleme emrinden oluşturulacak fişin irsaliye mi yoksa fatura mı olduğunun belirlendiği alandır. Aşağı ok tuşu ile seçim yapılabilir. |
| Fiş No | Oluşacak belge için başlangıç numarasıdır. Kayıtlı olan son belge numarasından bir büyüğü, program tarafından otomatik getirilir, istendiğinde değiştirilebilir. |
| Fiş Tarihi | Oluşacak belgelerin tarihidir. Günün tarihi program tarafından otomatik getirilir, istendiğinde değiştirilebilir. |
| Entegre Tarihi | Belge tipinin fatura seçilmesi halinde aktif olan alandır. Burada girilecek tarih faturanın muhasebeye işlenme tarihi olup, Stok, Cari, Kasa Hareket Kayıt Tarihi, Fatura Tarihi olacaktır. Programın muhasebe ile entegre kullanıldığı durumlarda entegre kayıt tarihi, fatura kayıt ekranlarında otomatik olarak gelir. Program, entegre kayıt tarihi olarak bilgisayardaki tarihi getirir, kullanıcı tarafından değiştirilebilir. |
| Açıklama | Oluşturulacak belge için açıklama bilgisinin girildiği alandır. |
| Referans Kodu | Referans uygulamasının kullanıldığı durumlarda aktif olan alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber tuşu yardımı ile kod seçimi yapılabilir. |
| Konteyner No | Konteyner numarasının bilgi amaçlı girildiği alandır. |
| Ödeme Kodu | Tanımlaması yapılan ödeme kodlarından birinin, ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber tuşu yardımı ile girildiği alandır. |
| Lokal Depo | Oluşturulacak belgenin, lokal depo uygulamasına göre listelenmesi isteniyorsa işaretlenir. |
| Giden Depo | Sevkiyatın yapılacağı depo bilgisinin girildiği alandır. |
| Ambar | Oluşturulacak belge için ambar bilgisinin girildiği alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber tuşu yardımı ile ambar seçimi yapılabilir. |
| Cari Kodu | Bu alana Cari Modül/Cari Sabit Kayıtlarındaki satış noktasının (müşterilerinin) tanımlanmış cari kodu girilmelidir. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber tuşu yardımı ile cari kod seçilebilir. |
| Giriş Depo Kodu | Oluşturulacak belge için, ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber tuşu yardımı ile giriş depo kodunun seçildiği alandır. |
| Basım Yapılsın Mı? | Oluşan belgelerin basımı yapılacak ise işaretlenecek seçenektir. |
| Oluşturulacak Fişlerde Cari Karttaki Koşul Bilgisi Alınsın | Oluşturulacak belge için koşul kodu alanına, cari kartta bulunan koşul kodunun program tarafından otomatik aktarılması için kullanılan seçenektir. |
| Koşul Koduna Göre Ayrı Fişler Oluşturulsun | Koşul kodu farklı olan fişler için ayrı fişler oluşturulması istendiğinde işaretlenecek seçenektir. |
| Açıklamaya Göre Ayrı Fişler Oluşturulsun | Açıklama alanı farklı olan fişler için ayrı fişler oluşturulması istendiğinde işaretlenecek seçenektir. |
| Yükleme Numarasına Göre Ayrı Fişler Oluşturulsun | Yükleme numarası farklı olan fişler için ayrı ayrı fişler oluşturulması istendiğinde işaretlenecek seçenektir. |
| Fiş Oluşturulduktan Sonra Belge Açılsın | Yükleme fişi oluşturulduktan sonra belge açılması istendiğinde işaretlenecek seçenektir. |
| Kalem Sayısına Göre Fişler Oluşturulsun | Maksimum kalem sayısı alanında belirlenen kalem miktarına göre, ayrı fişler oluşması istendiğinde işaretlenecek seçenektir. |
| Maksimum Kalem Sayısı | Yükleme emrinden oluşturulan fişlerin içinde bulunacak maksimum kalem sayısının belirlendiği alandır. Maksimum kalem sayısı aşıldığında yeni bir belge oluşur. |
| Sipariş Numarasına Göre Fiş Oluşturulsun | Sipariş Numarasına göre yükleme fişi oluşturulması istendiğinde işaretlenecek seçenektir. |
| Tevkifat Hesaplansın | Yükleme emrinden fiş oluştururken, tevkifat hesaplamasının da yapılması istendiğinde işaretlenecek seçenektir. |
| Proje Koduna Göre Ayrı Fişler Oluşturulsun | Proje kodu farklı olan fişler için ayrı fişler oluşturulması istendiğinde işaretlenecek seçenektir. |
| İşlem Tamamlandıktan Sonra Fiş Oluşturma Ekranı Kapanmasın | İşlemler bittikten sonra fiş oluşturma ekranının kapanmaması istendiğinde işaretlenecek seçenektir. |
| ![](../../../../_assets/67af647263b81e237bf2.jpg) Hepsi Butonu | Ön sorgulamada girilen bilgiler doğrultusunda, listelenen yükleme emirlerinin hepsinin işaretlenmesi için kullanılan butondur. Bu buton kullanıldığında, bütün yükleme emirleri için irsaliye ya da fatura oluşturulacağı düşünülerek seçeneklerin hepsi işaretlenmiş olur. |
| ![](../../../../_assets/980037b21af0a20ddfd0.jpg) Fiş Oluştur Butonu | Seçilen yükleme emirlerinin irsaliye ya da fatura kayıtlarının oluşması için kullanılan butondur. Bu butonun aktif olması için en az bir yükleme emrinin seçili olması gerekir. Oluşan irsaliyeler "Satış İrsaliyesi" bölümünden, faturalar ise "Satış Faturası" bölümünden izlenebilir. |
| e-İrsaliye Oluşturulsun | Yükleme emirlerinden e-İrsaliye oluşturulması için kullanılan seçenektir. |
| e-İrsaliye Ek Bilgi Girişi | "e-İrsaliye Oluşturulsun" seçeneği işaretlendiğinde, "e-İrsaliye Ek Bilgi Girişi" yazısının üzerine tıklanarak "e-İrsaliye Ek Bilgi Girişi" ekranına ulaşılır. Bu ekrandan gerekli tanımlamaların yapılması durumunda, grid ekranda oluşan tüm belgelere ek bilginin kaydedilmesi sağlanır. |
