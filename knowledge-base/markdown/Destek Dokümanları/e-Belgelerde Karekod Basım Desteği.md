---
title: "e-Belgelerde Karekod Basım Desteği"
page_id: "117179365"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Belgelerde Karekod Basım Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Belgelerde Karekod Basım Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWIxMGY2YzAyLTRmODktNDgxZC04MTcxLTAzY2U2Mzk5ZmMyYiZsaW5rPWY2OWExMTdhLTEwYTgtNGU5Zi05MjMyLTYzMDg0ZGRiNzBjMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b10f6c02-4f89-481d-8171-03ce6399fc2b&link=f69a117a-10a8-4e9f-9232-63084ddb70c0&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-belgelerde-karekod-basim-destegi_117179379_117179365.html"
source_version: "2023-09-01T17:10:28.583+03:00"
source_bytes: 2183127
fetched_at: "2026-09-13T04:23:16+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Belgelerde Karekod Basım Desteği

01.09.2023 tarihli e-Belge uygulamalarında düzenlenen belgeler için "Karekod" basımı 9.0.49.1 patch dosyaları ile desteklenmiştir.

Bootstrap Visuals Callout

- *Gelir İdaresi Başkanlığı tarafından yayınlanan duyuruya ulaşmak için [tıklayınız.](https://ebelge.gib.gov.tr/dosyalar/kilavuzlar/Karekod_veya_Barkod_Standardi_Kilavuzu_V.1.0.pdf)*

Taslak oluşturma sırasında dizayn seçmeden yapılan basımlarda (Kodun içine gömülü dizaynlarda) Karekod basımı ilgili patch dosyaları ile desteklenmiştir. Ayrıca güncelleme sonrasında Temelset dizini altında Xslt klasöründe varsayılan xslt dosyalarında da güncelleme yapılmıştır. Xslt klasörü içinde, e-Fatura için general.xslt, e-Arşiv için arsiv.xslt, e-İrsaliye için irsaliye.xslt ve e-Müstahsil için müstahsil.xslt dosyaları içinde Karekod’ u basan ilgili kod blokları yer almaktadır.

Özel dizayn kullanımı durumunda, xslt dosyalarına aşağıdaki kod bloklarının eklenmesiyle Karekod basımı set bağımsız olarak yapılabilecektir.

Örneğin e-Fatura belgelerinde Karekod basımı için 2 adet kod bloku bulunmaktadır.

1. kod bloku **head** ile **style** arasına konmalıdır.

![](../_assets/3e53ac5de68fd766005e.png)

```text
Kopyalanacak 1. kod bloku
```

2.kod bloku ise, karekodun çıkacağı yere kopyalanması gerekmektedir. Karekod mevzuata göre sağ üstte yer almalıdır. Basım yapılacak yere göre xsltye aşağıdaki kod bloku kopyalanmalıdır. İlgili kod bloku aşağıda yer almaktadır.

**Not !!!** Bu kod bloku e-Fatura belgeleri için kullanılmaktadır. E-Arşiv, e-İrsaliye ve e-Müstahsil belgelerinde farklılık göstermektedir. E-Arşiv, e-İrsaliye, e-Müstahsil belgeleri için 2. Kod blokları dokümanın sonunda yer almaktadır.

![](../_assets/5ea144b3e0acbca77291.png)

```text
e-Fatura belgeleri için 2.kod bloku

                          <xsl:variable name="ettnValue">
                              <xsl:value-of select="n1:Invoice/cbc:UUID">

                              {
                              "vkntckn":"<xsl:value-of select="n1:Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID[@schemeID = 'TCKN' or @schemeID = 'VKN']">",
                              "avkntckn":"<xsl:value-of select="n1:Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID[@schemeID = 'TCKN' or @schemeID = 'VKN']">",
                              "senaryo":"<xsl:value-of select="n1:Invoice/cbc:ProfileID">",
                              "tip":"<xsl:value-of select="n1:Invoice/cbc:InvoiceTypeCode">",
                              "tarih":"<xsl:value-of select="n1:Invoice/cbc:IssueDate">",
                              "no":"<xsl:value-of select="n1:Invoice/cbc:ID">",
                              "ettn":"<xsl:value-of select="n1:Invoice/cbc:UUID">",
                              "parabirimi":"<xsl:value-of select="n1:Invoice/cbc:DocumentCurrencyCode">",
                              "malhizmettoplam":"<xsl:value-of select="n1:Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount">",
                              <xsl:for-each select="n1:Invoice/cac:TaxTotal/cac:TaxSubtotal[cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode = '0015']">
                                  <xsl:text>"kdvmatrah(<xsl:value-of select="cbc:Percent">)":"<xsl:value-of select="cbc:TaxableAmount">",

                              <xsl:for-each select="n1:Invoice/cac:TaxTotal/cac:TaxSubtotal[cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode = '0015']">
                                  <xsl:text>"hesaplanankdv(<xsl:value-of select="cbc:Percent">)":"<xsl:value-of select="cbc:TaxAmount">",

                              "vergidahil":"<xsl:value-of select="n1:Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount">",
                              "odenecek":"<xsl:value-of select="n1:Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount">"
                              }

                                                        var ettnValue=  "<xsl:value-of select="n1:Invoice/cbc:UUID">";                              var qrcode = new QRCode(document.getElementById("qrcode_" + ettnValue), {                              width : 140,                              height : 140,                              correctLevel: QRCode.CorrectLevel.L                              });                              var minifiedValues =document.getElementById("qrvalue_" + ettnValue).innerHTML.replace(/\s/g, '');                              qrcode.makeCode(minifiedValues)
```

![](../_assets/f4fe8cdb74c855e5059b.png)

e-Arşiv belgeleri için 2.kod bloku

\<xsl:variable name="ettnValue"\>

\<xsl:value-of select="n1:Invoice/cbc:UUID"\>

{

"vkntckn":"\<xsl:value-of select="n1:Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID\[@schemeID = 'TCKN' or @schemeID = 'VKN'\]"\>",

"avkntckn":"\<xsl:value-of select="n1:Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID\[@schemeID = 'TCKN' or @schemeID = 'VKN'\]"\>",

"senaryo":"\<xsl:value-of select="n1:Invoice/cbc:ProfileID"\>",

"tip":"\<xsl:value-of select="n1:Invoice/cbc:InvoiceTypeCode"\>",

"tarih":"\<xsl:value-of select="n1:Invoice/cbc:IssueDate"\>",

"no":"\<xsl:value-of select="n1:Invoice/cbc:ID"\>",

"ettn":"\<xsl:value-of select="n1:Invoice/cbc:UUID"\>",

"parabirimi":"\<xsl:value-of select="n1:Invoice/cbc:DocumentCurrencyCode"\>",

"malhizmettoplam":"\<xsl:value-of select="n1:Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount"\>",

\<xsl:for-each select="n1:Invoice/cac:TaxTotal/cac:TaxSubtotal\[cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode = '0015'\]"\>

\<xsl:text\>"kdvmatrah(\<xsl:value-of select="cbc:Percent"\>)":"\<xsl:value-of select="cbc:TaxableAmount"\>",

\<xsl:for-each select="n1:Invoice/cac:TaxTotal/cac:TaxSubtotal\[cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode = '0015'\]"\>

\<xsl:text\>"hesaplanankdv(\<xsl:value-of select="cbc:Percent"\>)":"\<xsl:value-of select="cbc:TaxAmount"\>",

"vergidahil":"\<xsl:value-of select="n1:Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount"\>",

"odenecek":"\<xsl:value-of select="n1:Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount"\>"

}

var ettnValue= "\<xsl:value-of select="n1:Invoice/cbc:UUID"\>";

var qrcode = new QRCode(document.getElementById("qrcode\_" + ettnValue), {

width : 140,

height : 140,

correctLevel: QRCode.CorrectLevel.L

});

var minifiedValues = document.getElementById("qrvalue\_"+ettnValue).innerHTML.replace(/\\s/g, '') ;

qrcode.makeCode(minifiedValues)

```text
e-İrsaliye belgeleri için 2.kod bloku                    <xsl:variable name="ettnValue">                        <xsl:value-of select="n1:DespatchAdvice/cbc:UUID">                                                                                    {                        "vkntckn":"<xsl:value-of select="n1:DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID[@schemeID = 'TCKN' or @schemeID = 'VKN']">",                        "avkntckn":"<xsl:value-of select="n1:DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID[@schemeID = 'TCKN' or @schemeID = 'VKN']">",                        "senaryo":"<xsl:value-of select="n1:DespatchAdvice/cbc:ProfileID">",                        "tip":"<xsl:value-of select="n1:DespatchAdvice/cbc:DespatchAdviceTypeCode">",                        "tarih":"<xsl:value-of select="n1:DespatchAdvice/cbc:IssueDate">",                        "no":"<xsl:value-of select="n1:DespatchAdvice/cbc:ID">",                        "ettn":"<xsl:value-of select="n1:DespatchAdvice/cbc:UUID">",                        "sevktarihi":"<xsl:value-of select="n1:DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchDate">",                        "sevkzamani":"<xsl:value-of select="substring(n1:DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchTime, 0,9)">",                        "tasiyicivkn":"<xsl:value-of select="n1:DespatchAdvice/cac:Shipment/cac:Delivery/cac:CarrierParty/cac:PartyIdentification/cbc:ID">",                        "plaka":"<xsl:value-of select="n1:DespatchAdvice/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID">"                        }                                                                var ettnValue=  "<xsl:value-of select="n1:DespatchAdvice/cbc:UUID">";                        var qrcode = new QRCode(document.getElementById("qrcode_" + ettnValue), {                        width : 140,                        height : 140,                        correctLevel: QRCode.CorrectLevel.L                        });                        var minifiedValues = document.getElementById("qrvalue_"+ ettnValue).innerHTML.replace(/\s/g, '');                        qrcode.makeCode(minifiedValues)
```

```text
e-Müstahsil belgeleri için 2.kod bloku                                                                            {                                        "vkntckn":"<xsl:value-of select="n1:CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID[@schemeID = 'TCKN' or @schemeID = 'VKN']">",                                        "avkntckn":"<xsl:value-of select="n1:CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID[@schemeID = 'TCKN' or @schemeID = 'VKN']">",                                        "senaryo":"<xsl:value-of select="n1:CreditNote/cbc:ProfileID">",                                        "tip":"MUHTAHSILMAKBUZU",                                        "tarih":"<xsl:value-of select="n1:CreditNote/cbc:IssueDate">",                                        "no":"<xsl:value-of select="n1:CreditNote/cbc:ID">",                                        "ettn":"<xsl:value-of select="n1:CreditNote/cbc:UUID">",                                        "parabirimi":"<xsl:value-of select="n1:CreditNote/cbc:DocumentCurrencyCode">",                                        "malhizmettoplam":"<xsl:value-of select="n1:CreditNote/cac:LegalMonetaryTotal/cbc:LineExtensionAmount">",                                        <xsl:for-each select="n1:CreditNote/cac:TaxTotal/cac:TaxSubtotal[cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode = '0003']">                                            "gvstopaj":"<xsl:value-of select="cbc:TaxAmount">",                                                                                <xsl:for-each select="n1:CreditNote/cac:TaxTotal/cac:TaxSubtotal[cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode = '9040']">                                            "merafonu":"<xsl:value-of select="cbc:TaxAmount">",                                                                                <xsl:for-each select="n1:CreditNote/cac:TaxTotal/cac:TaxSubtotal[cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode = '8001']">                                            "borsatescilucreti":"<xsl:value-of select="cbc:TaxAmount">",                                                                                <xsl:for-each select="n1:CreditNote/cac:TaxTotal/cac:TaxSubtotal[cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode = 'SGK_PRIM']">                                            "sgkprimkesintisi":"<xsl:value-of select="cbc:TaxAmount">",                                                                                "odenecek":"<xsl:value-of select="n1:CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount">"                                        }                                                                                                                var ettnValue=  "<xsl:value-of select="n1:CreditNote/cbc:UUID">";                                        var qrcode = new QRCode(document.getElementById("qrcode_" + ettnValue), {                                        width : 140,                                        height : 140,                                        correctLevel: QRCode.CorrectLevel.L                                        });                                        var minifiedValues = document.getElementById("qrvalue_" + ettnValue).innerHTML.replace(/\s/g, '');                                        qrcode.makeCode(minifiedValues)
```

![](../_assets/9be4f142d9d1139bbf90.png)

**Not!!!** Özel tasarım dizayn kullanımında xslt dosya yolu olarak …\\TemelSet\\XSLT klasörü içindeki xslt dosyaları verilmişse, güncelleme öncesinde bu dosyaların yedeklenmesi önerilir. Güncelleme sonrası bu dizindeki xslt dosyalarıda güncellenecektir.

**Not!!!** Logo Netsis Wings kullanımında taslak oluşturulduğunda karekod bilgisinin gelmediği durumda,

![](../_assets/1b2819047287d1b20e81.png)

**Sunucu Yönetimi** ekranında **IE Arttırılmış Güvenlik Yapılandırması** ayarının **Kapalı** konumunda olması gerekmektedir.

![](../_assets/16354a0e86808b48c37e.png)

Eğer birden fazla Wings kullanıcı açılmış ise, **Powershell** yönetici olarak açılıp aşağıdaki komut çalıştırıldığında tüm kullanıcılarda **IE Arttırılmış Güvenlik Yapılandırılması “Kapalı”** konumuma getirilmektedir.

![](../_assets/b621f2b11d24a9bbde7b.png)

function Disable-IEESC {
$AdminKey = "HKLM:\\SOFTWARE\\Microsoft\\Active Setup\\Installed Components\\{A509B1A7-37EF-4b3f-8CFC-4F3A74704073}"
$UserKey = "HKLM:\\SOFTWARE\\Microsoft\\Active Setup\\Installed Components\\{A509B1A8-37EF-4b3f-8CFC-4F3A74704073}"
Set-ItemProperty -Path $AdminKey -Name "IsInstalled" -Value 0
Set-ItemProperty -Path $UserKey -Name "IsInstalled" -Value 0
Stop-Process -Name Explorer
Write-Host "IE Enhanced Security Configuration (ESC) has been disabled." -ForegroundColor Green
}
Disable-IEESC

![](../_assets/96e4e0f44cc74caffa78.png)

**Not!!!** Taslak oluşturulduğunda karekodun çıkmaması durumunda **Denetim Masası-İnternet Seçenekleri- Güvenlik sekmesinde** İnternet Ayarı aşağıdaki ekranda da görüldüğü gibi **Varsayılan Seviye** yapılmalıdır.

![](../_assets/d1eac825eeba6973e4d5.png)

Ayrıca **Sunucu Yönetimi** ekranında **IE Arttırılmış Güvenlik Yapılandırması** ayarının “**Kapalı”** konumunda olması gerekmektedir.

![](../_assets/7f40ae42503f8a53b5e6.png)
