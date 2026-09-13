---
title: "Netsis Faiz Tahakkuk Mahsubu"
page_id: "66238128"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Faiz Tahakkuk Mahsubu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Faiz Tahakkuk Mahsubu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA0MWMwMTJiLTdmMzgtNDFmOS1iYjBmLTM5YmNiNzY4MTVkMyZsaW5rPThhNjE4MTkwLTkxMmUtNGE0Ny05ODY0LTZhMjY1ZGZhYzk5OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=041c012b-7f38-41f9-bb0f-39bcb76815d3&link=8a618190-912e-4a47-9864-6a265dfac998&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-faiz-tahakkuk-mahsubu_66238130_66238128.html"
source_version: "2022-11-02T15:08:10.883+03:00"
source_bytes: 1427578
fetched_at: "2026-09-13T04:24:34+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Faiz Tahakkuk Mahsubu

Netsis Faiz Tahakkuk Mahsubu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Faiz Tahakkuk Mahsubu

Gelir ve kurumlar vergisi mükelleflerinin beyan etmeleri gereken vergi matrahlarını doğru hesaplayabilmeleri için, dönem sonu işlemleri geçici vergi uygulaması nedeniyle takvim yılının üçer aylık döneminde yapılmaktadır. Faiz tahakkuk mahsubu oluşturulması bir dönem sonu işlemidir. Bankalardaki faiz söz konusu hesapların, dönem sonu itibariyle hesaplanan faiz tutarlarının tahakkuk esasında gelir/gider kaydı atılması işlemine faiz tahakkuk işlemi denir. Vadeli hesap gibi faiz geliri olan ya da kredi hesapları gibi faiz gideri olan tüm hesaplar faiz tahakkuk işlemine tabidir.
Faiz Tahakkuk Mahsubu uygulaması vadeli bir hesap (gelir kaydı) üzerinden anlatılacaktır.

#### Faiz Tahakkuk Mahsubu

Faiz tahakkuk işlemi ile, dönem sonunda tahsil edilmeyen ancak biriken faiz beyan edilmek üzere gelir olarak işlenmektedir.
Kredi hesaplarında faiz bir gider olduğu için faiz tahakkuk işlemi sonrasında bağlı hesaplara gider kaydı atılacaktır.
![](../_assets/48fc88872b8a09c0b2bd.png)
Yıl/Ay Kodu alanından girilen yıl/ay bilgisine göre vadesi geçmemiş hesaplar için yine girilen ayın son günü baz alınarak faiz hesaplanmaktadır.
Detaylı/Kümüle seçeneğinde, birden fazla bankaya ait faiz tahakkuk kaydının oluşması durumunda hareketlerin muhasebeye banka bazında detaylı ya da banka ayırmadan kümüle olarak aktarımı sağlanabilmektedir.
Banka Hesap Kayıtlarındaki Muhasebe Hesap kodları Kullanılsın parametresi ile, banka bazında faiz tahakkuk muhasebe kodu belirlenebilmektedir. Banka Hesap Kayıtlarındaki Muhasebe Hesap kodları Kullanılsın parametresi işaretlendiğinde banka tanımlarından alınan hesaplar kullanılacaktır.
Banka Hesap Kayıtlarındaki Muhasebe Hesap kodları Kullanılsın parametresi işaretlenmezse tahakkuk işlemi esnasında Faiz Muhasebe Kodu ve Tahakkuk Muhasebe Kodu alanlarında seçilen hesaplar kullanılmaktadır.
İşlem sonunda, hesaplanan faiz tutarı kadar faiz muhasebe koduna borç, tahakkuk muhasebe koduna alacak hareketinin atıldığı bir yevmiye fişi oluşmaktadır.

Kredi gibi gider kaydı olan işlemlerde faiz tutarı faiz muhasebe koduna alacak, tahakkuk muhasebe koduna borç hareketi atılmaktadır.
Örnek: Vadesiz bir mevduat hesabından 17.03.2021 tarihinde 10.000TL çekilip %4 faiz ile 1 ay vadeli bir vadeli mevduat hesabına aktarılmıştır. Mart sonunda faiz tahakkuk işlemi yapılacaktır.

#### Vadeli Mevduat Hesabı Tanımlama

Vadeli Mevduat Hesabı Tanımlama için örnek olarak, V1 kodu ile Hesap Tipi vadeli mevduat olan bir hesap açılmıştır. Vadeli hesaptan faiz geliri elde edileceği için faiz muhasebe koduna 642 faiz gelirleri, faiz tahakkuk muhasebe koduna ise 181 gelecek aylara ait gelir hesabı bağlanmıştır.
![](../_assets/d8184946298b68fe6cf7.png)

#### Repo/Vadeli Hesap Açma

Örnek vadeli hesap açma işlemi ile, 0046-VDSZ hesap kodlu vadesiz hesaptan 10.000TL çekilip, V1 kodlu vadeli hesaba %4 faiz ile 17.03/17.04 tarihleri arasında işlem görecek şekilde aktarılmış olacaktır. Bu işlemin sonunda V1 kodlu bankaya ve bağlı bulunduğu muhasebe koduna 10.000TL borç, 0046-VDSZ kodlu bankaya ve bağlı bulunduğu hesaba 10.000TL alacak hareketi atılacak ve vadeli mevduat hesabı açılmış olacaktır.
![](../_assets/a38db3586e96af711265.png)
![](../_assets/3da2436d49f3a3a1fff1.png)

#### Faiz Tahakkuk Mahsubu

Faiz Tahakkuk Mahsubuna örnek olarak, 31.03.2021 tarihinde bu vadeli hesap için biriken ancak tahsil edilmeyen faizin hesaplanması ve gelecek aylarda tahsil edilecek faiz geliri olarak işlenmesi için faiz tahakkuk mahsubu oluşturulacaktır.
![](../_assets/d4d8effcbac5b55c24e4.png)

İşlem sonrasında 17.03/31.03 tarihleri arası için 14 günlük biriken faiz, banka kartındaki faiz tahakkuk hesabına banka bazında detaylı olarak aktarılacaktır. Bu işlem sonrasında sadece yevmiye fişi oluşacak, banka hareketlerinde herhangi bir kayıt oluşmayacaktır.

Yatan tutar : 10.000 Faiz: %4

31.03/17.03 arası geçen gün:14

Faiz gelir kaydı 10000\*4\*14(gün)/36000 = 15,56

![](../_assets/0839f80460e316f0e018.png)

#### Faiz İşleme/Kapatma

Hesabın vadesi geldiğinde yapılacak işlem faiz işleme kapatmadır.
![](../_assets/eab7e4e8ee2504a61475.png)
Faiz İşleme/Kapatma işlemi ile vadeli hesaba faiz girişi gerçekleşecek ve sonrasında ana para ve elde edilen toplam faiz hesaptan alınıp vadesiz hesaba aktarılacaktır.

Oluşan banka hareketleri aşağıdaki gibi olacaktır:
![](../_assets/d178dbc0d141de7af494.png)![](../_assets/8979d5cee5d50c271603.png)

- 102 BANKALAR10034,44 (vadesiz)
102 BANKALAR10034,44 (vadeli)
102 BANKALAR34,44 (vadeli)
181 GEL.TAHAKK. 15,56
642 FAİZ GEL.18,88
Aylık Toplam Faiz10.000\*4\*31/36.000=34,44 Önceki Dönem Gelir Tahakkuku( - )=15,56
Dönem Faiz Geliri= 18,88
