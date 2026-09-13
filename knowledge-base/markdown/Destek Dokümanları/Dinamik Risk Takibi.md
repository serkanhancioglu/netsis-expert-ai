---
title: "Dinamik Risk Takibi"
page_id: "50680387"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Dinamik Risk Takibi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Dinamik Risk Takibi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWVkZjFlMjc3LTM1YjAtNGJjMC1hOGU1LTE1MGE1YWU5YWMxMSZsaW5rPTcwMTA3YTI3LTk4ZGMtNDc2Ny1iYjE2LTVhY2E0MDdkOWUzZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=edf1e277-35b0-4bc0-a8e5-150a5ae9ac11&link=70107a27-98dc-4767-bb16-5aca407d9e3f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dinamik-risk-takibi_79167490_50680387.html"
source_version: "2022-11-03T09:53:53.007+03:00"
source_bytes: 750209
fetched_at: "2026-09-13T04:26:22+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dinamik Risk Takibi

Dinamik Risk Takibi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Dinamik risk takibinin amaç ve faydaları şunlardır:

- Müşteri riskleri hesabında, borç bakiyesinin risk toplamını belli bir oranda etkilemesi sağlanır.
- Risk toplamının hesaplanmasında, risk öğelerine ait kısıt verebilir ve risk takibi daha etkin şekilde kullanılabilir.
- Risk toplamını etkileyecek olan borç bakiyesi Cari hareketlerden verilecek kısıtlara göre hesaplanabilir.
- Çek, senet, sipariş, irsaliye ve cari hareketlerin riske dahil olan kısımları kısıtlar verilerek belirlenebilir.

**Cari Risk Girişi**

![](../_assets/0047a6d5d7562ed4886b.png)

Netsis programlarında, faturalama vb. işlemler sırasında, müşterinin risk durumu kontrol edilebilir. Müşterinin toplam riski, verilen risk limitini aştığı durumda ise, işlem program tarafından durdurulur. Risk takibinin yapılabilmesi için, Cari Risk Girişi bölümünden, belli tanımlamaların yapılması gerekir.

Bu ekranda, müşterinin, riskini oluşturan belli kalemlerin, toplam riski hangi oranda etkilediği belirlenir. Bugüne kadarki uygulamada, müşterinin anlık borç bakiyesinin tamamı, toplam riskini etkilemekteydi. Yani borç bakiyesi, riskini %100 etkilemekteydi. Ekrana yeni eklenen "Cari Hareket Bakiyesi" risk kalemi ile, artık borç bakiyesi toplam riski belli bir oranda etkileyebilecektir.

Bu sahada 0'dan farklı bir oran olması, bakiye kontrolünün cari hareketlerinden yapılacağı anlamına gelir. Oran 0'a eşit ise eskisi gibi anlık bakiye (cari sabit kartındaki) kontrol edilir.

**Dinamik Risk Yönetimi**

**Risk Öğeleri:** Müşteri risklerini etkileyen risk öğelerinin, riski etkileyen toplam tutarının, belli kısıtlar verilerek hesaplanmasının sağlanması amacıyla kullanılabilecek bölümdür. Bu ekran yardımı ile Risk takibi yapılan öğeler için ayrı ayrı kısıtlar verilerek, ilgili öğenin risk toplamındaki değeri isteğe göre düzenlenebilecektir.
Kısıt verilmek istenen öğe işaretlendikten sonra ilgili öğenin risk toplamını ilgilendiren sahalar üzerinde kısıt değerleri verilebilir.

![](../_assets/3ddca8e7f66a52826859.png)

**Cari Hareket Bakiyesi**: Müşterinin doğrudan riskini etkileyen borç bakiyesi hesaplamasında, programın belli kısıtları dikkate alması için kullanılabilecek öğedir.

**Teminat**: Riski pozitif olarak etkileyen Teminat faktörü için kısıt verilebilecek bölümdür.

**Çek** **Asıl**: Cari Hesap Çek Alındı Kaydı ile sisteme kaydedilen asıl çeklerin oluşturduğu risk öğesi için kısıt verilebilecek bölüm.

**Çek** **Ciro**: Cari Hesap Çek Alındı Kaydı ile sisteme kaydedilen asıl çeklerin oluşturduğu risk öğesi için kısıt verilebilecek bölüm.

**Senet** **Asıl**: Cari Hesap Senet Alındı Kaydı ile sisteme kaydedilen asıl senetlerin oluşturduğu risk öğesi için kısıt verilebilecek bölüm.

**Senet** **Ciro**: Cari Hesap Senet Alındı Kaydı ile sisteme kaydedilen ciro senetlerin oluşturduğu risk öğesi için kısıt verilebilecek bölüm.

**Sipariş** **Üst**: Müşterilerin mevcut siparişlerinin riski etkilemesi istenmiş ise, sipariş kayıtlarında üst bilgiler sekmesindeki alanlar için kısıtlar verilebilecek bölüm.

**Sipariş** **Kalemleri**: Müşterilerin mevcut siparişlerinin riski etkilemesi istenmiş ise, siparişlerin kalem bilgileri sekmesindeki alanlar için kısıt verilebilecek bölüm.

**İrsaliye** **Üst**: Müşterilerin mevcut irsaliyelerinin riski etkilemesi istenmiş ise, irsaliye kayıtlarında üst bilgiler sekmesindeki alanlar için kısıtlar verilebilecek bölüm.

Kısıt verme işlemi tamamladıktan sonra, TAMAM butonuna basıldığında verilen kısıtlar doğru ise aşağıdaki gibi bir uyarı mesajı alınacaktır.

![](../_assets/b815dbf0698402c33f0b.png)

Verilen kısıtlar, sistemde riskin hesaplandığı viewleri (görüntü) doğrudan değiştirecektir. Dolayısıyla verilen kısıtlar, bir yerde firmanın risk politikasını belirleyen kısıtlar olmalıdır. Burada verilen kısıtlar risk takibi yapılan tüm müşteriler için geçerli olacaktır. Eğer farklı müşteri gruplarına farklı politikalar uygulanacaksa verilen kısıtlar buna göre belirlenmelidir. Aşağıda detaylı örnekler verilecektir.

**Kısıt Kontrolü:** Bu butona basıldığında aşağıdaki 'Risk Kısıt Kontrolü' ekranı açılır. Kontrol Et butonuna basıldığında verilen kısıtların nasıl bir SQL cümlesi oluşturacağı ve doğruluğu kontrol edilebilir.

![](../_assets/c030f3bd0d707d575db4.png)
Verilen kısıtlar doğru ise "Verdiğiniz kısıtlar doğrudur." şeklinde uyarı alınır.
![](../_assets/2bde05e9e733faae10f5.png)
**ÖRNEKLER**

1. 900 kodlu carinin, Cari Hareket Bakiyesinin %80'i risk hesaplamaya dahil olsun. Risk limiti 1000 Teminatı da 200 olsun

![](../_assets/526a9192f18fde012bd1.png)

Bu durumda 900 kodlu cariye kesilen çek, senet, irsaliye ve siparişlerin tutarlarının %80'i riskine yansıyacaktır. Örneğin cari harekete manuel girilen 100 TL'lik bir borç hareketinin 80 TL'lik kısmı borç toplamına yansıyacaktır ve carinin riski -1120 TL'ye düşecektir.

1. Şirketin Dinamik Risk Yönetimi için politikası, çek asıl ve senet asıl riski için proje kodu 01 olanların dahil olması yönünde olsun.

Müşteriden alınan 100 TL'lik bir çekin veya senedin öncelikle proje kodunun 01 olup olmadığı program tarafında kontrol edilecek, proje kodu 01 ise örnekteki cari için çek asıl riski alanına 100 TL yazacak, cari hareket bakiyesinin %80'i risk hesaplamaya dahil olduğu için de alacak toplamı alanına 80 TL'lik kısmını yazacaktır.

Aşağıda önce cari hareketleri sonra da cari risk girişi ekranına yansıması izlenebilir.

![](../_assets/427c128207068270e9cd.png)
![](../_assets/162ec5c79ceab8d8dfde.png)

Cari hareketten de görüldüğü gibi tutarları 100 TL olan iki ayrı çek, bir adet senet ve devir tipli bir borç hareketi var. Risk girişi ekranından da görüldüğü gibi proje kodu 01 olan çek ve senet risk hesaplamaya dahil edilmiş, proje kodu 02 olan diğer çek ise dahil edilmemiştir ancak proje kodu 02 olan devir hareketi riske dahil edilmiştir. Çünkü dinamik risk için çek ve senet hareketlerine ait kısıt verilmiştir.

1. Yukarıdaki 2.örnekte anlatılan politikanın müşteri grupları bazında farklılaştığını varsayalım. "G01" grup kodlu müşterilerde "01" proje kodlu kayıtların, "G02" grup kodlu müşterilerde ise "02" proje kodlu kayıtların riski etkilemesi isteniyorsa, aşağıdaki gibi bir tanımlama yapılabilir.

![](../_assets/be5df29355a586c431f6.png)

Sadece yukarıda verilen kısıtlar için çalışacak cümle şöyledir:

![](../_assets/d97f5ee3093c84b6c07f.png)
