---
title: "Netsis Vadeli Hesap Para Çekme"
page_id: "66256031"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Vadeli Hesap Para Çekme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Vadeli Hesap Para Çekme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc1OTI2NDRiLTM0Y2UtNDhmOC04OWI0LWE2NTIwM2ZlNWI5YyZsaW5rPTE5OTc0NmRmLTBmZTctNDM0MC1iM2U1LWE2MTRmNDNkNGI5OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7592644b-34ce-48f8-89b4-a65203fe5b9c&link=199746df-0fe7-4340-b3e5-a614f43d4b99&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-vadeli-hesap-para-cekme_80088236_66256031.html"
source_version: "2022-11-02T14:51:54.063+03:00"
source_bytes: 1102703
fetched_at: "2026-09-13T04:24:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Vadeli Hesap Para Çekme

Netsis Vadeli Hesap Para Çekme ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Vadeli mevduat hesapları; anında nakit paraya dönüştürülemeyen, bankadan çekilmesi için belirli bir zamanın dolması gerektiği, bu süre dolunca faiz getirisiyle birlikte çekilebilen ya da başka bir vadeye yatırılan hesap türüdür. Ancak günümüz şartlarında birçok banka vadeli hesaplardan vade bozulmadan para çekilebilmesini sağlamıştır. Netsis üzerinde ara dönemde para çekilebilecek vadeli hesaplar açılırken, Repo/Vadeli Hesap Açma ekranında "Vadesinden önce çekilebilir" parametresinin işaretli olması gerekir.

İşlem, aşağıdaki örnek senaryo üzerinden detaylı aktarılacaktır:

**Örnek:** 7 ay vadeli 40.000 TL'lik bir vadeli mevduat hesabı 2,06 faiz oranı ile ve vadesinden önce çekilebilir şekilde tanımlanmalı. 3. Ay sonunda faiz tahakkuk işlemi yapılıp, 9. ayda bu hesaptan 8.000 TL çekilmelidir. Vadesi geldiğinde kalan para üzerinden faiz işleme kapatma ile hesap kapatılmalıdır.

#### Adımlar

##### Vadeli Hesap Açma

Vadeli ve vadesiz hesaplar tanımlanıp Banka Hesap Bilgi-2 sayfasından muhasebe hesapları belirtilmiştir. Repo/Vadeli Hesap Açma ekranından 7 ay vadeli, 2,06 faiz oranı ile 40.000 TL'lik hesap "Vadesinden Önce Çekilebilir" parametresi ile açılmıştır.

![](../_assets/ca47305cc8226d42811e.png)![](../_assets/b6de6a4e08eefa10fec4.png)

İşlem sonunda vadesiz mevduat hesabından çıkan para, vadeli mevduat hesabına aktarılır. İşleme ait yevmiye fişi aşağıdaki gibi olur.

![](../_assets/b03a5759cf97ab9ec8c0.png)

##### Faiz Tahakkuk Kaydı

Geçici vergi dönemlerinde doğru beyan verebilmek adına hakedilen faizlere ait tahakkuk kaydı atılır. Bu örnekte de 8. ayın sonunda faiz tahakkuk işlemi çalıştırılarak 6,7 ve 8. aylara ait faiz geliri tahakkuk kaydı atılmıştır.

![](../_assets/7f6907f0813cad0a97b2.png)

Bu işlem ile banka hesap kartında tanımlanmış olan faiz muhasebe kodu ve faiz tahakkuk kodu kullanılarak ana para tutarının 3 aylık faiz getirisi tahakkuk edilmiştir.

Not: Faiz tahakkuk işlemi ve hesaplama detayı farklı bir dokümanda detaylı olarak anlatılmıştır. İncelemek için [tıklayınız](<Netsis Faiz Tahakkuk Mahsubu.md>).

![](../_assets/d45a728e2d585929361d.png)

Hesaplanan faiz tutarı= (40000\*2,06\*91)/36000=208,29TL

##### Vadeli Hesap Para Çekme

Bu ekran aracılığı ile vadeli hesaplardan para çekme işlemi gerçekleştirilir. Burada önemli nokta faiz tahakkukudur. Eğer örnekteki gibi vadeli hesaptan para çekilmeden önce bir faiz tahakkuku yapıldı ise para çekme işleminde bu tahakkuk kaydının çekilen tutara karşılık gelen kısmı program tarafından ters kayıt ile geri döndürülür.

![](../_assets/6e844bf1a11a087ab2ce.png)

Yukarıdaki işlem ile 01.09 tarihinde ilgili vadeli hesaptan 8000 TL çekilmiştir. Burada faiz tahakkuk ve faiz muhasebe kodu alanları, bu hesap için para çekilen tarihten önce bir tahakkuk çalıştırıldığı için aktif gelir. Herhangi bir tahakkuk kaydı atılmadı ise bu alanlar pasif gelecektir. Buna ek olarak tahakkuk işleminin çalıştırıldığı 31.08 tarihinden öncesi bir tarihe ait para çekme işlemi gerçekleştirilemez. Önce tahakkuk işlemi iptal edilmelidir.

İşlem sonucunda oluşan muhasebe kayıtları ve vadeli/vadesiz banka hareketleri aşağıdaki gibidir.

![](../_assets/69b642d76c38a3e4db10.png)![](../_assets/34aeffbf51c8eff9fff1.png)

8. Ay sonunda yapılan tahakkuk işleminin, çekilen 8.000TL'ye karşılık gelen kısmı ters çevrilmiştir.

İşleme ait yevmiye fişi aşağıdaki gibidir:

![](../_assets/a969fcd42b3d106f0f5c.png)

Tahakkuk kaydı esnasında 3 aylık faiz geliri olarak tahakkuk edilen 208,29TL'nin hesaptan çekilen 8.000 TL'ye karşılık gelen kısmı olan 41,66TL 681-önceki dönemde kar işlenenler hesabına alınmış ve 181-faiz tahakkuk hesabından çıkarılmıştır.

Hesaplanan iade tahakkuk tutarı=(8.000\*2,06\*91)/36000=41,66TL

##### Faiz İşleme Kapatma

Hesabın vadesi geldiğinde yani 7 ayın sonunda faiz işleme kapatma çalıştırılmıştır. Kalan tutarın (ilk yatırılan tutar-toplam çekilen tutar) faiz geliri program tarafından hesaplanır ve faiz geliri alanına yazılır.

![](../_assets/219332ca61db2372cd35.png)

Hesaplanan faiz tutarı=(Anapara kalan tutar\*faiz oranı\*vade(gün))/36000

((40000-8000)\*2,06\*213)/36000 = 390,03 TL

Hesap kapatma yapıldığında vadeli hesaba hesaplanan faiz tutarı kadar giriş ve kalan ana para + faiz tutarı kadar çıkış hareketi atılırken, vadesiz hesaba kalan ana para+ faiz tutarı kadar giriş hareketi atılır.

![](../_assets/d80d1a448047d4ab0788.png)

Bu işleme ait yevmiye fişinde banka hareketlerindeki bu tutarların dışında önceden tahakkuk edilen faiz tutarının da faiz geliri olarak 102 hesaba dönüşü yer alır.

![](../_assets/0a12c85371b1f1208cb4.png)

##### Vadeli Hesap Para Çekme İptali

Bir vadeli hesaba ait para çekme işlemi iptal edilebilir. Burada aranan koşul hesabın kapatılmamış olmasıdır. Vadeli hesap para çekme ekranından ilgili hesap çağılır son para çekme iptali butonu ile iptal işlemi sağlanır. Eğer para çekme işleminde gerçekleştirilmiş bir tahakkuk ters maddesi varsa, para çekme iptali ile o kayıtta silinecektir.

##### Raporlama

Spot Kredi/Vadeli -Repo Hesapların Dökümü raporunda hesaba yatan, çekilen tutarlar ve faiz tutarı izlenebilmektedir.

![](../_assets/af81add1cf0db7baec41.png)![](../_assets/cfd1c05d7e78fb6eb3ca.png)
