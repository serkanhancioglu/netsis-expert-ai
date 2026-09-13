---
title: "e-Fatura Uygulaması"
page_id: "22804184"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "E-Fatura İşlemleri"
  - "e-Fatura Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / E-Fatura İşlemleri / e-Fatura Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdmMDI5MjcyLWFkMjUtNDMwMC1hMzc1LTllNzY4YzY4NmY0YyZsaW5rPTg0M2VkYjE1LWU5MTktNDlkMy05OGNlLTc4OGY5MDVjMzc5YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7f029272-ad25-4300-a375-9e768c686f4c&link=843edb15-e919-49d3-98ce-788f905c379a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-fatura-uygulamasi_22805051_22804184.html"
source_version: "2022-10-24T12:29:21.853+03:00"
source_bytes: 106304
fetched_at: "2026-09-13T04:01:53+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Fatura Uygulaması

"Elektronik Fatura Uygulaması", tanımlanan standartlara uygun e-Faturaların, taraflar arasında güvenli ve sağlıklı bir biçimde dolaşımını sağlamak amacı ile oluşturulan uygulamaların genel adıdır.

e-Fatura sisteminde satıcı ve alıcı e-Fatura gönderme ve alma konusunda yeterli alt yapıya ve alıcı ve satıcı e-Fatura düzenleme yetkisine sahip olmalıdır. e-Fatura ve uygulama yanıtının, vergi kanunları ve ilgili mevzuata uygun olarak düzenlenmesi gerekir.

![](../../../../../_assets/c72e8f79d7177fc56184.jpg)

e-Fatura uygulamasında "Gönderici Birim", "Merkez" ve "Posta Kutusu" olmak üzere 3 temel rol bulunur.

![](../../../../../_assets/0928cf869c0056374581.jpg)

**Gönderici Birim Rol Tanımı**

Gönderici Birim'in, e-Fatura ve sistem yanıtı üzerindeki yetkisi aşağıdaki şekildedir:

- Oluşturmaya imkan verir/oluşturur.
- Elektronik olarak imzalar veya Mali Mühür ile onaylar.
- Saklar.
- Yanıtın veri aktarım protokolü ile belirlenen veri kurallarına uygunluğunu denetler.
- Merkeze iletir.

Gönderici Birim'in, merkezden gelen uygulama yanıtı ve sistem yanıtı üzerindeki etkisi aşağıdaki şekildedir:

- Alır.
- Veri aktarım protokolü ile belirtilen veri kurallarına uygunluğunu denetler.
- İşler.
- Elektronik imza veya **Mali Mühür** doğrulaması yapar.
- Saklar.

**Posta Kutusu Rol Tanımı**

Posta Kutusu'nun, merkez üzerinden gelen elektronik fatura ve sistem yanıtı üzerindeki yetkisi aşağıdaki şekildedir:

- Alır.
- Elektronik imza veya **Mali Mühür** doğrulaması yapar.
- Fatura ve sistem yanıtının, veri aktarım protokolü ile belirtilen veri kurallarına uygunluğunu denetler.
- İşler.
- Saklar.

Posta Kutusu'nun, uygulama yanıtı ve sistem yanıtı üzerindeki yetkisi aşağıdaki şekildedir:

- Oluşturmaya imkan verir/oluşturur.
- Elektronik olarak imzalar veya **Mali Mühür** ile onaylar.
- Saklar.
- Fatura ve sistem yanıtının, veri aktarım protokolü ile belirtilen veri kurallarına uygunluğunu denetler.
- Merkez’e iletir.

**Merkez Rol Tanımı**

Merkez rolün, kendisine gelen e-Fatura ve uygulama yanıtı üzerindeki etkisi aşağıdaki şekildedir:

- Alır.
- Fatura ve uygulama yanıtının, veri aktarım protokolü ile belirtilen veri kurallarına uygunluğunu denetler.
- İşler.
- Elektronik imza veya Mali Mühür doğrulaması yapar.
- İlgili adrese iletir.
- İlgili adrese sistem yanıtı oluşturur ve iletir.

Merkez rolün, kendisine gelen sistem yanıtı üzerindeki etkisi aşağıdaki şekildedir:

- Alır.
- Sistem yanıtının, veri aktarım protokolü ile belirtilen veri kurallarına uygunluğunu denetler.
- İşler.
- Elektronik imza veya **Mali Mühür** doğrulaması yapar.
- İlgili adrese iletir.
- "Gönderici", "Posta Kutusu" ve "Merkez" tarafından oluşturulan belgeler, öngörülen şemalara, şema kurallarına, diğer veri kurallarına ve standartlara uygun olmak zorundadır. Uygulama ile ilgili her adımda loglama yapmak zorundadır.

e-Fatura uygulaması iki şekilde kullanılabilir:

- Temel faturalama işlemleri için oluşturulan ve [http://www.efatura.gov.tr](http://www.efatura.gov.tr) adresinde hizmete sunulan e-Fatura portalı aracılığıyla yapılabilir. Bu sistemde mükellefler ilave bir yazılım kullanmadan işlemlerini "GİB" portalı üzerinde yapabilecekleri gibi, Logo Netsis tarafından oluşturulan UBL-TR formatına uygun e-Fatura dosyalarını da portala yükleyebilirler.
- Bilgi işlem sistemlerinin e-Fatura uygulamasına entegre edilmesi ile yapılabilir. Bu uygulamada mükellefler mühürlenen ya da imzalanan satış ve alış faturalarını portal yerine Logo Netsis uygulaması içinden doğrudan iletip alabilir.
