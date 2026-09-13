---
title: "Anlık e-Belge Gönderme Taslak ve Basım İşlemleri"
page_id: "108660624"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Anlık e-Belge Gönderme Taslak ve Basım İşlemleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Anlık e-Belge Gönderme Taslak ve Basım İşlemleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ1OWRkN2E2LTU0ZmMtNDEwOC1iYWFkLTQzZWUyZWVjMmIwYyZsaW5rPTgwNWM5OWMwLWVhMjQtNGRmMC1hOGZkLTc5ODUzZmU3ODEyNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d59dd7a6-54fc-4108-baad-43ee2eec2b0c&link=805c99c0-ea24-4df0-a8fd-79853fe78127&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "anlik-e-belge-gonderme-taslak-ve-basim-islemleri_111247618_108660624.html"
source_version: "2023-06-01T14:02:04.897+03:00"
source_bytes: 1247013
fetched_at: "2026-09-13T04:23:29+00:00"
generator: "netsis-scraper 1.0.0"
---
# Anlık e-Belge Gönderme Taslak ve Basım İşlemleri

Anlık e-Belge gönderme, taslak ve basım işlemleri hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

9038 setinde e-Fatura, e-Arşiv ve e-İrsaliye kayıtlarında anlık e-Belge taslak oluşturma ve gönderim özellikleri desteklenmiştir. Henüz kayıt aşamasında iken, taslak oluşturma ve taslak gönderim işlemleri yapılabilmektedir. Bu özelliğe ek olarak 9045 setiyle birlikte, anlık e-Belge gönderiminde e-Belgelerin basımı ve kullanıcının belge basımı için gerekli ayarları yapabilmesi desteklenmiştir.

Örnek bir satış faturası üzerinde anlık e-Belge gönderimi, basım ve basım ayarları özellikleri aşağıda gösterilmiştir. E-Fatura serili bir satış faturası girildiğini varsayalım.

Girilen belgenin Toplamlar sekmesinde "**Anlık e-Fatura Gönderimi**" parametresi bulunmaktadır. Bu parametre işaretliyken yapılan bir kayıt işleminde, "**e-Fatura** **Oluşturma** **Parametreleri**" başlıklı ekran gelir. Toplu e-Fatura Oluşturma parametreleri ekranında olduğu gibi bu ekranda da taslak oluşturma, gönderim ve basım ile ilgili parametreler listelenmektedir.

![](../_assets/c3510420b7ecbb8526f9.png)

Bu ekranda ek olarak "**Sadece Taslak Oluşturulsun**" seçeneği yer almaktadır. Eğer bu seçenek işaretli olarak kayıt işlemi yapılırsa, ilgili belge için kayıt sırasında sadece taslak oluşturma işlemi yapılacaktır. Oluşan taslağın gönderilmesi, Toplu e-Fatura Oluşturma ekranından yapılacaktır.

![](../_assets/b3f70c4f23aad9d7148c.png)

"**Sadece** **Taslak** **Oluşturulsun**" parametresi işaretli değilse, belge kaydı sırasında hem taslak oluşturma işlemi hem de oluşan taslağın gönderimi yapılacaktır.

Toplu e-Fatura Oluşturma adımında olduğu gibi, taslak oluşturma ve taslak gönderimi sırasında yapılan kontroller bu ekranda yapılmaktadır. Taslak oluşturmaya veya gönderime engel olacak bir durum varsa bu ekranda da görüntülenmektedir.

Örneğin taslak oluşturulmuş ancak taslak gönderim sırasında bir hata alınmışsa, bu durumda ilgili belge için sadece taslak oluşturulmuş olacak. Taslak oluşan belge Toplu e-Fatura Oluşturma erkanında taslaklar sekmesinde yer alacaktır. Hata giderildikten sonra tekrar gönderimi sağlanır.

![](../_assets/f0626b1434369d30206b.png)

Belge kaydı sırasında başarılı bir şekilde taslak oluşturulmuş ve taslak başarılı bir şekilde gönderilmişse, belge e-Fatura Giden kutusuna düşecektir.

**Not:** e-Fatura için taslak oluşturulup gönderildikten sonra tekrar ilgili belge açıldığında toplamlar sekmesinde "**Anlık** **e-Fatura** **Gönderimi**" parametresi görünmez.

9045 setiyle birlikte anlık e-Belge gönderiminde e-Belgelerin basımı ve kullanıcının belge basımı için gerekli ayarları yapabilmesi sağlanmıştır. Bu kapsamda oluşturulan belgenin toplamlar sekmesinde yer alan "**Anlık e-Fatura Gönderimi**" parametresi işaretlenerek tamam butonuna basıldığında "**e-Fatura** **Oluşturma** **Parametreleri**" isimli ekran karşımıza gelir.

"**Sadece** **Taslak** **Oluşturulsun**" parametresi ile birlikte "**Basım** **yapılsın**" parametresi işaretlenerek belge tamamlandığında, ilgili belge için taslak oluşturulacak ve oluşan taslak e-Belge varsayılan yazıcıya gönderilerek basımı sağlanacaktır.

Sadece "**Basım yapılsın**" parametresi işaretlenerek belge tamamlandığında, ilgili belge için taslak oluşturulacak ve oluşan taslak e-Belgenin gönderimi yapılacak ve giden e-Fatura belgesi varsayılan yazıcıya gönderilerek basımı sağlanacaktır.

Taslak veya gönderilen e-Belgeler için bir basım ayarı yapılacaksa, "**Basım** **Ayarı** **Yapılacak**" parametresinin işaretlenmesi gerekmektedir. Parametre işaretlendiğinde "**Basım Ayarları**" isimli ekran gelir. Bu ekranda "**Yazıcı** **seçilsin**" işaretlenirse, ekrana bir yazıcı listesi gelecek ve ilgili yazıcı seçilerek basım yapılabilecektir. "**Yazıcı** **Ayarı** **Yapılsın**" işaretlenirse, varsayılan yazıcıdan nasıl bir basım işlemi gerçekleştirilmesi isteniyorsa, bununla ilgili ayarlar yapılarak basım yapılabilecektir.

![](../_assets/f8dd3ff25acc8611d28b.png)![](../_assets/33e391910d1ecfea20e0.png)
