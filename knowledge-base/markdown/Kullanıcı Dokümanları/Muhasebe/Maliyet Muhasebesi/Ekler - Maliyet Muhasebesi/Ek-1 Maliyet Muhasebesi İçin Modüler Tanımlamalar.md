---
title: "Ek-1 Maliyet Muhasebesi İçin Modüler Tanımlamalar"
page_id: "24752309"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Maliyet Muhasebesi"
  - "Ekler / Maliyet Muhasebesi"
  - "Ek-1 Maliyet Muhasebesi İçin Modüler Tanımlamalar"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Maliyet Muhasebesi / Ekler / Maliyet Muhasebesi / Ek-1 Maliyet Muhasebesi İçin Modüler Tanımlamalar"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ2MmIwMTVhLWQ2ZTYtNGQ3ZC1iZTU1LTRkYzZhNTAxYzk1NyZsaW5rPWUwYjJiMGE5LTRiMTQtNDU3Zi05NWI2LTM2YjdmNjEzOGY1MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=462b015a-d6e6-4d7d-be55-4dc6a501c957&link=e0b2b0a9-4b14-457f-95b6-36b7f6138f50&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-1-maliyet-muhasebesi-icin-moduler-tanimlamalar_24752311_24752309.html"
source_version: "2022-12-02T15:02:28.840+03:00"
source_bytes: 128836
fetched_at: "2026-09-13T04:15:16+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-1 Maliyet Muhasebesi İçin Modüler Tanımlamalar

Maliyet muhasebesi için modüler tanımlamalarla ilgili ayrıntılı bilgiye bu dokümandan ulaşılır.

Maliyet Muhasebesi modülü; Stok, Üretim, Fatura, Muhasebe ve Entegrasyon modülleri ile entegre, Personel, Demirbaş programları ile bağlantılı çalışır. Maliyet Muhasebesi modülünden kayıt ve işlem yapılması Stok, Üretim, Fatura, ve Muhasebe modüllerindeki kayıtların eksiksiz girilmesini gerektirir. Bunlar;

- **Stok Modülü'nde;** parametre girişinden maliyet sistemi parametresinin işaretlenmesi, hammadde, mamul ve yarı mamul stok sabit kayıtlarının ayrı ayrı tanımlanması,
- **Muhasebe Modülü'nde**; muhasebe hesap planının eksiksiz girilmesi,
- **Üretim Modülünde** - **Üretimler reçetelerle yapılıyorsa -** ürün reçetelerinin oluşturulması gerekir.

Üretimi iki aşamadan oluşan bir A firmasının ele alındığı varsayıldığında;

A firmasında, 1. aşamada iki ayrı yarı mamul üretilmekte, 2. aşamada ise bu yarı mamuller kullanılarak bir mamul üretilmektedir. Bu bilgiler ışığında, A firmasının Maliyet Muhasebesi kurulumunu sırasıyla aşağıdaki şekilde gerçekleşir.

**Parametre Kayıtları**

![](../../../../_assets/822420f6a0c3b1b9b338.png)

Maliyet Muhasebesi kayıtlarının oluşturulması ve entegre işlemlerinin yapılması için ilk işlem, Stok → Stok Parametreleri bölümünden maliyet sistemini sorgulayan parametrenin işaretlenmesi ve maliyet tipinin seçilmesi gerekir.

Maliyet sisteminin işaretlenmesi sayesinde, Stok → İşlemler → Maliyet Oluşturma bölümünün çalışması ile oluşan değerler, stok kayıtları ek sahalardaki birim maliyet sahasına program tarafından - ilk madde ve ambalaj malzemeleri için - atanır.

**Stok Sabit Kayıtlarının Tanımlanması**

![](../../../../_assets/2c1df24b987165773254.png)

Maliyet Muhasebesi için ön çalışmaların ilk etabı stok kayıtlarının tanımlanmasıdır. Maliyet Muhasebesi'ni oluşturmak için tüm hammadde, yarı mamul ve mamullerin stok sabit kayıtlarından tanımlanması gerekir.

A firmasının stokları aşağıdaki şekilde kodlanmıştır. A firmasında YM1 ve YM2 üretilmiştir ve bu iki yarı mamul MM1’in üretiminde kullanılmıştır.

**Hammaddeler**

```text
H1                    Hammadde 1
```

```text
H2                    Hammadde 2
```

```text
H3                    Hammadde 3
```

**Mamul Grubu 1**

```text
MM1                Mamul 1
```

**Yarı Mamul Grubu**

```text
YM1                 Yarı Mamul 1
```

```text
YM2                 Yarı Mamul 2
```

**Ambalaj Malzemeleri**

```text
AMB1              Ambalaj Malzemesi
```

Stok kayıtlarının oluşturulmasında maliyet muhasebesine yönelik önemli noktalar şunlardır;

Stok Kartı Kayıtları ekranında aynı maliyet grubuna ait olan stok kayıtlarının **ölçü birimlerinin** aynı standartta oluşturulmasına dikkat edilmesi gerekir.

Tüm stok kayıtlarının, Ek Bilgiler sekmesinden tanımlanan, **Türü ve Mamul Grup** bilgilerinin girilmesi gerektiğine dikkat edilmesi gerekir.

![](../../../../_assets/053853e042d1f02afae0.png)

Stok kartlarındaki tanımlamalardan önce, Maliyet Muhasebesi modülündeki Mamul Grup Kodu tanımlamalarının yapılması gerekir. Mamul Grup Kodu, Maliyet Muhasebesi modülünden tanımlanan Maliyet Grup Kodunun girildiği alandır. Bu alanda, maliyet grup kodlarının rehberine ulaşılır. Maliyet grup kodlarının tanımlanması ile ilgili ayrıntılı açıklamalara [Maliyet Bilgi Girişi](<../Kayıt - Maliyet Muhasebesi/Maliyet Bilgi Girişi.md>) bölümünden ulaşılır.

Türü, maliyet hesaplamaları için belirteç olan sahadır. Maliyet Muhasebesi modülünden oluşan mahsup fişinde kullanılan hesaplar, bu sahadaki türe göre değişir. Bu sahada mamul, yarı mamul ve yan ürün olarak tanımlanan stok kodları için Mamul Grup Kodu bilgisinin mutlaka girilmesi gerekir.

Örneğe göre MM1 kodlu stok için Mamul tipi seçilmiştir. Ayrıca, yine kodlama örneğinde verilen stok kodlarından H1,H2,H3 için bu sahanın İlk madde, YM1 ve YM2 için Yarı mamul olarak belirtilmesi gerekir. Üretimde ambalaj için kullanılan AMB1'in Ambalaj Malzemesi olarak işaretlenmesi gerekir.

**Muhasebe Hesap Planının Tanımlanması**

Maliyet ana grupları (Ana ürün merkezleri), aynı zamanda Esas Üretim Gider Yeri merkezleridir. Tanımlamaların düzgün yapılması için, Muhasebe Modülü'ndeki hesap kodlarının üretim gider yerleri bazında açılması gerekir. Kullanıcı firmalar, bu konuda kendileri karar verebilirler. Eğer muhasebede hesap planı detayı olmadan, referans kodu sistemi ile çalışılıyorsa, ana ürün merkezi tanımlamalarında da referans kodlarını kullanarak maliyet hesaplamaları oluşturulabilir.

Maliyet hesapları, muhasebe hesap planında ürün bazında detay verilmeden oluşturulabilir. Fakat, ana hesap bazında sarf, maliyet ve satılan malın maliyeti mahsuplarının işlemleri çok zor, sektör bazında da bazen imkansızdır. Bu durumda, maliyet hesaplamalarının çekirdeği olan hammadde, yarı mamul ve mamul hesaplarının detaylandırılması, kontrol işlemlerini kolaylaştırır.

Ürün bazında detaylı maliyet hesaplamalarında, 26/12/1992 tarih ve 21447 sayılı Tek Düzen Hesap Planı ile ilgili tebliğ bunların çeşitlendirilmesini, yani ana ürün merkezlerine, yan ürün merkezlerine (Yardımcı üretim merkezlerine) ve masrafın çeşidine göre gruplara ayrılmasını gerekli görür.

Ana ve yardımcı ürün merkezlerinin, işletmelerin isteklerine göre detaylanmasına karşın, masraf çeşidi detayı, ilk madde malzeme giderleri, işçilik ücret ve giderleri, memur ücret ve giderleri, dışarıdan sağlanan fayda ve hizmetler, çeşitli giderler, vergi-resim ve harçlar, amortismanlar ve tükenme payları, finansman giderleri olarak ayrı ayrı tanımlanması gerekir.

Masraf çeşidine ait hesapların ana başlıklarını Muhasebe Sistemi Uygulama Genel Tebliği aşağıdaki şekilde açıklamıştır:

**Direkt İlk Madde ve Malzeme Giderleri**

Bu giderler esas üretim gider yerleri ile ilgili olup; mamulün bünyesine giren, mamulün temel öğesini oluşturan ve mamulün bünyesine doğrudan yüklenen maddelerin kullanımı için fiili tutarlarla **Direkt İlk Madde ve Malzeme Giderleri** hesabından izlenir.

**Direkt İşçilik Giderleri**

Bu giderler esas üretim gider yerleri ile ilgili olup, belli bir mamulün veya hizmetin üretim maliyetine doğrudan doğruya yüklenebilen işçilik giderlerini kapsar. Bu giderlerin hangi mamul veya mamul grubu için harcandığı izlenebilir ve herhangi bir dağıtım anahtarına gerek duyulmadan, işçi başına düşen çalışma süresi ölçülebilen işçilik giderlerinden oluşur. Esas üretim gider yerleri bazında aylık değerler, Netsis Personel programından muhasebeye entegre edilebilir.

**Genel Üretim Giderleri**

İşletmenin üretimi ve bu üretime bağlı hizmetler için yapılan direkt işçilik ve direkt hammadde ve malzeme dışında kalan giderlerin izlendiği hesaptır.

Bu giderlerin;

```text
         Üretim hizmet maliyeti ile ilgili bir gider niteliğini taşıması,
```

```text
        Çeşit ve değer yönü ile doğrudan doğruya değil, ancak dağıtım yoluyla üretim ve hizmet maliyetlerine yansıtılabilir nitelikte olması gereklidir.
```

Esas üretim merkezleri bazında, bu ana hesap altında işlenecek amortisman hesaplarının aylık ve yıllık değerleri, Netsis Demirbaş programından muhasebeye entegre edilebilmektedir.

Dönem sonlarında Esas Üretim Merkezlerine göre açıklanan hesaplar, yansıtma hesapları ile karşılaştırılarak kapatılır. Maliyet muhasebesi programında, maliyet mamul grupları bazında bu yansıtma hesapları da sorgulanmaktadır.

**Direkt İlk Madde Ve Malzeme Yansıtma Hesabı**

Dönem sonlarında, 710- Direkt İlk Madde ve Malzeme Giderleri bu hesapla karşılaştırılarak kapatılır.

**Direkt İşçilik Giderleri Yansıtma Hesapları**

Dönem sonlarında, 720-Direkt İşçilik giderleri hesabı bu hesapla karşılaştırılarak kapatılır.

**Genel Üretim Giderleri Yansıtma Hesabı**

Dönem sonlarında, 730-Genel Yönetim Giderleri bu hesapla karşılaştırılarak kapatılır. Sınai maliyet kapsamına giren hesaplar;

Hatırlanacağı gibi A firması iki ayrı safhadan oluşan bir üretim yapıyordu. Aşağıdaki bölümde Maliyet Ana Mamul Kodlarının tanımlamalarında bahsedileceği gibi, mamullerin üretimi iki ayrı safhadan meydana gelir. Öncelikle ilk safhada YM1 ve YM2 üretiliyor ve daha sonra bu yarı mamuller MM1’in üretimi için kullanılıyor. Maliyet Muhasebesi modülünde, Maliyet Ana Grup Kodu olarak YM’ler için 1. AŞAMA, MM1 için 2. AŞAMA tanımlanmış ve her türlü detay - Stok Sabit Kayıtları, Muhasebe Hesap Planı) bu iki safhaya göre oluşturulmuştur.

**Üretim Reçetelerinin Tanımlanması**

Üretici firmaların, ürün maliyetlerini hesaplanması için reçeteye tabi mamullerinin reçete kayıtlarını, Üretim → Kayıt → Reçete Kaydı bölümünden tanımlaması gerekir.

**Üretim → Reçete Kaydı** bölümünden, üretimi yapılacak mamuller için hammadde ve/veya yarı mamullerden oluşan reçetelerin kayıtları ile, izleme ve reçete değişiklikleri yapılabilir. Bütün mamul ve yarı mamullerin reçetelerinin bu bölümden ayrı ayrı kaydedilmesi gerekir.

Bünyede üretimi yapılan tüm mallar mamul veya yarı mamul, üretimi gerçekleştirmek için satın alınan mallar ise hammadde olarak düşünüldüğünde, hangi hammaddelerin hangi yarı mamuller içinde kullanıldığına göre yarı mamul reçeteleri ve hangi hammadde ve yarı mamullerin hangi mamuller içinde kullanıldığına göre de mamul reçeteleri oluşturulur.

Birden fazla seviyeli reçeteler de oluşturulabilir. Yarı mamul seviye sayısı istenen sayıda artırılabilir.

Reçete oluştururken, yarı mamuller ve mamuller olarak bir öncelik sırası yoktur. İstenen düzende reçete oluşturulabilir. Tek şart; tüm hammadde, yarı mamul ve mamul kodlarının stoklarda tanımlanmış olmasıdır.

Seviyelendirme ne kadar anlaşılır ve basit tutulursa, Üretim modülünde çalışmak o kadar kolaylaşır.

MM1 üretim reçetesinin oluşturulması için kullanılan hammadde, ambalaj ve yarı mamul listesinin örneği aşağıdaki şekildedir:

**MM1**

```text
          Hammaddeler
```

```text
                                      H4
```

```text
          Yarımamul 1
```

```text
                                      H1
```

```text
                                      H2
```

```text
          Yarımamul 2
```

```text
                                      H3
```

```text
         Ambalaj Malzemesi
```

```text
                                      AMB1
```

Maliyet Muhasebesi işlemlerinden önce hammadde maliyetlerinin oluşturulması için, üretim reçeteleri bazında üretim sonu kayıtlarının çalıştırılması gerekir. Üretim sonu kayıtlarıyla ilgili önemli noktalar, [Maliyet Hesaplatma](<../Kayıt - Maliyet Muhasebesi/Maliyet Hesaplatma.md>) bölümünde yer alır.
