---
title: "Tevkifat Uygulaması"
page_id: "88900863"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Tevkifat Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Tevkifat Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWU2Yjc1ZDBmLWNjNGItNGYwNC1hM2NhLWZiNjRlYjRiODEwYyZsaW5rPTAzODQ5OTczLTZlMGUtNGNhOC05YzY5LTMxNDc0MzcxYjQ0MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e6b75d0f-cc4b-4f04-a3ca-fb64eb4b810c&link=03849973-6e0e-4ca8-9c69-31474371b443&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tevkifat-uygulamasi_90670185_88900863.html"
source_version: "2022-11-02T14:29:55.667+03:00"
source_bytes: 879305
fetched_at: "2026-09-13T04:23:59+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tevkifat Uygulaması

Tevkifat Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

**Tevkifatlı Fatura Nedir?**

Para hususunda kesinti anlamına gelen bir kelime olan tevkifat; vergi bağlamında, vergiler üzerinde bölüşme veya kesinti yapma manasına gelmektedir. Normal ya da irsaliyeli faturadan bir farkı bulunmayan tevkifatlı faturayı diğerlerinden ayıran özelliği ise, faturaya işlenen verginin alıcı ve satıcı arasında bölüştürülerek ikisinden de alınıyor olmasıdır.

**Tevkifat Uygulamasında Dikkat Edilmesi Gereken Maddeler**

Öncelikle Satış ve Alış fatura parametrelerinde Ek Maliyet sekmesindeki Ek Maliyet\\\[2\\\] parametresi işaretlenmeli ve adına TEVKİFAT yazılmalıdır. Aynı ekranda bulunan "Tevkifat Oranı Pay/Payda" alanı hesaplanması istenen oran ile doldurulmalıdır.

![](../_assets/55934d14509ad5d8baae.png)

Entegrasyon kodlarında Ek Maliyet-2 hesapları doldurulmalıdır.

![](../_assets/a27ba452280b915637ee.png)

Bu tanımlamalardan sonra faturanın toplamlar sekmesinde, Ek maliyet 2 alanı "TEVKİFAT" adıyla açılmış olup değerine "-1" yazılıp tab ile çıkıldığında parametrelerde yazan oran üstünden tevkifat hesaplanacaktır.

Örnek ile muhasebe kaydını oluşturursak;

KDV hariç 10000 tl , %8 KDV ve 7/10 tevkifat oranı ise 10000\*%8= 800 tl KDV ve 800 \*7/10 =560 tl tevkifat tutarı olacaktır.

**Satış** **faturası** **muhasebe** **kaydı**

![](../_assets/af07458eda3013829c8f.png)

**Alış** **faturası** **muhasebe** **kaydı**

![](../_assets/8de92af8bfc7426c85c7.png)

Çoklu tevkifat oran tanımlama ekranında alış ve satış faturalarında farklı tevkifat kodları için özel kod 2 üzerinden tanımlama yapılabilmektedir. Burada özel kod 2 değerini faturanın üst bilgilerinde "özel kod 2 " alanına girdiğimiz zaman tanımladığımız hesap ve oranlar üstünden belgede hesaplama yapılacaktır.

![](../_assets/d1e7d4a8cc7566729159.png)

**Özel Parametreler İle Tevkifat Uygulaması**

Tevkifatlı faturalarda oluşan muhasebe fişindeki bazı hesaplar ve tutarlar farklı takip edilebilmektedir. Netsis ERP içinde desteklenen bu durumlar için özel parametrelerin tanımlı olması gerekmektedir. Özel parametreler sadece satış faturası için çalışmaktadır.

Grup kodu:FATURA , Anahtar:TEVKİFAT , Değer:C Özel Parametresi

Bu özel parametre ile KDV hesabı tevkifat düşülmüş tutar kadar çalışır, tevkifat hesabı çalışmayacaktır. Aynı örnek ile ilerlersek 800 - 560= 240 TL KDV hesabı çalışacaktır.

**Satış** **faturası** **muhasebe** **kaydı**

![](../_assets/6a64cb6143f4ec18879d.png)

Grup kodu:FATURA , Anahtar:TEVKİFAT , Değer:K Özel Parametresi

Çoklu tevkifat Oran Tanımlama ekranında, özel kod2 alanına göre farklı tevkifat oranları ve hesap kodları tanımlanabilmektedir. Bu özel parametre ile Çoklu Tevkifat Oran Tanımlama ekranında "Satış Hesap Kodu" alanındaki hesap koduna "KDV tutarından tevkifat tutarının düşülmüş değeri" atılmaktadır.

Aynı örnek ile ilerlersek 800 - 560= 240 TL Özel kod 2 ile bağlanan hesap çalışacaktır.

![](../_assets/5d8717173750e075107c.png)

**Satış** **faturası** **muhasebe** **kaydı**

![](../_assets/22ddac9568df00c7b994.png)

Eğer bu özel parametre tanımlanır fakat özel kod-2 değeri belgenin üst bilgilerinde girilmezse yine SATIŞ için entegrasyon kodlarındaki KDV hesabına tevkifat düşülmüş tutar atılacaktır. (TEVKİFAT/C özel parametresi ile aynı şekilde çalışmış olacaktır. )

**FATURA/TEVKIFATBORCALACAK Özel Parametresi**

Tevkifat tutarının cari hesaptan düşülmeden, ayrı bir satıra atılması sağlanmıştır . Cari hesabı borç çalışıyor ise aynı hesap tevkifat tutarı kadar alacak(satış faturasında), cari hesabı alacak çalışıyor ise aynı hesap tevkifat tutarı kadar borç(alış faturasında) çalışacaktır. Bu parametre kullanıldığında, belgenin kalemleri bazında farklı proje ve referans kodu girişi yapılmamalıdır.

**Satış** **faturası** **muhasebe** **kaydı**

![](../_assets/d3ab98fcfec4368d1278.png)

**Alış** **faturası** **muhasebe** **kaydı**

![](../_assets/0ae0ebc76d2090f1abaa.png)

Bu parametreyle beraber örneğin TEVKİFAT/K özel parametresi tanımlanırsa ,Satış faturasında tevkifatın düşülmüş tutarını özel kod-2 ile ile tanımlanan hesaba atılıp ayrıca yine Cari hesabı borç çalışıyor ise aynı hesap tevkifat tutarı kadar alacak çalıştırılacaktır.

**Satış** **faturası** **muhasebe** **kaydı**

![](../_assets/f59e258bbb4d1682d107.png)

**FATURA\\TEVKIFATCARIBAZINDA\\1 Özel Parametresi**

Tevkifat hesabının bazı carilerde hesaplanıp bazılarında hesaplanması istenmiyorsa kullanılacaktır. Muhasebe fişindeki hesapların çalışma şeklini etkilemeyecektir. Örneğin Cari karttaki alfasayısal kullanıcı tanımlı sahalardan talep edilen bir saha kullanılabilir, burada alfasayısal 1 kullanılacaksa DEGER alanına 1 yazılmalıdır. Cari karttta belirtilen Kullanıcı Tanımlı saha için değer E ise tevkifat hesaplanacak, H ise tevkifat hesaplanmayacaktır.

![](../_assets/474ad1015ffad0081503.png)

Güncel sette bu özel parametre Satış fatura parametreleri ekranında desteklenmiş durumdadır.

![](../_assets/c9907587c76640915f65.png)
