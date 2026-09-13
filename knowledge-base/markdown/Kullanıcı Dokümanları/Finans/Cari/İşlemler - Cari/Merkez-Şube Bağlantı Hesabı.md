---
title: "Merkez-Şube Bağlantı Hesabı"
page_id: "29983930"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "İşlemler / Cari"
  - "Merkez-Şube Bağlantı Hesabı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / İşlemler / Cari / Merkez-Şube Bağlantı Hesabı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMzZjQ5NGE3LTk3MmMtNGY3Ni1iNWIzLTczOGQ2MjM5MDY0MSZsaW5rPWFhNWVhYjJkLWM5ZDAtNDEzOC05MDg3LTczYjdiMDMwOWUyYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=33f494a7-972c-4f76-b5b3-738d62390641&link=aa5eab2d-c9d0-4138-9087-73b7b0309e2b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "merkez-sube-baglanti-hesabi_29984095_29983930.html"
source_version: "2022-10-31T10:57:40.937+03:00"
source_bytes: 97055
fetched_at: "2026-09-13T04:08:00+00:00"
generator: "netsis-scraper 1.0.0"
---
# Merkez-Şube Bağlantı Hesabı

Merkez Şube Bağlantı Hesabı işlemi, Finans Bölümü'nde İşlemler/Cari menüsünün altında yer alır. Merkez-Şube bağlantı hesabı, sadece merkez işletmede (ORTAK30) menüye eklenir. Merkez-Şube Bağlantı Hesabı; Ön Sorgulama, Genel Kısıtlar, Kısıt ve Ölçekleme sekmelerinden oluşur. Şubeli muhasebe ve şubeli cari sistemi kullanıldığında, şubelerden girilen alış faturalarına karşılık, ilgili satıcılara merkez tarafından ödeme yapılıyorsa, muhasebe mizanlarını dengelemek için ek işleme ihtiyaç duyulur. Çünkü hesaplar bakiye vermeye başlar.

**Örneğin:** Satıcının hareket kayıtlarının aşağıdaki şekilde olduğu varsayıldığında

```text
Açıklama          B / A         Tutar                   Şube KoduFaturanız           A               100.000.000        01Nakit Tediye      B               80.000.000          00
```

Bu hareketler için şubeden oluşan muhasebe kaydı

```text
Hesap Kodu     B / A         Tutar 153-01-001       B                100.000.000320-01-001       A                100.000.000
```

Bu hareketler için merkezden oluşan muhasebe kaydı

```text
Hesap Kodu      B / A          Tutar 320-01-001        B                 80.000.000100-01-001        A                 80.000.000
```

Bu durumda 320-01-001 numaralı hesap şubede 100.000.000 TL alacak, merkezde ise 80.000.000 TL borç bakiyesi verir. Aslında bu hesabın bakiyesi 20.000.000 TL'dir. Hesabın dengelenmesi amacıyla çalıştırılacak ek işlem için yapılması gerekenler şu şekildedir; hem merkez hem de kullanılacak şubeler için birer cari kart açılması gerekir. Merkez için açılacak cari kodun MERKEZ, şubeler için açılacak cari kodların SUBE1, SUBE2,... formatında olması gerekir. Aynı zamanda, açılan bu cari kodlar için muhasebede de torba hesap olarak kullanılacak hesap kodları açılmalı ve cari hesap kartlarına girilmelidir.

```text
Örneğe göre Merkez için açılan hesaba (MERKEZ) 900-01-001 hesap kodu, şube 1 için açılan cari koda (SUBE1) 900-01-002 hesap kodu girildiği varsayıldığında ve ek işlem çalıştırıldığında aşağıdaki mahsuplar oluşur. Hesap Kodu      B / A       Tutar                Şube Kodu900-01-002       B              80.000.000      00 (Şube1 torba hesap)320-01-001       A              80.000.000      00
```

```text
Hesap Kodu     B / A        Tutar                 Şube Kodu320-01-001      B              80.000.000       01900-01-001      A              80.000.000       01 (Merkez torba hesap)
```

Bu mahsuplarla, 320-01-001 hesap şubeye ait olduğu için merkezin bakiyesi kapatılır ve şubenin bakiyesi ise gerçek bakiyeye ulaşır.

**Ön Sorgulama**

Merkez Şube Bağlantı Hesabı ekranı Ön Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Merkez-Şube Bağlantı Hesabı Ekranı |  |
| --- | --- |
| Cari Kodu Aralığı | Cariye ait başlangıç ve bitiş kodlarının ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu yardımı ile seçilerek, merkez-şube bağlantı hesabı için kısıt verilmesini sağlayan alandır. |
| Tip | Merkez-şube bağlantı hesabı için tip kısıdının verildiği alandır. Hepsi, Alıcı, Satıcı, Kefil, Toptancı, Müstahsil ve Diğer olmak üzere yedi tip seçenek bulunur. |
| Grup Kodu | Merkez-şube bağlantı hesabı için grup kodu kısıdının verildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile grup kodları arasından seçim yapılabilir. |
| Kod-1/2/3/4/5 | Merkez-şube bağlantı hesabı için daha önceden tanımlaması yapılan Kod-1/2/3/4/5 kısıdının verildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılabilir. |
| İl | Merkez-şube bağlantı hesabı için il kısıdının verildiği alandır. |
| İlçe | Merkez-şube bağlantı hesabı için ilçe kısıdının verildiği alandır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Verilen kısıtlara göre merkez-şube bağlantısının yapılmasını sağlayan butondur. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar, Kalite Kısıtları ve Kısıt sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Merkez-şube bağlantı hesabı için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki merkez-şube bağlantı hesabı işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Merkez-şube bağlantı hesabı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Merkez-şube bağlantı hesabı için verilen kısıtların iptal edildiği butondur. |

**Genel** **Kısıtlar**

Merkez Şube Bağlantı Hesabı ekranı Genel Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Merkez-Şube Bağlantı Hesabı Ekranı |  |
| --- | --- |
| Yıl/Ay | Merkez-şube bağlantı hesabı için yıl/ay kısıdının verildiği alandır. |
| Kümülasyon |  |
| Cari Kodu | Bir cari hesabın o ayki borç/alacaklarının entegrasyona tek bir satır olarak aktarılması istendiğinde işaretlenmesi gereken seçenektir. |
| Muhasebe Hesap Kodu | Aynı muhasebe hesap koduna sahip tüm cari hesapların o ayki bütün borç/alacaklarının entegrasyona tek bir satır olarak aktarılması istendiğinde işaretlenmesi gereken seçenektir. |
| Tek Tek | Bir cari hesabın her hareketinin ayrı ayrı entegrasyona atılması istendiğinde işaretlenmesi gereken seçenektir. |
| Proje Kodu Kırılımı | Proje kodu kırılımı yapılması için kullanılan seçenektir. |
| Proje Kodu Aralığı | Proje başlangıç ve bitiş kod aralıklarının ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu yardımı ile seçilerek, merkez-şube bağlantı hesabı için proje kodu kısıdı verilen alandır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Verilen kısıtlara göre merkez-şube bağlantısının yapılmasını sağlayan butondur. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar, Kalite Kısıtları ve Kısıt sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Merkez-şube bağlantı hesabı için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki merkez-şube bağlantı hesabı işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Merkez-şube bağlantı hesabı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Merkez-şube bağlantı hesabı için verilen kısıtların iptal edildiği butondur. |

**Kısıt**

Merkez Şube Bağlantı Hesabı ekranı Kısıt sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Merkez-Şube Bağlantı Hesabı Ekranı |  |
| --- | --- |
| Sahalar | Merkez-şube bağlantı hesabı için kısıt verilmesi istenen alanlar yer alır. Ekle ![](../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "kısıt verilecek sahalar" kısmına eklenir. |
| Kısıt Verilecek Sahalar | Merkez-şube bağlantı hesabı için kısıt verilen sahaların yer aldığı alandır. Çıkar ![](../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Eşit, Küçük, Küçük veya Eşit, Büyük, Büyük veya Eşit, Arasında, Benziyor, Eşit Boş, Eşit Değil, İçinde Eşit Değil | **Eşit;** işaretlenen alanda belli bir sabit koşula göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "001" olan stok için liste alınacaksa "Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "001" girilir. Bu durumda, sadece "001" numaralı Stok Kodu için liste alınır. **Küçük;** işaretlenen alanda belli bir değerden küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den küçük" numaralı Stok Kodu için liste alınır. **Küçük veya Eşit:** işaretlenen alanda belli bir değere eşit veya küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den küçük" numaralı Stok Kodu için liste alınır. **Büyük;** işaretlenen alanda belli bir değerden büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den büyük" numaralı Stok Kodu için liste alınır. **Büyük veya Eşit;** işaretlenen alanda belli bir değere eşit veya büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den büyük" numaralı Stok Kodu için liste alınır. **Arasında;** seçilen alanla ilgili bir aralık tanımlanması istendiğinde kullanılması gereken seçenektir. Eğer belli bir başlangıç ve bitiş değeri arasında kalan değerlerle ilgili kısıt verilecekse kullanılması gereken seçenektir. Örneğin; Stok Kodu kıstasında, "Arasında" seçeneği seçilip \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" ve yine \<tab\> tuşu ile ilerlenerek altta bulunan alana "200" yazıldığı varsayılsın. Böylece stok kodu 100 ile 200 arasındaki stok kodları için liste alınır. **Benziyor;** cari ile ilgili kayıt ararken cari hesabın ismi tam olarak bilinmiyorsa benziyor seçeneği kullanılır. Örneğin; cari hesabın isminin CANEL ya da CENEL olacağı düşünülüyorsa, bu seçeneği seçtikten sonra alanın sağ tarafındaki kayıt alanına "C_NEL" yazıldığında, raporda cari ismi "C" ile başlayan ikinci karakteri herhangi bir karakter olan fakat sonu "NEL" ile biten kayıtlar listelenir. **Eşit Boş;** seçilen sahada hiçbir bilgi olmadığında kullanılan seçenektir. Bu seçenek alfanumerik sahalar için geçerlidir. Sıfırdan büyük veya sıfıra eşit bilgilerin aranması durumunda "Eşit", "Büyük Eşit", "Küçük Eşit" seçenekleri kullanılabilir. **Eşit Değil;** raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında, Benziyor ve Eşit Boş seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Eşit Değil" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Eşit Değil" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| İse/Değil ise | **İse;** raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumlu (dahil) anlamını taşıyorsa "İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "İse" seçeneği işaretlenirse, rapora stok kodu "0101" olan stokların dahil edileceği anlaşılır. **Değil İse;** raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Değil İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Değil İse" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| Ve/Veya | **Ve;** seçilen sahalarda zorunlu bağlantı koşulu sağlar. **Örnek 1:** Karmaşık bir stok kodlaması olduğu varsayıldığında; Bu kodlardan iki tanesinin raporda çıkması isteniyor fakat bu iki stok kodunun ortak hiçbir özelliği yok. Bu durumda, "Stok Kodu" sahası iki kez kısıt verilecek sahalar bölümüne aktarılır. 1.Stok Kodu kıstasında eşit bağlantısı kurularak ilk stok kodu girilir ve "VE" bağlacı işaretlenir. Daha sonra 2. Stok Kodu seçilerek yine eşit bağlantısı ile diğer bir stok kodu yazılır. Böylece, raporda sadece bu iki stok koduna ait bilgi alınır. Bu seçenekte tanımlanan her koşulun olması zorunludur. Yani, tanımlanan iki stok kodundan biri bile mevcut değil ise, rapor bilgi vermez. **Örnek 2:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; Verilen tanımlamalarda "VE" bağlacı kullanılırsa, mutlaka bu üç kısıta da sahip olan stoklar aranır ve bulunursa listelenir. Üç kısıttan herhangi birine sahip olmayan stoklar raporda listelenmez. **Veya;** seçilen sahalarda olabilirlik koşulu sağlar. Yani, tanımlanan koşullardan biri bile sağlansa ilgili raporla ilgili bilgi alınabilir. **Örnek 1:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; verilen tanımlamalarda "VEYA" bağlacı kullanılırsa, bu üç kısıttan birine bile sahip olan stoklar aranır ve bulunursa listelenir. |
| ![](../../../../_assets/c7275efbddc154ea1579.jpg) Kaydet | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Verilen kısıtlara göre merkez-şube bağlantısının yapılmasını sağlayan butondur. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar, Kalite Kısıtları ve Kısıt sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Merkez-şube bağlantı hesabı için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki merkez-şube bağlantı hesabı işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Merkez-şube bağlantı hesabı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Merkez-şube bağlantı hesabı için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

**Örneğin:** Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.
