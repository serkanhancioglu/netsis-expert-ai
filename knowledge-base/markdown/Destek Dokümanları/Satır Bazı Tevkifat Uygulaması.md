---
title: "Satır Bazı Tevkifat Uygulaması"
page_id: "50686951"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Satır Bazı Tevkifat Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Satır Bazı Tevkifat Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA4MmMzZDUxLTc2MzMtNDU1Zi1iNzM2LWZiZDNhNmIyNTk3NyZsaW5rPTE1YTJjZTY4LWI1M2YtNDFkOS04OWY1LWVlNGEyYTFkNTU5ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=082c3d51-7633-455f-b736-fbd3a6b25977&link=15a2ce68-b53f-41d9-89f5-ee4a2a1d559f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "satir-bazi-tevkifat-uygulamasi_80090465_50686951.html"
source_version: "2022-11-03T08:57:17.033+03:00"
source_bytes: 352913
fetched_at: "2026-09-13T04:25:18+00:00"
generator: "netsis-scraper 1.0.0"
---
# Satır Bazı Tevkifat Uygulaması

Satır Bazı Tevkifat Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Faturada tevkifat; Fatura içerisinde yer alan KDV tutarının belirli bir oranının alıcı tarafından ödenmesini sağlayan kesinti yöntemidir. Böylece devlete KDV tutarının bir kısmını satıcı öderken bir kısmını da alıcı ödemiş olur.
Faturanın tamamına aynı oranda tevkifat hesaplaması yapılabildiği gibi, fatura kalemleri bazında, farklı oranlara göre tevkifat hesaplanabilmesi sağlanabilmektedir.

Satır Bazı Tevkifat Uygulamasında Dikkat Edilmesi Gereken Maddeler şunlardır:

- Öncelikle bütün tevkifat uygulamaları için fatura parametrelerinde Ek Maliyet sekmesindeki Ek Maliyet (2) parametresi işaretlenmeli ve fatura alt limiti girilmelidir. Satır bazı tevkifat için ise; Fatura parametrelerinde özel kod ve açıklama sekmesinde bulunan özel kod 2 parametresi işaretlenir ve Özel kod-2 tanımlama ekranından kullanılacak olan tevkifat kodları tanımlanır.
![](../_assets/e2ecb2d8ace42e51c45f.png)![](../_assets/80c0b609432f823620b5.png)
- Gezgin\\Lojistik- Satış\\Fatura\\İşlemler \\Çoklu Tevkifat Oran Tanımlama bölümünden, Özel kod-2 bazında tevkifat oranları ve tevkifat için çalışacak muhasebe hesap kodları tanımlanır.
![](../_assets/b191c5b463335255660d.png)
- Stok bazında hangi Özel kod-2'nin kullanılacağı, stok kartında bulunan herhangi bir sahada tanımlanabilir. Firma için uygun olan saha, Gezgin\\Genel\\Yardımcı Programlar\\İşlemler\\Veri Tabanı Nesneleri menüsünde view sekmesinde bulunan FATURASTSABIT view'undaki sahalardan belirlenebilir. Belirlenen bu sahaya stok kartı kayıtlarından, Özel kod-2 değeri girilmelidir. (Örneğin Kod-1 kullanılsın.)
![](../_assets/612e6c40bf71c3c014e5.png)
![](../_assets/05bc90aa30eda3e3251d.png)![](../_assets/d97c093a864a2cb24883.png)
- Gezgin\\Genel\\Yardımcı Programlar\\Kayıt\\Özel parametreler menüsünde; Grup Kodu FATURA, Anahtar SATIRBAZITEVKIFAT tanımlaması yapılmalıdır. Parametrenin değer sahasına ise, Özel Kod-2'nin FATURASTSABIT view'ındaki hangi sahanın tercih edildiği bilgisi girilmelidir. Örneğin Özel kod-2 girişi için stok kartındaki Kod-1 sahası kullanılıyor ise, özel parametrede değer sahası KOD_1 şeklinde tanımlanmalıdır.
![](../_assets/2dfbdcea75329fb1d3da.png)

Satır bazı tevkifat uygulamasının kullanılması halinde, toplam sayfasında ek maliyet 2 sahasına "-1" değeri girilmeden tevkifat tutarı hesaplanacaktır.

Yukarıdaki ekran görüntülerinde yer alan bilgiler ile örneklendirecek olursak, Tevkifat = \\\[(1000\*0.08) \*5/10\\\] + \\\[(1000\*0.08) \* 9/10\\\] =112 olarak hesaplanmıştır.
