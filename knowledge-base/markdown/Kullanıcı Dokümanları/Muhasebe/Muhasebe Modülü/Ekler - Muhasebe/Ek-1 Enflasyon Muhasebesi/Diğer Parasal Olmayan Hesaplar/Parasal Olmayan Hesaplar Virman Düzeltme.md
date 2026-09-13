---
title: "Parasal Olmayan Hesaplar Virman Düzeltme"
page_id: "24740878"
product: "netsis-3-enterprise"
depth: 7
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Ekler / Muhasebe"
  - "Ek-1 Enflasyon Muhasebesi"
  - "Diğer Parasal Olmayan Hesaplar"
  - "Parasal Olmayan Hesaplar Virman Düzeltme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Diğer Parasal Olmayan Hesaplar / Parasal Olmayan Hesaplar Virman Düzeltme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWU2ODQxMGY1LWNhMmYtNGRkMS04ZDM3LTQ5NTRlMWE0YWQwYiZsaW5rPTg0YTM1YzdlLTUxMzAtNDRhMi04NDk2LWI0ZGMyMmZjM2Y1ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e68410f5-ca2f-4dd1-8d37-4954e1a4ad0b&link=84a35c7e-5130-44a2-8496-b4dc22fc3f5f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "parasal-olmayan-hesaplar-virman-duzeltme_41162249_24740878.html"
source_version: "2022-12-12T16:15:33.717+03:00"
source_bytes: 4328
fetched_at: "2026-09-13T04:14:24+00:00"
generator: "netsis-scraper 1.0.0"
---
# Parasal Olmayan Hesaplar Virman Düzeltme

Parasal Olmayan Hesaplar Virman Düzeltme ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Muhasebe Modülündeki bu adım, [Parasal Olmayan Hesaplar Virman Dekontu / Muhasebe](<Parasal Olmayan Hesaplar Virman Dekontu - Muhasebe.md>) bölümündeki örnekte yer alan düzeltmeleri ve "[Parasal Olmayan Hesaplar Virman Dekontu](<../../../../../Finans/Dekont/Kayıt - Dekont/Parasal Olmayan Hesaplar Virman Dekontu/index.md>)" bölümünden girilen fişleri otomatik düzeltir. Bu işlemden önce, Döviz Çevrim ve Enflasyon Düzeltmesi işlemlerinin çalıştırılması gerekir.

**Yıl Kodu:** İşlemin çalıştırılacağı yılın kodudur.

**Ay Kodu:** İşlemin çalıştırılacağı ayın kodudur.

**Tarih:** Düzeltme işlemi sırasında oluşan yevmiye fişlerinin aktarılacağı tarihtir. Düzeltme ayının son günü ön değer olarak getirilir.

Bu işlemde programın çalışma mantığı şöyledir;

- Dağıtılacak satır/satırların ilgili aydaki birim maliyet değeri, [Parasal Olmayan Hesaplar Enflasyon Raporu](<../../../../../Finans/Dekont/Kayıt - Dekont/Parasal Olmayan Hesaplar Virman Dekontu/index.md>) bölümündeki gibi hesaplanır. Örnekte, 1.215,5
- Dağıtılacak satır/satırların düzeltme farkları, kendi hesaplarına işlenir.

Satır düzeltilmiş değer = Miktar \* Birim Maliyet = 150 \* 1.215,5 = 182.325

Satır fark = Satır düzeltilmiş – Satır TL = 182.325 – 150.000 = 32.325

İşlenen fiş satırı;

| Hesap Kodu | Tutar |
| --- | --- |
| 159-999 | \<32.325\> |

- Maliyet taşınacak satır/satırlardaki parasal hesaplara hiçbir işlem yapılmaz.
- Dağıtılacak satır/satırlar için hesaplanan düzeltme farkı toplamı, karşılık çalışan (dağıtılmayacak satırlardaki tüm parasal olmayan hesaplar) her satıra oranlanarak taşınır. Farklar, bu satırların enflasyon fark hesaplarına işlenir.

Dağıtılacak satırlar toplam düzeltme farkı = 32.325

Örnekte, taşınacak parasal olmayan tek satır olduğu için toplam fark bu satıra taşınır.

İşlenen fiş satırı;

| Hesap Kodu | Tutar |
| --- | --- |
| 150-999 | 32.325 |

- Taşınacak satırların tamamı parasal hesap olursa, farkın tamamı enflasyon düzeltme hesabına taşınır.
