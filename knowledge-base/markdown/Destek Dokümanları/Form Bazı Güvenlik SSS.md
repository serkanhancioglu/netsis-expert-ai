---
title: "Form Bazı Güvenlik SSS"
page_id: "128583427"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Form Bazı Güvenlik SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Form Bazı Güvenlik SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWI0YTFiZDNlLTdkMmEtNDllNS04MGNkLWU2OTI5NzJjNjAzZSZsaW5rPWU2YmI2NWE2LTc0MDUtNGM5ZC04MzUzLTZlMWI5NTlmZjNkNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b4a1bd3e-7d2a-49e5-80cd-e692972c603e&link=e6bb65a6-7405-4c9d-8353-6e1b959ff3d4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "form-bazi-guvenlik-sss_128583427_128583427.html"
source_version: "2023-12-25T14:25:10.253+03:00"
source_bytes: 4899
fetched_at: "2026-09-13T04:22:59+00:00"
generator: "netsis-scraper 1.0.0"
---
# Form Bazı Güvenlik SSS

**Soru 1 : Mevcut form bazı güvenlik tanımı farklı kullanıcılar için kopyalanabilir mi?**

Mevcut tanımın farklı kullanıcılar için kopyalanması desteklenmemektedir. Kullanıcıları aynı gruba bağlayarak grup üzerinden form bazı güvenlik tanımlaması yapılabilir.

**Soru 2 : Standart ve Entegre pakette form bazı güvenlik uygulaması kullanılabilir mi?**

Standart ve Entegre pakette de form bazı güvenlik uygulaması kullanılabilir.

**Soru 3 : Demirbaş ve Personel programlarında form bazı güvenlik uygulaması kullanılabilir mi?**

Demirbaş programı için; Demirbaş Yönetimi \\ Demirbaş \\ Kayıt \\ Parametre Girişi ekranındaki ve Personel programı için; Ek Modüller \\ Yardımcı Programlar \\ Kayıt \\ İşletme-İşyeri Tanımları ekranındaki "Form Bazı Uygulaması" parametresinin aktif hale getirilmesi ile uygulamanın bu ürünlerde de kullanımı mümkün hale gelir.

**Soru 4 : Satış Faturası "Toplamlar" sekmesindeki "Anlık E-Belge Gönderimi" alanının form bazı güvenlik ile kapatılabilmesi mümkün müdür?**

9.0.50 sürümü ile birlikte Satış Faturası "Toplamlar" sekmesindeki "Anlık E-Belge Gönderimi" alanının form bazı güvenlik uygulaması ile kapatılabilmesi mümkün hale getirilmiştir.

**Soru 5 : Form bazı güvenlik ile belge üzerindeki sağ tık ile açılan menüler gizlenebilir mi?**

Belge üzerindeki sağ tık ile açılan menüler form bazı güvenlik ile gizlenememektedir. Bu menüler genellikle yetkiye bağlı olduğundan SSO üzerinden yetki kontrolü incelenebilir.

**Soru 6 : Form bazı güvenlik tanımlaması sonrasında "Argument out of range" uyarısı alınıyorsa ne yapılmalıdır?**

İlk kolon 0'a karşılık gelecek şekilde, form bazı güvenlik tanımlamasındaki "Grid kolon no" değerleri kontrol edilmelidir. Son kolonun değerini aşan bir grid kolon no tanımlaması varsa bu durumda "Argument out of range" uyarısı alınır.

**Soru 7 : Form Bazı Güvenlik uygulaması ile kur, döviz fiyat ve fiyat alanları "Değiştirilemez" olarak tanımlanmış fatura belgelerine yeni bir dövizli kalem eklendiğinde TL fiyat hesaplanmamaktadır.**

"Form Bazı Güvenlik" uygulaması ile kur, döviz fiyat ve fiyat alanları "Değiştirilemez" olarak tanımlanmış fatura belgelerine yeni bir dövizli kalem eklendiğinde, TL fiyatının da hesaplanması "FATURA/DOVTLFIYATHESAPLA" özel parametresi ile desteklenmiştir.

**Soru 8 : Form bazı güvenlik ile combobox veya listbox alanları kısıtlanabilir mi?**

Form bazı güvenlik tanımlamalarında seçilen nesnenin tamamı için işlem yapıldığından yalnızca combobox veya listbox alanları kısıtlanmamaktadır.

**Soru 9 : Form bazı güvenlik ekranından tüm kullanıcılar seçilerek kayıt yapılmak istendiğinde TBLNFDMAS_FKEY1 The conflict occured in database "XYZ" table dbo.TBLKULLANP uyarısı alınıyorsa ne yapılmalıdır?**

İlgili veri tabanında TBLKULLANP tablosunda -1 no'lu "INTERNAL" kullanıcısı olmadığında belirtilen uyarı alınmaktadır. Bu kullanıcı insert edilerek sorun giderilebilir.

**Soru 10 : Admin kullanıcılar için form bazı güvenlik tanımlaması yapılabilir mi?**

Admin kullanıcılar için form bazı güvenlik uygulaması desteklenmemektedir.
