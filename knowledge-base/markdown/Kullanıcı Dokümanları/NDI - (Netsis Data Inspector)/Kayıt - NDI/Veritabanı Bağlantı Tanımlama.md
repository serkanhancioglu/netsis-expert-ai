---
title: "Veritabanı Bağlantı Tanımlama"
page_id: "50682816"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "NDI - (Netsis Data Inspector)"
  - "Kayıt / NDI"
  - "Veritabanı Bağlantı Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / NDI - (Netsis Data Inspector) / Kayıt / NDI / Veritabanı Bağlantı Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk0NTMyM2QwLTY1YWEtNDJmMi04YjVhLTcyZGE0NGRlMTBmYSZsaW5rPTk0YWM5YWFjLWI0ZjktNDc3OS04OGU2LWQ1OGM0OTIwNDQ5NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=945323d0-65aa-42f2-8b5a-72da44de10fa&link=94ac9aac-b4f9-4779-88e6-d58c49204496&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "veritabani-baglanti-tanimlama_50682821_50682816.html"
source_version: "2022-09-16T11:04:15.837+03:00"
source_bytes: 10903
fetched_at: "2026-09-13T04:20:51+00:00"
generator: "netsis-scraper 1.0.0"
---
# Veritabanı Bağlantı Tanımlama

NDI aracılığıyla yapılan dizaynlar ile ilgili veri, istenen herhangi bir veritabanında saklanabilir. İstenirse, veriler birden fazla veritabanında da bulunabilir. Veritabanı Bağlantı Tanımlama bölümü, NDI uygulaması ile veritabanları arasındaki bağlantıları tanımlamak amacıyla kullanılır.

Veritabanı Bağlantı Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Veritabanı Bağlantı Tanımlama Ekranı |  |
| --- | --- |
| Bağlantı Kodu | Tanımlanan her veritabanı bağlantısı için serbest ve tekrarı olmayan bir kod belirlenmesi gerekir. Kullanıcı, kendi sistematiğine göre kodlama yapabilir. Belirlenen kod, dizaynların ve rehberlerin veritabanı bağlantı kodu bilgisinde belirtilecek olup, dizaynı ya da rehberi ilgilendiren verinin hangi veritabanında bulunduğunu tanımlar. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, bağlantı kodlarına ulaşılır. |
| Bağlantı Açıklama | Veritabanı bağlantısı için açıklama bilgisi girilen alandır. Hatırlatma amacıyla açıklayıcı bilginin yazılması gerekir. |
| Paket | NDI, Ticari, Personel, Demirbaş, İşletme, Diğer (Netsis paketleri dışında bir uygulama) paketleri arasından seçim yapılır. Netsis paketlerinden birine bağlantı yapılıyorsa, program otomatik olarak ilgili paketin hangi veritabanı sunucusunda çalıştığını algılar. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| Hesaplansın | Veritabanı bağlantısı, Netsis’in diğer paketleri içinden kullanılacak nesneler için tanımlandığında kullanılan seçenektir. Bu durumda, nesne paketin içinde çalışırken, veritabanı bağlantısını, kendi içinde çalıştığı paketle aynı şekilde yapar. |
| Veritabanı Sunucusu | Netsis paketleri dışında bir paket ile bağlantı yapılacağı zaman veritabanı sunucusunun isminin tanımlanması gerekir. Netsis paketleri ile bağlantıda, bağlanılacak veritabanı sunucusu bilgileri, pakete ait kurulum bilgilerinden otomatik olarak alınır ve sorgulanmaz. |
| Veritabanı Adı | Bağlanılacak veritabanı adının girildiği alandır. |
| Veritabanı Kullanıcı | Bağlanılacak veritabanı için hakları bulunan geçerli bir kullanıcı isminin girildiği alandır. Veritabanı Kullanıcı alanındaki kullanıcı ismi veritabanı kullanıcısı olup, Netsis paketlerinde tanımlanan kullanıcı isimleriyle ilgisi yoktur. NDI ve Diğer dışında, Netsis paketlerinden bir tanesi için bağlantı tanımlanıyorsa kullanıcı adı sorgulanmaz Bu durumda, veritabanı kullanıcı ismi, pakete ait kurulum bilgilerinden otomatik alınır. |
| Şifre | Veritabanı kullanıcısının veritabanına bağlanmak için kullandığı şifredir. NDI ve Diğer dışında, Netsis paketlerinden bir tanesi için bağlantı tanımlanıyorsa Kullanıcı Adı sorgulanmaz. Bu durumda, Veritabanı Kullanıcı Şifresi, Netsis’in güvenlik standartlarına göre otomatik oluşturulur. |
| Veritabanı Tip | NDI ve Netsis paketleri dışında bir paket ile bağlantı yapılacağı zaman sorgulanır. Netsis paketleri bağlantılarında ilgili paketin kurulum bilgilerinden otomatik alınır. MSSQL, Oracle ve DB2 veritabanları desteklenir. |
| Test | Veritabanı bağlantı tanımının geçerli olup olmadığının kontrolünü yapmak için kullanılan butondur. Eğer geçerli bir tanımlama yapılmışsa, sistem başarılı bir bağlantı yapıldığına dair uyarı verir. Eğer bağlantı tanımı geçersiz ise, veritabanına bağlanmaya çalışıldığında alınan hata, uyarı olarak ekrana gelir. Netsis paketleri içinden kullanılacak olan bağlantıları - paket seçilmiş ve hesaplanacak olan - NDI ortamından test etmek mümkün değildir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Veritabanı Bağlantı Tanımlama kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
