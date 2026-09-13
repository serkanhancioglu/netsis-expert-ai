---
title: "Entegrasyon Kodları"
page_id: "24740966"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Entegre"
  - "Kayıt / Entegre"
  - "Entegrasyon Kodları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Entegre / Kayıt / Entegre / Entegrasyon Kodları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA3M2MwMWQwLTVjYzMtNGFhOS05YzczLTRmNjQ3OTk4Y2IzZCZsaW5rPWEyMDJjZTYwLTA0ZTAtNDFiYy04ZmU1LTAyZjQxY2UxZWQ1MiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=073c01d0-5cc3-4aa9-9c73-4f647998cb3d&link=a202ce60-04e0-41bc-8fe5-02f41ce1ed52&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "entegrasyon-kodlari_24740997_24740966.html"
source_version: "2022-11-11T15:07:07.197+03:00"
source_bytes: 455474
fetched_at: "2026-09-13T04:14:44+00:00"
generator: "netsis-scraper 1.0.0"
---
# Entegrasyon Kodları

Entegrasyon Kodları, Muhasebe Bölümü'nde, "Kayıt/Entegre" menüsünün altında yer alır. Entegrasyon Kodları, "Ön Muhasebe" modülleri ile "Muhasebe" modülü arasındaki entegrasyonun kurulması için tanımlamaların yapıldığı bölümdür. "Entegrasyon Kodları" ekranı; Fatura Genel, Fatura Genel-2, Fatura İskonto-1, Fatura İskonto-2, Fatura Ek Maliyet, Fatura KDV, Fatura İade KDV, Sigara Uygulaması, Stok/Cari, Senet/Çek ve Genel sekmesinden oluşur.

**Fatura Genel**

Fatura Entegre bölümü; "Fatura" modülünden yapılan işlemlerden, fatura ve depolar arası transfer işlemleriyle ilgili entegrasyon bağlantısının yapılacağı bölümdür.

Entegrasyon Kodları ekranı Fatura Genel sekmesinde yer alan bilgiler aşağıdaki şekildedir:

| Entegrasyon Kodları Ekranı | Fatura Entegre |
| --- | --- |
| Satış Faturaları Entegre | Satış faturaları kayıtlarından oluşacak yevmiye fiş kayıtlarının program tarafından entegrasyon bölümüne işlenmesi için kullanılan seçenektir. İşaretlenmediği zaman, satış faturasının "Ön Muhasebe" modüllerine entegrasyonu yapılır fakat muhasebe kayıtları oluşmaz. |
| Alış Faturaları Entegre | Alış faturaları kayıtlarından oluşacak yevmiye fiş kayıtlarının program tarafından entegrasyon bölümüne işlenmesi için kullanılan seçenektir. İşaretlenmediği zaman, alış faturasının "Ön Muhasebe" modüllerine entegrasyonu yapılır fakat muhasebe kayıtları oluşmaz. |
| Depolar Arası Transfer Entegre | Transfer fiş kayıtlarının (yevmiye maddeleri şeklinde), program tarafından otomatik olarak "Entegre" bölümünde oluşturulması için kullanılan seçenektir. "Depolar Arası Transfer" işlemleri yoksa veya bu işlemlerin muhasebeye otomatik olarak işlenmesi istenmiyorsa, "Depolar Arası Transfer Entegre" seçeneğinin işaretlenmemesi gerekir. "Depolar Arası Transfer" işlemlerinde; programın stoklar için kullanacağı muhasebe hesap kodları, malların "Detay Kodları Tanımlama" bölümündeki "Satış Diğer-3" kodunda tanımlanacak hesap kodu olacaktır. İşlemi yapabilmek için; stoklar muhasebede **detaylı** ise Stok → Kayıt → [Muhasebe Detay Kod Girişi](<../../../Lojistik - Satış/Stok/Kayıt - Stok/Muhasebe Detay Kod Girişi.md>) bölümündeki, **detaylı değil ise** Entegrasyon → Kayıt → Entegrasyon Kodları → Stok/Cari sekmesindeki stoklarla ilgili "Satış Diğer-3" alanına, "Depolar Arası Transfer" işlemlerinin muhasebeleştirilmesinde kullanılması istenen hesap kodlarının girilmesi gerekir. |
| Faturadan Miktarlar Muhasebeye Geçecek | Alış/satış faturalarındaki miktarsal kayıtların, muhasebede stok muavinlerine aktarılması için kullanılan seçenektir. Muhasebeye stok miktarlarının aktarılması sonucu, "Muhasebe" modülünde ön muhasebe ile kontrol amaçlı stok takibi yapma imkanı elde edilerek, miktarsal mizan ve fiş dökümlerinin alınması sağlanır. |
| Ölçü Birimi | “Faturadan Miktarlar Muhasebeye Geçecek“ seçeneğinin işaretlenmesi ile aktif hale gelen seçenektir. Muhasebeye aktarılacak miktarların, stokların ölçü birimi-1, ölçü birimi-2, ölçü birimi-3 değerlerinin hangisi üzerinden hesaplama yapılacağı belirlenir. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| **İskonto Entegre** |  |
| Satış Faturası İskontoları Entegre | Satış faturaları kayıtlarında uygulanan iskonto tutarlarının, muhasebede bir iskonto hesabına veya iskontonun tipine göre ayrı ayrı iskonto hesaplarına aktarılması için kullanılan seçenektir. |
| Alış Faturası İskontoları Entegre | Alış faturaları kayıtlarında uygulanan iskonto tutarlarının, muhasebede bir iskonto hesabına veya iskontonun tipine göre ayrı ayrı iskonto hesaplarına aktarılması için kullanılan seçenektir. |
| Özel Kod-2 İle Değişim | Fatura parametrelerinde "Özel Kod-2" parametresinin işaretlendiği durumlarda, fatura kaydı sırasında girilecek kod-2 alanlarına göre, ayrı kodlu faturaların iskonto tutarlarının ayrı hesaplarda muhasebeleşmesi için kullanılan seçenektir. |
| **Özel Kod 1** |  |
| Özel Kod ile Satış Hesapları Değişsin | Fatura parametrelerinde "Özel Kod-1" parametresinin işaretlendiği ve "Stok Sabit Kayıtları" bölümündeki satış fiyatlarıyla bağlantılı olarak veya değişik amaçlarla sınıflama yapılmak üzere kodlar tanımlandığında, ayrı kodlarla kesilen satış faturası yevmiye kayıtlarının, muhasebede malların ayrı satış hesapları altında oluşturulması için kullanılan seçenektir. Satış faturalarındaki Özel Kod-1 uygulaması ile bağlantılı bir seçenektir. Stokların, ayrı satış hesapları muhasebede detaylı şekilde ise Stok → Kayıt → [Muhasebe Detay Kod Girişi](<../../../Lojistik - Satış/Stok/Kayıt - Stok/Muhasebe Detay Kod Girişi.md>), detaylı değil ise Entegrasyon → Kayıt → [Entegrasyon Kodları](<Entegrasyon Kodları.md>) → "Stok/Cari" sekmesinden tanımlanır. Fatura parametrelerinde tanımlanan "Özel Kod-1" kodları ile stok satış hesaplarının bağlantıları yapıldıktan sonra, muhasebe bağlantıları kurulur. “Özel Kod ile Satış Hesapları Değişsin” parametresi işaretlendiğinde, sorgulamanın hemen altında yer alan "Özel Kod" alanlarının yanına, satış hesabına karşılık gelen "Satış Kodu" girilir. **Örneğin,** Fatura parametrelerinde "Özel Kod-1" olarak stokların peşin satışları için (P), vadeli satışları için de (V) kodu tanımlandığı varsayıldığında ve stoklar için detaylı olarak veya "Entegrasyon" bölümünde "Satış Hesabı" koduna peşin satışların muhasebe hesap kodu, "Satış Diğer-1" koduna da vadeli satışların muhasebe hesap kodu girildiğinde; "Özel Kod ile Satış Hesabı Değişsin" parametresi işaretlenerek, ÖZEL KOD-1: (P), SATIŞ KODU-1: (1), ÖZEL KOD-2: (V), SATIŞ KODU-2: (2) şeklinde kayıt oluşturulması gerekir. |
| Özel Kod ile Alış Hesapları Değişsin | Fatura parametrelerinde "Özel Kod-1" parametresinin işaretlendiği ve "Stok Sabit Kayıtları" bölümündeki alış fiyatlarıyla bağlantılı olarak veya değişik amaçlarla sınıflama yapılmak üzere kodlar tanımlandığında, ayrı kodlarla kesilen alış faturası yevmiye kayıtlarının, muhasebede malların ayrı alış hesapları altında oluşturulması için kullanılan seçenektir. Alış faturalarındaki Özel Kod-1 uygulaması ile bağlantılı bir seçenektir. Stokların, ayrı alış hesapları muhasebede detaylı şekilde ise Stok → Kayıt → Muhasebe Detay Kod Girişi, detaylı değil ise Entegrasyon → Kayıt → [Entegrasyon Kodları](<Entegrasyon Kodları.md>) → "Stok/Cari" sekmesinden tanımlanır. Fatura parametrelerinde tanımlanan "Özel Kod-1" kodları ile stok alış hesaplarının bağlantıları yapıldıktan sonra, muhasebe bağlantıları kurulur. “Özel Kod ile Alış Hesapları Değişsin” parametresi işaretlendiğinde, sorgulamanın hemen altında yer alan "Özel Kod" alanlarının yanına, alış hesabına karşılık gelen "Alış Kodu" girilir. **Örneğin,** Fatura parametrelerinde "Özel Kod-1" olarak stokların peşin alışları için (P), vadeli alışları için de (V) kodu tanımlandığı varsayıldığında ve stoklar için detaylı olarak veya "Entegrasyon" bölümünde "Alış Hesabı" koduna peşin alışların muhasebe hesap kodu, "Alış Diğer-1" koduna da vadeli alışların muhasebe hesap kodu girildiğinde; "Özel Kod ile Alış Hesabı Değişsin" parametresi işaretlenerek, ÖZEL KOD-1: (P), ALIŞ KODU-1: (1); ÖZEL KOD-2: (V), ALIŞ KODU-2: (2) şeklinde kayıt oluşturulması gerekir. |
| **Maliyet Dağıtım** |  |
| Alış Faturalarına Yapılan Dağıtım Entegre Edilsin | Alış faturalarına yapılan maliyet dağıtımının muhasebeye entegre edilmesi için kullanılan seçenektir. |
| Satış Faturalarına Yapılan Dağıtım Entegre Edilsin | Satış faturalarına yapılan maliyet dağıtımının muhasebeye entegre edilmesi için kullanılan seçenektir. |
| Maliyet Dağıtımı Satış Gelir Hesabı | "Satış Faturalarına Yapılan Dağıtım Entegre Edilsin" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, "Satış Hesabı" seçenekleri arasından seçim yapılarak, maliyet dağıtımı satış gelir hesabının belirlenmesini sağlar. |
| Maliyet Dağıtımı Satış İskonto hesabı | "Satış Faturalarına Yapılan Dağıtım Entegre Edilsin" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, "Satış Hesabı" seçenekleri arasından seçim yapılarak, maliyet dağıtımı iskonto gelir hesabının belirlenmesini sağlar. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Fatura Genel-2**

Entegrasyon Kodları ekranı Fatura Genel sekmesinde yer alan bilgiler aşağıdaki şekildedir:

| Entegrasyon Kodları Ekranı | Kanunen Kabul Edilmeyen Giderler (KKEG) |
| --- | --- |
| Gider Hesabı | Gider hesabının tanımlandığı alandır. |
| KKEG | KKEG hesabının tanımlandığı alandır. |
| KDV Detay Hesabı | Binek Oto Uygulaması kapsamında KKEG kullanıldığında, KKEG KDV'sinin ayrı bir kayıt olarak atılmasını sağlayan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodları arasından seçim yapılır. |
| **Alış İçin Geri Kazanım Katılım Payı Desteği (GEKAP)** |  |
| GEKAP Hesabı | Alış belgeleri için muhasebe hesabına gidecek GEKAP hesabının belirlendiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesaplar arasından seçim yapılır. |
| GEKAP İade Hesabı | Alış belgeleri için muhasebe hesabına gidecek GEKAP iade hesabının belirlendiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesaplar arasından seçim yapılır. |
| GEKAP Ambalaj Hesabı | Alış belgeleri için muhasebe hesabına gidecek GEKAP ambalaj hesabının belirlendiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesaplar arasından seçim yapılır. |
| GEKAP İade Ambalaj Hesabı | Alış belgeleri için muhasebe hesabına gidecek GEKAP iade ambalaj hesabının belirlendiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesaplar arasından seçim yapılır. |
| **Satış İçin Geri Kazanım Katılım Payı Desteği (GEKAP)** |  |
| GEKAP Hesabı | Satış belgeleri için muhasebe hesabına gidecek GEKAP hesabının belirlendiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesaplar arasından seçim yapılır. |
| GEKAP İade Hesabı | Satış belgeleri için muhasebe hesabına gidecek GEKAP iade hesabının belirlendiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesaplar arasından seçim yapılır. |
| GEKAP Ambalaj Hesabı | Satış belgeleri için muhasebe hesabına gidecek GEKAP ambalaj hesabının belirlendiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesaplar arasından seçim yapılır. |
| GEKAP İade Ambalaj Hesabı | Satış belgeleri için muhasebe hesabına gidecek GEKAP iade ambalaj hesabının belirlendiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesaplar arasından seçim yapılır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Fatura İskonto-1**

Fatura İskonto-1 sekmesi, "Fatura" modülünde, parametrelerden iskonto kullanımının onaylanması durumunda kullanılacak olan iskontoların entegrasyon bağlantısının yapıldığı sekmedir.

Fatura İskonto-1 sekmesinin aktif hale gelmesi için; "Fatura Genel" sekmesinde yer alan “Satış/Alış Faturası İskontoları Entegre” seçeneklerinin işaretlenmesi gerekir.

Entegrasyon Kodları ekranı Fatura İskonto-1 sekmesinde yer alan bilgiler aşağıdaki şekildedir:

| Entegrasyon Kodları Ekranı |  |
| --- | --- |
| Özel Kod-2 Değeri | Entegrasyon Kodları → Fatura Genel → "Özel Kod-2 ile Değişim" parametresinin işaretlenmesi ile aktif hale gelen alandır. Bir veya birden fazla "Kod-2" değeri için ayrı ayrı iskonto hesapları tanımlanması sağlanır. Bunu gerçekleştirmek için önce, ilk "Kod-2" değerinin girilmesi ve alt kısımdaki iskonto hesaplarının tanımlanmasından sonra tekrar ekranın üst kısımına geçilerek ekrana gelecek olan "Kod-2" değeri alanına ikinci "Kod-2" değerinin girilmesi gerekir. Alt kısıma geçildiğinde, ikinci "Kod-2" değeri için iskonto hesaplarının tanımlanması gerekir. İskonto hesaplarının bu şekilde ayrımının yapılması için, "Fatura" parametrelerindeki "Özel Kod-2" parametresinin işaretlenmesi gerekir. "Fatura" parametrelerindeki “Özel Kod-2 Boş Geçilmesin” parametresi işaretlenmiş ve bu bölümde bir veya birden fazla "Kod-2" değeri yukarıda anlatıldığı şekilde tanımlanmışsa; fatura kayıtları sırasında, "Özel Kod-2" alanına mutlaka burada tanımlanan değerlerden birinin girilmesi gerekir. Aksi halde program gerekli kontrolü yaparak, "Özel kod-2" alanının boş bırakılmasına izin vermez. |
| Satır İskontosu Hesabı | "Fatura" parametrelerinde “Mal Bazı İskontosu” parametresi işaretlendiği ve fatura kayıtlarında satır bazında iskonto kullanıldığı durumlarda, satır iskonto tutarlarının (alış ve satış faturaları için ayrı ayrı) işlenmesi istenen muhasebe alt hesabı için alış/satış hesap kodlarının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Mal Fazlası İskonto Hesabı | "Fatura" parametrelerinde “Mal Fazlası İskontosu” parametresi işaretlendiği ve fatura kayıtlarında mal fazlası (satışta verilen hediye) kullanıldığı durumlarda, mal fazlası iskonto tutarlarının (alış ve satış faturaları için ayrı ayrı) işlenmesi istenen muhasebe alt hesabı için alış/satış hesap kodlarının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Genel İskonto-1, 2, 3 Hesabı | "Fatura" parametrelerinde "Genel İskonto" parametrelerinin işaretlendiği ve fatura kayıtlarında fatura altı iskontolarının kullanıldığı durumlarda, genel iskonto-1, 2, 3 olarak oluşan iskonto tutarlarının (alış ve satış faturaları için ayrı ayrı) işlenmesi istenen muhasebe alt hesabı için alış/satış hesap kodlarının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Fatura İskonto-2**

Fatura İskonto-2 sekmesi, "Muhasebe" modülünde birden fazla iskonto hesabının açılması durumunda (her bir mal veya mal grubu için iskonto hesabı açılmış ise) iskonto bağlantısının yapıldığı sekmedir.

Entegrasyon Kodları ekranı Fatura İskonto-2 sekmesinde yer alan bilgiler aşağıdaki şekildedir:

| Entegrasyon Kodları Ekranı |  |
| --- | --- |
| Mal Bazında İskonto Var Mı? | İskonto hesaplarının, muhasebede her mal için ayrı iskonto hesabı olacak şekilde tutulması için kullanılan seçenektir. |
| Mal Bazında İskonto Tipi | "Mal Bazında İskonto Var Mı?" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Mal bazında detaylı iskonto hesapların işlenecek iskonto tipinin girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, "Satır İskontosu", "Fatura Alt-1 İskontosu" ve "Genel İskonto" seçenekleri arasından seçim yapılır. "Genel İskonto" işaretlendiğinde, iskonto hesabı takibi yine mal bazında olur fakat tüm iskontoların toplamı detaylı olarak takip edilir. |
| Alışta/Satışta İskonto Mal Bazında | Sadece alış iskontoları, sadece satış iskontoları veya her ikisi için de iskontolar mal bazında tutulabilir. Seçeneğin işaretlenmesi ile, detaylı takip yapılacak hesabın belirlenmesi sağlanır. |
| Alışta/Satışta Hangi Satış Kodu (1..7)ın | İskonto hesaplarının mal bazında detaylı takip edilmesi için, malların iskonto kodlarının Stok → Kayıt → Muhasebe Detay Kod Girişi bölümünde, detay kodlarının "Satış Hesabı" veya "Diğer-1, 2, 3, 4, 5, 6, 7, 8" hesabı alanlarına yazılması gerekir. Alış için ayrı, satış için ayrı hesap kodu kullanılacaksa, alanların ikisinin de kullanılması gerekir. İskonto hesabı stokların detaylı takip edilmesi için, kodların "Satış Hesabı" alanına girilmesi halinde (1), Diğer-1, 2, 3, 4, 5, 6, 7, 8 hesaplarından birine girilmesi halinde ise, sırasıyla (2), (3), (4), (5), (6), (7), (8) seçeneklerinden birinin kullanılması gerekir. |
| Alış/Satış İade İskonto Mal Bazında | Bu seçeneğin işaretlenmesi ile İade tipli Alış ve Satış faturalarının iskontolarının hangi hesaplarda mal bazında tutulacağı belirtilecektir. |
| Alış/Satış İade Hangi Satış Kodu (1..7) | İade tipli alış ve satış faturası iskonto hesaplarının detaylandırılması istenen satış kodunun girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçenekler arasından seçim yapılır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Fatura Ek Maliyet**

Fatura Ek Maliyet, "Fatura" parametrelerinde fatura içinde belirtilecek ek maliyetlerin (Nakliye, Ambalaj gibi) açılarak tanımlanması durumunda, ilgili maliyetlerin muhasebe bağlantılarının yapıldığı sekmedir.

Entegrasyon Kodları ekranı Fatura Ek Maliyet sekmesinde yer alan bilgiler aşağıdaki şekildedir:

| Entegrasyon Kodları Ekranı |  |
| --- | --- |
| Alışta Ek Maliyet-1, 2 Hesabı | [Alış Parametreleri](<../../../Lojistik - Satış/Fatura/Kayıt - Fatura/Alış Parametreleri.md>) → "Ek Maliyet" parametrelerinin işaretlendiği ve fatura kayıtlarında fatura altı ilave maliyetlerin kullanıldığı durumlarda, ek maliyet-1, 2 olarak oluşan maliyet tutarlarının (alış ve satış faturaları için ayrı ayrı) işlenmesi istenen muhasebe alt hesabı için alış/satış hesap kodlarının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Alışta/Satışta Ek Maliyet 3 Hesabı | Hal Fatura Uygulaması ile ilgili parametre işaretli iken fatura kaydı işlemine başlandığında "Hal Fatura Tipi" alanı aktif hale gelir. Bu alanda "Komisyoncu" tipi seçilerek kesilen masraflar, "Ek Maliyet 3 Hesabı" alanından izlenir. |
| Satışta Ek Maliyet-1, 2 Hesabı | [Satış Parametreleri](<../../../Lojistik - Satış/Fatura/Kayıt - Fatura/Satış Parametreleri.md>) → "Ek Maliyet" parametrelerinin işaretlendiği ve fatura kayıtlarında fatura altı ilave maliyetlerin kullanıldığı durumlarda, ek maliyet-1, 2 olarak oluşan maliyet tutarlarının (alış ve satış faturaları için ayrı ayrı) işlenmesi istenen muhasebe alt hesabı için alış/satış hesap kodlarının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Alışta/Satışta ÖTV Hesabı | Alış ve satışlarda "Özel Tüketim Vergisi" kullanıldığında, işlenmesi istenen muhasebe alt hesabı için hesap kodu girilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Alışta/Satışta İade ÖTV Hesabı | İade alış ve satışlarda "Özel Tüketim Vergisi" kullanılıyorsa, kullanıldığında, işlenmesi istenen muhasebe alt hesabı için hesap kodu girilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. Hesap kodları, seviye takibine göre kodlanır. |
| Alışta/Satışta ÖTV Satış Kodu | ÖTV tutarının işleneceği hesabın satış kodunun girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, satış kodları arasından seçim yapılır. Alış ve satışlarda "Özel Tüketim Vergisi" tutarlarının işleneceği muhasebe hesabı, diğer alanlardan da tanımlanacağı gibi, istendiğinde stok detay kodlarındaki satış hesaplarından da takip edilebilir. |
| Alışta/Satışta ÖTV Tevkifat Hesabı | Alış ve satışlarda "ÖTV Tevkifatı" kullanıldığında, işlenmesi istenen muhasebe alt hesabı için hesap kodu girilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Alışta/Satışta İade ÖTV Tevkifat Hesabı | İade alış ve satışlarda "ÖTV Tevkifatı" kullanılıyorsa, kullanıldığında, işlenmesi istenen muhasebe alt hesabı için hesap kodu girilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Fatura KDV**

Fatura KDV, işletmenin kullandığı KDV oranlarına göre, muhasebe bağlantılarının yapılmasını sağlayan sekmedir. Bir veya birden fazla KDV oranına göre tanımlama yapılabilir.

![](../../../../_assets/5d57a02c39b4cf4336a5.png)

Entegrasyon Kodları ekranı Fatura KDV sekmesinde yer alan bilgiler aşağıdaki şekildedir:

| Entegrasyon Kodları Ekranı |  |
| --- | --- |
| Değişik KDV Oranları | Stoklarda kullanılan değişik KDV oranlarına göre, fatura kaydı sırasında oluşan KDV tutarlarının ayrı muhasebe kodları altında muhasebeleştirilmesi için kullanılan seçenektir. Muhasebe hesap planındaki oranlara göre ayrı ayrı değil de, tek bir indirilecek KDV ve tek bir ödenecek KDV hesabı kullanıldığında kullanılmaması gerekir. |
| KDV Oranı Sayısı | "Değişik KDV Oranları" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Muhasebe kodunun tanımlanacağı KDV oranı sayısının girildiği alandır. En fazla 5 farklı KDV oranı için muhasebe kodu girişi yapılabilir. |
| Mal Bazında KDV | "Değişik KDV Oranları" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. KDV muavin hesaplarının, stok kartı bazında takip edilmesi için kullanılır. Bu tür uygulamalarda program, alış/satış faturalarının muhasebe kodlarını stok detay kodlarındaki "Diğer-2" ve "Diğer-3" alanlarından okuyarak entegre eder. Program, "Mal Bazında KDV" uygulamasının gerektirdiği zorunlulukları uyarı ekranı ile belirtir. "Mal Bazında KDV" uygulaması yapılmasının ilk şartı, stok alış ve satış hesaplarının muhasebede muavin bazında detaylı tutulması ve Entegrasyon Kodları → Stok/Cari sekmesinde “Mal Alış/Satış Hesapları Detaylı ” seçeneğinin işaretlenmesidir. Stok → Kayıt → "Muhasebe Detay Kod Girişi" bölümünden mallar bazında detay kodu tanımlamasının yapılması gerekir. Stokların, muhasebe detay kodları "Diğer-2" alanına ödenen (alış faturaları için entegre edilecek KDV hesap kodu), "Diğer-3" alanına da hesaplanan (satış faturalarında entegre edilecek olan KDV muhasebe hesap kodu) hesap kodunun girilmesi gerekir. Fatura işlemlerinde, iskonto tutarları muhasebeye entegre edildiğinde ve bu uygulama kullanıldığında, program stokların KDV tutarını iskontoyu düşerek hesaplayamaz. KDV tutarı iskontosuz matrah üzerinden hesaplanacağı için, malların KDV hesaplamalarında hatalar oluşur. Bu nedenle, fatura işlemlerinde mal bazında iskonto ya da fatura altı iskonto kullanılıyorsa bu özelliğin kullanılmaması gerekir. |
| KDV Oranı | Muhasebe hesap kodları tanımlanacak KDV oranlarının, oran olarak değerinin girildiği alandır. **Örneğin,** %18 KDV oranı için muhasebe hesap kodları tanımlanacağı zaman 18 değerinin girilmesi gerekir. |
| İndirilecek, Hesaplanan KDV Hesabı | Fatura kaydı sırasında, oranı yazılan KDV ile ilgili oluşacak tutarların, muhasebede indirilecek ve ödenecek olmak üzere işlenmesi istenen muhasebe hesap kodlarının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Fatura İade KDV**

![](../../../../_assets/41fe3ce604a17ed0697d.png)

Entegrasyon Kodları ekranı Fatura İade KDV sekmesinde yer alan bilgiler aşağıdaki şekildedir:

| Entegrasyon Kodları Ekranı |  |
| --- | --- |
| İade KDV Oranı | "Alış/Satış İade Fatura" işlemlerinde, "İade KDV Oranları" alanına "Fatura KDV" sekmesinde tanımlanan KDV oranlarının otomatik olarak ekrana geldiği alandır. Üzerinde değişiklik yapılabilir. |
| İndirilecek/Ödenecek KDV Hesabı | "Alış/Satış İade Fatura" işlemlerinde İade KDV tutarlarının aktarılacağı hesapların girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. "Fatura KDV" sekmesinde girilen KDV oranlarının sıralamasına bağlı kalınması gerekir. İade KDV'de oran bazında ayrım yapılmışsa, "Fatura KDV" sekmesinde girilen ilk KDV oranına göre, bu alana da söz konusu KDV’nin iade hesabının girilmesi gerekir. Kaç adet KDV hesabı kullanılıyorsa, "Fatura KDV" sekmesinde hepsi tanımlanır. "Fatura İade KDV" sekmesinden de, kullanılan KDV oranlarının hepsinin iade karşılık hesapları girilir. Program, iade işlemlerinde bu alanda girilen hesapları baz alarak, KDV tutarlarını bu sekmeden girilen hesap kodlarına entegre eder. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Sigara Uygulaması**

Sigara Uygulaması sekmesindeki her bir alanın tanımı, programa özel parametre olarak eklenir.

Tanımlanacak Özel Parametreler aşağıdaki şekildedir:

```text
Grup Kodu                 Anahtar                         Değer
```

```text
1) FATURA                 SIGARA_KDV                       0
```

```text
2) FATURA                 SIGARA_CARI                    Cari kartlardaki rapor kodlarından ya da Kullanıcı Tanımlı Sahalardan bir tanesi girilir. (Cari kartlarda da bu alana SIGARA yazılır)
```

```text
3) FATURA                 SIGARA_STOK                   Stok kartlarındaki rapor kodlarından ya da Kullanıcı Tanımlı Sahalardan bir tanesi girilir. (Stok kartlarda da bu alana SIGARA yazılır)
```

```text
4) FATURA                 SIGARA_ENTEGRASYON   1.....8 (Stok Detay Kodundaki Satış Diğer hesaplarından biri girilir)
```

```text
5) FATURA                 SIGARAKDVKODU             391-01-001 (direkt KDV hesabı girilir)
```

4 numaralı özel parametre, stok bazında KDV uygulandığı zaman kullanılır.

5 numaralı özel parametre ise, sabit bir KDV hesabı olduğu zaman kullanılır. Her iki durumda da ikinci olarak hesaplanan KDV, entegrasyon parametrelerindeki KDV hesap kodlarından aktarılır.

![](../../../../_assets/f88c741f635363514829.png)

Entegrasyon Kodları ekranı Sigara Uygulaması sekmesinde yer alan bilgiler aşağıdaki şekildedir:

<table>

<tbody>
<tr>
<th>Entegrasyon Kodları Ekranı</th>
<th> </th>
</tr>
<tr>
<td>Sigara Özel KDV Uygulaması</td>
<td>Sigara Özel KDV Uygulamasını aktif hale getirmek için kullanılan seçenektir.</td>
</tr>
<tr>
<td>Sigara KDV Muhasebe Kodu</td>
<td>

<p>"Sigara Özel KDV Uygulaması" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, muhasebe kodları arasından seçim yapılır.</p>

</td>
</tr>
<tr>
<td>Sigara KDV İade Muhasebe Kodu</td>
<td>

<p>"Sigara Özel KDV Uygulaması" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, muhasebe kodları arasından seçim yapılır.</p>

</td>
</tr>
<tr>
<td>Sigara Entegrasyon Satış Hesap Kodu Alanı</td>
<td>"Sigara Özel KDV Uygulaması" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile "Satış Diğer 1,......,8" seçenekleri arasından seçim yapılır.</td>
</tr>
<tr>
<td><strong>Sabit Kartlarında "SIGARA" Yazılacak Alan</strong></td>
<td> </td>
</tr>
<tr>
<td>Cariler İçin/Stoklar İçin</td>
<td>
<p>Stokun nihai satış fiyatı; stok kartındaki "Satış Fiyatı 4" alanına (özel fiyat sistemi varsa fiyat listesinde yine 4. fiyata nihai satış fiyatı yazılır), stokun bayi fiyatı; kullanılmakta olan satış fiyatına, stok kartlarında; özel parametre alanına SIGARA_STOK, cari kartlarında; özel parametre alanına SIGARA_CARI tanımlandığında hesaplamanın yapılışı aşağıdaki şekilde gerçekleşir:</p>

<table>
<tbody>
<tr>
<th> </th>
<th>A</th>
<th>B</th>
<th>C</th>
<th>D</th>
</tr>
<tr>
<td>1</td>
<td>Nihai Satış Fiyatı</td>
<td>18.000</td>
<td>KDV Dahil</td>
<td>Satış Fiyatı 4</td>
</tr>
<tr>
<td>2</td>
<td>Bakkala Satış Fiyatı </td>
<td>14.080</td>
<td>KDV Dahil</td>
<td>Satış Fiyatı</td>
</tr>
<tr>
<td>3</td>
<td> </td>
<td>2.746</td>
<td>KDV</td>
<td>= B1-(B1/1,18)</td>
</tr>
<tr>
<td>4</td>
<td> </td>
<td>11.334</td>
<td>600 Gelir Hesabı</td>
<td>= B2-B3</td>
</tr>
<tr>
<td>5</td>
<td> </td>
<td>2.040</td>
<td>391 X Hesabı</td>
<td>= B4*0,18</td>
</tr>
<tr>
<td>6</td>
<td> </td>
<td>706</td>
<td>391 Y Hesabı</td>
<td>= B3-B5</td>
</tr>
<tr>
<td colspan="1">7</td>
<td colspan="1"> </td>
<td colspan="1">14.080</td>
<td colspan="1"> </td>
<td colspan="1">= B4+B5+B6</td>
</tr>
</tbody>
</table>

</td>
</tr>
<tr>
<td colspan="1">

<p><img src="../../../../_assets/39d77b8716226638d9ce.jpg"/> Tamam</p>

</td>
<td colspan="1">Girilen bilgilerin onaylanmasını sağlayan butondur.</td>
</tr>
<tr>
<td colspan="1">

<p><img src="../../../../_assets/973111d004995dca0113.jpg"/> İptal</p>

</td>
<td colspan="1">Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur.</td>
</tr>
</tbody>
</table>

**Stok/Cari**

Stok/Cari sekmesi, stokların ve cari hesapların muhasebe entegrasyon bağlantısını yapmak için gerekli tanımlamaların yapıldığı sekmedir. "Stok" ve "Cari" modüllerinde hareket kaydı elle (manuel) yapılan kayıtlar, genel muhasebeye entegre olarak işlenmez. Bu sekmede yapılacak tanımlamalar ile, "Fatura", "Kasa", "Dekont" gibi bölümlerden yapılan entegre kayıtlardan stokları ve/veya cari hesapları ilgilendiren muhasebe maddelerinin doğru oluşması sağlanır. Yapılacak tanımlamalara göre, "Cari" ve "Stok" modüllerinde ayrıca bir bağlantı yapılıp yapılmayacağı belirlenir.

![](../../../../_assets/ccda9973389eb6bb7dc1.png)

Entegrasyon Kodları ekranı Stok/Cari sekmesinde yer alan bilgiler aşağıdaki şekildedir:

| Entegrasyon Kodları Ekranı |  |
| --- | --- |
| Mal Alış Hesabı Detaylı | Stoklarla ilgili alış faturalarından kaynaklanan muhasebe kayıtlarının oluşturulması sırasında, tek bir alış hesabı kullanılması için işaretlenen seçenektir. Mal alış hesapları birden fazla ve stok kayıtları/grupları bazında değişkenlik gösteriyorsa "**Mal Alış Hesabı Detaylı"** seçeneği işaretlenerek, detaylı tanımlamanın Stok → Kayıt → Muhasebe Detay Kod Girişi bölümünden yapılması gerekir. |
| Mal Alış Hesabı | "Mal Alış Hesabı Detaylı" seçeneği işaretlenmediği zaman aktif hale gelen alandır. Muhasebe hesap planındaki tek mal alış hesabının hesap kodu girilir. Tüm malların alış faturalarının stoklarla ilgili kayıtları, girilecek hesaba işlenir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Satıştan İade Hesabı | "Mal Alış Hesabı Detaylı" seçeneği işaretlenmediği zaman aktif hale gelen alandır. Muhasebe hesap planındaki tek iade alış hesabının hesap kodu girilir. Tüm malların satıştan iade faturalarının "Alış Faturaları" bölümünden oluşturulacak stoklarla ilgili kayıtlarının işlendiği hesaptır. "Alış Faturaları" bölümünden girilen iade fatura kayıtları için, "Satıştan İade Hesabı" alanına girilen muhasebe kodu kullanılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg)ile, hesap kodları arasından seçim yapılır. |
| Mal Satış Hesabı Detaylı | Stoklarla ilgili satış faturalarından kaynaklanan muhasebe kayıtlarının oluşturulması sırasında, tek bir satış hesabı kullanılması için işaretlenen seçenektir. Mal satış hesapları birden fazla ve stok kayıtları/grupları bazında değişkenlik gösteriyorsa "**Mal Satış Hesabı Detaylı"** seçeneği işaretlenerek, detaylı tanımlamanın Stok → Kayıt → [Muhasebe Detay Kod Girişi](<../../../Lojistik - Satış/Stok/Kayıt - Stok/Muhasebe Detay Kod Girişi.md>) bölümünden yapılması gerekir. |
| Mal Satış Hesabı | Mal Satış Hesabı Detaylı" seçeneği işaretlenmediği zaman aktif hale gelen alandır. Muhasebe hesap planındaki tek mal satış hesabının hesap kodu girilir. Tüm malların satış faturalarının stoklarla ilgili kayıtları, girilecek hesaba işlenir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. Stok satış hesapları ayrı satış fiyatlarından kesilen faturalar veya herhangi bir amaçla belirlenecek bir kodlamaya göre ayrı kodlarla kesilen faturalar bazında farklılaşma gösterecekse, satış hesabı olarak dört ayrı satış hesabı tanımlanabilir. Bu hesaplar "Fatura" modülünde belirlenecek kodlarla bağlanabilir. Faturaların kodlama işlemi "Fatura" modülünden yapılır. Bu uygulama için, Satış Parametreleri → "Özel Kod-1" alanı kullanılır. "Özel Kod-1" alanında, fatura kaydı sırasında ayrı satış hesaplarına aktarılacak faturalar için ayrı birer kod belirlendikten sonra, stokların her bir özel koda karşılık gelen satış hesapları da "Mal Satış Hesabı" ile "Diğer Satış Hesapları" alanlarında tanımlanır. Son işlem olarak, Entegrasyon Kodları → Fatura Genel sekmesinde tanımlanan "Özel Kod-1" ile, tanımlanan satış hesaplarını bağlama işleminin yapılması gerekir. Böylece, Özel Kod-1 değerinden herhangi birine karşılık gelen bir satış hesabı kodu belirlenir. |
| Alıştan İade Hesabı | "Mal Satış Hesabı Detaylı" seçeneği işaretlenmediği zaman aktif hale gelen alandır. Muhasebe hesap planındaki tek iade satış hesabının hesap kodu girilir. Tüm malların satıştan iade faturalarının "Satış Faturaları" bölümünden oluşturulacak stoklarla ilgili kayıtlarının işlendiği hesaptır. "Satış Faturaları" bölümünden girilen iade fatura kayıtları için, "Alıştan İade Hesabı" alanına girilen muhasebe kodu kullanılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg)ile, hesap kodları arasından seçim yapılır. |
| Diğer Satış Hesabı-1, 2, 3 | Mal Satış Hesabı Detaylı" seçeneği işaretlenmediği zaman aktif hale gelen alandır. Muhasebe hesap planındaki tek mal satış hesabının hesap kodu girilir. "Mal Satış Hesabı" alanında olduğu gibi, herhangi bir amaçla ayrı kodlarla kesilen faturaların ayrı satış hesaplarında muhasebeleşmesi ve birden fazla satış hesabı tanımlamak için kullanılan alanlardır. Satış Parametreleri → "Özel Kod-1" kodlarına karşılık gelecek hesap kodları Diğer-1, Diğer-2, Diğer-3 seçenekleri altında tanımlandıktan sonra, Entegrasyon Kodları → Fatura Genel sekmesinden özel kodlar ile satış hesapları bağlanabilir. Tek satış kodunun bulunduğu durumlarda, diğer bütün satış kodları mal satış hesap kodunun aynısı olabilir. Diğer satış hesapları fatura kodlamaları bazında ve birden fazla satış hesabı tanımlanması dışında; Fatura → İşlemler → Depolar Arası Transfer işlemi, Üretim modülü, Entegrasyon/İskonto hesaplarının gruplandırılması gibi bölümlerde yedek hesap kodları olarak da kullanılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Müşteri Hesabı Detaylı | "Cari Hesap Kayıtları" bölümünde yer alan "Tip" alanı (A)lıcı ve (D)iğer olan kayıtlar için tanımlama yapılan alandır. Müşterilerle ilgili, ön muhasebedeki "Fatura", "Dekont", "Kasa" gibi bölümlerden kaynaklanan muhasebe kayıtlarının oluşturulması sırasında, kullanılması istenen müşteriler hesabı, tüm müşteriler için tek ise, "**Müşteri Hesabı Detaylı"** seçeneğinin işaretlenmemesi gerekir. Müşteri hesapları birden fazla ve cari hesap kayıtları/grupları bazında değişkenlik gösterdiğinde; "Müşteri Hesabı Detaylı" seçeneği işaretlenerek, detaylı tanımlama Cari → Kayıt → Cari Hesap Kayıtları → Cari Kart 2 → "Muhasebe Kodu" alanlarına, ilgili hesap kodları girilir. |
| Müşteri Hesabı | "Müşteri Hesabı Detaylı" seçeneği işaretlenmediği zaman aktif hale gelen alandır. Muhasebe hesap planındaki tek müşteri hesap kodu girilir. Tüm müşteriler için entegre bölümlerden oluşan cari hesaplarla ilgili kayıtlar, "Müşteri Hesabı" alanında belirlenen hesaba işlenir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Satıcı Hesabı Detaylı | Cari Hesap Kayıtlarında bulunan "Tip" alanı (S)atıcı olan kayıtlar için tanımlama yapılacak alandır. Ön muhasebede Fatura, Dekont, Kasa gibi bölümlerden kaynaklanan muhasebe kayıtlarının oluşturulması sırasında, kullanılması istenen satıcılar hesabı tüm satıcılar için tek ise, "Satıcı Hesabı Detaylı" seçeneğinin işaretlenmemesi gerekir. Satıcı hesapları birden fazla ve cari hesap kayıtları veya grupları bazında değişkenlik gösterdiğinde "Satıcı Hesabı Detaylı" seçeneği işaretlenerek, detaylı tanımlamanın Cari → Kayıt → Cari Hesap Kayıtları →Cari Kart 2 sekmesinde yer alan "Muhasebe Kodu" alanlarına ilgili hesap kodlarının girilerek yapılması gerekir. |
| Satıcılar Hesabı | "Satıcı Hesabı Detaylı" seçeneği işaretlenmediği zaman aktif hale gelen alandır. Muhasebe hesap planındaki tek satıcı hesap kodu girilir. Tüm satıcılar için entegre bölümlerden oluşan cari hesaplarla ilgili kayıtlar, "Satıcılar Hesabı" alanında belirlenen hesaba işlenir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. Müşteri veya satıcı hesaplarının detaylı takip edilmediği durumlarda; Entegrasyon Modülü → Müşteri-Satıcı Borç/Alacak Mahsup fişlerine, söz konusu alanda girilen müşteri veya satıcı hesap kodları aktarılmaz. Dolayısı ile, ilgili mahsup fişlerinde borç/alacak tutmaz. Sadece, entegrasyondaki mahsup fişlerinin muhasebeye aktarılması sırasında ilgili hesaplar kullanılır ve mahsup bakiyeleri eşitlenir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Senet/Çek**

Entegrasyon Kodları Senet/Çek sekmesi, Senet/Çek modüllerinden yapılan kayıtların muhasebeye entegrasyonunu sağlamak için gerekli tanımlamaların yapıldığı sekmedir.

![](../../../../_assets/7a95c00858b67810f095.png)

Entegrasyon Kodları ekranı Senet/Çek sekmesinde yer alan bilgiler aşağıdaki şekildedir:

| Entegrasyon Kodları Ekranı |  |
| --- | --- |
| Müşteri Senetleri Entegre | "Müşteri Senetleri" modülünden giriş/çıkışları oluşturulan senet kayıtlarının muhasebeye entegre işlenmesi için kullanılan seçenektir. |
| Müşteri Senetleri Hesabı | "Müşteri Senetleri Entegre" seçeneği işaretlendiğinde aktif hale gelen alandır. Muhasebe Hesap Planı girişinde tanımlanan, müşteri senetlerinin takip edildiği hesap kodunun girilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Borç Senetleri Entegre | "Borç Senetleri" modülünden ciro ve ödentileri oluşturulan borç senetleri kayıtlarının, muhasebeye entegre işlenmesi için kullanılan seçenektir. |
| Borç Senetleri Hesabı | "Borç Senetleri Entegre" seçeneği işaretlendiğinde aktif hale gelen alandır. Muhasebe Hesap Planı girişinde tanımlanan, borç senetlerinin takip edildiği hesap kodunun girilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Müşteri Çekleri Entegre | "Müşteri Çekleri" modülünden giriş/çıkışları oluşturulan çek kayıtlarının muhasebeye entegre işlenmesi için kullanılan seçenektir. |
| Müşteri Çekleri Hesabı | "Müşteri Çekleri Entegre" seçeneği işaretlendiğinde aktif hale gelen alandır. Muhasebe Hesap Planı girişinde tanımlanan, müşteri çeklerinin takip edildiği hesap kodunun girilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Borç Çekleri Entegre | "Borç Çekleri" modülünden ciro ve ödentileri oluşturulan borç çekleri kayıtlarının muhasebeye entegre işlenmesi için kullanılan seçenektir. |
| Borç Çekleri Hesabı | "Borç Çekleri Entegre" seçeneği işaretlendiğinde aktif hale gelen alandır. Muhasebe Hesap Planı girişinde tanımlanan, borç çeklerinin takip edildiği hesap kodunun girilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Kur Farkı Borç Hesabı | "Çek ve Senet Parametreleri" bölümlerinde yer alan “Döviz Uygulaması Var” parametresinin işaretlenerek, döviz tutarları ile kayıt girişi yapan firmalar için kullanılacak çek/senet kayıtlarının kayıt tarihi ve ödenme tarihi arasında oluşan kur farkı tutarlarının aktarılacağı muhasebe hesap kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile hesap kodları arasından seçim yapılır. Bu bölüm, "Dekont" modülünden yapılan "Çek/Senet İşlemleri" sonucu ortaya çıkan kur farkı için de geçerlidir. "Dövizli Çekler Kur Farkı Kaydı" bölümünün çalıştırıldığı durumlarda oluşan kur farkı tutarları, "Kur Farkı Borç Hesabı" alanında belirlenen hesaba entegre edilir. Alanın boş bırakılması, ilgili bölümün çalıştırılması ile oluşan kur farkı tutarlarının muhasebede herhangi bir hesaba aktarılmamasına sebep olacağı için yevmiye fişlerinde fark tutarı oluşur. |
| Kur Farkı Alacak Hesabı | "Müşteri Çekleri/Müşteri Senetleri Parametreleri" bölümlerinde yer alan “Döviz Uygulaması Var” parametresinin işaretlenerek, senet/çek bilgilerini döviz birimleri tutarları ile kayıt yapan firmalar için kullanılacak çek/senet kayıtlarının kayıt tarihi ile ödenme tarihi arasında oluşan kur farkı tutarlarının aktarılacağı muhasebe hesap kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. Bu bölüm, "Dekont" modülünden yapılan "Çek/Senet İşlemleri" sonucu ortaya çıkan kur farkı için de geçerlidir. "Dövizli Çekler Kur Farkı Kaydı" bölümünün çalıştırıldığı durumlarda oluşan kur farkı tutarları, "Kur Farkı Alacak Hesabı" alanında belirlenen hesaba entegre edilir. Alanın boş bırakılması, ilgili bölümün çalıştırılması ile oluşan kur farkı tutarlarının muhasebede herhangi bir hesaba aktarılmamasına sebep olacağı için yevmiye fişlerinde fark tutarı oluşur. |
| Dövizli Senet/Çek İçin Özel Hesap Kodu Uygulaması Var Mı? | Müşteri çek/senet ve borç çek/senetleri dövizli takip eden firmalar için, senet ve çeklerin döviz tiplerine göre ayrı hesaplarda takip edilmesi için kullanılan seçenektir. Seçeneğin işaretlenmesinin dışında, muhasebe hesap planında çek ve senetler için döviz tiplerine göre muavin hesapların açılması gerekir. Program girilen senet/çek için belirlenen döviz tipini entegrasyon modülündeki muavin hesap kodunun son dijitine aktarır. **Örneğin,** Borç çeklerinin "Entegrasyon" modülündeki hesap kodunun 103-01-001 olduğu varsayıldığında; borç çeki kaydedilirken döviz tipi olarak 1 girilirse, muavin hesabın son dijiti de 1 olduğu için aynı hesap kodunu kullanır. Döviz tipi olarak 2 girilirse, muavin hesap kodunu 103-01-002 olarak atar. Dolayısı ile muhasebede de mutlaka 103-01-002 hesap kodunun açılması gerekir. Parametrenin işaretlenmesi ile, program içinden yapılabilen ve entegrasyon kayıtları bölümündeki senet/çek hesaplarının kullanıldığı işlemlerde (Kasa Modülü → Senet-Çek İşlemleri, Dekont Modülü → Portföydeki Senet/Çek Karşılıksız İşlemi gibi) söz konusu fonksiyon kullanılır. |
| Dekont/Senet Çek Modülünde Kur Farkı Kayıtları Yapılsın Mı? | Dövizli senet/çek işlemi yapan firmalarda oluşacak kur farklarının ilgili modüllere işlenip işlenmemesi durumunun kontrol edilmesi için kullanılan seçenektir. Seçenek işaretlenmediği zaman Senet/Çek modüllerindeki ciro ve kur farkı kayıtlarında ve Dekont modülündeki tahsil ve ödendi kayıtlarında kur farkı hesaplanmaz. İşaretlendiğinde ise, Senet/Çek modüllerindeki ciro ve kur farkı kayıtlarında, "Dekont" modülündeki tahsil ve ödendi kayıtlarında kur farkı hesaplanır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Genel**

![](../../../../_assets/d635a002a715c3e1e82d.png)

Entegrasyon Kodları ekranı Genel sekmesinde yer alan bilgiler aşağıdaki şekildedir:

| Entegrasyon Kodları Ekranı |  |
| --- | --- |
| Yuvarlama Nedeni İle Fark Veren Fişlerde Kapatma Hesap Kodu | Yuvarlama nedeniyle (faturalardaki iskonto tanımlamaları ve dövizli işlemlerde oluşan küsuratlar sebebi ile) fiş izleme bölümlerinin toplamlarında fark oluşabilir. Seçenekli ya da Toplu Aktarma bölümlerinden, muhasebe fişlerinin aktarım sırasında bakiye vererek oluşmaması için, söz konusu alana girilen muhasebe hesap koduna program tarafından küsurat atanarak fişlerin bakiye vererek oluşması engellenir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılarak kapatma hesap kodu girilir. |
| Aktarım Yuvarlama Bazı (Kr) | Entegrasyondan "Muhasebe" modülüne aktarım yapılacak kayıtlar için, kuruş cinsinden girilecek yuvarlama bazının tanımlandığı alandır. Söz konusu alana değer girildiğinde kayıtlar, yuvarlama bazındaki değere göre yuvarlanıp daha sonra aktarılır. **Örneğin,** yuvarlama bazı 1 girildiğinde; 1 kuruş, 10 girildiğinde; 10 kuruş, 100 girildiğinde; 1 TL gibi yuvarlama yapılır. |
| İşlem Tipi Bazında Hesap Kodu Değişimi | İşlem Tipi Uygulaması kullanıldığında, entegrasyona işlenecek kayıtların hesap kodlarının işlem tipi bazında değiştirilmesi için kullanılan seçenektir. İşlem Tipi Uygulaması ile ilgili detaylı bilgi için; Entegrasyon → Kayıt → İşlem Tipi Tanımlama dokümanına bakılabilir. |
| Entegrasyon Havuz Sistemi Kapatılsın | Fişlerin aktarıldığı entegrasyon havuz sisteminin kapatılması için kullanılan seçenektir. |
| Muhasebeye Doğrudan Aktarım Yapılsın | Fişlerin muhasebeye doğrudan aktarımının yapılması için kullanılan seçenektir.. |
| Muhasebe Fişlerinin Düzeltme ve Silmesinde Ters Kayıt Yapılsın | Entegre edilecek muhasebe fişlerinin düzeltme ve silinmesi işlemlerinde ters kayıt yapılması için kullanılan seçenektir. |
| Fiş Basımı Yapılsın | Fiş basımının yapılması için kullanılan seçenektir. |
| Gün Bazında Aktarım Yapılsın | Muhasebe fişlerinin entegrasyona aktarılırken gün bazında aktarılması için kullanılan seçenektir. |
| Kullanıcı Bazında Aktarım Yapılsın | Muhasebe fişlerinin entegrasyona aktarılırken kullanıcı bazında aktarılması için kullanılan seçenektir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
