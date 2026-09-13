---
title: "MRP Sonuçlarından Depolar Arası Transfer Oluşturma"
page_id: "50668663"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "İşlemler / MRP"
  - "MRP Sonuçlarından Depolar Arası Transfer Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / İşlemler / MRP / MRP Sonuçlarından Depolar Arası Transfer Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ2ZmU1NjNmLTRhNzUtNDI1OC04NzE5LTU4YmJkNDVjYjM0ZSZsaW5rPTIxMjg1ZWUxLWU3OTItNDExZC05NDVkLTgyZDFhZWNkYmRiNiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=46fe563f-4a75-4258-8719-58bbd45cb34e&link=21285ee1-e792-411d-945d-82d1aecdbdb6&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mrp-sonuclarindan-depolar-arasi-transfer-olusturma_50668816_50668663.html"
source_version: "2022-10-21T09:17:13.797+03:00"
source_bytes: 9083
fetched_at: "2026-09-13T04:20:04+00:00"
generator: "netsis-scraper 1.0.0"
---
# MRP Sonuçlarından Depolar Arası Transfer Oluşturma

MRP Sonuçlarından Depolar Arası Transfer Oluşturma, Üretim Bölümü'nde, "İşlemler/MRP" menüsünün altında yer alır. Malzeme Gereksinim Raporu alındıktan sonra mamul, yarı mamul ve hammadeler için, gereksinim miktarlarının stoktan karşılanacak kısmının başka bir depoya transfer edilmesi için kullanılan bölümdür. MRP Uygulaması için yapılması gereken standart bir işlem değildir.

MRP Sonuçlarından Depolar Arası Transfer Oluşturma uygulamasının kullanılması için Stok modülünde yer alan “Lokal Depo Uygulaması” parametresinin işaretlenmesi gerekir.

MRP Sonuçlarından Depolar Arası Transfer Oluşturma ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| MRP Sonuçlarından Depolar Arası Transfer Oluşturma Ekranı |  |
| --- | --- |
| Numara | Oluşacak depolar arası transfer fişinin numarasıdır. Depolar arası transfer bölümünde kullanılan son fiş numarasının bir fazlası program tarafından otomatik olarak getirilir. |
| Giriş Depo Kodu | Gereksinim miktarlarının stoktan karşılanacak kısmının aktarıldığı depo kodudur. Bu alana girilen depo kodunun önceden Stok → Lokal Depo Tanımlama bölümünden tanımlanması gerekir. |
| Çıkış Depo Kodu | Mamul, yarı mamul ya da hammaddeler için gereksinim miktarlarının stoktan karşılanacak kısmının çıkış yapılacağı depo kodudur. Bu alana girilen depo kodunun önceden Stok → Lokal Depo Tanımlama bölümünden tanımlanması gerekir. |
| Tarih | Oluşacak depolar arası transfer fişinin tarihidir. |
| Stoklar Kümüle İşlensin mi? | Plan içerisinde birden fazla tekrarlayan mamul, yarı mamul, ya da hammadde miktarlarının stoktan karşılanacak kısmının toplam rakamları ile aktarılması için kullanılan seçenektir. |
| Proje Kodu | Yardımcı Programlar → Kayıt → Şirket Şube Parametreleri → “Proje Uygulaması Var” parametresi işaretli iken aktif hale gelen alandır. Girilen proje kodu, oluşacak depolar arası transfer fişine aktarılır. Proje kodlarının önceden Muhasebe → Proje Kodu Girişi bölümünden tanımlanması gerekir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Fatura modülünde “Depolar Arası Transfer” fişlerinin oluşturulması için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
