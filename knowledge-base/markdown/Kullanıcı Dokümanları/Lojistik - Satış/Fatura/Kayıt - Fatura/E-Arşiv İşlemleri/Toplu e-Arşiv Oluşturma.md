---
title: "Toplu e-Arşiv Oluşturma"
page_id: "50659779"
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
  - "E-Arşiv İşlemleri"
  - "Toplu e-Arşiv Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / E-Arşiv İşlemleri / Toplu e-Arşiv Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPThhNDkzZDI5LTE5NTEtNDMwNS05ZjUzLThjOGFiOWRlYzE5NiZsaW5rPTkzZTZhNmZkLTFjMDAtNGRhNi1hOGE5LWRjNWY4MTM2YmZjYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8a493d29-1951-4305-9f53-8c8ab9dec196&link=93e6a6fd-1c00-4da6-a8a9-dc5f8136bfcb&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "toplu-e-arsiv-olusturma_50659781_50659779.html"
source_version: "2022-10-24T14:49:48.930+03:00"
source_bytes: 96293
fetched_at: "2026-09-13T04:02:20+00:00"
generator: "netsis-scraper 1.0.0"
---
# Toplu e-Arşiv Oluşturma

Toplu e-Arşiv Oluşturma, e-Arşiv tipli satış faturası oluşturulduktan sonra toplu halde e-Arşiv oluşturulması için kullanılan bölümdür. Toplu e-Arşiv Oluşturma; İşlem Tipi, Ön Sorgulama ve Cari Kısıtlar sekmesinden oluşur.

**İşlem Tipi**

Toplu e-Arşiv Oluşturma ekranı İşlem Tipi sekmesindeki alanlar ve içerdiği bilgiler şunlardır:

| Toplu e-Arşiv Oluşturma Ekranı |  |
| --- | --- |
| e-Arşiv Oluşturma İşlem Tipi | e-Arşivin oluşturulacağı işlem tipi sistem tarafından otomatik olarak "Temel Set" seçili gelir. |
| Oluşacak Belgenin Gönderim Şekli e-Posta Olsun | Kaydedilen faturanın e-Posta olarak oluşturulması için kullanılan parametredir. Kullanılacak dizaynda e-Posta ataması yapmak için Dizayn Modülü → Dizayn Kayıtları ekranında yer alan e-fatura XML Tag alanının “Customer-Electronic Mail” olarak seçilmesi gerekir. XSD şema kontrolünden geçirilip ZIP formatı ile sıkıştırılan e-Arşiv faturaları, Zaman Damgası ile mühürlenmek üzere entegratöre "Toplu e-Arşiv Oluşturma" işlemi ile “Oluşacak Belgenin Gönderim Şekli e-Posta Olsun” parametresi seçilerek oluşturulan taslaklar, e-Fatura Listesi ekranındaki gridde, “Gönderim Tipi” kolonu “e-Posta” olarak görüntülenir. |
| Oluşacak Belge İnternet Satış Tipli Olsun | İnternet üzerinden yapılan satışlar için e-Arşiv oluşturulması istendiğinde işaretlenmesi gereken seçenektir. İşaretlendiğinde, açılan gridde sadece internet satış için tanımlanan seriye ait faturalar listelenir.<br>"Taslak Oluşturma" işlemi yapılırken dizayn rehberine, sadece dizayn tipi “e-Arşiv İnternet” olan dizaynlar gelir. Dizayn Tipi “e-Arşiv İnternet” olan dizaynlar için "e-Fatura XML Tag" alanının “AdditionalDocumentReference” seçilmesi ve e-Arşiv için zorunlu alanların (Web Adresi, Ödeme Şekli, Ödeme Aracısı Adı, Ödeme Tarihi, Gönderim Tarihi, Gönderi Taşıyan TCKN/VKN ve Gönderi Taşıyan Unvan Bilgileri) atanması gerekir. Entegratöre iletilen e-Arşiv faturaları, "e-Arşiv Giden Kutusu" ekranından izlenebilir. Bu ekranda belge detayına ulaşılabildiği gibi farenin sağ tuşu ile açılan “Şube Değiştir” seçeneği ile şube kodunda değişiklik yapılabilir, “Kontrol Durumu” ile açıklama bilgisi girilebilir veya “e-Arşiv İptal Faturası Oluştur” ile iptal faturası oluşturulabilir. İptal edilen fatura üzerine tekrar sağ tuşa tıklandığında “Satış Faturası Sil” seçeneği ile satış faturası iptali gerçekleştirilir. Arşivlenmesi için entegratöre iletilen faturaların Zaman Damgası ile mühürlenmiş dosyalarına "Sorgula" butonuna tıklanarak ulaşılabilir. Mühürlenmiş belgelerin basım işlemi ise "Toplu e-Arşiv Basımı" ekranından yapılır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam Butonu | Seçilen alanların kaydedilerek toplu e-Arşiv oluşturulması için kullanılan butondur. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku Butonu | Daha önceden saklanan kısıtların aynısının ekrana tekrar gelmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla Butonu | İşaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Toplu e-Arşiv oluşturulması istenen belgeler için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki toplu e-Arşiv oluşturma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal Butonu | E-Arşiv oluşturulması istenen belgeler için verilen kısıtların iptal edildiği butondur. |

**Ön Sorgulama**

Toplu e-Arşiv Oluşturma ekranı Ön Sorgulama sekmesindeki alanlar ve içerdiği bilgiler şunlardır:

| Toplu e-Arşiv Oluşturma Ekranı |  |
| --- | --- |
| Belge No Aralığı | Toplu e-Arşiv oluşturulması istenen faturaların belge numarası aralığının girildiği alandır. Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) butonu yardımı ile belge numarası seçimi yapılır. |
| Cari Kod Aralığı | Toplu e-Arşiv oluşturulması istenen faturaların cari kod aralığının girildiği alandır. Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) butonu yardımı ile cari kod aralığı seçimi yapılır. |
| Tarih Aralığı | Toplu e-Arşiv oluşturulması istenen faturaların tarih aralığının girildiği alandır. |
| Kod-1/Kod-2 | e-Arşiv'lerin Kod-1/Kod-2 değerlerine göre ekrana gelmesini sağlamak amacıyla kullanılan alanlardır. |
| Cari Grup Kodu | Toplu e-Arşiv oluşturulması istenen faturaların cari grup kodunun seçildiği alandır. Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) butonu yardımı ile cari grup kodu seçimi yapılır. |
| Şubeler Dahil Edilsin | Toplu e-Arşiv oluşturma işlemine şubelerin de dahil edilmesi isteniyorsa işaretlenecek alandır. |
| Proje Kodu Aralığı | Toplu e-Arşiv oluşturulması istenen faturaların proje kod aralığının girildiği alandır. Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) butonu yardımı ile proje kodu seçimi yapılır. |
| Belge Tipi | "Yurt İçi Faturalar Getirilsin" ve "Yurt Dışı Faturalar Getirilsin" olmak üzere iki seçimden oluşur. Aşağı ok butonu yardımıyla belge tipi seçimi yapılır. **"Yurt Dışı Faturalar Getirilsin" seçeneğinin farkı:** Kullanıcının Dış Ticaret lisansı varsa, sadece Dış Ticaret modülünden girilen proforma belgeler ekrana gelir Lisansı yoksa faturadan girilen belgeler ekrana gelir. |
| Gönderici Bilgileri Teslim Cariden Alınsın | Faturada girilen teslim cari bilgilerindeki e-arşiv mükelleflerinin listelenmesi için kullanılan seçenektir. |
| Belgedeki Kalemler Kümüle Edilsin | Stok Adı, buyersidentification alanı, manufacturersidentification alanı, Satır İskontosu, KDV, Fiyat, Tevkifat, Sipariş Bağlantısı veya İrsaliye Bağlantısı aynı olan kalemlerin kümüle edilmesi için kullanılan seçenektir. |
| Satırda İskonto Dikkate Alınmasın | Oluşan e-Arşiv belgelerinin kalem bilgilerindeki mal ve hizmet tutarı alanına brüt fiyat yazılması için kullanılan seçenektir. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam Butonu | Seçilen alanların kaydedilerek toplu e-Arşiv oluşturulması için kullanılan butondur. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku Butonu | Daha önceden saklanan kısıtların aynısının ekrana tekrar gelmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla Butonu | İşaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Toplu e-Arşiv oluşturulması istenen belgeler için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki toplu e-Arşiv oluşturma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal Butonu | E-Arşiv oluşturulması istenen belgeler için verilen kısıtların iptal edildiği butondur. |

**Cari Kısıtlar**

Toplu e-Arşiv Oluşturma ekranı Cari Kısıtlar sekmesindeki alanlar ve içerdiği bilgiler şunlardır:

| Toplu e-Arşiv Oluşturma Ekranı |  |
| --- | --- |
| Kod-1,2,3,4,5 | Toplu e-Arşiv oluşturmak için kod-1,2,3,4,5 kısıdının girildiği alanlardır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam Butonu | Seçilen alanların kaydedilerek toplu e-Arşiv oluşturulması için kullanılan butondur. Butona basılması ile birlikte fatura listesinin yer aldığı ekran açılır. CTRL butonu basılı halde iken, oluşturulması istenen faturanın üzerine tıklanarak, faturaların tek tek seçilmesi sağlanır. SHIFT butonu basılı halde iken, oluşturulması istenen fatura aralığı üzerine tıklanarak, faturaların çoklu seçimi sağlanır. ![](../../../../../_assets/26f10477190948aac2d2.png) Taslak Oluştur ![](../../../../../_assets/0a7b217912e33a3e059a.jpg) butonu ile seçilen faturaların e-fatura taslağı listesi ekrana gelir. Faturaların gönderimi yapılmadan önce, istenirse toplu olarak basımı yapılabilir. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku Butonu | Daha önceden saklanan kısıtların aynısının ekrana tekrar gelmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla Butonu | İşaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Toplu e-Arşiv oluşturulması istenen belgeler için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki toplu e-Arşiv oluşturma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal Butonu | E-Arşiv oluşturulması istenen belgeler için verilen kısıtların iptal edildiği butondur. |
