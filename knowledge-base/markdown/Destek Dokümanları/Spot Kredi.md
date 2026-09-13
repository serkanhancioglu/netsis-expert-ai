---
title: "Spot Kredi"
page_id: "90669146"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Spot Kredi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Spot Kredi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWRhZThkY2Y0LTVhZWQtNGJlYy04ODgxLTAxMjcxMWQwNDZkOCZsaW5rPTY5ZDdhNWU3LWJlODktNDhhZC1hMjU0LWNmZjFlYmJlYzBjMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=dae8dcf4-5aed-4bec-8881-012711d046d8&link=69d7a5e7-be89-48ad-a254-cff1ebbec0c3&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "spot-kredi_90670249_90669146.html"
source_version: "2022-11-02T14:15:19.120+03:00"
source_bytes: 773759
fetched_at: "2026-09-13T04:23:55+00:00"
generator: "netsis-scraper 1.0.0"
---
# Spot Kredi

Spot Kredi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Spot krediler, piyasa koşullarındaki gelişmeler göz önüne alınarak kısa ve orta vadeli finansman ihtiyaçlarını karşılamaya yönelik olarak kullandırılan kredilerdir.

Spot kredide anapara ödemesi kredi vadesi sonunda tek seferde ödenir. Bu yüzden spot krediye geri ödeme planı bağlanamaz.

**Spot Kredi Tanımlamaları**

Spot kredi kullanımı için Banka Hesap Kayıtları ekranından Nakit Kredi - Spot ve kredi kullanım anında çalışacak olan Vadesiz Mevduat tipli banka hesapları tanımlanmalıdır.

![](../_assets/8b790e5e82ccc88053b7.png)

**Spot Kredi Açma**

Hesap tanımlama işlemi yapıldıktan sonra kullanılan kredinin kaydı Banka\\İşlemler\\Spot Kredi Açma ekranından yapılır. Burada önemli nokta kredi açılışında kullanılacak Nakit Kredi – Spot tipli banka hesabının bakiye vermemesidir. Bir banka bir kredi açılışında kullanıldıktan sonra faiz işleme kapatma ile kapatılana kadar farklı bir kredi açılışında kullanılmaz.

Aşağıdaki ekran görüntüsünde 01.08.2022 tarihinde 30.09.2022 vadeli 2,5 faiz oranı ile 50.000 TL'lik kredi açılış işlemi yapılmıştır.

Faize vergi dahil parametresi, girilen oran üzerinden hesaplanan faizin içerisinde BSMV,KKDF vergilerine ait tutarında olduğunu belirtmek için kullanılır. İşaretlenmediği durumda BSMV ve KKDF banka parametrelerinde belirlenen oranlar üzerinden ayrıca hesaplanır.

Bu bilgiler ile hesap açılış işlemi F5 ya da kaydet butonu aracılığı ile tamamlanır.

![](../_assets/210ca7b9543c865159c5.png)

Hesap açılış işlemi sonrasında banka hareketleri ve işleme bağlı yevmiye fişi aşağıdaki gibi olur.

![](../_assets/537183b1b36b762071aa.png)

Çekilen krediye ait bilgiler, hesaplanan faiz Spot Kredi/ Vadeli – Repo Hesapları Dökümü raporundan izlenir.

![](../_assets/018549f26218ed56cc58.png)

Not: Dönemsellik ilkesi gereği spot kredilerde faiz tahakkuk işlemi yapılır. Kredinin vadesi gelmese de faiz giderinin tahakkuk edilmesi gerekir. Bu işlem için [Netsis Faiz Tahakkuk Mahsubu](<Netsis Faiz Tahakkuk Mahsubu.md>) dokümanından faydalanabilirsiniz.

Hesap açılış işlemi sonrasında girilen faiz oranı değiştirilmek istenirse Spot Kredi Açma ekranında gridde bulunan kaydın üzerinde sağ klik Spot Kredi Faiz Değişikliği işlemi kullanılır.

Eğer açılan kredi herhangi bir işlem görmeden iptal edilmek istenirse yine Spot Kredi Açma ekranında gridde bulunan kaydın üzerinde sağ klik yapılır ve Kaydı İptal Et işlemi çalıştırılır.

**Faiz İşleme Kapatma**

Kredinin vadesi geldiğinde faiz ve ana para ödemesi Banka\\İşlemler\\Faiz İşleme-Kapatma ekranından yapılır. Ön sorgulamadan kredi hesabı seçilip Faiz Bilgileri sayfasına geçildiğinde krediye ait ana para, faiz oranı, kredi vadesi gibi bilgiler otomatik olarak getirilir. Faiz Hesapla butonuna basıldığında faiz tutarı hesaplanır ve ana para + faiz olarak vadesiz mevduat hesabına alacak, kredi hesabına borç olarak aktarılır.

![](../_assets/37fb79d9adeb95d829e7.png)

Faiz İşleme/Kapatma işlemi sonrasında banka hareketleri ve işleme bağlı yevmiye fişi aşağıdaki gibi olur.

![](../_assets/d50f508529a545133649.png)![](../_assets/0549da6b38a555613bc7.png)

İşlemin sonucunda spot hesabın bakiyesi sıfırlanır. Yeni kredi işlemlerinde kullanılabilir hale gelir.

**Faiz Hesaplama**

Repo hesaplar aylık, haftalık, günlük olarak açılabilir. Burada faiz hesaplaması açılış ve kapanış tarihleri üzerinden yapılır. Örneğimizde açılış 01.08.2022 ile kapanış 30.09.2022 tarihleri arasındaki 60 gün üzerinden 208,33 TL faiz hesaplanmıştır.

Ana Para:50000 Faiz Oranı:2,5

Kapanışa kadar geçen süre: 60 gün

(50.000\*2,5\*60)/36000= 208,33 TL
