---
title: "Yüklenilen KDV Devir Girişi"
page_id: "50684690"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Kayıt / Muhasebe"
  - "Yüklenilen KDV Devir Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Kayıt / Muhasebe / Yüklenilen KDV Devir Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ5MTc3M2Y5LTUzZTktNGUxNC1iNjFlLWYzMDU2NmMxNjI3YiZsaW5rPWU5NWM0MTlkLWU3YmQtNGZkYi1hZWVhLWQzNzA2ZjNhNDA4OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=491773f9-53e9-4e14-b61e-f30566c1627b&link=e95c419d-e7bd-4fdb-aeea-d3706f3a4088&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yuklenilen-kdv-devir-girisi_50684692_50684690.html"
source_version: "2022-09-28T17:50:05.967+03:00"
source_bytes: 6629
fetched_at: "2026-09-13T04:13:07+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yüklenilen KDV Devir Girişi

Yüklenilen KDV Devir Girişi, yüklenilen KDV uygulamasını kullanan müşterilerin, daha önceki dönemlerde beyan ettiği alış faturalarının, devir girişini yapacakları bölümdür. Yüklenilen KDV Devir Girişi ekranında devir girişinin yapılması zorunlu değildir fakat daha önce beyan edilen faturaların kalan miktarlarını girmek için genel anlamda gerekli bir ekrandır. Ekran ilk açıldığında daha önceden girilmiş kayıtların hepsi akıllı grid üzerinde listelenir.

Yüklenilen KDV Devir Girişi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yüklenilen KDV Devir Girişi Ekranı |  |
| --- | --- |
| Serbest Giriş | "Serbest Giriş" seçeneği işaretlenmezse; devir girişi yapılacak alış faturaları, şirket bilgisi seçilerek, program üzerindeki faturalar üzerinden seçilir. Bu durumda sadece aşağıdaki alanlar aktif hale gelir ve diğer alanlardaki bilgiler program tarafından otomatik olarak ekrana getirilir ve bilgi amaçlı olarak gösterilir. |
| Şirket İsmi | Şirket rehberinde SIRKETLER30 üzerindeki şirket bilgilerinin otomatik getirildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile şirket isimlerine ulaşılır. |
| Alış Fatura No | Alış Fatura No rehberinde Cari Kod ve Fatura No bazında alış faturaları listelenir. Kullanıcı, rehberden seçim yaptığında, alış faturasına ait cari kod ve tarih bilgisi otomatik olarak ekrandaki "Cari Kodu", "Tarih" ve "GGB No" alanlarına program tarafından getirilir. Kullanıcı rehberden seçim yapmayıp fatura numarasını kendisi girerse, aşağıdaki şekilde bir kontrol yapılarak kondisyona göre karar verilir: İlgili fatura numarası için tek bir cariye ait alış faturası bulunuyorsa "Cari Kodu" otomatik olarak ekrana getirilir ve "Tarih", "GGB No", "Resmi Belge No" bilgisi de otomatik gelir. Aksi durumda "Tarih" ve "GGB No" bilgisini "Cari Kodu" seçiminden sonra ekrana getirmek gerekir. |
| Cari Kodu | "Alış Fatura No" bilgisine uygun olarak "Cari Kodu" seçiminin yapıldığı alandır. Cari Kodu rehberinde sadece seçilmiş olan "Alış Fatura Numarası'nda" bulunan cariler listelenir. Rehber üzerinde standart olarak cari rehberinde kullanılan alanlar gösterilir. Cari Kod çıkışında alış faturası kesin olarak belirleneceği için "Tarih", "GGB No" ve "Resmi Belge No" alanın da güncellenmesi gerekir. |
| Resmi Belge No | Serbest Giriş sırasında bu alana kullanıcı e-Belge tipindeki devir girişleri için manuel olarak giriş yapabilir. Girilecek numaranın 16 hane olması zorunludur. |
