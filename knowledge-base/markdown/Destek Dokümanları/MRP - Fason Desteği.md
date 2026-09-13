---
title: "MRP - Fason Desteği"
page_id: "50669180"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "MRP - Fason Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / MRP - Fason Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWYwMWIzNzkzLTllMzctNDYxZi1hNmQ1LWI5YmQ4NjdhZWE5NSZsaW5rPWFhZmMwYTM5LWVkNjktNDIwZS04MjNlLWI3Y2FjZWQ2Y2E2MSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f01b3793-9e37-461f-a6d5-b9bd867aea95&link=aafc0a39-ed69-420e-823e-b7caced6ca61&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mrp-fason-destegi_50669182_50669180.html"
source_version: "2022-12-19T09:55:06.267+03:00"
source_bytes: 40860
fetched_at: "2026-09-13T04:25:32+00:00"
generator: "netsis-scraper 1.0.0"
---
# MRP - Fason Desteği

MRP-Fason Desteği ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Üretimin belli aşamalarının tamamının ya da bir kısmının firma dışında yaptırıldığı durumlarda Fason Uygulaması kullanılır. MRP'de fason üretilecek yarı mamulün malzemeleri planlanabilir ve tedariği yapılabilir.

Bazı firmalar fasona bu bileşenleri irsaliye ile iletir ve yine yarı mamul girişini irsaliye olarak yapar. Bu tür çalışmada bileşenler ya da yarı mamul faturalandırılmaz ve sisteme sadece işçilik faturası kaydedilir. Malzeme stok hareketleri ise, DAT ile bileşenlerin fason depoya çıkılması, ÜSK ile fason depodaki bileşenlerin sarfı ve yarı mamulün stoklara girişi şeklinde sağlanır. Diğer bir çalışma şekli ise, bileşenlerin fason firmaya faturalandırılması ve yarı mamulün fatura karşılığı fason firmadan satın alınması şeklinde olur. Müşteri/Satıcı Planlama Kayıtlarında sipariş oranı verilen yarı mamullerin, verilen oranda ilgili satıcıda ürettireceği - geri kalanı firmada üretilir - varsayılır. Bir yarı mamul için toplamı 100'ü geçmeyecek şekilde birden fazla satıcı kartına sipariş oranı girilebilir. Bu durumda birden fazla tedarik sağlayan firmada, istenen oranlarda üretileceği varsayılır.
Fason bileşenler için Müşteri-Satıcı Stok Kayıtları ekranına "Fason Seçimi" alanı eklendi.

Fason Seçimi alanında iki adet seçenek sunulur; İş Emri Açılsın ve Sipariş Açılsın

MRP sonuçlarından yarı mamul ihtiyaçları, belirtilen oranlarda ilgili satıcılara Satıcı Siparişi ya da İş Emri olarak oluşturulur. Satıcı Siparişi oluşturulduğu zaman; malzemelerin fason firmaya faturalanacağı ve yarı mamulün üretildikten sonra, oluşturulan bu siparişe istinaden irsaliye/fatura ile teslim alınacağı varsayılır. İş Emrinin oluşturulduğu zaman; doğru fason deposunda oluşturulması için, Lokal Depo Tanımlamaları ekranındaki cari kodun, satıcının cari kodu olmasına dikkat edilmesi gerekir. Satıcı cari kodundan ilgili lokal depo bulunur ve iş emri bu depoda oluşturulur. Malzemelerin bu lokal depoya DAT - irsaliye - ile transfer edilmesi gerekir. Yarı mamul üretildiğinde, fason depoda bu iş emrine istinaden ÜSK yapılması gerekir. ÜSK sırasında mamul giriş deposu olarak, firmanın kendi depolarından biri seçilebilir.

![](../_assets/edc672734822a95233b9.png)

> [!NOTE]
> Fason Uygulaması'nın kullanılması için MRP Parametreleri-"Sipariş Bazında Rezervasyon Sistemi" parametresinin seçilmesi gerekir.
