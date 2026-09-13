---
title: "Netsis Ebat Hesaplaması"
page_id: "66238995"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Ebat Hesaplaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Ebat Hesaplaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTRjZDg0MTJhLTU3NmItNDA2My04MGJhLTA1ZTNiNWEzNWY1NiZsaW5rPWM1NDNkM2IyLWM5NTAtNDcwNy1hMTliLTQ5ZGU3YWU4ODUyMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=4cd8412a-576b-4063-80ba-05e3b5a35f56&link=c543d3b2-c950-4707-a19b-49de7ae88523&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-ebat-hesaplamasi_90669913_66238995.html"
source_version: "2022-11-03T09:54:56.307+03:00"
source_bytes: 350989
fetched_at: "2026-09-13T04:26:24+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Ebat Hesaplaması

Netsis Ebat Hesaplaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Cam, halı vb. sektörlerde kullanılan Ebat Uygulamasının Netsis'te kullanılabilmesi için, öncelikli olarak Satış Fatura Parametrelerinde Genel-2 sekmesinde "**Ebat Bilgisi Girilsin**" ve "**Ebatlar Kaça** **Bölünsün**" parametrelerinin işaretli olması gerekmektedir.

Ayrıca Satış Fatura Parametrelerinde uygulamanın çalışabilmesi için, "**İkinci Miktar Sorulsun**" parametresinin işaretlenmesi ve "**Farklı** **Birimlerden** **Mal** **Çıkışı** **Yapılsın**" parametresinin işaretlenmemesi gerekmektedir.

![](../_assets/ada206b866e6409f2a96.png)

**Ebat Bilgisi Girilsin** parametresinin kullanılabilmesi için Satış Fatura Parametrelerinde Genel-2 sekmesinde "**Ek** **Alan** **Kullanılsın**" seçeneğinin seçilmesi gereklidir. Bu sayede, stok kartlarına tanımlanan ebat bilgileri fatura kayıtlarında Ek Alan-1'e getirilecektir.

Bu bağlantılı iki parametre işaretlendiğinde, fatura kaydı sırasında, mal kalemleri bazında ebat bilgileri girilip ve toplam ebat hesaplatması yapılmaktadır.

**Ebatlar Kaça Bölünsün (1\>1, 2\>10, 3\>100, 4\>1000)**

Ebat bilgisi girilip, toplam ebat hesaplatabilmek için bu parametreden ebatların kaça bölüneceği seçilmelidir.

Örneğin, cam sektöründe cam ebatları, en-boy olarak **mm** ölçülerinde giriliyor ve faturalama işlemi **m²** üzerinden yapılıp fiyatlandırılıyor olsun. Bu durumda, Satış Fatura Parametrelerinde **"Ek** **Alan Kullanılsın**", "**Ebat Bilgisi Girilsin**" parametreleri işaretlenmiş ve "**Ebatlar kaça bölünsün**" parametresinin **1000** olarak seçilmesi gereklidir.

Ayrıca bu türden hesaplama yapılması istenen ürünlerin stok sabit bilgilerindeki 1. ölçü birimi, **m²** olarak girilmelidir. Eğer malların ebatları belli olup fatura bazında değişmiyorsa ve bu ürünler için 3. ölçü birimi kullanılmıyorsa, yine o ürün için stok sabit bilgi kayıtlarında 2. çevrim pay ile 2. çevrim payda değerlerine bu ebat bilgileri kaydedilebilir. Bu bilgiler faturada mal bazında Ek Alan- 1 sahasına program tarafından getirilecektir.

Bu tanımlamalara göre aşağıdaki örnek stok kartındaki tanımlama aşağıdaki gibi yapılmalıdır. Br- 2 ve Br-3 için pay/payda değerleri 1500/2000 olarak girilir.

![](../_assets/e3b930038439d866e9eb.png)

Yukarıda bahsedilen parametre ve tanımlamalar yapıldıktan sonra, örnek olarak oluşturulan Cam stoku için Fatura girildiğinde, kalemler sekmesinde ilgili stok seçimi sonrasında Ek Alan-1 kısmında 1500X2000 değeri otomatik olarak getirilip miktar kısmında da 1500X2000=3000000 değeri program tarafından yazılmaktadır. Ardından kaç adetlik bu parçadan satılıyor ya da alınıyorsa miktar alanına girilir. Örnek için 4 adet giriş yapıldığında, sistem girilen değeri dönüştürüp miktar sahasına 12 m², 2. Miktar sahasına da 4 adet bilgisini yazacaktır.

![](../_assets/e66b27fc460ea3b9d3ce.png)
![](../_assets/df8b544f78a888067f3c.png)
