---
title: "e-Fatura ve e-Arşiv Faturaları için Enerji Uygulaması"
page_id: "132449471"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Fatura ve e-Arşiv Faturaları için Enerji Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Fatura ve e-Arşiv Faturaları için Enerji Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMwMzEwNTA0LWQxMTQtNGU1NC04ZWY0LTE4NGExNDVlMTJkNSZsaW5rPTMzMTcwNjE3LWUyNjctNDRjMS05ZTllLWNkOTA4YzEwZDdkYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=30310504-d114-4e54-8ef4-184a145e12d5&link=33170617-e267-44c1-9e9e-cd908c10d7da&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-fatura-ve-e-arsiv-faturalari-icin-enerji-uygulamasi_134054212_132449471.html"
source_version: "2024-02-09T10:42:28.090+03:00"
source_bytes: 6657009
fetched_at: "2026-09-13T04:23:07+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Fatura ve e-Arşiv Faturaları için Enerji Uygulaması

Vergi Usul Kanunu Genel Tebliği (Sıra No:509)'nde Değişiklik Yapılmasına Dair 550 Sıra [No.lu](http://No.lu) Tebliğ ile 2/4/2022 tarihli ve 31797 sayılı Resmî Gazete'de yayımlanan Şarj Hizmeti Yönetmeliği kapsamında Enerji Piyasası Düzenleme Kurumundan şarj ağı işletmeci lisansı alan mükellefler

ile bu mükellefler tarafından sertifika verilen şarj istasyonu işletmecilerine e-fatura uygulamasına geçme zorunluluğu getirilmiştir. e-Fatura ve e-Arşiv faturaları için Enerji Uygulaması hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

9053 setiyle birlikte e-Fatura ve e-Arşiv faturaları için Enerji Uygulaması desteği getirilmiştir.

- Sunulan şarj hizmetine ilişkin e-Faturanın 7 günde bir düzenlenmesi durumunda kesilecek olan e-Faturalar "**ENERJI**" senaryosu ile, e-Arşiv faturaları ise, "**e-Arşiv Fatura**" senayosu ile düzenenecektir. Bu belgelerin fatura tipi "**SARJ**" olacaktır.
- Sunulan şarj hizmetine ilişkin faturanın teslim anında düzenlenmesi durumunda, e- Faturalar "**ENERJI**" senaryosu ile e-Arşiv faturaları ise, "**e-Arşiv** **Fatura**" senayosu ile düzenenecektir. Bu belgelerin fatura tipi "**SARJANLIK** " olacaktır.

Oluşacak olan belgelerde şarj işleminin Başlama/Bitiş Tarih/Saat bilgileri, plaka, araç kimlik no alanları zorunlu ortak alanlardır.

Bunların haricinde SARJ faturaları için, bilgilerin GİB Teknolojiye anlık olarak bildirilmesinde oluşturulacak ESURAPORID ve bu bilginin oluşturulduğu tarih bilgisi ESURAPORTARIHI, SARJANLIK faturalarında ise, kalemlerde şarj ünitesi seri numarası alanları zorunludur.

Enerji Faturalarının Netsis içerisinde düzenleyebilmek için, Satış Fatura Parametrelerinde Genel 3 sekmesinde "**Enerji** **Fatura** **Uygulaması**" parametresinin işaretlenmesi gerekmektedir.

Bu parametre işaretlendiğinde, Satış Faturası' nın Üst Bilgiler sekmesinde "**Şarj** **Tipi**" alanı gelir ve "**Şarj ve** **Şarj** **Anlık**" seçeneklerinden biri seçilir.

![](../_assets/1148a0d41e6fac81f26c.png)

![](../_assets/559c1c427af095eb1e41.png)

Enerji faturalarında yer alması zorunlu alanların xml dosyası oluşturulurken, Satış Faturası Üst Bilgiler sekmesindeki Açıklama alanlarından okunabilmesi için, aşağıda belirtilen 4 adet özel parametre tanımlanmalıdır. Bu özel parametrelerin Grup Kodu: EFATURA dır. Anahtar kısımlarımda ESURAPORID, ESURAPORTARIHI, SARJARACKIMLIK ve SARJPLAKA bilgiler yer almalıdır. Değer kısımlarında ise, faturadaki hangi üst açıklama bilgisinin kullanılması isteniyorsa, ilgili açıklamanın sıra bilgisi girilmelidir.

Örneğin; e-Belge taslak oluşturma sırasında zorunlu alanlardan biri olan ESURAPORID alanının Fatura üst açıklama 1 alanından getirilmesi isteniyorsa, ilgili parametrenin değer alanına 1 girilmelidir.

Benzer şekilde, zorunlu alanlardan bir diğeri olan ESURAPORTARIHI alanının Fatura üst açıklama 2 alanından getrilmesi isteniyorsa, ilgili parametrenin değer alanına 2 girilmelidir.

Şarj Araç Kimlik Numarasının SARJARACKIMLIK alanının Fatura üst açıklama 3 alanından getirilmesi isteniyorsa, ilgili parametrenin değer alanına 3 girilmelidir.

Plaka bilgisinin SARJPLAKA alanının Fatura üst açıklama 4 alanından getirilmesi isteniyorsa, ilgili parametrenin değer alanına 4 girilmelidir.

![](../_assets/41b76a1a375363dbefea.png)

![](../_assets/c53c4780c050e0a8fe5c.png)![](../_assets/a0e93e350192feb685cd.png)

Diğer zorunlu alan bilgileri için, Dizayn Kayıtlarında e-Devlet XML Tagleri olarak InvoicedPeriod- StartDate, InvoicedPeriod-EndDate, InvoicedPeriod-StartTime, InvoicedPeriod-EndTime değerleri eklenmiştir. Bu taglerle eşleştirilecek alanlar için de, değerlerin okunacağı alanlar belirlenmelidir.

StartDate: Şarj işleminin dönemin başladığı tarih

StartTime: Şarj işleminin dönemin başladığı zaman

EndDate: Şarj işleminin dönemin bittiği tarih

EndTime: Şarj işleminin dönemin bittiği zaman

Aşağıdaki örneğe göre InvoicePeriod-StartDate tagi Fatura Üst Bilgiler Açıklama 5 alanıyla, InvoicePeriod-EndDate tagi Fatura Üst Bilgiler Açıklama 6 alanıyla, InvoicePeriod-StartTime tagi Fatura Üst Bilgiler Açıklama 7 alanıyla ve son olarak InvoicePeriod-EndTime tagi Fatura Üst Bilgiler Açıklama 8 alanıyla eşleştirilmiştir. İstenirse farklı alanlarla da eşleştirme yapılır.

![](../_assets/132e0bf162de9d837cfc.png)

![](../_assets/315ea7ad232525f74614.png)

![](../_assets/7864a6e8561eac04a114.png)

"**SARJ** **ANLIK**" Fatura tipiyle kesilen faturaların kalem bilgilerinde "**Şarj** **Seri**" alanı aktif olmaktadır. Buraya yazılacak olan veri oluşturulan taslaktaki şarj ünitesi seri numarası alanına yazılmaktadır.

![](../_assets/e0e1555e259937cdde5f.png)

Şarj işleminde hizmetin "**KWH**" cinsinden birim miktarı/fiyatı yazılmalıdır. Hizmet için açılan Stok Kartı Kayıtları ekranında ölçü birimi olarak Kilowatt saat (KWH) seçilmelidir.

![](../_assets/d715780b4d565aba07c4.png)

Bu tanımlanan ölçü birimi de e-Fatura İşlemleri\>Birim Eşleştirme ekranında Uluslararası Ölçü Birim Kodu olan KWH (KwH) ile eşleştirilmelidir.

![](../_assets/69f6e56673ee2874d22e.png)

<table>

<tbody>
<tr>
<th colspan="4">
<p><strong>ENERJİ</strong> <strong>FATURALARI</strong></p>
</th>
</tr>
<tr>
<td colspan="2">
<p><strong>e-Fatura</strong></p>
</td>
<td colspan="2">
<p><strong>e-Arşiv</strong></p>
</td>
</tr>
<tr>
<td colspan="2">
<p><strong>Senaryo:</strong> <strong>ENERJI</strong></p>
</td>
<td colspan="2">
<p><strong>Senaryo:</strong> <strong>e-Arşiv</strong> <strong>Fatura</strong></p>
</td>
</tr>
<tr>
<td>
<p><strong>Fatura</strong> <strong>Tipi:</strong> <strong>SARJ</strong></p>
</td>
<td>
<p><strong>Fatura</strong> <strong>Tipi:</strong> <strong>SARJ</strong> <strong>ANLIK</strong></p>
</td>
<td>
<p><strong>Fatura</strong> <strong>Tipi: SARJ</strong></p>
</td>
<td>
<p><strong>Fatura</strong> <strong>Tipi: SARJ</strong> <strong>ANLIK</strong></p>
</td>
</tr>
<tr>
<td>
<p>ESURAPORID ESURAPORTARIHI</p>
</td>
<td>
<p>-</p>
</td>
<td>
<p>ESURAPORID ESURAPORTARIHI</p>
</td>
<td>
<p>-</p>
</td>
</tr>
<tr>
<td>
<p>Şarj Araç Kimlik No</p>
</td>
<td>
<p>Şarj Araç Kimlik No</p>
</td>
<td>
<p>Şarj Araç Kimlik No</p>
</td>
<td>
<p>Şarj Araç Kimlik No</p>
</td>
</tr>
<tr>
<td>
<p>Şarj Plaka No</p>
</td>
<td>
<p>Şarj Plaka No</p>
</td>
<td>
<p>Şarj Plaka No</p>
</td>
<td>
<p>Şarj Plaka No</p>
</td>
</tr>
<tr>
<td>
<p>-</p>
</td>
<td>
<p>Şarj seri No</p>
</td>
<td>
<p>-</p>
</td>
<td>
<p>Şarj Seri No</p>
</td>
</tr>
<tr>
<td>
<p>Şarj işleminin dönemin<br/>
			başladığı/bittiği<br/>
			tarih/saat</p>
</td>
<td>
<p>Şarj işleminin dönemin<br/>
			başladığı/bittiği<br/>
			tarih/saat</p>
</td>
<td>
<p>Şarj işleminin dönemin<br/>
			başladığı/bittiği<br/>
			tarih/saat</p>
</td>
<td>
<p>Şarj işleminin dönemin<br/>
			başladığı/bittiği<br/>
			tarih/saat</p>
</td>
</tr>
</tbody>
</table>

**SARJ tipli e-Fatura ve e-Arşiv Faturası**

SARJ tipli satış faturası girerken Şarj Tipi: Sarj seçilmelidir.

![](../_assets/cf54e8012ab5ddc8b730.png)

Şarj tipli Fatura için zorunlu alanların girişi (özel parametrelerde ESURAPORID, ESURAPORTARIHI, SARJARACKIMLIK, SARJARACPLAKA alanları için Fatura üst bilgilerindeki hangi açıklama alanlarının kullanılacağı ve dizayn içerisinde şarj döneminin başlangıç/bitiş tarih/saat bilgileri belirtilmelidir) yapılmalıdır.

![](../_assets/2f6dcfc063464bd1a3e9.png)

![](../_assets/a29c47fd4b32c9362fd8.png)

Şarj tipli e-Belge oluştuğunda oluşan xmlde zorunlu alanların yer aldığı tag bilgileri aşağıdaki gibidir.

\<cbc:ProfileID\>ENERJI\</cbc:ProfileID\>

\<cbc:InvoiceTypeCode\>SARJ\</cbc:InvoiceTypeCode\>

\<cac:InvoicePeriod\>

\<cbc:StartDate\>2024-01-30\</cbc:StartDate\>

\<cbc:StartTime\>11:10:31\</cbc:StartTime\>

\<cbc:EndDate\>2024-02-08\</cbc:EndDate\>

\<cbc:EndTime\>11:10:31 \</cbc:EndTime\>

\</cac:InvoicePeriod\>

\<cac:AdditionalDocumentReference\>

\<cbc:ID schemeID="ESURaporID"\>123456789\</cbc:ID\>

\<cbc:IssueDate\>2024-01-01\</cbc:IssueDate\>

\</cac:AdditionalDocumentReference\>

\<cac:AccountingCustomerParty\>

\<cac:Party\>

\<cac:PartyIdentification\>

\<cbc:ID schemeID="PLAKA"\>35AC9908\</cbc:ID\>

\</cac:PartyIdentification\>

\<cac:PartyIdentification\>

\<cbc:ID schemeID="ARACKIMLIKNO"\>14725896\</cbc:ID\>

\</cac:PartyIdentification\>

\<cac:accountingcustomerparty\>\<cac:party\>

**SARJ ANLIK tipli e-Fatura ve e-Arşiv Faturası**

![](../_assets/35c0245fa1a84b16868c.png)

SARJ ANLIK tipli satış faturası girerken Şarj Tipi: Sarj Anlık seçilmelidir.

![](../_assets/e4d3b0dd9fdf53cdf685.png)

Şarj Anlık tipli Fatura için zorunlu alanların girişi (özel parametrelerde SARJARACKIMLIK, SARJARACPLAKA alanları için Fatura üst bilgilerindeki hangi açıklama alanlarının kullanılacağı ve dizayn içerisinde şarj döneminin başlangıç/bitiş tarih/saat bilgileri belirtilmelidir) yapılmalıdır.

Ayrıca Fatura Kalem Bilgileri sekmesinde, kalem bazında şarj ünitesi seri numarası bilgisi Şarj Seri alanına girilmelidir.

![](../_assets/683c662ed9828e5bc168.png)

![](../_assets/7b2ad23985258d2e8fe1.png)

Şarj Anlık tipli e-Belge oluştuğunda oluşan xmlde zorunlu alanların yer aldığı tag bilgileri aşağıdaki gibidir.

\<cbc:ProfileID\>ENERJI\</cbc:ProfileID\>

\<cbc:InvoiceTypeCode\>SARJ\</cbc:InvoiceTypeCode\>

\<cac:InvoicePeriod\>

\<cbc:StartDate\>2024-01-30\</cbc:StartDate\>

\<cbc:StartTime\>11:10:31.0100000+03:00\</cbc:StartTime\>

\<cbc:EndDate\>2024-02-08\</cbc:EndDate\>

\<cbc:EndTime\>11:10:31.0110000+03:00\</cbc:EndTime\>

\</cac:InvoicePeriod\>

\<cac:AccountingCustomerParty\>

\<cac:Party\>

\<cac:PartyIdentification\>

\<cbc:ID schemeID="PLAKA"\>35AC9908\</cbc:ID\>

\</cac:PartyIdentification\>

\<cac:PartyIdentification\>

\<cbc:ID schemeID="ARACKIMLIKNO"\>14725896\</cbc:ID\>

\</cac:PartyIdentification\>

\<cac:Item\>

\<cac:ItemInstance\>

\<cbc:SerialID\>123369987\</cbc:SerialID\>

\</cac:ItemInstance\>

\</cac:Item\>

"Enerji Faturası Uygulaması" parametresi hem satış hem de alış tarafına eklenmiştir. Bu parametre Alış Fatura Parametreleri \> Genel 3 Sekmesinde bulunmaktadır.

![](../_assets/619aff2311a764db7a57.png)

Gelen SARJ ve SARJ ANLIK tipli e-Faturalardan Alış faturası oluşturma adımında, oluş alış faturasının tipinin "Şarj veya şarj Anlık" tipinde oluşabilmesi için de bu parametrenin işaretlenmesi gerekmektedir.
