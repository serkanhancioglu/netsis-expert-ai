---
title: "Karbon Ayakizi Hesaplama Eklentisi"
page_id: "80088366"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Karbon Ayakizi Hesaplama Eklentisi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Karbon Ayakizi Hesaplama Eklentisi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM2MjkyYzk0LTkyZDQtNDIyNi1iNWQ4LTk0MTU4YjQxMTBlMiZsaW5rPTIxYmU1YzNiLWM1MTAtNDY5Ny04MDEyLTM4N2UxMWRjNTUzMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c6292c94-92d4-4226-b5d8-94158b4110e2&link=21be5c3b-c510-4697-8012-387e11dc5532&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "karbon-ayakizi-hesaplama-eklentisi_90669560_80088366.html"
source_version: "2022-11-02T14:38:45.903+03:00"
source_bytes: 74911
fetched_at: "2026-09-13T04:24:07+00:00"
generator: "netsis-scraper 1.0.0"
---
# Karbon Ayakizi Hesaplama Eklentisi

Karbon Ayakizi Hesaplama Eklentisi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

9.0.38 sürümü ile Netsis içerisinde desteklenen Karbon Ayak İzi Hesaplama eklentisi ile belli tüketim tiplerinde yapılan işlemlerin karbondioksit salınımına, yani doğaya ne kadar etkisi olduğunu hesaplayabilir, planlamalarınızı bu açıdan gözden geçirebilirsiniz. Karbon Ayak İzi Eklentisi, Netsis ana menüsü üzerindeki eklenti ekle butonuna basılarak, kullanılabilir eklentiler sekmesi üzerinden kullanımda seçeneği işaretlenerek aktif hale getirilebilmektedir.

![](../_assets/88eed480827267b0fffe.png)

Eklenti eklendikten sonra çift tıklanarak açıldığında karşımıza aşağıdaki şekilde ekran çıkacaktır.

![](../_assets/ebd947fea7d505acd8b2.png)

Karbon ayak izi hesaplama ekranı üzerinde 4 farklı tüketim tipi için hesaplama yapılabilmekte ve eklenen her kayıt grid üzerine atılarak "Toplam CO2 Salınımı (Ton)" sahası güncellenmektedir.

Tüketim tipi seçenekleri; Hava ulaşımı, Kara Ulaşımı, Elektrik Tüketimi ve Isınma Değerleridir.

Hava Ulaşımı tüketim tipi seçildiğinde "Uçuş Süresi (Tek Yön-Saat)" ve "Uçuş Sayısı" alanları aktif gelmektedir.

Kara Ulaşımı tüketim tipi seçildiğinde "Yakıt Türü" seçimi yapılabilmekte (Benzin, Dizel, LPG) ve "Yıllık Tüketim (lt)" giriş yapılabilmektedir.

Elektrik Tüketimi tüketim tipi seçildiğinde "Yıllık Toplam Tüketim (KWH)" girişi yapılabilmektedir.

Isınma Değerleri tüketim tipi seçildiğinde ise "Yakıt Türü" seçimi yapılabilmekte (Doğalgaz, Kömür, LPG, Fuel-Oil) ve "Yıllık Toplam Tüketim" bilgisi girilebilmektedir.

Ekranın en alt bölümünde karbon ayak izini azaltmaya yönelik bilgilendirme amaçlı ipuçları gösterilmektedir.

Seçilecek tüketim tipine göre grid üzerinde hesaplanacak "C02 Salınımı (Kg)" ve form üzerindeki "Toplam C02 Salınımı (Ton)" alanları için formüller aşağıdaki şekildedir:

- Hava Ulaşımı (Kg) = (60 \* Uçuş Süresi (saat) \* Uçuş Sayısı \* 0.9488) - 5.4647
- Kara Ulaşımı (Kg) = Yıllık Toplam Tüketim (lt) \* Yakıt Türü Katsayısı (Benzin: 2.239, Dizel: 2.599, LPG: 1.679)
- Elektrik Tüketimi (Kg) = Yıllık Toplam Tüketim (kwH) \* 0.472
- Isınma Değerleri (Kg) : Yıllık Toplam Tüketim \* Yakıt Türü Katsayısı (Doğalgaz: 2.02, Kömür: 2.04, LPG: 1.679, Fuel-Oil: 2.961)
- Toplam CO2 Salınımı (Ton) = (Hava + Kara + Elektrik + Isınma) / 1000

**Örnek uyarlama**

Kara ulaşımı için yakıt türü benzin toplam yıllık tüketimi 15 girilmesi durumunda hesaplamalar aşağıdaki şekildedir.

"CO2 Salınımı (Kg)" değeri 15 \* 2.599 = 38.985 Kg "Toplam C02 Salınımı (Ton)" alanında gösterilecek değer ise 38.985 / 1000 = 0.038985 Ton olacaktır.
![](../_assets/70379ec1e2ff83bca564.png)
Hava ulaşımı için uçuş süresi 4, uçuş sayısı 10 girilmesi durumunda ise; "CO2 Salınımı (Kg)" değeri = (60 \* 4 \* 15 \* 0.9488) - 5.4647 = 3410.2153 Kg "Toplam C02 Salınımı (Ton)" alanında gösterilecek değer ise (3410.2153 + 38.985) / 1000 = 3.449200 Ton

![](../_assets/6e5990f4b34079a63367.png)

Not: Eklenen kayıtlar veri tabanı seviyesinde saklanmamakta olup ekran her açıldığından yeniden hesaplama yapacak şekilde boş gelmektedir. F7 ile satırlarda silme işlemi, F8 ile de yeni kayıt ekleme işlemi yapılabilmektedir.
