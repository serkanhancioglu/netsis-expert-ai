---
title: "Modül Raporlarına Kolon Ekleme"
page_id: "153157752"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Modül Raporlarına Kolon Ekleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Modül Raporlarına Kolon Ekleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWExZGVhNDBiLTAyNTMtNGQ3Mi05OTE0LWUzMzUwNDYwYzQ1MCZsaW5rPTYxZTM3ODQxLTc3ZDUtNDFiNy1iNjc1LTYyZjE4MTQxZWMxZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a1dea40b-0253-4d72-9914-e3350460c450&link=61e37841-77d5-41b7-b675-62f18141ec1e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "modul-raporlarina-kolon-ekleme_153157752_153157752.html"
source_version: "2024-09-26T15:48:51.937+03:00"
source_bytes: 462274
fetched_at: "2026-09-13T04:22:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Modül Raporlarına Kolon Ekleme

Modül raporları için sonuç gösteriminin yapıldığı ekranlarda kullanıcı tanımlı kolon ekleme özelliği desteklenmektedir. Bu sayede standart raporlarda özel sorgular kullanılarak istenen kolonların eklenmesi ile rapor sonuçları özelleştirilebilmektedir.

Bu özellik Netsis Standart ve Enterprise paketlerinde 9.0.43 ve üzeri sürümlerde desteklenmektedir.

Taslak olarak kaydedilen modül raporlarında, Rapor Seçenekleri menüsündeki "Kullanıcı Tanımlı Kolon Ekleme" seçeneği aktif olmaktadır. Bu seçenek için aynı zamanda yetki kontrolü yapılmaktadır. Admin rolündeki veya SSO'da "Yardımcı Programlar" modülü "Rapor – Kullanıcı Tanımlı Kolon

Ekleme" yetkisine sahip olan kullanıcılarda aktif gelmektedir. Rapordaki kolon özelleştirmeleri taslak bazında yapıldığı için taslak olarak kaydedilmemiş bir rapor açıldığında ilgili buton pasif görünecektir.

Kullanıcı Tanımlı Kolon Ekleme menüsüne giriş yapıldığında 3 sekmeden oluşan tanımlama ekranı açılmaktadır. Bu ekrandaki anahtar saha, kolon sorgu tanımı, kolon tanımlama sekmelerinden sırasıyla işlem gerçekleştirildikten sonra yapılan tanımlama son sekmeden Kaydet butonu ile kaydedilmektedir.

![](../_assets/c9a9439a2d82eb08208c.png)

**"Sorgu Anahtar Sahaları" Sekmesi**

Bu sekmede kullanıcı tanımlı sahaların listelenmesi için yazılacak SQL sorgusunda kullanılacak anahtar sahaların tanımlamaları yapılmaktadır. Anahtar sahalar, seçilen sütun için sayfa ve satır numarası bazında değişken verileri içermektedir.

**Sorguda Kullanılacak Kolon:** Anahtar saha seçimi için sütun bilgisinin seçildiği alandır.

**Değerleme Tipi:** "Satır Değeri" ve "Üst Satırlarda Ara" şeklinde iki tip bulunmaktadır.

- Satır Değeri: Sorguda Kullanılacak Kolon alanında belirlenen sütunun ilgili satırlarının anahtar saha seçilmesi için kullanılır.

![](../_assets/d3da7879888a93b89b64.png)

- Üst Satırlarda Ara: "Aranacak Değer" ve "Döndürülecek Değer Kolonu" alanlarında belirtilen değerlere göre "Sorguda Kullanılacak Kolon" üzerinde aktif rapor satırından başlanarak üst satırlara doğru arama yapılmaktadır. "Aranacak Değer" değer alanında belirtilen koşul ifadesinin sağlandığı satırdaki "Döndürülecek Değer Kolonu" anahtar saha olarak kaydedilmektedir.

![](../_assets/d2d45d3b26ba993a3e73.png)

**Aranacak Değer:** "Değerleme Tipi" alanında "Üst Satırlarda Ara" seçildiğinde "Eşit", "Eşit Değil", "Benzer" operatörleri kullanılarak metin alanında belirtilen ifadenin aranması sağlanır.

**Döndürülecek Değer Kolonu:** "Değerleme Tipi" alanında "Üst Satırlarda Ara" seçildiğinde ve "Aranacak Değer" ifadesindeki koşul sağlandığında anahtar sahanın belirleneceği sütun bilgisinin seçildiği alandır.

Üst Satırlarda Ara olarak eklenen bir anahtar sahada eğer aktif satır boş ise üstündeki satırlardan ilgili değer getirilebilmektedir.

**Kolon Tanımlarını Sil:** F7 Tuşu ile aynı işlevi gerçekleştirerek aktif rapor taslağındaki kullanıcı tanımlı kolona ait bilgilerin silinmesini sağlar.

**"Kolon Sorgu Tanımı" Sekmesi**

Rapora eklenmesi istenen sahalar için SQL sorgu cümlesinin yazıldığı bölümdür. Anahtar sahalar sekmesinde tanımlanan sahalar TBLANAHTARSAHALAR tablosuna kaydedilmektedir. Bu tablo ile raporda özel kolonlara verilerin getirileceği tablo/view nesnesi joinlenerek getirilecek alanlar belirlenmektedir.

![](../_assets/aa8929f9725a2b889eda.png)

*Örnek Sorgu:*
*SELECT CS.CARI_IL, SS.GRUP_KODU*
*FROM TBLANAHTARSAHALAR A*
*LEFT JOIN CASABIT CS ON (A.#Anahtar1=CS.CARI_KOD)*
*LEFT JOIN STSABIT SS ON (A.#Anahtar2=SS.STOK_KODU)*

**"Kolon Tanımlama" Sekmesi**

**Kolon Başlığı:** Rapora eklenecek kolonlara ait başlık bilgisinin tanımlandığı alandır. En fazla 50 karakter uzunluğunda başlık bilgisi girilebilir.

**Sorgu Saha Adı:** Rapora eklenecek kolonun SQL ifadesinde belirtilen adıdır.

**NDS Tipi:** Rapora eklenen kolondaki verilerin Netsis Ondalık Sistemi ekranındaki ondalık seçeneklere göre gösterilmesi için kullanılan alandır.

**Veri Kuralı:** Kullanıcı tanımlı kolonda gösterilecek verilerin Kalın-İtalik-Renk seçenekleri ile hücre biçimlendirmesinin özelleştirilebildiği alandır.

**Basım Kuralı:** "Başlık Basım Kuralı" ve "Veri Basım Kuralı" alanlarının aktif hale gelmesi için kullanılan seçenektir. Bu seçenekler ile kolon başlığının veya verinin hangi koşulda rapora yazdırılabileceği belirlenebilmektedir.

**Başlık Basım Kuralı:** "Kolon" alanındaki değer ve seçilecek operatör bazında metin alanına girilen ifadenin kontrolü sağlanmaktadır. Başlık bilgisinin hangi koşulda raporda gösterileceği bu seçenek ile belirlenebilir.

**Veri Basım Kuralı:** Kolondaki verinin hangi koşulda rapora yazdırılacağının belirlenmesi için kullanılan seçenektir. "Eşit", "Eşit Değil", "Benzer" operatörleri kullanılarak bir ifade belirtilebilir.

![](../_assets/3244eebb03704a50a42d.png)
![](../_assets/93ae2eabcc95497f1763.png)
