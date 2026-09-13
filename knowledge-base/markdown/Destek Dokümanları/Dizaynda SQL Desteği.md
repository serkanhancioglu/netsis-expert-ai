---
title: "Dizaynda SQL Desteği"
page_id: "50689323"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Dizaynda SQL Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Dizaynda SQL Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY2NmU3ZmVlLTRjYWItNDIyOS05Mjk2LThkNzJiNWIwNDAwOSZsaW5rPTBkYjQ5Y2RmLTQxNTMtNDVkMS04NGI4LTcyMjM4YmJiNjI1MSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=666e7fee-4cab-4229-9296-8d72b5b04009&link=0db49cdf-4153-45d1-84b8-72238bbb6251&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dizaynda-sql-destegi_80090309_50689323.html"
source_version: "2022-11-02T16:10:27.137+03:00"
source_bytes: 277634
fetched_at: "2026-09-13T04:25:12+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dizaynda SQL Desteği

Dizaynda SQL ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Dizayn modülünden hazırlanan dizaynlarda, dizayn tanımlama ekranında bulunan Kalem Bilgisi sayfasındaki Tip alanından *"Sql"* tipi seçilerek, veritabanından herhangi bir bilgi dizayna getirilebilmektedir. Bu tip kalem kayıtlarında Sql sorgusu e-Fatura, e-Arşiv, e-İrsaliye ve normal dizaynlar için desteklenmektedir. Görsel dizaynın kendisi tablo ya da View'e bağlı olarak veri getirmesi nedeni ile bu tip dizaynlarda yer almamaktadır.
![](../_assets/6c6342fd6b1f2ae029cc.png)
Sql tipi, basımda veri tabanından değer getirilmesi için kullanılacaktır.
Örneğin; e-Fatura dizaynına, cari kartta ek bilgiler bölümünde açıklama1 sahasında yazan bilginin dizaynın en altına basılması istensin. Bu bilgi istenirse tip sahasından *"Program"* seçeneğinda uygun alan belirlenerek yapılabilir. Ya da tip sahasından *"Sql"* seçilerek yine istenilen koşullara göre sorgu yazılıp, sorgu sonucunun basılması sağlanabilir.
Bu örnek için tip olarak *"Sql"* seçeneği kullanılsın. Bu seçenek seçildiği anda saha ve alan no bölümleri pasifleşecektir ve sistem *"Select"* ile başlayan bölüme Sql sorugunun yazılmasını isteyecektir.
![](../_assets/034d123653ac49185933.png)
Buraya yazılan sorgunun *"Select"* ile başlamaması gerekmektedir. Çünkü sistem basım esnasında bu komutu otomatikman göndermektedir. Sorgu içerisinde *"Where"* kısıtı kullanılabilir aynı zamanda *"Join"* yapıları da yine bu bölümde kullanılabilmektedir. Sorgu cümlesinin yazıldığı bölüm Sql sayfası olarak değerlendirilebilir. Burada *Where* koşulundan sonra tanımlanacak olan kısıtlar sabit değil, belgeye göre değişkenlik gösteriyor ise sağ klikte yer alan fonksiyonlardan uygun olanın kullanılması gerekmektedir. Burada önemli olan yazılan sorgunun tek bir değer döndürmesidir.
Sql sorgu bölümünde sağ klik yapıldığında üç tür fonksiyon gelmektedir.

Bu fonksiyonlar; *VT_Sayisal(), VT_Karakter() ve VT_Tarih()'tir.*

***VT_Sayisal()*** : Sayısal kısıt vermek için kullanılır.

***VT_Karakter():*** Alfasayısal kısıt vermek için kullanılır.

***VT_Tarih():*** Tarih kısıtı vermek için kullanılır.

Sorgu için uygun olan fonksiyon belirlendikten sonra bu fonksiyonun hangi alan için çalışacağının belirlenmesi gereklidir. Programdaki tüm alan bilgilerine Saha Rehberi seçeneği tıklanarak ulaşılabilir. Örnek cümlede belge üzerinde yazan cari kod bilgisi cari kart tablosu ile eşleştirilip, buradak Açıklama1 sahasının okunması sağlanmıştır. ***VT_Karekter({1002})*** için saha rehberine bakıldığında *Cari* *Kod* bilgisi olduğu görülecektir.
*ACIK1* *FROM* *TBLCASABIT* *WHERE* *CARI_KOD=* *VT_Karekter({1002})*
***VT_Sayisal()*** ve ***VT_Tarih()*** fonksiyonlarının kullanımı da VT_Karakter'de olduğu gibidir.
Tek fark, fonksiyonlarda girilecek olan alan numarasına sahip sahanın sayısal ya da tarih formatında olması gerektiğidir.
e-Fatura dizaynı için Sql'den elde edilen verinin xmlde basılabilmesi için xml tag eşleştirmesinin de yapılması gereklidir. Dizaynda bu bilginin en altta yer alması istendiği için "e-Devlet Xml Tag" bölümünden *Invoice* *Notes* eşleştirmesi yapılmıştır.
Sql'den veri alınması için gerekli tanımlamalar tamamlanmıştır. Girilen e-Fatura belgesi için taslak oluşturulduğunda, bu faturanın carisinin kart bilgilerinde Açıklama1 sahasında girilmiş bir bilgi varsa bu bilgi dizayna gelecektir.
Bu örnek için M002 carisinin kartında Açıklama1 bölümünde "e-Fatura mükellefidir." bilgisi yer almaktadır. Bu bilginin dizayna basması beklenmektedir.
![](../_assets/81a68e94ee30b23d24a7.png)
![](../_assets/00ca6773d3ab999a02df.png)
![](../_assets/419ed28861335b5ce0aa.png)
