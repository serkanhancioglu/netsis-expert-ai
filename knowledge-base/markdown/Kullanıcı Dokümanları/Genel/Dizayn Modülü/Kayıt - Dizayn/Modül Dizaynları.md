---
title: "Modül Dizaynları"
page_id: "24752341"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Dizayn Modülü"
  - "Kayıt / Dizayn"
  - "Modül Dizaynları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Dizayn Modülü / Kayıt / Dizayn / Modül Dizaynları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ4Mzg1ZDNhLTQ5MDItNDJjNy05ZjIzLWEzMzc3YTRhOWIxMiZsaW5rPTk3YWI3OGRkLWY1YjUtNDlkMi05YTRjLTM0YWUxODhjNTBlMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=48385d3a-4902-42c7-9f23-a3377a4a9b12&link=97ab78dd-f5b5-49d2-9a4c-34ae188c50e2&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "modul-dizaynlari_24752386_24752341.html"
source_version: "2022-10-17T16:02:37.530+03:00"
source_bytes: 50162
fetched_at: "2026-09-13T04:15:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# Modül Dizaynları

Modül Dizaynları, Genel Bölümü'nde Kayıt/Dizayn Modülü menüsünün altında yer alır. Basım yapılacak modüllerin tanımlandığı ve oluşturulacak dizayn isimlerinin girildiği bölümdür. "Dizayn Kayıtları" bölümünde yer alan sorgulamalar genel amaçlıdır. Kullanıcılar, oluşturacakları dizayn alanlarını kendileri tespit ederek serbestçe tanımlamalarını yaparlar. Oluşturulan dizaynlar, isimleri ile saklanır. İlgili dizaynın modül bağlantısı, bu alandaki "Dizayn Adı" bölümünden yapılır. Aynı modüle ait birden fazla dizayn formu varsa, "Sorulsun mu?" alanının "Evet" olarak işaretlenmesi gerekir. Dizayn oluşturmanın ilk şartı, dizayn isimlerinin tanımlanması ya da "Sorulsun mu?" alanına gereken yanıtın girilmesidir.

![](../../../../_assets/b903fffd6e68cdc34e2a.png)

Modül Dizaynları ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Modül Dizaynları Ekranı |  |
| --- | --- |
| Modül Adı | Dizaynın hazırlanacağı modülün girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile modüller arasından seçim yapılır. |
| Dizayn Adı | Dizaynı oluşturulan modüle ait dizayn isminin girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlı dizaynlar arasından seçim yapılır. Dizaynı oluşturulacak modül için, ilgili dizaynın adı yazıldığında, modülün çıktısının dizayn formu program tarafından aranır ve basımı yapılır. Çıktı basımı alınmayacak olan modül için, "Modül Adı" alanının boş bırakılması gerekir. **Örneğin;** Alış faturası kayıtlarından sonra basım yapılması istenmediği zaman, alış faturaları için herhangi bir dizayn adı girilmez. Eğer bu alana dizayn adı girilip dizayn tanımlaması yapılmamışsa, ilgili bölümden yapılan kayıtta dizayn ismine göre basım yapılmaya çalışılır ama dizayn tanımlaması olmadığı için program hata kodu vererek işlemi sonlandırır. |
| Sorulsun Mu? | Bazı firmalarda birden fazla form dizaynı kullanılır. **Örneğin;** Satış faturalarında farklı seri numarasına göre ya da merkez şube ayrımına göre form dizaynlarında farklılıklar olabilir. Bu tür durumlarda birden fazla dizayn tanımlaması yapılarak, ilgili modüllerden yapılan kayıtlarda "Dizayn Adının" sorgulanması için "Evet" olarak işaretlenmesi gerekir. "Evet" seçeneğinin işaretlenmesi ile, ilgili modülde dizayn basılacağı zaman "Dizayn Adı" sorgulanır ve otomatik olarak "Dizayn Adı" alanında girilen isim, ilgili sorgu ekranına aktarılır. "Hayır" seçeneği işaretlendiğinde ise, ilgili formun sadece "Dizayn Adı" alanında girilen dizayn formuna uygun basılacağı anlamına gelir. Program, ilgili modülden yapılacak basımlarda "Dizayn Adı" sorgulaması yapmaz. "Dizayn Adı" alanında girilen dizayna göre direkt basım yapar. |
| Log Tutulsun | Log Tutulsun "Evet" olarak işaretlendiğinde, dizayn basımlarının "Dizayn" modülünde bulunan "Basım Log Raporu" ile raporlanması sağlanır. Bu sayede, bir belgenin daha önceden basılıp basılmadığı da anlaşılır. |
| Tekrarlı Basım Kontrolü | Tekrarlı basım kontrolü için seçim yapılan alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile; İşleme Devam Et, Onay İste veya Reddet seçenekleri arasından seçim yapılır. |

İlgili kayıtlar girildikten sonra “Kaydet” ![](../../../../_assets/865524a70e225c89c107.jpg) butonu ile kayıt tamamlanır. Açılan bir kayıt, kayıt sil ![](../../../../_assets/2df4b343310bcd16b01e.jpg)butonu ile iptal edilir veya üzerinde değişiklik yapılması için kaydet ![](../../../../_assets/865524a70e225c89c107.jpg) tuşu kullanılarak düzeltilir.

Kaydedilen satır üzerinde değişiklik yapılması istendiğinde, ilgili satırının üzerinde çift tıklayarak seçim yapılması halinde, gerekli alan/alanların üzerinde değişiklik yapılabilir. Kaydedilen satır aynı şekilde seçildikten sonra araç çubuklarında bulunan ![](../../../../_assets/2df4b343310bcd16b01e.jpg) kayıt silme butonu ya da klavyedeki F7 butonu yardımıyla ilgili satır silinir.
