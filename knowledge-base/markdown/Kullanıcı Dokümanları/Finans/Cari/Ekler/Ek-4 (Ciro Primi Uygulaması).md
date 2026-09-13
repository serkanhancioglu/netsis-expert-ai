---
title: "Ek-4 (Ciro Primi Uygulaması)"
page_id: "22805761"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Ekler"
  - "Ek-4 (Ciro Primi Uygulaması)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Ekler / Ek-4 (Ciro Primi Uygulaması)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE5MjdlZWE5LWViNzAtNGM5Mi1iYzA3LTk5YzAxMWQyZTkzYSZsaW5rPWVmZTJjYjc1LWQ5MmItNGFkNS05MWVmLWQxOWNlNDdmMzAxMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a927eea9-eb70-4c92-bc07-99c011d2e93a&link=efe2cb75-d92b-4ad5-91ef-d19ce47f3011&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-4-ciro-primi-uygulamasi_29991629_22805761.html"
source_version: "2022-11-21T15:12:26.603+03:00"
source_bytes: 252112
fetched_at: "2026-09-13T04:08:51+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-4 (Ciro Primi Uygulaması)

Ciro Primi uygulaması hakkında ayrıntılı bilgiler bu dokümanda yer alır.

Cari → Kayıt → Koşul Kayıtları bölümünde yer alan "Ciro primi uygulaması" örnek verilerek açıklanacak olursa; "G01" grup koduna dahil cari hesaplar için aylık periyodlarda ciro primi iskontosunun hesaplanarak uygulanacağı varsayıldığında, uygulamada takip edilmesi ve yapılması gereken dört aşama vardır. Ciro Primi uygulaması aşamaları şunlardır; Ciro Primi Hak Ediş Bilgilerinin Tanımlanması, Koşul Kayıtlarının Tanımlanması, Satış Faturası Kayıtları, Dönem Sonu Ciro ve Hak Ediş Hesaplama.

**1- Ciro Primi Hak Ediş Bilgilerinin Tanımlanması**

Cari → Kayıt → Cari Parametreleri → " Ciro primi için kullanılacak cari rapor kodu sahası” parametresinde “Grup Kodu” seçildikten sonra ilgili grup için Ciro Primi Hak Ediş bilgileri girilir. Aşağıdaki örnekte, tanımlanan hak ediş bilgileri yer alır.

![](../../../../_assets/f4fb2388c259a2525086.png)

**Koşul Kayıtlarının Tanımlanması**

Ciro primi için; Koşul Sabit, Genel Koşul ve Detay Koşul Kayıtları tanımlanır.

![](../../../../_assets/63116711481fc3167aff.png)

Aşağıdaki örnekte, ciro primi için tanımlanan koşul kodu "CP1’dir.

![](../../../../_assets/c1eaddf59ed79da3a611.png)

Örnekteki koşul tanımlamalarında "Başlangıç Tarihi" olarak "02/11/2017" girilmiştir. Yani, cari hesapların bu tarihten itibaren olan alımları için ciro primi hesaplanır. Koşul tanımlamaları yapılırken "Bitiş Tarihi" boş bırakılır. Bunun sebebi, ilgili koşulların, "Dönem Sonu Ciro ve İskonto Hak Ediş Hesaplama” işlemi ile program tarafından dönem sonunda kapatılmasından kaynaklanır.

![](../../../../_assets/e57f140bfac33a75ef29.png)

"Detay Koşul Kayıtları" tanımlanırken, "Başlangıç Tarihi" olarak 02/11/2017 girilmiştir. "080" grup koduna sahip stoklar için ciro primi uygulanır. Bu yüzden "Koşul Rapor Kodu" alanına "080" grup kodu girilir. Koşul kayıtları bu şekilde kaydedildikten sonra, "G04" grup koduna sahip cari hesapların kartlarına ilgili koşul kodu girilir.

**3- Satış Faturası Kayıtları**

01/11/2017 - 30/11/2017 tarihleri arasında G01 grup koduna sahip 00015 kodlu cari için girilen satış faturalarına ait bilgiler aşağıdadır:

| Stok Kod | Miktar | Fiyat | Tutar |
| --- | --- | --- | --- |
| 1 | 2000 | 1 | 2.000 |
| 2 | 2500 | 1 | 2.500 |

00015 kodlu müşteriye Kasım ayında toplam 4.500 TL tutarında satış yapılmış ve bu satışın tamamı, ciro primi iskontosu uygulanacak stoklardan yapılmıştır.

**Dönem Sonu Ciro ve Hak Ediş Hesaplama**

Kasım ayına ait satışlar tamamlandıktan sonra ciro primi iskonto hesaplamaları yapılır.

![](../../../../_assets/3a00dc1da803781d93a8.png)

Örneğe göre, işlem çalıştırılırken "Tarih Aralığı" olarak Kasım ayının ilk ve son günü girilmiş. Bu durumda, Kasım ayındaki satışlar göz önünde bulundurularak ciro primi hesaplanır. Eğer, müşterilerin Kasım ayından önceki dönemlerden kalan ve Kasım ayında kullanılmamış iskonto hak edişleri olsaydı, ilgili tutarlar "Bakiye Ciro İskontoları Devretsin” seçeneği işaretlendiği için Aralık dönemine aktarılacaktı. İşlem tamamlandığında, Başlangıç tarihi 02/11/2017 olarak yapılan koşul tanımlamaları kapatılarak, aynı kod ile 02/12/2017 tarihinde başlayan yeni koşullar program tarafından oluşturulur.

![](../../../../_assets/681cff3a19f559349ccd.png)

Yukarıdaki ekranda da görüldüğü gibi, Kasım dönemi için tanımlanan koşul kapatılmış. Bu koşul ile "Başlangıç Tarihi" dışında aynı bilgilere sahip yeni bir koşul tanımlanmış. Girilen bilgilere göre cari hesabın Kasım ayında yaptığı alımlar 4.500 TL’dir. "Ciro Prim Hak Ediş Bilgilerinde" bu tutar ilk aralığa girdiği için, %5 oranında mal fazlası iskontosu hak etmiştir. Cari hesabın hake ettiği mal fazlası iskontosu oranı (4.500 \* 0,05= 225 TL) olarak hesaplanmıştır.

İşlemler sonucu Aralık ayında kesilen faturalara, müşterinin hakettiği ciro primi, mal fal fazlası iskontosu olarak yansıtılır.

![](../../../../_assets/5024d2f27965ffc92b6e.png)

İlgili cari için kesilen satış faturasının kalem bilgilerinde, ciro primi uygulamasına dahil edilen stoklardan biri girilir. Stok için "Miktar" ve "Fiyat" bilgileri girildikten sonra \<tab\> tuşu ile ilerlendiğinde, girilen fiyata göre mal fazlası miktarı program tarafından ekrana getirilir.

Örnekte, miktar olarak 500, fiyat olarak ise 1TL girilmiş. Cari hesabın hakettiği ciro primi 225 TL olduğu için, girilen miktarın 225 tanesi (225 \* 1) mal fazlası iskontosu olarak işlenir. "Miktar" alanı ise 275 adete düşürülür. Ancak, fatura kaydı sırasında miktar olarak 100 girilmiş olsaydı, "Koşul Sabit Kayıtları" bölümünde bulunan “Fatura Satırında Maksimum Mal Fazlası İskonto Oranı (%)” alanına 90 girildiği için, cari daha fazla ciro primi haketmesine rağmen ilgili fatura ile sadece 90 adet mal fazlası almış olacaktı. Kalan prim hakkı saklı tutularak daha sonra kesilen faturalara işlenmiş olacaktı. Satış faturası bu şekilde kesildiğinde, 01/11/2017 - 30/11/2017 tarihleri arasında 00015 nolu cari için "Dönem Sonu Ciro ve İskonto Listesi" alınan rapor aşağıdaki gibi olacak.

![](../../../../_assets/8381b06ec76f470bf130.png)
