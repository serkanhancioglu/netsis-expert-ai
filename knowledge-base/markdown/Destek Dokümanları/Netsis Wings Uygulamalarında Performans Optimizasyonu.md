---
title: "Netsis Wings Uygulamalarında Performans Optimizasyonu"
page_id: "111247827"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Wings Uygulamalarında Performans Optimizasyonu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Wings Uygulamalarında Performans Optimizasyonu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY5NTA3ODVkLTJjNmItNGZlZS05OTk1LWE0ZTVlZjMwMTg3MSZsaW5rPWNhMDlhNjU3LTUwZWEtNDhiNy05MjlkLWEwNTNiMTA1M2JkMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6950785d-2c6b-4fee-9995-a4e5ef301871&link=ca09a657-50ea-48b7-929d-a053b1053bd1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-wings-uygulamalarinda-performans-optimizasyonu_111247828_111247827.html"
source_version: "2023-05-05T15:26:52.823+03:00"
source_bytes: 271889
fetched_at: "2026-09-13T04:23:24+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Wings Uygulamalarında Performans Optimizasyonu

Netsis Wings uygulamalarında performans optimizasyonu için tercih edilen "One browser Per Windows Session" modunun kullanımı hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Netsis Wings ürünlerinin Windows Server işletim sistemlerinde kurulu olması durumunda performans artışı sağlamak için "One browser Per Windows Session" modu desteklenmektedir. Bu özellik etkileştirildiğinde, tarayıcı üzerinden uygulamaya giriş yapan her istemci için disconnect modunda çalışan bir kullanıcı oturumu başlatılır. Bu sayede birden fazla oturum altında yük dengeleme yapılarak Netsis Wings ürünlerinin daha yüksek bir performans ile kullanımı sağlanır.

Netsis Wings servisini "One browser Per Windows Session" modunda çalıştırmak için Netsis Wings Yönetim Paneli "Thinfinity.VirtualUI.Server" açılarak **Sessions** sekmesinden **"One browser Per Windows Session"** seçeneği işaretlenmelidir.

*Not: Bu özelliğin kullanımı için Wings sunucusunda "Remote Desktop Session Host" rolü yüklü olmalıdır.*

![](../_assets/091af951a47af7f944e1.png)

Mode alanında "One browser Per Windows Session" seçeneği işaretlendikten sonra alt bölümde yer alan oturum açma yönteminin belirlenmesi gerekir.

**Use the current interactive session or console** seçeneği yalnızca **"Shared Windows Session"** modu için kullanılabilir.

```text
Use these credentials yöntemi kullanıldığında aşağıda belirtilen kullanıcı oturum bilgileriyle, uygulamaya her giriş yapıldığında yeni bir oturum açılır.
Windows Server 2019 ve üzeri işletim sistemlerinde bazı güvenlik güncelleştirmeleri sebebiyle aynı kullanıcı ile birden çok RDS oturumu açılmasına izin verilmemektedir. Tanımlanan kullanıcıyla Windows üzerinde aynı anda birden fazla oturum açmaya izin vermek için aşağıdaki işlem adımları izlenmelidir.
> Run (Çalıştır)
 > gpedit.msc
  > Edit Group Policy (Grup İlkesini Düzenle)
   > Computer Configuration (Bilgisayar Yapılandırması)
    > Administrative Templates (Yönetim Şablonları)
     > Windows Components (Windows Bileşenleri)
      > Remote Desktop Services (Uzak Masaüstü Hizmetleri)
       > Remote Desktop Session Host (Uzak Masaüstü Oturumu Ana Bilgisayarı)
        > Connections (Bağlantılar)
         > Restrict Remote Desktop Services users to a single Remote Desktop Services session
(Uzak masaüstü hizmetleri kullanıcılarını bir uzak masaüstü hizmetleri oturumuyla sınırla) Seçeneğinin "Disable" (Kapalı) edilmesi gerekir.
```

![](../_assets/77c80663fa54471c962c.png)

![](../_assets/5527885530df55437f21.png)

Diğer bir oturum açma yöntemi ise **Create user on-demand** seçeneğidir. Bu seçeneğin kullanılması durumunda tarayıcıdan Wings uygulamasına giriş yapıldıkça oluşturulan sanal kullanıcılar üzerinden disconnect modunda oturum açma işlemi gerçekleştirilir. Create users on-demand kullanımı için **username prefix** alanına sanal olarak oluşturulması istenen kullanıcı adı yazılmalıdır. *Örneğin; "wingsuser"*

**Add to group** alanında ise sanal olarak oluşturulacak kullanıcıların hangi kullanıcı grubuna dahil edileceği belirlenir. Bu alana **"Administrators"** yazılarak yeni açılacak kullanıcılar Administrators grubuna dahil edilmelidir.

![](../_assets/0bea97286e58ad686864.png)

Tanımlamalar ekran görüntüsündeki gibi yapıldığında, Wings kullanıcıları uygulamaya giriş yaptıklarında otomatik olarak username prefix alanında belirtilen kullanıcı adı ile yeni bir kullanıcı hesabı oluşturulur ve disconnect modunda çalışması sağlanır.

Performans optimizasyonu için her kullanıcının uygulamaya girişinde bir Windows oturumu açılması yerine her 4 Wings kullanıcısında yeni bir oturum açma işleminin gerçekleştirilmesi tavsiye edilir. Bunun için C:\\Netsis\\ENTERPRISE9\\VUI dizininde yer alan **"load_balance.reg"** dosyası kayıt defterine eklenmelidir. Bu işlem tamamlanıp Wings servisi yeniden başlatıldığında 4 kullanıcının üzerinde bir giriş sayısına ulaşıldığında Windows kullanıcılarına otomatik olarak *"wingsuser2"* kullanıcısı açılarak uygulamaya giriş yapması sağlanır. Kullanıcı sayısı arttıkça "wingsuser3", "wingsuser4" oturumu açılmaya devam edecektir. Wings tarafından açılan kullanıcılar otomatik olarak **"Remote Desktop Users"** grubuna dahil edilir.

![](../_assets/a4ef8caedd6fd26cce1f.png)

Create users on-demand yöntemi kullanıldığında Sessions sekmesinde girilen kimlik bilgilerinin kullanılması için **Application\\Credentials** sekmesinde **"Use Server's Account"** seçeneği işaretlenmelidir.

Otomatik olarak oluşturulan Wings kullanıcılarında bölgesel ayarlar ve tarih formatının uygulama içinde doğru bir biçimde gösterimi için belirlenen formatın yeni açılacak tüm kullanıcılara uygulanması gerekir. Bunun için; ***Region \> Administrative*** ***\> Copy Settings \>New user accounts*** seçeneği işaretlenmelidir.

![](../_assets/8bf242144d53075e58f5.png)

*Not: Tanımlanan ayarların geçerli olması için Windows hizmetlerden "Thinfinity VirtualUI Service Manager" servisi yeniden başlatılmalıdır.*
