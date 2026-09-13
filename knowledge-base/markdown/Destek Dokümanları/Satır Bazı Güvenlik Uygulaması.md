---
title: "Satır Bazı Güvenlik Uygulaması"
page_id: "111247662"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Satır Bazı Güvenlik Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Satır Bazı Güvenlik Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTkzOGYxMzkxLTRjMjAtNGE1NC05ODVkLWNhYTAxMTRkZGNhNiZsaW5rPTNjY2EzZjA3LTAwZDktNDFlZi1hMTkzLTFlNDFiYzk2NTAzOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=938f1391-4c20-4a54-985d-caa0114ddca6&link=3cca3f07-00d9-41ef-a193-1e41bc965039&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "satir-bazi-guvenlik-uygulamasi_111247672_111247662.html"
source_version: "2023-05-05T11:25:49.383+03:00"
source_bytes: 372437
fetched_at: "2026-09-13T04:23:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# Satır Bazı Güvenlik Uygulaması

Netsis Satır Bazı Güvenlik uygulamasıyla ilgili ayrıntılı bilgiye bu dokümandan ulaşılır.

Netsis Satır Bazı Güvenlik sistemi, veri tabanındaki kayıtları satır bazında görüntüleme ve işlem yetkilerinin, "Kullanıcı", "Kullanıcı Grubu" veya "Tüm Kullanıcılar" bazında sınırlandırılabilmesini sağlar.

Satır Bazı Güvenlik uygulaması, Oracle & SQL Server 2016 ve üzeri versiyonların tüm sürümlerinde (Express, Standard, Enterprise) kullanılabilir.

Satır Bazı Güvenlik Sisteminin kullanılabilmesi için Şirket / Şube / Parametre Tanımları ekranından **Güvenlik** **Uygulaması** parametresinin **"Satır** **Bazı** **Güvenlik** **Sistemi"** veya **"Hepsi"** olarak seçilmesi gerekir.

![](../_assets/e7117438b65604ea258a.png)

Güvenlik tanımlamaları, "Genel\\Kullanıcı İşlemleri\\Kayıt\\Satır Bazı Güvenlik" menüsünden gerçekleştirilir.

Örneğin; Kullanıcılar il bazında tanımlanan kullanıcı gruplarına bağlıdır. Her kullanıcının yalnızca bağlı olduğu ilde bulunan müşterileri görüntüleme ve işlem yetkisinin tanımlanması istenmektedir.

İzmir için örnek tanımlama aşağıdaki gibi gerçekleştirilir.

Kısıt Kapsamı alanında Grup seçeneği işaretlenerek Grup Kodu rehberinden "IZMIR" kullanıcı grubu seçilir.

Veritabanı Nesnesi, kısıtlamanın yapılacağı tablo nesnesinin belirtiği alandır. Örneğimizde Cari Hesap Kayıtları ile ilgili bir kısıtlama yapılacağı için "TBLCASABIT" nesnesi seçilir.

![](../_assets/1792c0567bf88277a395.png)

Satır Bazı Güvenlik ile **izleme** ve **işlem** olmak üzere iki çeşit kısıtlama yapılabilir.

**İzleme** **Kısıtı:** Seçilen kullanıcıların belirlenen kısıt ifadesine uygun kayıtları görüntüleyebilmesi veya görüntüleyememesi için kullanılan kuraldır.

Örn; Kullanıcının sadece İzmir'e iline ait kayıtları görüntülemesi için (@CARI_IL='IZMIR'),

İzmir dışındaki tüm kayıtları görüntüleyebilmesi için (@CARI_IL\<\>'IZMIR') şeklinde tanımlanabilir.

Örneğimizdeki kısıt tanımlandıktan sonra İzmir grubuna bağlı bir kullanıcı tarafından programa giriş yapıldığında ekranlarda, raporlarda ve rehberlerde cari il bilgisi İzmir olmayan kayıtların gösterilmesine izin verilmeyecektir.

İzleme seçilerek oluşturulan kısıtlar **NFS_RLS_PREDICATE_XXX_FILTER** (XXX Tablo Adı) adıyla oluşturulan Table Valued Function'a eklenir.

**İşlem** **Kısıtı:** Seçilen kullanıcılar için kısıt ifadesinde belirtilen kayıtlarda, kayıt, düzelme ve silme işlemlerinin engellenmesi için kullanılır.

Örneğin; Yetki grubu "İzmir" olan bir kullanıcı tarafından cari il bilgisine "İzmir" dışında bir kayıt girilmek istendiğinde ekran görüntüsündeki uyarı alınacaktır.

![](../_assets/51d5b72fe16e68d6d231.png)

İşlem kısıtı seçilerek oluşturulan kayıtlar **NFS_RLS_PREDICATE_XXX_BLOCK** (XXX Tablo Adı) adıyla oluşturulan Table Valued Function'a eklenir.

**Hepsi** seçilerek oluşturulan kayıtlar ise; **NFS_RLS_PREDICATE_XXX**\_**FILTER** ve **NFS_RLS_PREDICATE_XXX_BLOCK** için oluşturulan Table Valued Function'a eklenir.

*Not: Kısıt Tipi seçeneği* *sadece SQL Server veritabanlarında* *kullanılabilir.*

**Detaylı** **Tanım:** Detaylı Tanım yöntemi seçildiğinde alttaki bölüme istenen kısıt tanımı serbest bir biçimde yazılabilir. Kısıt tanımlarında saha adının başında @ ifadesi yer almalıdır.

*Örn;* *@CARI_KOD LIKE 'M%' AND @CARI_TIP = 'A' AND (@CARI_IL = 'IZMIR' OR @CARI_IL = 'AYDIN')*

**Basit Tanım:** Basit Tanım yönteminde SQL cümlesinin yazıldığı bölüm yerine saha listesinin bulunduğu bir tablo ekrana gelecektir. Saha Adı alanından tablonun kısıt ifadesinin yazılacağı saha adı seçilir ve ilgili operatör belirtilerek değer alanlarına kısıt değeri yazılır.

![](../_assets/3442db8caa3e13a51d9e.png)

Birden fazla alana kısıt vermek için sağ klik menüsü "Araya Satır Ekle" seçeneği kullanılabilir.

**Tablo Sahaları**

"Veritabanı Nesnesi" alanında seçilen tabloya ait sahaların izlenmesi için kullanılan butondur. Böylece, kısıt verilecek tablonun saha isimlerine bu ekrandan bakılabilir.

Satır bazı güvenlik kısıtları kaydedildiğinde Row-Level Security (RLS) tanımları için gereken table valued function nesneleri otomatik olarak oluşturulur ve bu fonksiyonlar oluşturulan policy'lere otomatik eklenir.

Yukarıdaki tanımlara göre function ve policy aşağıdaki gibi oluşur.

Predicate Block Function (Kısıt Tipi İşlem/Hepsi Seçildiğinde)

CREATE FUNCTION \[dbo\].\[NFS_RLS_PREDICATE_BLOCK_TBLCASABIT\] (@SUBE_KODU AS INTEGER,@ISLETME_KODU AS INTEGER,@CARI_KOD AS VARCHAR(MAX),@CARI_TEL AS VARCHAR(MAX),@CARI_IL AS VARCHAR(MAX),@ULKE_KODU AS VARCHAR(MAX),@CARI_ISIM AS VARCHAR(MAX),@CARI_TIP AS VARCHAR(MAX)………)

RETURNS TABLE

WITH SCHEMABINDING AS

RETURN SELECT 1 AS RESULT

WHERE 1=1

AND 1=( CASE

WHEN ( CAST( SESSION_CONTEXT(N'NETSIS_GROUP_ID' ) AS INTEGER )='-18' ) THEN

CASE WHEN (@CARI_IL = 'IZMIR' AND @CARI_TIP='A') THEN 1 ELSE 0 END

WHEN ( CAST( SESSION_CONTEXT(N'NETSIS_GROUP_ID' ) AS INTEGER )='-19' ) THEN

CASE WHEN (@CARI_IL = 'ISTANBUL' AND @CARI_TIP='A') THEN 1 ELSE 0 END

WHEN ( CAST( SESSION_CONTEXT(N'NETSIS_GROUP_ID' ) AS INTEGER )='-20' ) THEN

CASE WHEN (@CARI_IL='ANKARA' AND @CARI_TIP='A') THEN 1 ELSE 0 END

ELSE 1 END)

GO

Predicate Filter Function (Kısıt Tipi İzleme/Hepsi Seçildiğinde)

CREATE FUNCTION \[dbo\].\[NFS_RLS_PREDICATE_FILTER_TBLCASABIT\] (@SUBE_KODU AS INTEGER,@ISLETME_KODU AS INTEGER,@CARI_KOD AS VARCHAR(MAX),@CARI_TEL AS VARCHAR(MAX),@CARI_IL AS VARCHAR(MAX),@ULKE_KODU AS VARCHAR(MAX),@CARI_ISIM AS VARCHAR(MAX),@CARI_TIP AS VARCHAR(MAX)………)

RETURNS TABLE

WITH SCHEMABINDING AS

RETURN SELECT 1 AS RESULT

WHERE 1=1

AND 1=( CASE

WHEN ( CAST( SESSION_CONTEXT(N'NETSIS_GROUP_ID' ) AS INTEGER )='-18' ) THEN

CASE WHEN (@CARI_IL = 'IZMIR' AND @CARI_TIP='A') THEN 1 ELSE 0 END

WHEN ( CAST( SESSION_CONTEXT(N'NETSIS_GROUP_ID' ) AS INTEGER )='-19' ) THEN

CASE WHEN (@CARI_IL = 'ISTANBUL' AND @CARI_TIP='A') THEN 1 ELSE 0 END

WHEN ( CAST( SESSION_CONTEXT(N'NETSIS_GROUP_ID' ) AS INTEGER )='-20' ) THEN

CASE WHEN (@CARI_IL='ANKARA' AND @CARI_TIP='A') THEN 1 ELSE 0 END

ELSE 1 END)

GO

Security Policy

CREATE SECURITY POLICY \[dbo\].**\[NETSIS_POLICY_RLS_TBLCASABIT\]**

ADD FILTER PREDICATE \[DBO\].**\[NFS_RLS_PREDICATE_FILTER_TBLCASABIT\]**(\[SUBE_KODU\],\[ISLETME_KODU\],\[CARI_KOD\],\[CARI_TEL\],\[CARI_IL\],\[ULKE_KODU\],\[CARI_ISIM\],\[CARI_TIP\],\[GRUP_KODU\]……………) ON \[dbo\].\[TBLCASABIT\],

ADD BLOCK PREDICATE \[DBO\].**\[NFS_RLS_PREDICATE_BLOCK_TBLCASABIT\]**(\[SUBE_KODU\],\[ISLETME_KODU\],\[CARI_KOD\],\[CARI_TEL\],\[CARI_IL\],\[ULKE_KODU\],\[CARI_ISIM\],\[CARI_TIP\],\[GRUP_KODU\]……………) ON \[dbo\].\[TBLCASABIT\]

WITH (STATE = ON, SCHEMABINDING = ON)

GO

**Kuralları Yeniden oluştur**

Satır bazı güvenlik kuralları doğru bir şekilde çalışmadığında veya Security Policy ve Function nesnelerinin içeriğinde kuralların doğru çalışmasını etkileyen bir değişiklik meydana geldiğinde Policy ve Function nesnelerinin yeniden oluşmasını sağlar.

**Kural Önizleme**

Tanımlanan kuralların önizlemesi için kullanılan ekrandır. Ön izlemesi istenen Kullanıcı veya Grup kodu ve ilgili veritabanı nesnesi seçim yapıldıktan sonra \<\<tab\>\> tuşuna basıldığında, tabloda seçilen kullanıcının görüntüleyebileceği kayıtlar listelenir. Örn; “IZMIR” grubundaki kullanıcılar tarafından programa giriş yapıldığında, kısıt verilen tablodaki kayıtların nasıl görüntüleceği aşağıdaki gibi izlenebilir.

![](../_assets/dbc9d6f5369267544cd5.png)

Satır bazı güvenlik uygulamasında dikkat edilmesi gereken bazı durumlar vardır. Örneğin bir kullanıcı için belirli bir stok grubu kısıtlandığında, kısıt kapsamındaki kullanıcı tarafından Maliyet Oluşturma işlemi çalıştırıldığında yetkisi olmayan stok grubu için maliyet işlemi çalıştırılmayacaktır. Bu nedenle bu gibi işlemlerin kısıtlı olmayan kullanıcılarda yapılması önerilir.

*Not: Satır bazı güvenlik kısıtlamaları admin kullanıcılar için yapıldığında dikkate alınmamaktadır.*
