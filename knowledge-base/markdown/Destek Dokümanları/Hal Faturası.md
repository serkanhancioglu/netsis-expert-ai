---
title: "Hal Faturası"
page_id: "66250662"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Hal Faturası"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Hal Faturası"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWRlY2U4ZDdmLTgzMzgtNDcyMS04NWM2LTFlZTQ4Y2VmNDAwNyZsaW5rPTk1NDJkYmE4LWY1MjUtNGExNS1iMjM2LWJhMmNjYjJjYjNmOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=dece8d7f-8338-4721-85c6-1ee48cef4007&link=9542dba8-f525-4a15-b236-ba2ccb2cb3f8&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hal-faturasi_80088483_66250662.html"
source_version: "2022-11-02T14:54:40.327+03:00"
source_bytes: 876382
fetched_at: "2026-09-13T04:24:25+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hal Faturası

Hal Faturası ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

5957 sayılı Sebze ve Meyveler ile Yeterli Arz ve Talep Derinliği Bulunan Diğer Malların Ticaretinin Düzenlenmesi Hakkında Kanun hükümlerine göre komisyoncu veya tüccar olarak sebze ve meyve ticaretiyle iştigal eden mükelleflere 1/1/2020 tarihi itibariyle e-Fatura, e-Arşiv Fatura, e-İrsaliye, e-Müstahsil Makbuzu ve e-Defter Uygulamalarına geçiş zorunluluğu getirilmiştir. Bu kapsama "Komisyoncu" ve "Tüccar" olarak tanımlanan mükellefler girmektedir.
**Komisyoncu,** malların toptan satışı amacıyla kendi adına ve başkası hesabına komisyon esası üzerinden çalışan meslek mensuplarına denir.
**Tüccar,** malların toptan satışı amacıyla kendi adına ve hesabına çalışan meslek mensuplarını ifade etmektedir.
Bu kapsamda Netsis' te e-Fatura ve e-Arşiv belgeleri için, 9.0.27 setinden itibaren HKS diğer bir deyişle Hal Fatura senaryolarının desteği getirilmiştir. Hal Faturası uygulamasının kullanılabilmesi için, Alış ve Satış parametrelerinde "**Hal** **Faturası** **Uygulaması**" parametresinin işaretlenmesi gerekmektedir.
![](../_assets/fc2d3dc23e4dce8ec387.png)
Ayrıca Entegrasyon Kodları ekranında Fatura Ek Maliyet sekmesinde Ek Maliyet-3 alanı, hem alış hem de satış tarafı için eklenmiştir. Komisyoncu tipinde kesilen faturalar için girilen masraflar Ek Maliyet-3 alanında gösterilecektir.
![](../_assets/a3f1f5760eca827d4509.png)
Hal Faturası Uygulaması parametresi işaretliyken girilen belgede **Hal Faturası Tipi** alanı aktif gelir. Uygulama kapsamında düzenlenecek e-Fatura ve e-Arşiv Fatura belgeleri için; senaryo "HKS" belgenin tipi mükellefin tipine göre "Komisyoncu" ya da "Satış" olmaktadır. Komisyon tipinde bir hal faturası düzenlenecekse "**Komisyoncu**", satış tipinde bir hal faturası düzenlenecekse "**Satış**" seçeneği seçilmelidir.

Hal Faturası Tipi Komisyoncu seçilmesi durumunda, kalemler sekmesinde kalem bazında 19 haneden oluşan ürüne ait künye bilgisinin girilmesi gerekmektedir.
**Ürün** **künyesi:** Sebze ve meyvelerin perakende olarak satışa sunulduğu yerlerde bulunması zorunlu olan ve tüketicilerimize ürünün tarladan sofraya yolculuğunu gösteren bir kimlik belgesidir. Ürün künyesinde; Hal Kayıt Sistemi künye numarası, ürünün üretim tarihi, üreticinin adı soyadı/ ticaret unvanı, ürünün miktarı, üretim yeri, işletme adı ve perakendecinin ürünü aldığı fiyat yer almaktadır. İthal edilen ürünler için ithalata ilişkin bilgileri bulunmaktadır. Ayrıca, künyeler üzerinde ürüne ilişkin detaylı bilgilere ulaşmayı sağlayan karekodlar yer almaktadır. Toplamlar sekmesinde de e-Fatura Senaryosu "**Hal** **Faturası**" olarak görünmektedir.
![](../_assets/dafb45017c0d35315b1b.png)
![](../_assets/1bace26b0824866cf9d2.png)![](../_assets/691bad96909e4f06ad30.png)
Ayrıca Toplamlar sekmesinde sağ klik menüsünde Hal Faturası Masraf Girişi bulunmaktadır. Hal Faturası Masraf Girişi ekranında Komisyoncu tipli hal faturasına ait masraf kalemlerinin oranları ve bu masraf kalemlerine ait varsa kdv oranları girilmektedir. Bu girilen oranlara göre masraf tutarları hesaplanmaktadır.
![](../_assets/46755487a2ce9506e928.png)![](../_assets/427fc82a58fa8cbffaf5.png)
Masraf girişi sonrasında Tamam a basılarak masraf ekranı kapatılır ve belge tamamlanır. Masraf tutar toplamı Alt Maliyet 3 alanına atılır.
![](../_assets/705b4fc07c056c87d763.png)

Hal Faturası Tipi Satış seçilmesi durumunda, kalemler sekmesinde kalem bazında 19 haneden oluşan ürüne ait künye bilgisi, Mal Sahibi ve Mal Sahibi Vkn/Tckn bilgilerinin girilmesi gerekmektedir.
Toplamlar sekmesinde de e-Fatura Senaryosu "**Hal** **Faturası**" olarak görünmektedir. Ayrıca Toplamlar sekmesinde sağ click menüsünde Hal Faturası Masraf Girişi menüsü gelmez. Satış tipli Hal faturasında masraf girişine gerek yoktur.
![](../_assets/808af469637ab61f612d.png)
![](../_assets/e678b318a2410bbb4667.png)
![](../_assets/27e2086d97a76a0cc01c.png)
![](../_assets/edd04c79ce1e0d14e5fb.png)
