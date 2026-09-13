---
title: "Hızlı Hücre Kodu Tanımlama"
page_id: "95650772"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Dinamik Depo"
  - "İşlemler / Dinamik Depo"
  - "Hızlı Hücre Kodu Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Dinamik Depo / İşlemler / Dinamik Depo / Hızlı Hücre Kodu Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWNiYjk5Y2FiLTQ3ODUtNGZjYy1iZjNmLTA0ZGYwNDVhZjRiMCZsaW5rPTI5MjE5NjA2LWI3NTctNDdjNy1hNjc2LTQzNzdkYmVkMDNiNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=cbb99cab-4785-4fcc-bf3f-04df045af4b0&link=29219606-b757-47c7-a676-4377dbed03b4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hizli-hucre-kodu-tanimlama_95650773_95650772.html"
source_version: "2022-10-31T12:12:49.060+03:00"
source_bytes: 10674
fetched_at: "2026-09-13T04:06:16+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hızlı Hücre Kodu Tanımlama

Hızlı Hücre Kodu Tanımlama, Dinamik Depo-İşlemler menüsünün altında yer alır. Hızlı Hücre Kodu Tanımlama, hücre kodlarının belli bir format belirleyerek hızlıca açılması için kullanılan bölümdür.

Hücre kodlaması, malların yerleştirilmesinde ve toplanmasında çok önemlidir. Hızlı Hücre Kodu Tanımlama bölümü kullanılarak, belirlenen kodlama formatında hızlı hücre kodları açılabilir.

Hızlı Hücre Kodu Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hızlı Hücre Kodu Tanımlama |  |
| --- | --- |
| Hücre Maske | Açılacak hücreler için formatın belirlendiği alandır. Yatayda ve/veya dikeyde hücreleri otomatik açılabilir. Yatayda hücrelerin açılması istendiğinde; hücre kodlarının başına gelecek karakter/karakterleri yazıp, buna bitişik olarak {1} karakter dizisi yazılmalıdır.<br>Örneğin; HY{1} şeklinde bir hücre maskesi, HY ile başlayan ve numaralandırması yatay aralık bölümünde verilecek olan hücreler açılacağı anlamına gelir. HY60, HY61, HY62 HY69 gibi. Dikeyde hücrelerin açılmasını istendiğinde; hücre kodlarının başına gelecek karakter/karakterleri yazıp, buna bitişik olarak {2} karakter dizisi yazılmalıdır.<br>Örneğin; HD{2} şeklinde bir hücre maskesi, HD ile başlayan ve numaralandırması dikey aralık bölümünde verilecek olan hücreler açılacağı anlamına gelir. HD20, HD21, HD22 HD29 gibi. İstenirse hem yatayda hem de dikeyde hücreler tanımlanabilir. Örneğin; HY{1}HD{2} şeklinde bir hücre maskesi, HY60HD20, HY61HD20, HY62HD20, HY69HD20, HY60HD21, HY61HD21, HY62HD21, .... , HY69HD21, HY60HD22, HY61HD22, HY62HD22,, HY69HD22, HY60HD29, HY61HD29, HY62HD29,, HY69HD29 şeklinde hücreler açılacağı anlamına gelir. |
| Yatay | Hücrelerin yatayda hangi sayıdan başlayıp hangi sayıda biteceğinin belirlendiği alandır. Yukarıdaki örnekte yatay aralık 60-69 olmalıdır. |
| Dikey | Hücrelerin dikeyde hangi sayıdan başlayıp hangi sayıda biteceğinin belirlendiği alandır. Yukarıdaki örnekte dikey aralık 20-29 olmalıdır. |
| Hücre Grup Kodu | Daha önceden tanımlı bir hücre grup kodu bu alana girilirse açılacak hücre kodlarına, burada girilen grup kodu atanır. Boş bırakılabilir. Rehber butonu ile grup kodlarına ulaşılır. |
| Depo Kodu | Açılacak hücreler için baz alınacak lokal depo kodunun girildiği alandır. Açılan hücrelerin, lokasyon takibi yapılan depolardan hangisinde olduğunu belirtir. Rehber butonu ile depo kodlarına ulaşılır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
