---
title: "Kamu e-Faturası Oluşturma"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kamu e-Faturası Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kamu e-Faturası Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMyMGJiMzExLTdhMGEtNDc4Ny1hMTIxLTNlOWVjNzZjNzRlYSZsaW5rPTJiYmYzNTRmLTJlOGEtNDk4Yy05ZWUxLWY4OTVlOTI4ZGE0NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=320bb311-7a0a-4787-a121-3e9ec76c74ea&link=2bbf354f-2e8a-498c-9ee1-f895e928da46&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kamu-e-faturasi-olusturma.html"
source_version: ""
source_bytes: 6848
fetched_at: "2026-09-13T04:22:13+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kamu e-Faturası Oluşturma

GİB e-Fatura Uygulamasına kayıtlı olan vergi mükellefleri, Muhasebat Genel Müdürlüğü (MGM) tarafından geliştirilen Harcama Yönetim Sistemini (HYS) kullanan kamu idareleri ve bunlara bağlı harcama birimleri adına, GİB e-Fatura Uygulaması aracılığı ile e-Fatura düzenleyip gönderebilir.

Netsis içerisinde de oluşan kamu e-Faturalarının senaryosu "KAMU" olarak oluşmaktadır.

[Kamu e-Fatura Teknik Kılavuz](https://ebelge.gib.gov.tr/dosyalar/kilavuzlar/Kamu_e-Fatura_Teknik_Kilavuzu_v1.5.pdf) linkinden GİB' in yayınladığı Kamu e-Fatura Teknik Kılavuzu' na ulaşabilirsiniz.

9.0.19.1 sürümünden itibaren Kamu İdarelerine e-Fatura gönderimi desteklenmiştir.

Kamu idarelerine e-fatura gönderimi yapılırken Banka Bilgisi, Harcama Birim VKN Bilgisi belirtilmesi zorunludur.

**Banka Bilgisi** kısmında, ödemenin yapılacağı IBAN bilgisi girilmelidir. Banka bilgisi için **PayeeFinancialAccount** tagi kullanılmaktadır. PayeeFinancialAccount taginin altında yer alan Para Birimi için kullanılan **CurrecyCode** tagi zorunlu olup, Ödeme Notu için kullanılan PaymentNote taginin kullanımı zorunlu değildir.

Örnek kullanım IBAN;

\<cac:PaymentMeans\>

\<cac:PayeeFinancialAccount\>

\<cbc:ID\>TR111111111111111111111111\</cbc:ID\>

\<cbc:CurrencyCode\>TRY\</cbc:CurrencyCode\>

\<cbc:PaymentNote\>Payment Note\</cbc:PaymentNote\>

\</cac:PayeeFinancialAccount\>

…

\</cac:PaymentMeans\>

**Harcama** **Birimi** **VKN** **Bilgisi** kısmında, ödemeyi yapacak harcama birimi VKN bilgisi girilmelidir.

Örnek kullanım (Ödemeyi Yapacak Harcama Birimi VKN);

\<cac:BuyerCustomerParty\>

\<cac:Party\> …

\<cac:PartyIdentification\>

\<cbc:ID schemeID="VKN"\>1288331521\</cbc:ID\>

\</cac:PartyIdentification\> … \</cac:Party\>

\</cac:BuyerCustomerParty\>

Program içerisinde kamu carileri için, Cari Hesap Kayıtları Ek Bilgiler sekmesinde "**Kamu Carisi**" parametresi işaretlenmelidir. Bu parametre işaretlendiğinde Toplu e-Fatura Oluşturma ekranından taslak oluşturulduğunda kamuya ait etiketlerin oluşması sağlanmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/9aa0b22f-2fa4-45c9-ba31-7eb3b7906b33/kamu1.png)

Program içerisinde girilen bilgiler ve yapılan tag eşleştirmeleri aşağıda yer almaktadır. Gerekli tag ler için tanımlanan alan bilgileri değiştirilebilir. Gerekli bilgiler farklı alanlardan getirilebilir.

Dizayn içerisinde, **ödemenin yapılacağı IBAN bilgisi** Cari Hesap Kayıtları Ek Bilgiler sekmesinde Açıklama1 alanından getirildiği varsayıldığında,

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b24bed7f-1a25-443d-8eab-9c22ef356c0d/kamu2.png)

Açıklama1 alanına tanımlanan IBAN bilgisi dizaynda aşağıdaki gibi PaymentMeans- PayeeFinancialAccount-ID tagi ile eşleştirilir.

Yer:Üst, Tip:Program, Saha:Cari, Alan no:5029 ve e-Devlet XML Tag alanında da PaymentMeans- PayeeFinancialAccount-ID tagi seçilir. Satır, Sütun ve uzunluk bilgisi girilerek kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/4e1cc716-d252-461a-b437-705b4d3272b5/kamu3.png)

Dizayn içerisinde, **Para Birimi** bilgisi, dizayn içinde sabit bir değerden getirildiği varsayıldığında, Para Birimi, dizaynda aşağıdaki gibi PaymentMeans-PayeeFinancialAccount-CurrencyCode tagi ile eşleştirilir.

Yer:Üst, Tip:Sql, Değer için 'Para Birimi 'ne ise, o bilgi girilir. e-Devlet XML Tag alanında da PaymentMeans-PayeeFinancialAccount-CurrencyCode tagi seçilir. Satır, Sütun ve uzunluk bilgisi girilerek kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/096f084a-38fa-4ba7-b3d4-d01c998550a8/kamu4.png)

**Harcama Birimi VKN Bilgisi** dizayn içinde tanımlanmasına gerek yoktur. Kamu faturası girişinde Toplamlar sekmesinde, fatura carisi ile harcama birimi ödemesi yapacak cari aynı ise, herhangi bir seçim yapmaya gerek olmadan belge tamamlanır. Oluşan taslak e-Faturada Harcama Birimi VKN bilgisi ile ilgili taglere program fatura carisinin VKN bilgisini atar.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0891c091-ef2c-46d0-bc1e-8745cb5b0c49/kamu5.png)

Kamu faturası girişinde Toplamlar sekmesinde, fatura carisi ile harcama birimi ödemesi yapacak cari farklı ise, bu durumda sağ click menüsünde "**e-Fatura Ödemesi Yapacak Harcama Birimi**" seçilir. e-Fatura ödemesi yapacak harcama birimi için cari seçilerek belge tamamlanır. Oluşan taslak e-Faturada Harcama Birimi VKN bilgisi ile ilgili taglere program burada seçilen carinin VKN bilgisini atar.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/21443fa9-58fd-43ec-92c0-8e687df9d6cf/kamu6.png)

Tüm bu tanımlamalar sonrasında oluşan Kamu e-Faturasının görüntüsü aşağıdaki gibidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d1671e94-e4a3-4977-ae3f-e0a4a818b5ba/kamu7.png)

Kamu e-Faturası örnek dizayn için [tıklayınız](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/02cca163-5226-4062-9a85-43c9d030dfb3/KAMUDZN.rar)
