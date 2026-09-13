---
title: "Netsis Sigorta Poliçe Takibi"
page_id: "74719407"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Sigorta Poliçe Takibi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Sigorta Poliçe Takibi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTBlMThlNTc1LTdkY2ItNGFlYS1hZjNjLTAzN2U2Yzc5NWMzNSZsaW5rPTU0MzMwNGYzLTM0YzItNGI5YS05ZmMwLWY4MTZiYTk0MWI4OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0e18e575-7dcb-4aea-af3c-037e6c795c35&link=543304f3-34c2-4b9a-9fc0-f816ba941b88&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-sigorta-police-takibi_80087457_74719407.html"
source_version: "2024-03-01T18:14:32.963+03:00"
source_bytes: 2052809
fetched_at: "2026-09-13T04:24:13+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Sigorta Poliçe Takibi

Şirketlerin yaptığı sigortalar sonucunda oluşan poliçelerin tanımlanması, muhasebe kayıtlarının oluşturulması, tahakkuk işlemlerinin yapılması, ödemelerin takibi ve poliçelerin yenilenmesi amacıyla Sigorta Poliçe Takibi desteği getirilmiştir.
Poliçe takibi sırasında süreç şu şekilde işlemektedir:

- Öncelikle sigorta acentesi üzerinden yapılan poliçenin genel bilgileri Netsis üzerine kaydedilmekte ve ödeme planı bilgileri girilmektedir. Poliçe açılışı için poliçe dekont kaydı oluşturulmaktadır. Poliçe tutarının ilgili muhasebe dönemi içindeki kısmına karşılık gelen toplam tutar 180 hesaba ve geri kalan kısmı 280 hesaba borç olarak işlenmekte ve bunlara karşılık olarak da ödeme planına uygun vadelerle acente firmasının cari koduna alacak kaydı atılmaktadır.
- Sonraki her ay ödeme planına uygun olacak şekilde poliçe taksitleri sigorta acentesine ödenmektedir ve aynı zamanda poliçe tahakkuk işlemi yapılarak 180 hesaptaki ilgili aya karşılık gelen tutar daha önceden poliçe tanımlarında belirtilen 7'li gider hesaplarına virman yapılmaktadır.

**Poliçe Tip Tanımları**

Poliçe tiplerinin tanımlandığı ekrandır. Bu ekran üzerinden yapılan tanımlamalar daha sonra "Poliçe Tanımlar" ekranındaki "Poliçe Tipi" alanı üzerinde listelenecektir.

Poliçe tip kodu ve açıklama alanlarına program içerisinde takip edilmek istenilen kod ve açıklama bilgisi girilmelidir.

Bağlantı tipi, ilgili poliçe tipinin demirbaş veya personel paketleriyle bağlantılı kullanılmak isteniyor ise seçilebilir. Diğer seçili olması durumunda herhangi bir paketle bağlantı kurulmayacaktır.

Poliçe tanımında bağlantı girişi zorunlu olsun parametresi bağlantı tipinin demirbaş veya personel seçilmesi durumunda aktif hale gelmekte olup, seçilmesi durumunda poliçe tanımı ekranında demirbaş veya personel tipli bağlantıların da girişi zorunlu hale gelecektir.

![](../_assets/13cac13c910f63c9c7f4.png)

**Poliçe Tanımları**

Bu ekran üzerinden yapmış olduğumuz poliçeye ait detay tanımlar, ödeme planı girişleri ve ödemeler takip edilebilmektedir.

**Poliçe Bilgileri Sekmesi**

![](../_assets/23abec641051f2ca6ffe.png)

Poliçe No: Sigorta poliçe numarası bilgisidir.
Yenileme No: Sigorta poliçesi üzerindeki yenileme no bilgisidir.
Cari Kod: Sigorta poliçesinin hangi acente ile yapıldı ise acentenin cari kodu bilgisi girilmelidir.
Sigorta Firma Kodu: Bu alan zorunlu bir alan değildir ve istenirse sigorta firmasının hangi sigortaya bağlı olduğunu takip edebilmek amacıyla cari kodu bazında seçim yapılıp raporlama amaçlı kullanılabilir.
Poliçe Tipi: "Poliçe Tip Tanımları" ekranında tanımlanan kayıtların "Tip Açıklama" bilgisi gösterilmektedir. Seçilmesi zorunlu bir alandır.
Durumu: Poliçenin durum bilgisi yer alır. Günün tarihine göre poliçenin durumu dinamik şekilde gösterilmektedir. Durum bilgileri aşağıdaki şekildedir.

- Yürürlükte: Günün tarihi poliçe başlangıç ve bitiş tarihleri arasında yer alıyorsa,
- Yürürlüğe Girecek: Günün tarihi poliçe başlangıç tarihinden küçük ise,
- Yürürlük Dışı: Günün tarihi poliçe bitiş tarihinden büyük ise.

<u>Tanzim Tarihi/Yeri:</u> Sigorta poliçesinin düzenleme tarihi ve düzenleme yeri bilgileri bu iki alana girilebilmektedir. "Tanzim Tarihi" alanı zorunlu bir alandır. "Tanzim Yeri" alanı ise zorunlu değildir.

<u>Başlangıç Tarihi: </u>Poliçenin yürürlüğe gireceği tarih bilgisidir.

<u>Bitiş Tarihi:</u> Poliçenin yürürlükten çıkacağı tarih bilgisidir.

<u>Döviz Tipi: </u>Varsayılan olarak 0 (TL) olarak gelmektedir. Bu alana sıfırdan farklı bir değer girilir ise "Döviz Kuru" sahası aktif olmakta ve otomatik olarak "Tanzim Tarihi" alanındaki tarihe ait kur bilgisi yazılmaktadır.

<u>Döviz Kuru:</u> "Döviz Tipi" alanında sıfırdan farklı bir değer seçilmesi durumunda kur bilgisine sıfırdan büyük bir değer girilmelidir.

<u>Döviz Tutarı:</u> "Döviz Tipi" alanında sıfırdan farklı bir değer seçilmesi durumunda girilen döviz tutarı bilgisidir.

<u>Tutar:</u> Poliçenin tutar bilgisidir. Eğer "Döviz Tipi" sahasında sıfırdan farklı bir değer seçilmiş ise \[Döviz Tutarı \* Döviz Kuru\] değeri otomatik olarak "Tutar" sahasına yazılmaktadır. Eğer "Döviz Tipi" sahasında sıfırdan farklı bir değer seçilmiş ve Tutar sahasındaki değer değiştiriliyor ise \[Tutar / Döviz Tutar\] değeri "Döviz Kuru" sahasına otomatik olarak yazılmaktadır.

<u>Gelecek Aylar Gid. Hs.:</u> Gelecek aylara ait kullanılmak istenilen gider hesap bilgisidir.

<u>Gelecek Yıllar Gid. Hs.:</u> Gelecek yıllara ait kullanılmak istenilen gider hesap bilgisidir.

Poliçe dekont kaydı oluşturulurken ay bazında farklı hesap kodlarına tutarlar aktarılmak isteniyor ise hesap kodunda ay kodunun takip edildiği seviyeye "?" karakteri yazılarak tanım yapılabilir. Bu şekilde "?" içeren bir değer girilirse "Muhasebe Parametreleri" ekranındaki "Seviye Takibi" sekmesindeki "Seviye Takibi Yapılsın" parametresinin seçili olması durumunda seviye takibine uygun şekilde girişinin yapılıp yapılmadığının kontrolü sağlanmaktadır.

<u>Plasiyer Kodu:</u> "Şirket-Şube Parametre Tanımları" ekranında plasiyer kodu uygulaması işaretli ise plasiyer kodu girilmelidir.

<u>Proje Kodu</u>: "Şirket-Şube Parametre Tanımları" ekranında proje kodu uygulaması işaretli ise proje kodu girilmelidir.

<u>Referans Kodu</u>: "Muhasebe Parametreleri" ekranında "Yevmiye" sekmesinde "Fişlerde Referans Kodu Sorulsun" parametresi işaretli ise referans kodu girilmelidir.

<u>Açıklama-1</u>: Poliçe için girilmek istenilen ek açıklama bilgisidir.

<u>Açıklama-2:</u> Poliçe için girilmek istenilen ek açıklama bilgisidir.

<u>Açıklama-3:</u> Poliçe için girilmek istenilen ek açıklama bilgisidir.

<u>Belge Ekle:</u> Bu butonun aktif olabilmesi için daha önceden kaydedilmiş bir kaydın seçilmiş olması gerekmektedir. Butona tıklandığında standart belge ekleme bileşeni açılmakta ve ilgili poliçe tanımı için belge eklenerek TBLEVRAK tablosu altında saklanabilmektedir.

<u>Hatırlatıcı Kaydı Oluştur:</u> Bu butonun aktif olabilmesi için daha önceden kaydedilmiş bir kaydın seçilmiş olması gerekmektedir. Ekran üzerinden hangi kullanıcılar için hatırlatıcı oluşturulmak isteniyor ise kullanıcı listesinden kullanıcılar seçilip, hatırlatma için poliçe bitiş tarihine kalan gün sayısı seçimi yapılmalıdır. "Kaydet" butonuna tıklandığında seçilen her bir kullanıcı için hatırlatma kaydı oluşturulacaktır.

![](../_assets/f187b4367b0550fd2db6.png)

<u>Tahakkuk Mahsubu:</u> Bu butonun aktif olabilmesi için daha önceden kaydedilmiş bir kaydın seçilmiş olması ayrıca ilgili kayıt için "Ödeme Planı" ve "Gider Hesapları" sekmesindeki tanımların yapılmış olması gerekmektedir. Butona tıklandığında Poliçe No, Yenileme No ve Cari Kodu bilgileri kullanılarak "Poliçe Tahakkuk Mahsubu" ekranı açılacak ve ilgili kısıtlar ekrana geçilecektir.

<u>Tahakkuk İptali:</u> Bu butonun aktif olabilmesi için daha önceden kaydedilmiş bir kaydın seçilmiş olması gerekmektedir, ayrıca ilgili kayıt için daha önceden poliçe dekont kaydı oluşturulmuş olmalıdır, yani grid üzerinde "Dekont No" bilgisi dolu olmalıdır. Butona tıklandığında Poliçe No, Yenileme No ve Cari Kodu bilgileri kullanılarak "Poliçe Tahakkuk İptali" ekranı açılacak ve ilgili kısıtlar ekrana geçilecektir.

**Ek Bilgiler Sekmesi**

**![](../_assets/e7f8036716ba0605e0fc.png)**

Poliçe Tanımları için "Yardımcı Programlar\> Kayıt\> Saha Tablo Eşleştirmesi" ekranındaki "Finans" menüsü altında yer alan "Poliçe Tanımları" seçeneği ile ek alanlar eklenebilmektedir.

![](../_assets/64571373337f7b932d02.png)

**Demirbaş/Personel Bağlantı Sekmesi**

**![](../_assets/ab6dfd0cf73df6f51a14.png)**

Bu sekmenin görünür olabilmesi için seçilen poliçe tipinin bağlantı tipinin "Demirbaş Bağlantılı" veya "Personel Bağlantılı" olması gerekmektedir, aksi halde sekme gözükmeyecektir. Ayrıca seçilen poliçe tipine göre Netsis üzerinde demirbaş paketiyle veya personel paketiyle bağlantı tanımlarının yapılıp yapılmadığı kontrol edilmektedir.

Seçilen "Poliçe Tipi" demirbaş bağlantılı ise sekme ismi "Demirbaş Bağlantı", personel bağlantılı ise "Personel Bağlantı" olarak gösterilmektedir.

Seçilen poliçe tipinin bağlantı tanımına göre demirbaş kodu veya personel kodu bilgisi sorulacak ve demirbaş/bordro paketlerinden ilgili tanımlar seçilerek n tane kayıt bağlantı olarak poliçeye bağlanabilmektedir. Aynı zamanda eklenecek her bir bağlantı kaydı için kullanıcı tanımlı ek açıklamaları girilebilmesi amacıyla "Yardımcı Programlar\>Kayıt\> Saha Tablo Eşleştirmesi" ekranındaki "Finans" menüsü altına "Poliçe Bağlantı Tanımları" seçeneği ile ek sahalar eklenebilmektedir.

![](../_assets/72101771696f12706c1e.png)

**Gider Hesapları Sekmesi**

Gider hesapları sekmesi üzerinden "Tahakkuk Oluşturma" sırasında kullanılacak gider hesapları yüzde şeklinde oran verilerek ve birden fazla olabilecek şekilde tanımlanabilmektedir. Bir poliçe tanımı için %100 oranını aşacak şekilde gider hesabı tanımlanamaz, bu yüzden bütün gider hesaplarının toplam oranının %100'ü aşıp aşmadığı kontrol edilmeli ve aksi bir durumda "Gider hesaplarının toplam oranı %100'ü aşamaz." uyarısı alınmaktadır.

![](../_assets/957b2f9d5bff37eb34ae.png)

<u>Gider Hesabı:</u> Gider hesabı tanımı yapılmalıdır, zorunlu bir alandır.

<u>Oran (%):</u> Zorunlu bir sahadır ve varsayılan olarak sıfır gelmelidir. Bu sahaya sıfırdan küçük bir değer girilemez.

**Ödeme Planı Sekmesi**

Ödeme planı sekmesi üzerinden "Poliçe Dekont Kaydı" sırasında cari kodunu alacaklandırma için atılacak kayıtlara ait vade tarihi belirlenebilmektedir. Oluşturulan ödeme planının tarihlerine ve tutarlarına uygun olacak şekilde cari hesabına alacak kaydı atılmaktadır.

Sekme üzerindeki "Ödeme Tarihi" alanı zorunlu bir sahadır ve varsayılan olarak günün tarihi olarak gelmektedir. Aynı şekilde "Taksit Tutarı" sahası da zorunlu bir sahadır ve sıfırdan büyük bir değer girilmelidir. Eğer "Poliçe Bilgileri" sekmesindeki "Döviz Tipi" sahası sıfırdan farklı ise grid üzerinde "Döviz Tutarı" bilgisi gösterilmektedir. Grid üzerindeki "Döviz Tutar" bilgisi \[Taksit Tutarı \* Poliçe Bilgileri sekmesindeki Döviz Kuru\] şeklinde hesaplanmaktadır.

Eğer ilgili taksit için "Ödeme Kaydı" butonu ile bir ödeme dekont kaydı atılmış ise, grid üzerinde yer alan "Ödendi" sahasında "Evet" değeri yazılmakta ve ödeme için atılan dekonta ait bilgiler "Dekont Seri" ve "Dekont No" sahalarında gösterilmektedir

Grid üzerine atılan kayıtların toplam taksit tutarı "Poliçe Bilgileri" sekmesinde "Tutar" sahasından daha büyük olamaz, büyük olması durumunda "Toplam taksit tutarı poliçenin tutarından büyük olamaz." uyarısı alınmaktadır.

<u>Ödeme Planı Oluştur:</u> Bu ekran üzerinde "Başlangıç Tarihi", "Peşinat Tutarı" ve "Taksit Sayısı" bilgilerine göre toplu şekilde ödeme planının oluşturulması sağlanmaktadır. "Başlangıç Tarihi" alanı varsayılan olarak "Poliçe Bilgileri" sekmesindeki "Başlangıç Tarihi" olarak getirilmektedir, istenir ise değiştirilebilir. "Peşinat Tutarı" alanı varsayılan olarak sıfır gelmektedir ve doldurulması zorunlu değildir. "Taksit Sayısı" alanı varsayılan olarak 0 olarak gelmekte ve sıfırdan büyük bir değer girilmesi zorunludur.

"Plan Oluştur" butonuna tıklandığında grid üzerinde daha önceden oluşturulmuş bir ödeme planı varsa öncelikle uyarı verilerek kullanıcıdan onay istenecektir: "Daha önceden oluşturulmuş ödeme planı silinecektir. Emin misiniz?" Kullanıcı onay verirse eski ödeme planı silinip yeni ödeme planı oluşturulacaktır.

Ödeme planı oluşturma süreci aşağıdaki şekilde çalışmaktadır.

<u>Tümünü Sil:</u> Bu butona tıklandığında grid üzerinde yer alan ödeme planı satırlarının tümü silinmektedir.

<u>Poliçe Dekont Kaydı:</u> Bu butona tıklandığında tanımlanan poliçenin açılışı için gerekli dekont kaydı atılmaktadır. "Dekont Seri" bilgisi girişi yapılarak dekont oluşturulmaktadır. Oluşan dekont numarası bilgisi, poliçe bilgileri sekmesindeki grid alan üzerinden izlenebilmektedir. Dekont Açıklama Politikası seçimleri ile poliçe tanımlama ekranında girilen açıklama bilgilerinin oluşturulacak dekonta taşınması sağlanabilmektedir. Otomatik seçilmesi durumunda ise mevcut yapıdaki açıklama bilgileri ile dekont oluşturulması sağlanır. Serbest giriş seçilmesi durumunda ise Açıklama alanına manuel olarak girilen açıklama ile dekont kaydı oluşacaktır.

![](../_assets/5d0b29d091a9826ba26c.png)

Poliçe Dekont İptali: Bu butonun aktif olabilmesi için ilgili poliçe için "Poliçe Dekont Kaydı" işlemi çalıştırılmış olmalıdır. Butona tıklandığında daha önceden atılan poliçe dekont kaydının silinmesi sağlanacaktır. Eğer ilgili poliçe için "Poliçe Tahakkuk Mahsubu" oluşturulmuş ise veya ödeme planındaki herhangi bir taksit için "Ödeme Kaydı" yapılmış ise "Tahakkuk Mahsubu veya Ödeme Kaydı olan poliçelerin dekont kayıtları iptal edilemez." uyarısı alınmaktadır.

Ödeme Kaydı: Bu butonun aktif olabilmesi için grid üzerinden mevcut bir satır seçilmiş ve ilgili poliçe için "Poliçe Dekont Kaydı" işlemi çalıştırılmış olmalıdır. Bu ekran üzerinden "Dekont Seri" ve "Banka Hes. Kodu" bilgileri girilmelidir.

Ödeme İptali: Bu butonun aktif olabilmesi için grid üzerinden mevcut bir satır seçilmiş olmalı ve bu satır için daha önceden bir ödeme kaydı atılmış olmalıdır. Butona tıklandığında ödeme kaydı için atılan dekont silinmekte ve "Ödeme Planı" sekmesindeki grid üzerinde "Ödendi", "Dekont Seri", "Dekont No" alanları güncellenmektedir.

**Poliçe Tahakkuk Mahsubu**

Poliçe tahakkuk ekranı üzerinden ilgili poliçe veya poliçeler için 180 hesap üzerinde bulunan borç tutarları aylık olarak "Gider Hesapları" sekmesinde 7'li hesaplara tanımlanan oranlar dahilinde virman yapılmaktadır. Ekran üzerinden verilen filtrelere göre birden fazla poliçe için toplu işlem yapılabilmektedir.

![](../_assets/3afc4df47faa85adc04a.png)

Ay / Yıl: Doldurulması zorunlu bir sahadır ve varsayılan olarak günün tarihine uygun ay/yıl bilgisi getirilmektedir.

Cari Kodu: Opsiyonel bir sahadır. Bu alana bir cari kodu girildiğinde sadece ilgili cariye ait poliçe tanımları için tahakkuk işlemi çalıştırılmaktadır.

Poliçe / Yenileme No: Opsiyonel bir sahadır. Bu alana bir poliçe no ve yenileme no girildiğinde sadece bu poliçe no ve yenileme no için tahakkuk işlemi çalıştırılmaktadır.

Proje Kodu Poliçe Tanımlarından Getirilsin: Proje uygulaması açık ise varsayılan olarak işaretli gelmektedir. Bu seçenek seçildiğinde atılacak dekont kaydındaki proje kodu bilgisi poliçe tanımları üzerinden getirilmektedir.

Proje Kodu: Bu alanın seçilebilir olması için proje uygulaması açık olmalıdır ve "Proje Kodu Poliçe Tanımlarından Getirilsin" parametresi seçili olmamalıdır. Bu alana girilen değer atılacak dekont kaydındaki proje kodu bilgisi olarak kullanılmaktadır.

Referans Kodu Poliçe Tanımlarından Getirilsin: Referans uygulaması açık ise varsayılan olarak işaretli gelmektedir. Bu seçenek seçildiğinde atılacak dekont kaydındaki referans kodu bilgisi poliçe tanımları üzerinden getirilmektedir.

Referans Kodu: Bu alanın seçilebilir olması için referans uygulaması açık olmalıdır ve "Referans Kodu Poliçe Tanımlarından Getirilsin" parametresi seçili olmamalıdır. Bu alana girilen değer atılacak dekont kaydındaki referans kodu bilgisi olarak kullanılmaktadır.

Plasiyer Kodu Poliçe Tanımlarından Getirilsin: Plasiyer uygulaması açık ise varsayılan olarak işaretli gelmektedir. Bu seçenek seçildiğinde atılacak dekont kaydındaki plasiyer kodu bilgisi poliçe tanımları üzerinden getirilmektedir.

Plasiyer Kodu: Bu alanın seçilebilir olması için plasiyer uygulaması açık olmalıdır ve "Plasiyer Kodu Poliçe Tanımlarından Getirilsin" parametresi seçili olmamalıdır. Bu alana girilen değer atılacak dekont kaydındaki plasiyer kodu bilgisi olarak kullanılmaktadır.

Dekont Seri: Doldurulması zorunlu bir sahadır, tanımlı dekont serilerinden birinin girişi yapılmalıdır.

Açıklama: Opsiyonel bir sahadır, ekran açılışında varsayılan olarak "Sigorta Tahakkuk Mahsubu" şeklinde dolu getirilmektedir. Bu alana yazılan açıklama bilgisi oluşturulacak dekont kaydının açıklama sahasına yazılacaktır.

**"Mahsup Oluştur"** butonuna tıklandığında sadece "Poliçe Dekont Kaydı" oluşturulmuş ve ilgili ay için tahakkuk mahsubu oluşturulmamış poliçeler için işlem yapılmaktadır. Eğer seçilen ay/yıl ve filtreler için tahakkuk oluşturulacak poliçelerin içinde önceki ay/yıl' a ait tahakkuk işlemi yapılmamış poliçeler bulunuyorsa işlem yarıda kesilerek "Daha önceki aylar için tahakkuk işlemi yapılmamış poliçeler bulunmaktadır, öncelikle daha önceki aylar için işlem yapmanız gerekmektedir." uyarısı verilmektedir.

**Poliçe Tahakkuk İptali**

Poliçe tahakkuk iptali ekranı üzerinden ilgili poliçe veya poliçeler için verilen ay/yıl için daha önceden oluşturulan tahakkuk mahsupları iptal edilebilmekte, yani silinebilmektedir.

![](../_assets/591cef9714f8f17ddd44.png)

Ekrandaki Ay/Yıl bilgisi zorunlu alanlardır. Diğer alanlar için yapılacak kontroller "Poliçe Tahakkuk Mahsubu" ekranındaki gibidir ve doldurulursa filtre olarak kullanılmaktadır.

"İptal Et" butonuna tıklandığında eğer seçilen ay/yıl ve filtreler için tahakkuk iptali yapılacak poliçelerin içinde sonraki ay/yıl'a ait tahakkuk kayıtları olan poliçeler bulunuyorsa işlem yarıda kesilmekte ve "Daha sonraki aylar için tahakkuk iptali yapılmamış poliçeler bulunmaktadır, öncelikle daha sonraki aylara ait kayıtları iptal etmeniz gerekmektedir." uyarısı verilmektedir.

**Poliçe Tanım Raporu**

Cari \>Rapor" menüsü altına "Poliçe Tanım Raporu" ismiyle yeni bir rapor eklenmiştir. Bu rapor üzerinde "Poliçe Tanımları" ekranındaki "Poliçe Bilgileri" sekmesinde yer alan bilgiler raporlanabilmektedir.

![](../_assets/1129f56363bb69cf40fb.png)

**ÖRNEK UYGULAMA**

![](../_assets/6143cb595b402192c628.png)

Poliçe Sabit Bilgileri;

- Poliçe No = 00000000000000000002
- Poliçe Toplam Tutarı = 15000 TL
- Poliçe Başlangıç Tarihi = 24.02.2022
- Poliçe Bitiş Tarihi = 24.02.2023
- Poliçe Gün Sayısı = Poliçe Bitiş Tarihi - Poliçe Başlangıç Tarihi = 24.02.2023 - 24.02.2022 = 365 gün
- Günlük Tutar: (Poliçe Toplam Tutarı / Poliçe Gün Sayısı) 15000/365 = 41,0958
- Ödeme Planı
  - Peşinat : 10000 TL (24.02.2022)
  - 4 Taksit : (15000 - 10000) / 4 = Aylık 1250 TL

Oluşturulacak Dekont Bilgileri;

Dekont kaydı sırasında "Poliçe Bilgileri" sekmesindeki "Gelecek Aylar Gid. Hs" ve "Gelecek Yıllar Gid. Hs." alanlarında tanımlanan 180 ve 280 hesaplar poliçe tutarının tamamını bölüşecek şekilde borçlandırılmaktadır. İlgili muhasebe döneminin içine giren kadarlık tutar 180 hesaba, diğer döneme sarkan tutar 280 hesaba yazılmaktadır. Bu noktada "Muhasebe Parametreleri" ekranındaki "Mali Yıl Başlangıç Ayı" parametresine göre muhasebe dönemleri kararlaştırılmalıdır. Dekont belgesinde karşı bacak olarak da "Poliçe Bilgileri" sekmesindeki "Cari Kodu"na ödeme planındaki tutar ve tarihler üzerinden alacak kaydı atılmaktadır. Proje uygulaması veya Referans uygulaması aktif ise atılacak dekont kaydının proje kodu ve referans kodu bilgileri "Poliçe Bilgileri" sekmesinde girilen değerler üzerinden alınmaktadır.

Bu örnek üzerinden "Mali Yıl Başlangıç Ayı"nın 1 olduğunu yani yıl sonunda yeni muhasebe dönemine geçildiğini varsayalım. "Gelecek Aylar Gid. Hs" ve "Gelecek Yıllar Gid. Hs." için ay bazında takip yapılmıyorsa, yani hesap tanımları için "?" ifadesi kullanılmamış ise, oluşacak dekont satırları aşağıdaki gibi olacaktır:

*180-000-001*: 12780,82 \>\> Poliçe başlangıç tarihinden muhasebe döneminin sonuna kadarki kalan gün sayısı \* Günlük Tutar = (01.01.2023 - 24.02.2022) \* 41,0958 = 311 \* 41,0958 = 12780,82 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi // Açıklama = Poliçe No: 00000000000000000002)
*280-001-001*: 2219,18 \>\> Toplam Poliçe Tutarı - 180 Hesaba aktarılan tutar = 15000 - 12780,82 = 2219,18 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi // Açıklama = Poliçe No: 00000000000000000002)
*320-001-001*: 10000 \>\> Peşinat (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi // Açıklama = Poliçe No: 00000000000000000002/1. Taksit)
*320-001-001*: 1250 \>\> 1. Taksit (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Taksit Tarihi // Açıklama = Poliçe No: 00000000000000000002/2. Taksit)
*320-001-001*: 1250 \>\> 2. Taksit (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Taksit Tarihi // Açıklama = Poliçe No: 00000000000000000002/3. Taksit)
*320-001-001*: 1250 \>\> 3. Taksit (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Taksit Tarihi // Açıklama = Poliçe No: 00000000000000000002/4. Taksit)
*320-001-001*: 1250 \>\> 4. Taksit (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Taksit Tarihi // Açıklama = Poliçe No: 00000000000000000002/5. Taksit)

![](../_assets/fefb68bf753a93f0ab03.png)

Eğer bu örnekte "Gelecek Aylar Gid. Hs" ve "Gelecek Yıllar Gid. Hs." için ay bazında takip yapılıyorsa, yani hesap tanımları için "?" ifadesi kullanılmış ise 180 ve 280 hesaplara atılacak tutarlar aylık bazda bölüştürülecek ve hesap kodunda "?" olan bölüm ay kodu ile yer değiştirilerek kayıt atılacaktır.

Örneğin hesap kodu olarak 180-000-??? ve 280-001-??? olarak tanımlama yapıldığını düşünürsek aşağıdaki gibi satırlar atılacaktır:

![](../_assets/e43880421c09511835d3.png)
180-000-002: 205,48 TL \>\> (3. ayın ilk günü - Sigorta başlangıç tarihi) \* Günlük Tutar = (01.03.2022 - 24.02.2022) \* 41,0958 = 5 \* 41,0958 = 205,479 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
180-000-003: 1273,97 TL \>\> (3. ayın son günü - 2. ayın son günü) \* Günlük Tutar = (31.03.2022 - 28.02.2022) \* 41,0958 = 31 \* 41,0958 = 1273,969 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
180-000-004: 1232,88 TL \>\> (4. ayın son günü - 3. ayın son günü) \* Günlük Tutar = (30.04.2022 - 31.03.2022) \* 41,0958 = 30 \* 41,0958 = 1232,874 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
180-000-005: 1273,97 TL \>\> (5. ayın son günü - 4. ayın son günü) \* Günlük Tutar = (31.05.2022 - 30.04.2022) \* 41,0958 = 31 \* 41,0958 = 1273,969 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
180-000-006: 1232,88 TL \>\> (6. ayın son günü - 5. ayın son günü) \* Günlük Tutar = (30.06.2022 - 31.05.2022) \* 41,0958 = 30 \* 41,0958 = 1232,874 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
180-000-007: 1273,97 TL \>\> (7. ayın son günü - 6. ayın son günü) \* Günlük Tutar = (31.07.2022 - 30.06.2022) \* 41,0958 = 31 \* 41,0958 = 1273,969 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
180-000-008: 1273,97 TL \>\> (8. ayın son günü - 7. ayın son günü) \* Günlük Tutar = (31.08.2022 - 31.07.2022) \* 41,0958 = 31 \* 41,0958 = 1273,969 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
180-000-009: 1232,88 TL \>\> (9. ayın son günü - 8. ayın son günü) \* Günlük Tutar = (30.09.2022 - 31.08.2022) \* 41,0958 = 30 \* 41,0958 = 1232,874 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
180-000-010: 1273,97 TL \>\> (10. ayın son günü - 9. ayın son günü) \* Günlük Tutar = (31.10.2022 - 30.09.2022) \* 41,0958 = 31 \* 41,0958 = 1273,969 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
180-000-011: 1232,88 TL \>\> (11. ayın son günü - 10. ayın son günü) \* Günlük Tutar = (30.11.2022 - 31.10.2022) \* 41,0958 = 30 \* 41,0958 = 1232,874 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
180-000-012: 1273,97 TL \>\> (12. ayın son günü - 11. ayın son günü) \* Günlük Tutar = (31.12.2022 - 30.11.2022) \* 41,0958 = 31 \* 41,0958 = 1273,969 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
280-001-001: 1273,97 TL \>\> (1. ayın son günü - 12. ayın son günü) \* Günlük Tutar = (31.01.2023 - 31.12.2022) \* 41,0958 = 31 \* 41,0958 = 1273,969 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi)
280-001-002: 945,21 TL \>\> Toplam Poliçe Tutarı - 180/280 hesaplara aktarılan toplam tutar = 15000 - 14054,79 = 945.21 TL (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi) \>\> Son ay için (Toplam Poliçe Tutarı - 180/280 hesaplara aktarılan toplam tutar) formülüyle hesaplama yapmamızın sebebi virgülden sonraki kuruş farkını engelleyip, toplam poliçe tutarını tam olarak tutturmaktır.
320-001-001: 10000 TL\>\> Peşinat (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Poliçe Başlangıç Tarihi) 320-001-001: 1250 TL\>\> 1. Taksit (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Taksit Tarihi)320-001-001: 1250 TL\>\> 2. Taksit (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Taksit Tarihi)320-001-001: 1250 TL\>\> 3. Taksit (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Taksit Tarihi)320-001-001: 1250 TL\>\> 4. Taksit (İşlem Tarihi = Poliçe Başlangıç Tarihi // Vade Tarihi = Taksit Tarihi)
![](../_assets/6efa87e6765d7389ef69.png)

Ödeme Kaydı Dekont Kayıtları;

![](../_assets/9a4921ba2c16e3d002a6.png)

1.Taksit için ödeme kaydı oluşturulduğunda cari hesaba borç banka hesabına alacak kaydı atılarak dekont oluşturulur.

![](../_assets/1b45115a12565e5e9397.png)

2.Taksit için ödeme kaydı oluşturulduğunda da yine aynı şekilde cari hesaba borç banka hesabına alacak kaydı atılarak dekont oluşturulur. Oluşan dekont numaraları Ödeme Planı sekmesi üzerinden ilgili satırda izlenebilmektedir. Ödendi bilgisi ise ödeme yapılması durumunda "Evet" olarak değişmektedir.

![](../_assets/55121cb1a979eb0dc23d.png)

Poliçe tahakkuk kaydı

"Gelecek Aylar Gid. Hs" için ay bazında takip yapılmıyorsa, yani hesap tanımları için "?" ifadesi kullanılmamış ise;
2. ay için tahakkuk işlemi;

770-001-001: 164,38 \>\> (3. ayın ilk günü - poliçe başlangıç tarihi) \* Günlük Tutar = (01.03.2021 - 24.02.2021) \* 41,0958 = 5 \* 41,0958 = 205,48
180-001-001 hesap: 205,48

\3. ay için yapılan tahakkuk işlemi;
770-001-001: 1273,79 \>\> (3. ayın son günü - 2. ayın son günü) \* Günlük Tutar = (31.03.2021 - 28.02.2021) \* 41,0958 = 31 \* 41,0958 = 1273,97
180-001-001 hesap: 1273,97

"Gelecek Aylar Gid. Hs" için ay bazında takip yapılıyorsa, yani hesap tanımları için "?" ifadesi kullanılmış ise;
2. ay için yapılan tahakkuk işlemi;

770-001-001: 164,38 \>\> (3. ayın ilk günü - poliçe başlangıç tarihi) \* Günlük Tutar = (01.03.2021 - 24.02.2021) \* 41,0958 = 5 \* 41,0958 = 205,48
180-001-002 hesap: 205,48

\3. ay için yapılan tahakkuk işlemi;
770-001-001: 1273,79 \>\> (3. ayın son günü - 2. ayın son günü) \* Günlük Tutar = (31.028.02.2021) \* 41,0958 = 31 \* 41,0958 = 1273,97
180-001-003 hesap: 1273,97
![](../_assets/6a203daf50225654f579.png)
![](../_assets/826b78a0002fa7b0e728.png)

Bu örnekte gider hesabı olarak %100 oranında 770-001-001 hesabının tanımlandığı varsayılmıştır. Birden fazla gider hesabı oranlar şeklinde tanımlanmış olsaydı toplam tutarı bu hesaplar arasında kendi oranlarına göre bölüştürüp 7'li hesaplara birden fazla satır borç kaydı oluşturulacaktır.
