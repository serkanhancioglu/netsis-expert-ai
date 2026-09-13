---
title: "Dekont Parametreleri"
page_id: "22805945"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Dekont"
  - "Kayıt / Dekont"
  - "Dekont Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Dekont Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ2OWY0MTY0LTIxMmEtNDU5Ni04NzE1LTc0OTAzYzIzZDE2MyZsaW5rPTc0YzBjNTI2LWE4N2ItNDhkYi04YjNiLTRmNWQ3ODk0Yjk3MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d69f4164-212a-4596-8715-74903c23d163&link=74c0c526-a87b-48db-8b3b-4f5d7894b970&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dekont-parametreleri_22805962_22805945.html"
source_version: "2022-12-01T09:44:22.767+03:00"
source_bytes: 222730
fetched_at: "2026-09-13T04:09:22+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dekont Parametreleri

Dekont Parametreleri, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. Dekont Parametreleri, "Dekont Modülü" ile ilgili parametre tanımlarının yapıldığı bölümdür.

![](../../../../_assets/d041fb7676346fa937db.png)

Dekont Parametreleri ekranının alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Dekont Parametreleri Ekranı |  |
| --- | --- |
| Miktar Girişi Yapılsın | Dekont işlemleri sırasında, tutar bilgilerinin yanı sıra miktar takibi de yapmak isteyen firmaların işaretlemesi gereken parametredir. Bu parametre işaretlendiğinde, bazı dekont kayıtlarında var olan "Miktar" alanları aktif hale gelir ve miktar bilgisi girişi yapılması sağlanır. |
| Ek Açıklama Bilgi Girişi Yapılsın | Kayıt girişi esnasında sorgulanan tek satırlık açıklama bilgisinin yanı sıra ek açıklama girmek isteyen firmaların işaretlemesi gereken parametredir. Bu parametre işaretlendiğinde, "Ek Açıklama" alanları aktif hale gelir. Sadece "Genel Dekont Kaydı" ve "Genel Gider Cari Hesap Fatura Kaydı" bölümleri için geçerlidir. |
| Valör Bilgisi Girişi Yapılsın | Dekont işlemlerinde istenen güne göre valör hesaplatmak isteyen firmaların işaretlemesi gereken parametredir. Parametre işaretlendiğinde, "Genel Dekont Kaydı", "Serbest Meslek Makbuzu" ve "Genel Gider Cari Hesap Fatura Kaydı" ekranlarında "Valör Başlangıç Tarihi" ve "Valör Günü" sorgulanır. Bu bilgilere göre hesaplanan vade tarihi, ilgili cari hareketlerin vade tarihi alanlarına aktarılır. |
| Bakiye Veren Dekonttan Çıkılmasın | Dekont borç ve alacak tutarlarının bakiye vermesi durumunda, bakiye düzeltilmeden dekont ekranından çıkılmaması için kullanılan parametredir. |
| Entegrasyon Açıklamaya Dekont No Yerine Fiş No Atılsın | Entegrasyonda oluşan mahsup fişindeki "Yevmiye Açıklama" alanına, dekont numarası yerine fiş numarasının aktarılması için kullanılan parametredir. |
| Entegrasyon Açıklamaya Dekont/Seri No Otomatik Atılsın | Entegrasyonda oluşan mahsup fişindeki "Yevmiye Açıklama" alanına, dekont numarası veya dekont seri numarasının aktarılması için kullanılan parametredir. |
| Entegrasyona İşlem Tarihi Yerine Entegre Tarihi Atılsın | Girilen dekontun işlem tarihi ne olursa olsun, içinde bulunulan günün tarihi ile entegrasyon havuzuna aktarılması için kullanılan parametredir. |
| Özel Basım | Dekont modülündeki basımlarda programın standart basımının değil, "Dizayn Modülü" kullanılarak yapılan özel dizaynlarının kullanılması için işaretlenen parametredir. |
| Fiş Numaraları İçinde Bulunulan Şube Koduna Göre Oluşturulsun | Dekont kaydı için oluşturulacak fiş numaralarının, şube koduna göre oluşturulması için kullanılan parametredir. |
| Dekont Kaydında B Formu Seçili Gelmesin | Dekont kaydında seçili gelen B Formu seçeneğinin, seçili gelmemesi istendiğinde işaretlenmesi gereken parametredir. DEKONT/BFORM_ISARETLI_GELMESIN özel parametresinin tanımlanması gerekir. Özel parametrenin Değer alanına 0 (sıfır)girildiğinde tüm şirketlerde, "Şirket Kodu" girildiğinde ise sadece o şirkette uygulanması sağlanır. Birden fazla şirkette uygulanması için şirket kodlarının arasına virgül konularak girilmesi gerekir. **Örneğin:** SIRKET1, SIRKET2. |
| Dekont Tamamlama Kullanılmasın | Dekont oluşturduktan sonra tamamlama yapılmaması için kullanılan parametredir. |
| Bakiye Veren Dekont Tamamlanabilsin | Dekont kaydı yapılırken, bakiye veren dekontun tamamlanması için kullanılan parametredir. Parametre işaretlendiğinde, bakiye veren dekonta rağmen "yeni dekont" oluşturma işlemi yapılabilir. |
| KDV Ön Değer (Dahil/Hariç) | "Genel Dekont Kaydı" ve "Genel Gider Cari Hesap Fatura Kaydı" bölümünde sorgulanan KDV alanlarında, ön değerin belirlenmesi için kullanılan parametredir. **Örneğin:** "Dahil" seçeneği işaretlendiğinde KDV alanlarında ön değer olarak "Dahil" seçeneği gelir. |
| İhracat Kapatma Döviz Takibi | Dekonttan ihracat kapatma sırasında, fiili kurun bu parametrede seçilecek alana göre gelmesi için kullanılan parametredir. Fatura Parametrelerini Uygula, Döviz Alış, Döviz Satış, Efektif Alış ve Efektif Satış seçeneklerinden oluşur. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İşaretlenen parametrelerle ilgili işlemlerin gerçekleşmesini sağlayan butondur. Parametrelerle ilgili işlemlerin programa yansıması için programın kapatılıp tekrar açılması gerekir. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | İşaretlenen parametrelerden vazgeçilmesi halinde kullanılan butondur. |
