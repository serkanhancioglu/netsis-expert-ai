---
title: "Barkod Dizayn / Demirbaş"
page_id: "50684001"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Demirbaş"
  - "İşlemler / Demirbaş"
  - "Demirbaş Barkod İşlemleri"
  - "Barkod Dizayn / Demirbaş"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Demirbaş / İşlemler / Demirbaş / Demirbaş Barkod İşlemleri / Barkod Dizayn / Demirbaş"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTBiNGQwMTMxLWQ4NWQtNDZmOC04ZDdhLTY5N2M2NTQ0MTFmZCZsaW5rPTA3NjIxY2E3LTYxZjUtNDYwMy1hMWQ3LTM5ZDVmOWY0YTNhOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0b4d0131-d85d-46f8-8d7a-697c654411fd&link=07621ca7-61f5-4603-a1d7-39d5f9f4a3a8&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "barkod-dizayn-demirbas_90670287_50684001.html"
source_version: "2022-09-26T10:48:32.437+03:00"
source_bytes: 112799
fetched_at: "2026-09-13T04:21:28+00:00"
generator: "netsis-scraper 1.0.0"
---
# Barkod Dizayn / Demirbaş

Demirbaş modülü Barkod Dizayn bölümü, Genel Bilgiler ve Saha Bilgileri olmak üzere iki sekmeden oluşur.

**Genel Bilgiler**

Barkod Dizayn ekranı Genel Bilgiler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Barkod Dizaynı Ekranı |  |
| --- | --- |
| Dizayn Kodu | Barkod dizaynına verilecek kodun girildiği alandır. Dizayn kodu en fazla 20 alfa numerik karakterden oluşur. Tanımlanan dizaynın adı, sağ taraftaki alana yazılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, daha önceden tanımlanan dizayn kodlarına ulaşılabilir. |
| Yazıcı İsmi | Kullanılan yazıcının isminin belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, dizaynın kullanıcı tarafından elle yapıldığı durumlarda desteklediği yazıcılar içinden seçim yapılır. Desteklenen yazıcılar; Zebra, Zebra TLP2844, Zebra Z 4M, Tec B-482, Tec B-442, Tec B-472, Tec B-430, Eltron TLP2642, Intermec 301, Intermec 3400, Sato CX200, Clever Code TDP-643, Datamax Allegro2, Datamax E CLASS, Argox X-2000, TSC TTP243-M'dir. Ancak dizaynlar, başka bir programda txt formatında hazırlanarak Logo Netsis'e yükleniyorsa, burada bulunan listenin dışındaki barkod yazıcılar desteklenir. |
| Dizaynın Basılacağı Port | Barkod etiketinin hangi porttan basılacağının belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, LPT1, LPT2, COM1, COM2 veya TEXT seçeneklerinden biri seçilebilir. "TEXT" seçeneğinin seçilmesi halinde barkod basımı yapıldığında, C dizininde TXT türünde bir dosya oluşturulur. |
| Ribbon | Burada belirlenecek kıstas etiket türüne göre değişir. Kullanılacak etiket termal etiketse "Hayır", ribbon ise '"Evet" seçeneği işaretlenir. |
| Etiketin Genişliği | Kullanılan etiketin satırının toplam genişliğinin girildiği alandır. Buraya girilecek değer dot cinsinden olmalıdır. |
| Etiketin Boyu | İki satır arasındaki boşluğun, etiketin net boyuna eklenmesiyle hesaplanan uzunluktur. Bu değerin dot cinsinden girilmesi gerekir. |
| Etiketin Sayısı | Bir satırda bulunan etiket sayısının girildiği alandır. |
| Satır Etiket Arası Boşluk | Bir satırda bulunan etiketler arasındaki boşluğun dot cinsinden girildiği alandır. |
| Satır Etiketlerin Boyu | Bir satırda bulunan etiketlerin net uzunluklarının dot cinsinden girildiği alandır. ![](../../../../_assets/739c2cd793e023c14efc.png) |
| Satır Boşluk | Barkod satırları arasındaki boşluğun girildiği alandır. |
| Sütun Boşluk | Barkod etiketinin sütunlarının yanında bulunan boşluğun girildiği alandır. |
| ![](../../../../_assets/8ac32bb3a254429f996d.png) Dosya Yükle | Barkod dizaynının farklı bir programda yapıldıktan sonra, Logo Netsis'e aktarılması için kullanılan butondur. Bu butona basılarak, TXT formatında hazırlanan dizayn dosyası seçilir. |

**Saha Bilgileri**

Barkod Dizayn ekranı Saha Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Barkod Dizaynı Ekranı |  |
| --- | --- |
| Alan Tipi | Basılacak alanın nasıl tanımlanacağının belirlendiği bölümdür. Alan tipi olarak "Program" seçildiğinde "Basılacak Alan" bölümü aktif hale gelir ve stok sabitte bulunan alanlar seçilebilir. Böylece, gerekli bilgiler program tarafından basıma yansıtılır. Alan tipi olarak "Text" seçildiğinde ise "Text" alanı aktif hale gelir ve basım yapılması istenen bilgi elle girilebilir. |
| Barkod | Dizayn içinde yer alan barkodun tanımlanması için işaretlenmesi gereken seçenektir. "Basılacak Alan" sahasından barkod olarak tanımlanmış alan seçilir. |
| Barkod Tipi | Barkod kutucuğunun işaretlenmesiyle "Barkod Tipi" alanı aktif hale gelen alandır. Basımını yapacağınız barkodun tipinin belirlenmesini sağlar. Alanın sağ tarafında yer alan aşağı ok butonu yardımı ile, EAN 13, EAN 8, CODE 128 ve CODE 39 barkod tiplerinden biri seçilir. |
| C.Digit | "Check Digit" uygulamasının desteklenmesi istendiğinde işaretlenmesi gereken alandır. **Örneğin,** Stok kodlarının barkod olarak basılması istendiğinde, stok kodları 6 karakter olarak tanımlanırsa ve barkod 7 karakterden oluşacaksa, "Check Digit" işaretlendiğinde, program 7. rakamı otomatik hesaplar. |
| Basılacak Alan | Alan Tipi olarak "Program" seçildiğinde aktif hale gelen alandır. Bu alan stok sabitte bulunan alanları ve bu alanlara ait bilgileri içerir. Alanın sağ tarafında yer alan aşağı ok butonu ile basılacak alan seçenekleri arasından seçim yapılır. |
| Dizayn Alan No | Stok sabit bilgileri dışında (fatura belgesinden basım sırasında) belgeye ait bazı bilgilerin basımı için kullanılan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, belgedeki alanlara ait alan numaralar seçilebilir. |
| Et. Sol. Mes. (dot) | Etikete basım yapılacak alanın soldan mesafesinin dot cinsinden girildiği alandır. |
| Et. Üst. Mes. (dot) | Etikete basımı yapılacak alanın üstten mesafesinin dot cinsinden girildiği alandır. |
| Açısı | Basımı yapılacak alanın yazım yönünün değişmesini sağlayan alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile 0, 90, 180 ve 270 derecelik açılar seçilebilir. |
| Karakter Büyüklük | Basılacak karakter büyüklüğünün girildiği alandır. |
| Karakter Genişlik | Basılacak karakter genişliğinin girildiği alandır. |
| Font | Basım sırasında kullanılması istenen yazı tipinin girildiği alandır. Bu bölüm için kullanılan değerler yazıcıdan yazıcıya değişir. |
| Ondalık | Tanımlama sırasında sayısal alanlardan birinin seçilmesi halinde aktif olan alandır. Sayısal bilgilerin ondalık değer basımını sağlar. Basılacak alanın içereceği ondalık karakter miktarının belirtilmesi gerekir. |
| Text | "Alan Tipi" alanında "Text" seçeneğinin işaretlenmesi halinde aktif olan alandır. Bu durumda, basılacak bilginin program tarafından otomatik getirilmeyip kullanıcı tarafından bilgi girişi yapılacağı anlaşılır. Basımı yapılacak Text bilgisi bu alana girilir. |
| TL Fiyat | Basılacak alan olarak fiyat alanlarından birinin seçilmesi halinde, fiyat bilgisinin YTL olarak değil de, bir milyona bölünmemiş eski haliyle (TL) basımı için kullanılan seçenektir. Bu alan sadece YTL'ye ilk geçiş aşamasında kullanılmış olup, şu an için kullanımı söz konusu değildir. |
| Fiyat Yuvarlama | "TL Fiyat" alanı işaretlendiğinde aktif olan seçenektir. Bu alan sadece YTL'ye ilk geçiş aşamasında kullanılmış olup, şu an için kullanımı söz konusu değildir. |
| Sıra No | Stoklar için girilen birden fazla seri bilgisinin barkod etiketlerine basımı için kullanılan seçenektir. "Seri No" alanı için "Sıra No" bilgisi 0,1,2…. olan birden fazla satır tanımlanarak, tüm seri bilgisinin basımı sağlanır. |
| Uzunluk | Basılacak bilgiye ait uzunluğun dot cinsinden girildiği alandır. |
