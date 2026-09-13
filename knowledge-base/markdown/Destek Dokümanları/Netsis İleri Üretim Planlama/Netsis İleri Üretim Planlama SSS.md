---
title: "Netsis İleri Üretim Planlama SSS"
page_id: "80090196"
product: "netsis-3-enterprise"
depth: 3
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis İleri Üretim Planlama"
  - "Netsis İleri Üretim Planlama SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis İleri Üretim Planlama / Netsis İleri Üretim Planlama SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWI2MmFjZjk2LTJjYTAtNGQxMS1iMzE2LWU3ZmU0ZTgxOTcyOCZsaW5rPTEwOGEyNDg4LWMyYjctNDEzNi1iOTQxLWQ4ZDM4MjY3YjRkMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b62acf96-2ca0-4d11-b316-e7fe4e819728&link=108a2488-c2b7-4136-b941-d8d38267b4d1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-ileri-uretim-planlama-sss_80090200_80090196.html"
source_version: "2022-05-23T13:26:04.190+03:00"
source_bytes: 54651
fetched_at: "2026-09-13T04:25:04+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis İleri Üretim Planlama SSS

**İleri üretim** **planlama** **modülü** **ne** **amaçla** **kullanılır?**
İleri üretim planlama modül, bir işletmede tamamlanması planlanan siparişlerin hangi istasyonlarda, hangi sırayla ve hangi kaynaklar kullanılarak üretilmesi gerektiğini hesaplamaya ve sonuçları bir Gantt şeması üzerinde çizelgelemeye yarar. Böylelikle doğru zamanda, doğru üretim, en uygun kaynak kullanımıyla gerçekleştirilir ve işletme hedeflerine ulaşılması sağlanmış olur.
**İleri** **üretim** **planlama** **modülünü** **hangi** **ERP** **çözümleriyle** **birlikte** **kullanabilirim?**
İleri üretim planlama modülü, Logo Netsis Wings Enterprise ve Logo Netsis 3 Enterprise ERP çözümleri
ile birlikte kullanılabilmektedir.
**Fabrika** **vardiya** **planı** **tanımlaması** **yaptığımda** **makine,** **kaynak** **ve** **istasyon** **gibi** **tüm** **üretim** **birimlerim** **yalnızca** **bu** **plan** **dahilinde** **mi** **çalışabilecek?**
Fabrika vardiya planı aksi bir tanımlama yapılmadığı sürece tüm üretim birimleri için geçerli olacaktır. Ancak tekil üretim birimleri için (makine, istasyon, kaynak gibi) fabrika vardiya planından farklı vardiya planları yapılması da mümkündür.
**Üretim tesisimde aynı ürünün işlem görebileceği birden fazla makinem var ve ilgili ürün** **farklı makinelerde farklı işlem sürelerine sahip. Modül içinde bu detayda tanımlama yapabilir** **miyim?**
Operasyon-makine eşleştirme ekranı kullanılarak, tanımlı tüm stok kodları için makine bazında farklı işlem süreleri girişine izin verilmektedir.
**Üretim tesisimde farklı şekillerde işlem yapan makinelerim var. Uygulama üzerinde farklı** **tipte** **makineleri** **tanımlamak mümkün** **mü?**
İleri üretim planlama modülünde, normal (single processor), normal (multi processor), fason, fırın, sürekli fırın, montaj hattı, manuel montaj, kazan ve robot olmak üzere toplam 9 farklı makine tipi desteklenmektedir. Her makine tipi farklı bir iş yapma mantığıyla geliştirildiğinden, makinelerin planlama mantıkları da birbirinden farklıdır.
**Yüksek** **miktardaki** **iş** **emirlerimi** **tek** **makineye** **planlamak** **zorunda** **mıyım?**
Uygulama tarafından 3 farklı iş emri bölme politikası desteklenmektedir. İş emirlerini bölmeden, iş emirlerini en az sayıda makine kullanılacak şekilde bölerek ya da iş emirlerini tüm alternatif makinelere eşit şekilde bölerek çalışabilmek mümkündür.
**Üretim sırasında dikkat etmem gereken bazı istisnai durumlar var. Örneğin, bazı ürünleri art arda üretmemeyi tercih ediyorum. Çizelgelemenin bu gibi üretim kısıtlarımı dikkate almasını sağlayabilir miyim?**
İleri üretim planlama modülü içinde bulunan "Kural Tanımlama" ekranı üretim kısıtlarının programa tanımlanabilmesini sağlar. Programda "Birlikte yapılamaz", "Birlikte yapılabilir" ve "Art arda yapılamaz" olmak üzere 3 farklı kural tipi desteklenmektedir.
**İleri üretim planlama modülü içinde kendi sistemime özel algoritmalar geliştirebilir miyim?**
İleri üretim planlama modülü ile birlikte açık kaynak kodlu algoritma kütüphanesine erişebilmeniz ve .NET ortamında kendi algoritmalarınızı yazabilmeniz mümkündür.
**Kaynaklarımın ömür takiplerini bu modül üzerinden yapabilir miyim?**
Kaynak tanımlama ekranı üzerinden kaynaklara ait ömür detaylarının girişi yapılabilmektedir. Aynı zamanda bakımı/tamiri yapılabilen kaynakların bakımlarına ait detayların girişi de mümkündür. Bakım detayları girilmiş kaynaklar için otomatik bakım talebi oluşturulma desteği de bulunmaktadır. Bu şekilde kullanılan kaynaklar, bakım süreleri boyunca çizelgeleme dışında tutulacaktır. Ek olarak tamir edilebilen kaynaklar için çizelgeleme sonucuna göre tahmini bakım planı raporu da alınabilmektedir. Böylece gelecek dönemlerde tahminen hangi kaynakların hangi zaman aralıklarında bakımda olacağı raporlanabilir.
**Üretim** **tesisimde** **ürün,** **makine** **ve** **operasyon** **bazında** **hazırlık** **sürelerim** **farklılık** **gösteriyor.** **Bu** **farklı** **hazırlık** **sürelerini ileri** **üretim** **planlama** **modülünde** **nasıl** **tanımlayabilirim?**
Hazırlık süresi tanımlama ekranı kullanılarak operasyon bazında hazırlık süresi girilebileceği gibi, belirli koşullarda oluşan hazırlık süreleri için de tanımlamalar yapılabilmektedir. Uygulama kullanılarak kaynak değişimi, ürün değişimi, operasyon değişimi ve operasyonun kendisine ait hazırlık süresi olması durumları için hazırlık süresi tanımlanması mümkündür. Ek olarak, Script desteği ile işletmeye ait özel hazırlık süresi tanımlamalarının yapılabilmesi de desteklenmiştir.
**Dinamik bir üretimim var, iş emri önceliklerim gün içinde değişebiliyor. İleri üretim** **planlama** **modülü** **ile** **çizelge** **oluşturulduktan** **sonra** **gelişen** **değişiklikleri** **çizelgeye** **nasıl** **yansıtabilirim?**
Çizelgeleme Gantt Ekranı üzerinde iş emirleri için sürükle-bırak desteği bulunmaktadır. Bu özellik sayesinde modül tarafından yapılan plana manuel müdahale etmek mümkün kılınmıştır. Ek olarak istenilen iş emirlerinin, istenilen tarih ve saate sabitlenmesi de mümkündür. Böylelikle sabitlenen iş emirlerinin yerleri program tarafından değiştirilmeyecektir.
**Daha** **önce** **oluşturduğum** **çizelgelere** **ulaşmaya** **ihtiyacım** **oluyor.** **Bu** **desteği** **sağlıyor** **musunuz?**
Oluşturulan çizelgelerin taslak olarak kaydedilmesi ve daha sonra görüntülenebilmesi mümkündür. Hatta taslak olarak kaydedilen bir çizelgenin yeniden etkin hale getirilerek tekrar kullanılabilmesi de desteklenmiştir.
**İş emirlerimden çizelgelenemeyenler olursa nasıl anlayacağım?**
İleri üretim planlama modülü kullanıcılarına 11 farklı rapor seçeneği sunmaktadır. "Çizelgelenemeyen İşler Raporu" da bu raporlardan biridir. Çizelgeleme yapıldıktan sonra "Çizelgelenemeyen İşler Raporu" alınarak hem mevcut iş emirleri içinde çizelgelenemeyenler varsa listelenebilmekte hem de çizelgelenemeyen iş emirlerinin çizelgelenememe sebepleri görüntülenebilmektedir.
**Bazı** **operasyonlarımı** **üretim** **tesisimin** **dışında** **fason** **olarak** **gerçekleştiriyorum.** **Tedarikçilerimin** **üstlendiği** **bu** **operasyonları** **çizelgelemeye** **dahil** **edebilir miyim?**
Makine tiplerinde desteklenen "Fason" tipli makine bu gibi durumlarda kullanılmak üzere tasarlanmıştır. Dış tedarikçiler tarafından üstlenilen operasyonlar fason tipli makine ile eşleştirilebilir ve bu makine tipi seçildiğinde kullanılabilen "Fason Lojistik Planı" yardımıyla bu sürece ait tüm detaylar uygulamaya tanımlanabilir. Örneğin, fason üreticisine yalnızca belli gün ve saatlerde gönderim yapılıp yine yalnızca belli gün ve saatlerde teslim alınabiliyorsa fason lojistik planına bu gün ve saatler kaydedilebilmektedir. Ek olarak fason üreticisinin kapasite kısıtı olması durumları için kullanılabilen "Kapasite" desteği de mevcuttur.
**Üretim** **tesisimde** **makineler** **haricinde** **tepsi,** **kalıp,** **taşıma** **arabası,** **kasnak** **gibi** **üretim** **kısıtı** **yaratan** **yardımcı** **malzemeler** **kullanıyorum.** **Çizelgeleme** **yapılırken** **bunlar** **dikkate** **alınacak** **mı?**
Kalıp ve taşıma arabası gibi, üretimde kullanılan tüm yardımcı malzemelerin kaynak olarak tanımlanması ve çizelgelemede dikkate alınması mümkündür.
**Üretim** **tesisimde** **enjeksiyon** **prosesi** **gerçekleştiriyorum.** **Bu** **operasyona** **ait** **bir** **desteğiniz** **var mı?**
Enjeksiyon prosesi olan kullanıcılar için özel olarak geliştirilmiş olan "Enjeksiyon Algoritması" sayesinde bu operasyona birebir uyumlu şekilde çizelgeleme yapılabilmesi mümkün kılınmıştır.
**İleri** **üretim** **planlama** **modülü** **kullandığım** **diğer** **paketlerle** **entegre** **çalışabilir** **mi?**
Personel ya da demirbaş paketi olan kullanıcılar, ileri üretim planlama uygulamasını bu paketlerle entegre şekilde kullanabilirler.
**Belirli** **bir** **ömrü** **olan** **ve** **tamiri** **mümkün** **olmayan** **kaynaklar** **kullanıyorum.** **Bu** **kaynakları** **nasıl** **takip** **edebilirim?**
Tamiri mümkün olan, olmayan tüm kaynaklar için ömür takibi özelliği kullanılabilmektedir. İlgili kaynağın ömrü kullanıcı tarafından tanımlandıktan sonra program tarafından takibi yapılacak ve ömrü dolduğunda kullanım dışı bırakılacaktır. Ek olarak stok tipli kaynak için ömür takibi de yine stok kartı üzerinden yapılmakta, tanımlanan toplam ömür verisine göre stok bakiyesi güncellenmektedir.
**Üretim** **tesisimde** **kullandığım** **kalıplarımın** **bazıları** **aynı** **anda** **birden** **çok** **ürün** **çıkarabiliyor, bazıları ise farklı şekillerde kullanılarak farklı ürünler çıkarabiliyor. Buna benzer** **durumlar** **için** **kullanım esnekliği** **sağlıyor** **musunuz?**
Kaynak tanımlama ekranında desteklenen "Ürün Eşleştirme" sekmesi ile aynı anda birden fazla ürün işleyen bir kaynağın, işleyebildiği tüm ürünler tanımlanabilmektedir. Bu ürünlerin kaynaktan aynı anda çıkma durumu ise parametrik olarak kontrol edilebilmektedir. Ayrıca bir kaynak birden fazla şekilde kullanılarak farklı ürünler çıkarabiliyorsa, bu alternatiflerin her birini bir set olarak tanımlayabilmek de mümkündür.
**Çizelgelemenin** **hangi** **mantıkla** **çalıştırılacağına** **müdahale** **edebilir** **miyim?**
Çizelge modelleme aracı sayesinde kullanıcıların, çizelgeleme modellerini kendilerinin oluşturmasına ve çizelgeleme algoritmalarına müdahale etmesine olanak sağlanmıştır. Oluşturulacak modelin istenilen mantıkta çalıştırılabilmesi için algoritma, script ve if/else blokları kullanılabilir. Ayrıca bu blokları bağlamak için kullanılması gereken bağlantı bloğu ve algoritmanın bittiğini belirtmek için kullanılan end bloğu desteği sağlanmaktadır. Yanı sıra "Algoritma Opsiyonları" ekranı kullanılarak, programda desteklenen algoritmaların çalışma mantığında değişiklikler yapmak da mümkündür.
**Üretim tesisimde sürdürmekte olduğum operasyonlara ait detayları anlık olarak makine** **bazında** **takip etmek** **istiyorum.** **Bunu** **Netsis üzerinden** **yapabilir miyim?**
Üretim sahasında yapılan operasyonlara ait tüm detaylar (üretim miktarı, makine-personel- operasyon bilgileri, başlangıç-bitiş zamanları gibi) "Üretim Akış Kaydı" modülü sayesinde kayıt altına alınabilmektedir. Ek olarak çizelgeleme uygulaması da Üretim Akış Kaydı modülüyle entegre çalışmaktadır ve sahadaki anlık duruma göre çizelgeleme yapmaktadır. Örneğin mevcut durumda bir makinede üretimi devam eden bir iş emri varsa, iş emrinin kalan miktarı yine aynı makineye planlanacak şekilde çizelgeleme yapılacaktır.
**Sahadan** **toplanan** **üretim** **verileri** **ile** **ileri** **üretim** **planlama** **uygulamasının** **planladığı** **sonuçları** **karşılaştırabilir** **miyim?**
Çizelgeleme raporları altında yer alan "Çizelgeleme Sonucu – UAK Karşılaştırma" raporu kullanılarak, planlanan süreler ile gerçekleşen süreleri karşılaştırmak mümkündür.
**İleri** **üretim** **planlama** **uygulamasının** **makine** **bakım** **modülü** **ile** **entegrasyonu** **var** **mıdır?**
İleri üretim planlama uygulaması, makine bakım modülü üzerinden arıza veya periyodik bakımlar için açılan bakım emirlerini dikkate alarak çalışmaktadır. Bu yüzden de makine/kaynak için duruş olarak planlanan tarih aralıklarında ilgili makine/kaynağa iş planlanmamaktadır.
**Üretim** **tesisimde** **aynı** **operasyonu** **yapabildiğim** **alternatif** **makinelerim** **var.** **Bu** **makinelerin** **hangisinin** **öncelikli** **kullanılacağına** **karar** **verebilir** **miyim?**
İleri üretim planlama uygulaması kullanılarak makine bazında öncelik belirlemek mümkündür. Hatta ürünlerle eşleştirilmiş makineler bulunması durumunda, aynı ürünün alternatif makinelerinden hangisine öncelik verileceği de uygulama üzerinden belirlenebilir ve çizelgelemenin bu önceliklere göre oluşturulması sağlanabilir.
**Üretim tesisimde montaj hatlarım var. İleri üretim planlama uygulamasını kullanmaya** **başlamadan** **önce** **montaj** **hatlarımdaki** **optimum** **çevrim** **sürelerini** **belirlemek** **ve** **bu** **hatlardaki** **alt** **operasyonları hangi yerleşim düzenini kullanarak yapmam gerektiğine karar vermek istiyorum.** **Bu** **konuda** **karar** **verme** **sürecimi** **destekleyecek bir** **uygulamanız** **var** **mı?**
İleri üretim planlama uygulaması kapsamında desteklenen "Montaj Hattı Dengeleme" uygulaması bu amaçla geliştirilmiştir. Bu uygulama sayesinde kullanıcının belirleyeceği çevrim süresi aşılmayacak şekilde optimum çevrim süresi belirlenebilir ve alt operasyonlar için en uygun yerleşim planı tasarımına ulaşılabilir.
**İleri** **üretim** **planlama** **uygulaması** **dışında** **bir** **API** **üzerinden** **çizelgeleme** **uygulamasını** **çalıştırıp** **sonuç** **alabilir miyim?**
NetOpenX üzerinden çizelgeleme uygulamasının çalıştırılması ve sonuçların alınması desteklenmiştir.
**Enjeksiyon** **sektörü** **için** **neden** **farklı** **bir algoritma** **var,** **ne** **işe** **yarıyor?**
Enjeksiyon sektöründe faaliyet gösteren firmalar kalıp değişimlerini en aza indirecek ve aynı zamanda termin tarihlerine uygun olan planlara ihtiyaç duymaktadırlar. Bu sebeple enjeksiyon algoritması, kalıp değişimlerinden kaynaklanan hazırlık sürelerini en aza indirecek bulanık mantık (fuzzy logic) tabanlı özel bir algoritma olarak tasarlanmıştır. Böylece sektörel ihtiyaca en uygun çözüm sağlanması hedeflenmiştir.
**İleri** **üretim** **planlama** **uygulaması** **üretim** **sistemim** **için** **optimum** **çizelgeleme** **sonucunu** **verebilecek** **mi?**
Çizelgeleme problemleri yapısı gereği çok fazla alternatif çözüm içerdiği için büyük verilerde optimum çözüm bulmak nerdeyse imkansızdır. Ancak ileri üretim planlama uygulamasında kullanılan sezgisel tabanlı optimizasyon algoritmaları sayesinde optimuma en yakın sonuçları elde etmek mümkündür.
**Plastik enjeksiyon sektöründe faaliyet gösteren bir işletmem var ve üretim sahasındaki** **enjeksiyon makinelerim yarı-otomatik veya tam-otomatik çalışabiliyor. Yarı-otomatik** **makinelerde** **tek** **personel** **aynı** **anda** **2** **veya** **3** **makineye** **bakabiliyor.** **Tam-otomatik** **makineler** **ise** **personel olmadan çalıştırılıyor. İleri üretim planlama modülünde bu tanımlamaları yapabilecek** **miyim?**
Enjeksiyon algoritması kapsamında desteklenen yarı-otomatik veya tam-otomatik makine tanımlamaları bu amaçla kullanılmaktadır. Enjeksiyon algoritması bu tanımlamaları dikkate alarak çizelgeleme yapmaktadır. Böylece üretim tesislerindeki personel kısıtları gerçeğe en uygun olacak şekilde modellenebilmektedir.
**Üretim tesisimde kullandığım bazı kalıpların göz yapısı bulunuyor ve eş zamanlı olarak** **farklı** **ürünleri** **üretebiliyor.** **Ancak** **bazı** **durumlarda** **kalıbın** **bazı** **gözlerini** **kapatıp** **bu** **şekilde** **üretim** **yapıyorum.** **İleri** **üretim** **planlama** **modülünde** **bu** **tanımlamaları** **destekleyecek** **bir** **altyapı** **bulunuyor** **mu?**
Kaynak tanımlama ekranındaki "Ürün Eşleştirme" sekmesi kullanılarak, eş zamanlı üretilebilecek ürün setlerinin tanımlanması mümkündür. Bu aşamada kalıbın bütün gözleri açıkken üretilebilecek ürün setleri ve kalıbın gözleri kapatıldığında üretilebilecek ürün setleri ayrı ayrı tanımlanabilmektedir. Kalıbın kullanım şekline uygun ürün setinin aktifleştirilip diğer setlerin pasife çekilebilmesi uygulama tarafından desteklenmektedir.
