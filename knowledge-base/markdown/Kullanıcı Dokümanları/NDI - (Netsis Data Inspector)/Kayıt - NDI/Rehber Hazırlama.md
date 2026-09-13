---
title: "Rehber Hazırlama"
page_id: "50682733"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "NDI - (Netsis Data Inspector)"
  - "Kayıt / NDI"
  - "Rehber Hazırlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / NDI - (Netsis Data Inspector) / Kayıt / NDI / Rehber Hazırlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTYyZGVlYzQxLWQ5YjUtNDIwNS1hOThjLTZlNDgwMGVkNmNjMSZsaW5rPTM1NTY3M2MxLTU0NjQtNGY0Yi1iMGE5LTQ1ZGMzZTUwZDY4OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=62deec41-d9b5-4205-a98c-6e4800ed6cc1&link=355673c1-5464-4f4b-b0a9-45dc3e50d688&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "rehber-hazirlama_50682735_50682733.html"
source_version: "2022-09-16T09:47:32.540+03:00"
source_bytes: 9201
fetched_at: "2026-09-13T04:20:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Rehber Hazırlama

Rehber Hazırlama bölümü ile, NDI tasarımlarında kullanılacak olan her çeşit rehber tanımlaması yapılabilir, topluca izlenebilir ve yönetilebilir. Rehber Hazırlama bölümünde tanımlanan bir rehber, aynı amaca hizmet eden birçok tasarımda ve bir tasarım içinde birden fazla kullanılabilir. Rehberin tasarıma eklenmesi için VCL/Rehber tuşunun kullanılması gerekir.

Rehber Hazırlama ekranı; Rehber Tanımlama ve Rehber Detay olmak üzere iki sekmeden oluşur.

**Rehber Tanımlama**

Rehber Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Rehber Hazırlama Ekranı |  |
| --- | --- |
| Rehber Kodu | Tanımlanan her rehber için serbest ve tekrarı olmayan bir kod belirlenmesi gerekir. Kullanıcı kendi sistematiğine kodlama yapabilir. Belirlenen kod, dizayn ortamında tasarıma eklenen rehber butonunun rehber kodu özelliğinde belirtilir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlı rehber kodlarına ulaşılır. |
| Açıklama | Tanımlanan rehbere ait açıklama bilgisi girilen alandır. Hatırlatma amacıyla, rehberin içeriği ve kullanım amacı ile ilgili bilgi yazılmasında fayda vardır. |
| Veritabanı Bağlantı Kodu | NDI ile birden fazla veritabanında bulunan tablolar için rehber tanımlanabilir. **Örneğin;** Hem Temelset hem de Personel veritabanlarına ait rehber tanımlanabilir. Her bir veritabanı bağlantısı tanımına bir kod verilir. Bu alanda ise, tanımlanan veritabanı bağlantılarından hangisinin kullanılacağı, veritabanı bağlantı kodu verilerek belirlenir. Tanımlı veritabanı bağlantıları, alanın rehberi aracılığıyla da belirlenebilir. |
| Tablo Adı | Rehber ile ilişkili olan, arama yapılacak ve görüntülenecek tablo ya da View’in veritabanındaki adıdır. Tablo ya da View’in dizayn öncesinde, veritabanında SQL komutları yardımıyla oluşturulması gerekir. |
| Grup Kodu | Hazırlanan rehberlerin gruplanması için, ilgili rehberin içinde yer alacağı grubun belirlendiği alandır. Kullanıcı, kendi sistematiğine göre gruplandırma yapabilir. Herhangi bir grup kodu verilmezse NDI, rehberi GENELREHBER grubu altına alır. |
| Kısıt | Rehberin düzenlendiği tablodaki herhangi bir alana kısıt verilerek, rehberde gelen kayıt kümesinin daraltılması sağlanabilir. Kısıt cümlesi, SQL cümlelerinin, WHERE ile başlayan kısıt bölümünde yazılan formatta olması gerekir. |
| Tuş | Rehber kısayol tuşudur. CTRL ile birlikte, burada belirlenen tuşa basıldığında, rehber aktif hale gelir. |

**Rehber Detay**

Rehber ana tanımları tamamlandıktan sonra ve rehber tanımı ekranda seçiliyken, aynı ekrandaki ikinci sekmeye (Rehber Detay sekmesine) geçilerek rehber alanlarının tanımlamaları yapılır.

Rehber Detay ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Rehber Hazırlama Ekranı |  |
| --- | --- |
| Rehber | Detayları tanımlanan rehberin kodu ve açıklamasının izlendiği alandır. |
| Gösterim Sırası | Tanımlanacak sahanın rehberde kaçıncı sırada getirileceği bilgisinin girildiği alandır. |
| Alan Adı | Rehbere getirilecek olan alanın, tablodaki saha ismi karşılığıdır. |
| Odakla | Rehber açıldığında, arama amaçlı üzerinde durulacak olan sahanın hangisi olacağı belirlenir. **Örneğin;** Kod ve isim bilgilerinden oluşan bir rehberde, ilk saha Kod ve ikinci saha İsim olarak tanımlanmış olabilir. Ancak, sıklıkla isimden arama yapılacağı düşünüldüğü için rehber ilk açıldığında imlecin isim sahası üzerinde durması istenebilir. Rehber için tanımlanan sahalardan sadece bir tanesinin "Odakla" özelliği işaretlenebilir. |
| Dönüş | Rehber kullanılıp, arama sonucu bir kayıt tespit edildikten sonra, rehberden uygulamaya döndürülmesi istenen sahanın hangisi olduğunun belirlenmesi için kullanılan seçenektir. Örneğin; Kod ve İsim bilgilerinden oluşan bir rehberde, kod bilgisinin uygulamaya döndürülmesi istenir. Rehber için tanımlanan sahalardan sadece bir tanesinin "Dönüş" özelliği işaretlenebilir. |
| Açıklama | Rehbere getirilecek olan sahanın rehber sütun başlığıdır. |
| Rehber Test | Tanımlanan rehberin çalışmasını test etmek amacıyla kullanılan butondur. |
