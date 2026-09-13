---
title: "Ek-2 Demirbaş Paketinde Proje Takibi Uygulaması"
page_id: "24740926"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Ekler / Muhasebe"
  - "Ek-2 Demirbaş Paketinde Proje Takibi Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-2 Demirbaş Paketinde Proje Takibi Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTZkYzI1MTJmLWFiMmQtNDVkOC1iZjI0LTI5NjA0MGQ5YTEwMyZsaW5rPTJlM2E2NDYxLWYzMjgtNDRkZi04Y2EzLTE5YzVjYjk1NDgwYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6dc2512f-ab2d-45d8-bf24-296040d9a103&link=2e3a6461-f328-44df-8ca3-19c5cb95480a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-2-demirbas-paketinde-proje-takibi-uygulamasi_41162361_24740926.html"
source_version: "2022-12-13T08:59:22.837+03:00"
source_bytes: 6916
fetched_at: "2026-09-13T04:14:39+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-2 Demirbaş Paketinde Proje Takibi Uygulaması

Demirbaş Paketinde Proje Takibi Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Çalışılan firmada "Proje Kodu Uygulaması" kullanılıyor ve Demirbaş paketinde de ilgili projede kullanılan demirbaşların takibinin yapılması isteniyorsa, öncelikle demirbaş şirketinin ilişkilendirileceği ticari pakette Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → Parametreler → “Proje Kodu Uygulaması Var” seçeneğinin işaretlenmesi gerekir. Daha sonra, "Demirbaş" paketi ile proje takibi yapılan "Ticari" paketin ilişkilendirilmesi gerekir. İlişkilendirme işleminin yapılması için, Demirbaş paketinin "Parametre Girişi" bölümünde “Entegrasyon Yapılacak” parametresi seçilerek “Veritabanı Bilgileri” bölümünden ilgili ticari paket şirket adının girilmesi gerekir. Veritabanı bilgilerinde tanımlanan ticari şirkette “Proje Kodu Uygulaması Var” parametresi işaretli değilse, "Proje Kodu" ile ilgili alanlar aktif hale gelmez ve dolayısıyla "Proje Kodu Takibi" yapılmaz.

Demirbaş paketinde takip edilen projede, kullanılan demirbaşların, öncelikle Demirbaş → Kayıt → "Demirbaş Bilgi Kartı" bölümünde belirtilmesi gerekir.

Demirbaş hangi projede kullanılıyorsa, "Demirbaş Bilgi Kartı" bölümünde yer alan "Proje Kodu" alanına ilgili proje kodunun girilmesi gerekir. Bu alanda girilen proje kodunun, "Demirbaş" paketi ile entegre çalışan "Ticari" pakette Muhasebe → Kayıt → Proje Kodu Girişi → "Proje Sabit Tanımları" bölümünden tanımlamasının yapılması gerekir. Demirbaş kartı ile proje kodunun ilişkilendirme işlemi yapıldıktan sonra, hangi demirbaşın hangi projede kullanıldığı takip edilebilir.

Demirbaş bilgi kartında proje ile ilgili tanımlama işlemi bittikten sonra, ilgili demirbaşın takip edildiği projede ne kadar süre ile kullanıldığı, "Demirbaş Proje Bilgileri" ekranından tanımlanır.

### Demirbaş Proje Bilgileri

**Proje Kodu:** Takip edilen proje kodunun girildiği alandır. Tanımlanan proje kodu sadece tek bir proje için geçerli olup diğer projeler için kullanılmaz.

**Demirbaş Kodu:** "Proje Kodu" alanında belirtilen projede kullanılan demirbaş kodunun girildiği alandır.

**Başlangıç Tarihi:** "Proje Kodu" alanında belirtilen projede kullanılan demirbaşın, hangi tarihte kullanılmaya başlandığının belirtildiği alandır.

**Bitiş Tarihi:** "Proje Kodu" alanında belirtilen projede kullanılan demirbaşın, hangi tarihte kullanımının sona erdiğinin belirtildiği alandır.

> [!NOTE]
> Başlangıç ve bitiş tarihlerinin tanımlanması ile ilgili, projede hangi demirbaşın hangi tarih aralığında kullanıldığının takibi yapılabilir.

**Başlangıç Saati:** "Proje Kodu" alanında belirtilen projede, demirbaşın hangi saatten itibaren kullanılmaya başlandığının belirtildiği alandır.

**Bitiş Saati:** "Proje Kodu" alanında belirtilen projede, demirbaşın hangi saatte kullanımının sona erdiğinin belirtildiği alandır.

> [!NOTE]
> Başlangıç ve bitiş saatlerinin tanımlanması ile ilgili, projede hangi demirbaşın kaç saat kullanıldığının takibi yapılabilir.

"Demirbaş Proje Bilgileri" ekranında, takip edilen projelerde kullanılan demirbaşların, kullanıldıkları tarih ve süreler tanımlandıktan sonra değerleme ve amortisman ayırma işlemi yapıldığında, ilgili demirbaşın o projede kullanılan amortisman tutarı aşağıdaki şekilde hesaplanır:

Demirbaşın aylık amortisman tutarı: 200,

Demirbaşın ilgili proje için 1 ayda kullanıldığı gün sayısı: 10 olduğu varsayıldığında;

İlgili projede kullanılan demirbaşın amortisman tutarı: 200\*10/30 şeklinde hesaplanır.

"Demirbaş" paketinde ilgili projede kullanılan demirbaşların tanımlaması yapıldıktan sonra, "Ticari" pakette Muhasebe → Raporlar → Proje Takip Raporları → [Proje Detay Rapor](<../Raporlar - Muhasebe/Proje Takip Raporları/Proje Detay Rapor.md>) yada [Proje Kümüle Rapor](<../Raporlar - Muhasebe/Proje Takip Raporları/Proje Kümüle Rapor.md>) alınabilir.
