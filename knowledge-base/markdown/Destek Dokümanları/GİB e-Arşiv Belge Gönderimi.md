---
title: "GİB e-Arşiv Belge Gönderimi"
page_id: "80085005"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "GİB e-Arşiv Belge Gönderimi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / GİB e-Arşiv Belge Gönderimi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ3OTUxOGI1LTQyYjUtNGJiYS1hMmM1LTIwMTEwNTljN2E2NyZsaW5rPTAxMTI2ZGIzLWVmODEtNGNiYS04MWYzLTZkZWVjNTcxNmY5OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=479518b5-42b5-4bba-a2c5-2011059c7a67&link=01126db3-ef81-4cba-81f3-6deec5716f99&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "gib-e-arsiv-belge-gonderimi_80085014_80085005.html"
source_version: "2022-11-02T14:39:08.277+03:00"
source_bytes: 485805
fetched_at: "2026-09-13T04:24:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# GİB e-Arşiv Belge Gönderimi

GİB e-Arşiv Belge Gönderimi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Eski tebliğde e-Arşiv Fatura uygulaması, aynı gün içerisinde vergi mükellefi olanlar için kesilen faturaların toplam meblağının 5 Bin TL ve üzeri olması durumunda geçerliydi ve vergi mükellefi olmayanlara kesilen faturalar için ise 30 Bin TL'yi geçmesi durumunda e-Arşiv Fatura uygulanması şartı bulunuyordu. Yeni tebliğ ile, aynı gün içerisinde vergi mükellefi olmayanlara kesilen faturaların toplam tutarı 5 Bin TL'ye düşürülürken, vergi mükellefi olanlara kesilen faturalar için e-Arşiv Fatura düzenleme şartı GİB tarafından belirlenen fatura kesme sınırına eşitlendi. Bu sınır her yıl güncellenmekle birlikte, 2022 yılı için 2000 TL'dir. Bu değerlerin altındaki tutarlar için de isteğe bağlı e-arşiv faturası kesilebilmektedir fakat herhangi bir zorunluluk bulunmamaktadır.

9.0.40.1 sürümü ile GİB portal üzerinden kesilmesi gereken e-Arşiv faturalarının da Netsis üzerinden düzenlenip e-Logo entegratör aracılığı ile GİB'e gönderilmesi desteklenmiştir.

GİB e-Arşiv belge gönderimini sağlayabilmek için öncelikle GİB e-Arşiv lisansına sahip olmak gerekir. Ayrıca servis klasörü altında yer alan efaturaayarlar.exe üzerinde e-Arşiv Ayarları'nın ilgili işletme için tanımlanmış olmalıdır.

![](../_assets/829ca3bd111a60ddc33a.png)
![](../_assets/9be0dc90bd2d5f144c11.png)
İlgili lisansa sahip olunması durumunda e-Arşiv parametreleri ekranına **"GİB** **E-Arşiv** **Uygulaması** **Kullanılsın"** parametresi eklenecektir. Burada yapılan seçim işletme bazında çalışmaktadır. Yani bir işletme GİB e-Arşiv uygulamasını kullanabiliyor iken diğer bir işletme normal e-Arşiv uygulamasını kullanabilir.

![](../_assets/fc76855a07e09f281de9.png)
e-Logo üzerinden ise Ayarlar-Parametreler ekranı altında yer alan **"İnteraktif Vergi Dairesi (GİB Portal) Bağlantı Ayarları"** alanından GİB portal kullanıcı adı ve şifre bilgileri tanımlanmalıdır.

![](../_assets/c83018bf460eb450d9a3.png)

Parametre seçili işletmelerde girilen e-Arşiv için **Toplu e-Arşiv Oluşturma** ekranı üzerinden taslak oluşturulup gönderim yapılmalıdır. e-Arşiv basım tipli dizaynlar GİB e-Arşiv uygulaması için de kullanılabilir.

![](../_assets/f59ca3df84e54bdcc257.png)
GİB e-Arşiv gönderimlerinde her bir fatura gönderimi sırasında kullanıcılarımızın kayıtlı cep telefonu numarasına SMS kodu gönderilir. Bu SMS kodunun belirtilen süre içerisinde girişinin yapılması gerekir. Hatalı bir kod yazıldığında ya da belirtilen süre içerisinde giriş yapılmaması durumunda uyarı alınacaktır. Örneğin: İlgili sürede kod girişi yapılmadığında "S00000000001838 faturası için SMS doğrulama kodu alınamadı." uyarısı alınacaktır.

![](../_assets/564b140712f9a0f9e81f.png)

Gönderilen GİB e-Arşiv belgelerinin GİB fatura numarası, ilgili belge GİB Portal'a iletildikten sonra oluşur ve giden kutusunda sorgulama yapıldığında ilgili belgelerin GİB fatura numarası ve cevap açıklaması bilgileri otomatik olarak güncellenir.

![](../_assets/76de14f931e0c276ffd5.png)
