---
title: "Yatırım Girişi"
page_id: "50683420"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Demirbaş"
  - "Kayıt / Demirbaş"
  - "Yatırım Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Demirbaş / Kayıt / Demirbaş / Yatırım Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUyNzQyOGVjLTk1OWEtNDM4YS1iMjJhLTY3ZmM5MzY2NTIxNiZsaW5rPTZiMjQ1M2MxLTM5YjAtNDQ5OC04YjY5LWFlMzUzYzE3ZWQwZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=527428ec-959a-438a-b22a-67fc93665216&link=6b2453c1-39b0-4498-8b69-ae353c17ed0d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yatirim-girisi_50683422_50683420.html"
source_version: "2022-09-23T14:01:01.800+03:00"
source_bytes: 17470
fetched_at: "2026-09-13T04:21:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yatırım Girişi

Yatırım Girişi, firmaların, belli bir yatırımı gerçekleştirmek için ithal ettikleri veya yurtiçinden temin ettikleri malzemeleri, yatırımın tamamlanıp aktife atılacağı süreye kadar kaydetmelerini sağlayan bölümdür.

**Örneğin,** üretim yapan bir firmanın, yeni bir üretim hattı kurmayı planladığında, bu hatta kullanılması için bazı makinelere ihtiyacı vardır. Bu makinelerin yapımı için gerekli parçaları tek tek; ya ithal ederek ya da yurtiçinden temin ettiği için, makinelerin tamamlanmasından sonra demirbaşların aktife geçirilmesi gerekir. Bu yüzden, yatırım bilgilerinin girilmesinde "Yatırım Girişi" bölümü kullanılır. Yatırımın tamamlanmasından sonra Demirbaş Bilgi Kartı bölümünden, ilgili demirbaşların aktife geçirilmesi sağlanır. Bu işlemle aktife aktarılan demirbaşlarla ilgili yatırım bilgilerindeki “Aktife Atıldı” alanı program tarafından otomatik olarak işaretlenir.

Yatırım girişlerinin yapılacağı demirbaş kartının önceden açılmış olması gerekir. Yatırım Girişi ekranı; Yatırım Bilgileri ve Yatırım Ek Bilgileri sekmesinden oluşur.

**Yatırım Bilgileri**

Yatırım Girişi ekranı Yatırım Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yatırım Girişi Ekranı |  |
| --- | --- |
| Sıra No | Kaydedilecek yatırım için sıra numarası belirlenen alandır. Her kayıt için bir sıra numarası verilmesi gerekir. |
| Proje No | Yapılan proje veya yatırım için belirlenen numaradır. Farklı sıra numaralarında fakat aynı projeye ait birçok demirbaş kodu kaydı yapılabilir. |
| Demirbaş Kodu | İlgili proje veya yatırım için alınan demirbaş kodunun girildiği alandır. Demirbaş henüz aktife alınmadığı için Demirbaş Bilgi Kartı bölümünden bu kodun tanımlanması gerekmez. Aktife alınma işlemi sırasında, istenirse, girilen Demirbaş kodları kullanılarak demirbaş kayıtları yapılabilir. Boş bırakılmaz. Alanın sağ tarafında yer alan boşluğa Demirbaş Adı girilir. |
| Fatura No | Alınan demirbaş fatura numarasının girildiği alandır. |
| Fatura Tarihi | Alınan demirbaşın fatura tarihinin girildiği alandır. |
| Döviz Tipi | Demirbaşın alındığı döviz cinsinin belirlendiği alandır. |
| Döviz Tutar | Demirbaşın alış döviz tutarının girildiği alandır. |
| Fatura Tutarı | Alınan demirbaşın TL. cinsinden fatura tutarının girildiği alandır. Boş bırakılmaz. Aktife alma işlemi sırasında girilen tutarlar kullanılır. |
| KDV Tutarı | Alınan demirbaşın KDV tutarının girildiği alandır. Boş bırakılabilir. |
| Miktar | Kaydedilen demirbaş için alış miktarı girilen alandır. Bu alana 1'den büyük bir değer girildiğinde; aktife alma işlemi sırasında, istenirse ilgili projeye ait tutarlar miktara göre oranlanarak, miktar kadar demirbaş kartı oluşturulabilir. İlgili projeye ait herhangi bir masraf kaydının yapılması istenmediğinde ise, alanın 0 (Sıfır) olarak bırakılması gerekir. Program, aktife alma işlemi sırasında, miktarı 0 (Sıfır) olan kayıtların maliyet katkısı olduğunu anlar ve bu kayıtlardaki tutarları, girilen Demirbaş Kodu tutarına ekler. |
| Satıcı Kodu | Demirbaşın alındığı satıcı kodunun girildiği alandır. |
| Aktife Atıldı | Demirbaş aktife atılmışsa işaretlenmesi gereken seçenektir. |
| Aktife Atım Tarihi | Demirbaşın aktife atıldığı tarihin girildiği alandır. |
| Detay Kodu | Demirbaş Bilgi Kartı bölümünde sorgulanan ve demirbaş entegrasyonunda baz alınan Detay Kodu alanı, projedeki demirbaşlar aktife alındığında ilgili alana aktarılır. Boş bırakılabilir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, detay kodlarına ulaşılır. |
| Masraf Kodu | Demirbaş masraf kodunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodlarına ulaşılır. |
| Grup Kodu | Demirbaş Bilgi Kartı bölümünde sorgulanan ve rapor amacıyla kullanılan Grup Kodu alanı, projedeki demirbaşlar aktife alındığında ilgili alana aktarılır. |
| Rapor Kodu-1 Rapor Kodu-2 Rapor Kodu-3 | Demirbaş Bilgi Kartı bölümünde sorgulanan ve rapor amacıyla kullanılan bu alanlar, projedeki demirbaşlar aktife alındığında ilgili alanlara aktarılır. |
| Proje Kodu | Demirbaş için proje kodu girilen alandır. |
| Düzeltme Tipi | Demirbaş düzeltme tipi girilen alandır. |
| Devir Düzeltme Tutarı | Demirbaş devir düzeltme tutarının girildiği alandır. |

**Yatırım Ek Bilgileri**

Yatırım Girişi ekranı Yatırım Ek Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yatırım Girişi Ekranı |  |
| --- | --- |
| Sıra No | Yatırım Bilgileri sekmesindeki sıra numarasının izlendiği alandır. |
| İngilizce İsmi | Kaydedilen demirbaşın varsa İngilizce isminin girildiği alandır. |
| Muhasebe Kodu | Aktarım yapılacak muhasebe kodunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodlarına ulaşılır. |
| Ek Rapor Kodu-1,2,3,4,5,6,7,8 | Rapor amaçlı olarak bilgi girilen alanlardır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yatırım Girişi kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
