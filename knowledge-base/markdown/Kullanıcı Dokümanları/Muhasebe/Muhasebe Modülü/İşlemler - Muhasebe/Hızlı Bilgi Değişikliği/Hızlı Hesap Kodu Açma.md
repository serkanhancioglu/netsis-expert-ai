---
title: "Hızlı Hesap Kodu Açma"
page_id: "24740570"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "İşlemler / Muhasebe"
  - "Hızlı Bilgi Değişikliği"
  - "Hızlı Hesap Kodu Açma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / İşlemler / Muhasebe / Hızlı Bilgi Değişikliği / Hızlı Hesap Kodu Açma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTliOWVkMDJiLTIyNTYtNDA3Ni1hYTk4LTZkYmE0YzQ1NTJiOSZsaW5rPTk4MTljZTg1LWIxNDgtNDg3MC1hNDc2LWQ0ZjViZjgwNGE0YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9b9ed02b-2256-4076-aa98-6dba4c4552b9&link=9819ce85-b148-4870-a476-d4f5bf804a4a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hizli-hesap-kodu-acma_41157183_24740570.html"
source_version: "2022-10-06T11:40:30.900+03:00"
source_bytes: 23702
fetched_at: "2026-09-13T04:13:13+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hızlı Hesap Kodu Açma

Hızlı Hesap Kodu Açma, Muhasebe Bölümünde, "İşlemler/Muhasebe Modülü" menüsünün altında yer alır. Hızlı Hesap Kodu Açma, hesap planı kayıtlarında önceden tanımlanan bir ana hesap ve buna ait alt hesaplar (grup ve muavinler) baz alınarak, aynı yapıda yeni bir ana veya grup hesap oluşturmak için, hesap planı girişinde tek tek hesap kodu tanımlamak yerine kullanılan işlemdir.

![](../../../../../_assets/f0f5361be81ce1a3693f.png)

Hızlı Hesap Kodu Açma ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hızlı Hesap Kodu Açma Ekranı |  |
| --- | --- |
| Baz Alınacak Ana/Grup Hesap | Hesap planında önceden tanımlanan ve aynı yapıda açılacak diğer hesaplar için baz alınacak ana/grup hesabın girildiği alandır. Baz alınacak ana veya grup hesap, altındaki muavin hesaplarla birlikte sadece sabit bilgileri olmak üzere yeni hesap koduna kopyalanır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hesaplar arasından seçim yapılır. |
| Değişiklik Diğer Şirkette | İçinde bulunulan değil, diğer şirkette değişiklik yapılması istendiğinde (hesap planlarının aynı türde oluşturulması kaydı ile) baz alınacak ana ya da grup hesap, diğer şirketin hesap planına, oluşturulacak ana grup hesaba göre transfer olur. |
| Diğer Şirket | "Değişiklik Diğer Şirkette" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Değişikliğin yapılacağı şirket kodunun girilmesini sağlar. **Örneğin** ```text<br>100 (A)<br>``` ```text<br>100-01 (G)<br>``` 100-01-001 (M) hesap açıldığı varsayıldığında, baz alınacak hesap kodu 100, oluşturulacak hesap kodu 200 olursa: ```text<br>200 (A)<br>``` ```text<br>200-01 (G)<br>``` 200-01-001 (M) şeklinde hesaplar oluşturulur. Baz alınacak hesap kodu 100-01, oluşturulacak hesap kodu 100-02 olursa: ```text<br>100-02 (G)<br>``` 100-02-01 (M) şeklinde hesaplar oluşturulur. |
| Oluşturulacak Ana/Grup Hesap | Baz alınacak ana/grup hesap ile aynı yapıda açılacak yeni ana/grup hesap kodunun girildiği alandır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
