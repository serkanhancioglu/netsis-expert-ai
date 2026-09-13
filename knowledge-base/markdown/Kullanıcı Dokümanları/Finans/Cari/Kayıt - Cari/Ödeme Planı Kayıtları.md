---
title: "Ödeme Planı Kayıtları"
page_id: "22805119"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Kayıt / Cari"
  - "Ödeme Planı Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Kayıt / Cari / Ödeme Planı Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ2ZjcxMmI1LTJjNTItNGFiYS1iNTg3LTEwZDYyNzMyMjQ3MyZsaW5rPTE1Y2I4NmNkLTJiOGItNGMwNi1iYmJkLTlkNTk1OWVhMDcwZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=46f712b5-2c52-4aba-b587-10d627322473&link=15cb86cd-2b8b-4c06-bbbd-9d5959ea070d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "odeme-plani-kayitlari_28155905_22805119.html"
source_version: "2022-10-27T15:07:09.537+03:00"
source_bytes: 24115
fetched_at: "2026-09-13T04:07:47+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ödeme Planı Kayıtları

Ödeme Planı Kayıtları, Finans Bölümü'nde Kayıt/Cari menüsünün altında yer alır. Bu uygulama ile, programda tanımlanan ödeme planları "Müşteri Siparişi", "Satış İrsaliyesi" ve "Satış Faturası" bölümüne aktarılır.

"Cari Ödeme Planı" uygulaması ile, sipariş, irsaliye ve faturalarda daha önceden hazırlanmış ödeme planının girişi yapılabilir. Böylece, vade tarihleri ve bu tarihlerde ödenmesi gereken tutarlar, belirlenen ödeme planına göre program tarafından hesaplanır.

Uygulamanın desteklenmesi için; Lojistik-Satış → Fatura → Kayıt → Satış Parametreleri → “C/H vadelere bölünerek geçsin” parametresinin işaretlenmesi ve "Cari Modülünde" bulunan "Ödeme Planı Kayıtları" bölümü kullanılarak ödeme planlarının tanımlanması gerekir.

Ödeme Planı Kayıtları; Ödeme Planı-1, Ödeme Planı-2 ve Ödeme Planı İzleme olmak üzere üç sekmeden oluşur.

**Ödeme Planı-1**

Ödeme Planı Kayıtları ekranı Ödeme Planı-1 sekmesinde, ödeme planları ile ilgili genel tanımlamalar yapılır. Ödeme Planı Kayıtları ekranı Ödeme Planı-1 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ödeme Planı Kayıtları Ekranı |  |
| --- | --- |
| Ödeme Kodu | Tanımlanan ödeme planına için verilen koddur. En fazla 8 karakter olmak üzere alfa numerik veya numerik olarak tanımlanabilir. |
| Açıklama | Tanımlanan ödeme planı ile ilgili açıklamanın girildiği alandır. |
| Kilit | Bu seçeneğin işaretlenmesi halinde, tanımlanan ödeme planı ile ilgili işlem yapılamaz. |
| İşletmelerde Ortak | Ödeme planı hangi işletmede kullanılacaksa o işletmeye ait kod bilgisinin girildiği alandır. Merkez işletme dışındaki tüm işletmelerde, bu alan pasif olur ve içinde bulunulan işletme kodu program tarafından otomatik olarak ekrana getirilir. Ödeme planı tüm işletmelerde kullanılacaksa, -1 değeri girilir. |
| Şubelerde Ortak | Ödeme planı hangi şubede kullanılacaksa o şubeye ait kod bilgisinin girildiği alandır. Ödeme planı tüm şubelerde kullanılacaksa, -1 değeri girilir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.

**Ödeme Planı-2**

Ödeme Planı Kayıtları ekranı Ödeme Planı-2 sekmesinde bulunan alanlar, ödeme planı ile ilgili ayrıntılı tanımlamaların yapılması amacıyla kullanılır. Bir önceki sekmede ( Ödeme Planı-1) belirlenen "Ödeme Kodu" ve buna bağlı açıklama alanı bulunur. Ödeme Planı Kayıtları ekranı Ödeme Planı-2 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ödeme Planı Kayıtları Ekranı |  |
| --- | --- |
| Ödeme Kodu | Ödeme Planı-1 sekmesinde girilen ödeme kodu bilgisinin otomatik olarak aktarıldığı alandır. |
| Vade Tipi | Oluşturulan ödeme planındaki vade tarihlerinin tipinin belirlendiği alandır." Vade Tipi" olarak altı ayrı seçenek bulunur. Alanın sağ tarafında yer alan aşağı ok butonu ile seçenekler arasından tercih yapılır. **Fatura Tarihi:** Vade gününü, faturanın kesildiği gün olarak belirlemek amacıyla kullanılan seçenektir. **Örneğin:** Fatura ayın 10. günü kesilmişse, vade tarihi de ayın 10.günü olur. **Vade Günü:** Girilecek gün sayısına göre vade tarihinin oluşturulması amacıyla kullanılan seçenektir. **Örneğin:** Fatura ayın 10.günü kesildiyse ve Vade Günü değeri 20 ise, Vade Tarihi ayın 30.günü olur. **Sabit Gün:** Ayın belli bir gününün vade tarihi olarak tanımlanması için kullanılan seçenektir. **Örneğin:** Vade Gün değeri 18 ise, Vade Tarihi fatura kesim tarihine bakılmaksızın ayın 18.günü olur. **Son Gün:** Vade tarihini, ayın son günü olarak belirleyen seçenektir. **Son Gün+Vade Günü:** Vade tarihi ayın son günü olarak belirlenip bir sonraki güne, vade günü değeri eklenerek hesaplanır. Ödeme planı oluşturulurken, her ay için farklı vade tipi seçilebilir. |
| Sıra No | Belirlenen vade tarihi ve oranının, ödeme planında kaçıncı sırada yer alacağını belirleyen alandır. Sıra No, program tarafından aktarılır, değiştirilemez. |
| Gün | Vade tarihini belirlerken kullanılacak gün değerinin girildiği alandır. Vade Tipi alanında "Vade Günü" veya "Sabit Gün" seçildiğinde aktif hale gelir. **Örneğin:** "Vade Tipi" alanında "Sabit Gün" seçilerek "Gün" alanına 25 değeri girildiğinde, vade tarihi ayın 25'i olarak düzenlenir. "Vade Günü" seçildiğinde ise, bir önceki vade tarihinden 25 gün sonrası vade tarihi olarak belirlenir. Vade tarihleri oluşturulurken ilk verilen vade tarihi, diğer vade tarihlerinin oluşturulmasında baz alınır. |
| Oran | Belirlenen vade tarihinde, fatura toplamının ne kadarının ödeneceğinin belirlendiği alandır. Ödeme planında yer alan oranların toplamının %100 olması gerekir. |
| Rapor Kodu | Ödeme planı için belirlenen rapor kodu alanıdır. Öncede tanımlanan bir rapor kodu varsa, alanın sağ tarafında yer alan aşağı ok butonu yardımı ile rapor kodları arasından seçim yapılabilir. |
| Öteleme (Ay) | Bu alana yazılan değer kadar vade günü, ay olarak ileri tarihe aktarılır. "Son Gün" ve "Son Gün + Vade Günü" seçenekleri kullanıldığında aktif hale gelir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.

**Ödeme Planı İzleme**

Ödeme Planı İzleme bölümünde, tanımlanan ödeme planı ile ilgili bir modelleme yapılır. Böylece, ödeme planında yapılması gereken değişiklikler daha kolay görülür. Buradaki amaç, belirlenen fatura tarihine ve fatura toplamına göre oluşan ödeme planının izlenmesidir.

Ödeme Planı Kayıtlarının Fatura Modülünde Kullanımı ile ilgili detaylı bilgi için; Finans → Cari → Kayıt → Ek-6 (Ödeme Planı Uygulaması).

| Ödeme Planı Kayıtları |  |
| --- | --- |
| Ödeme Kodu | Ödeme Planı-1 sekmesinde girilen ödeme kodu bilgisinin otomatik olarak aktarıldığı alandır. |
| Fatura Tarihi | Ödeme planı yapılacak faturanın tarih bilgisinin girildiği alandır. |
| Fatura Toplam | Ödeme planı yapılacak faturanın toplam tutar bilgisinin girildiği alandır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin kaydedilmesi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerin iptal edilmesi için kullanılan butondur. |
