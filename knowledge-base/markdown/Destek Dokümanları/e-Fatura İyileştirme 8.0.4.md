---
title: "e-Fatura İyileştirme 8.0.4"
page_id: "50680056"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Fatura İyileştirme 8.0.4"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Fatura İyileştirme 8.0.4"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ5MmMwZDA0LTc0MjMtNDViOS04NWNiLTE2Y2FlOTQ2NjUxZiZsaW5rPTlkYWNjOWY1LTBlYjQtNGVkZC1iOWZkLWNkZTZhYWI0YjUxNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=492c0d04-7423-45b9-85cb-16cae946651f&link=9dacc9f5-0eb4-4edd-b9fd-cde6aab4b517&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-fatura-iyilestirme-8-0-4_82576531_50680056.html"
source_version: "2022-11-03T09:47:21.043+03:00"
source_bytes: 388943
fetched_at: "2026-09-13T04:26:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Fatura İyileştirme 8.0.4

e-Fatura İyileştirme 8.0.4 versiyonu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| Amaç ve Fayda | E-fatura uygulaması ile ilgili çeşitli yenilikler 8.0.4 seti ile birlikte yayınlandı: - Gelen e-faturaların alış faturasının yanı sıra genel dekont olarak da kaydedilmesi desteklendi.<br>- Efatura kayıtlarının verilerinin sıkıştırılarak saklanması çalışması tamamlandı.<br>- Gelen e-faturalardaki ekli dosyaların da izlenebilmesi desteklendi.<br>- Şubeler için farklı aliaslar takip edilebilmesi ve gelen aliasın şubesine faturaların kaydedilebilmesi desteklendi.<br>- Yeni entegratör entegrasyonları tamamlandı. 8.0.4 setiyle desteklenen entegratör listesi: LOGO, e-Finans, Veriban, Akbank ve Isis.<br>- Red edilen alış faturalarının Netsis entegrasyonun engellenmesi sağlandı.<br>- Gelir idaresinin talep ettiği; zarf boyutunun 5 mb. geçmemesi, tek zarfa 100'den fazla fatura eklenememesi ve birim kodlarında küçük harf kullanılmaması şeklindeki kontroller desteklendi.<br>- Dövizli oluşturulan e-faturaların net fiyat üzerinden oluşturulması desteklendi.<br>- Ara tablo kayıtlarının kullanıldığı durumlarda, dizayn modülünden xml tasarımının yapılabilmesi desteklendi. |
| Ürün Grubu | \[X\] Netsis Enterprise<br>\[X\] Netsis Standard<br>\[X\] Netsis Entegre |
| Modül | \[X\] Fatura |
| Kategori | \[X\] Yeni Fonksiyon |
| Versiyon Önkoşulu | 8.0.4 |

**Alış** **e-faturalarından** **Netsis** **Dekont** **Kaydı** **Desteği**

Gelen zarfların fatura detayında takip edildiği fatura bazlı liste ekranında Netsis alış faturası oluşturulabildiği gibi yeni eklenen "dekont oluşturma" işlemi ile gelen e-faturadan Netsis genel dekont kaydının oluşturulabilmesi desteklenmiştir.

![](../_assets/b00536ad0a9e18081431.png)

İlgili e-faturanın üstünde sağ klikte gelen menüden Dekont oluşturma işlemi çalıştırıldığında dekont kayıt ekranı açılmaktadır.
Açılan dekont oluşturma ekranına, e-faturadan cari bilgisi, gider kalemleri ve vergi ile ilgili bilgiler doldurularak gelmektedir. E-fatura mükellefinin vergi numarası cari kartlarda tanımlanmış ise, cari kodu dolu olarak gelmektedir, benzer şekilde KDV hesabı da entegrasyon kodlarından doldurularak gelmektedir. Gider kalemlerinin hesap kodu ise kullanıcı tarafından girilip ekrandaki gerekli kontroller geçildiğinde kaydet butonu ile dekont kaydı oluşturulabilmektedir.
Bu ekranda otomatik getirilen bilgileri kullanıcı istediği gibi değiştirebilmektedir, örneğin e-faturadan gelen gider kalemini silip kendi istediği sayıda satır ekleyip farklı masraf merkezlerine giderleri dağıtıp bu ekrandan dekont kayıdını tamamlayabilir. Oluşan dekont kaydı dekont modülündeki genel dekont kaydı ekranından incelenebilir. Bu ekran kullanılmadan gelen e-faturaları genel dekont kaydından kendisi kaydetmek istediğinde, girilen dekont ile e-faturanın ilişkisinin kurulabilmesi için dekont ekranında eşleştirme işlemleri desteklendi. Bu eşleme sayesinde kayıtlı olan dekotun e-faturasına hızlıca e-fatura görüntüle işlemi ile ulaşabilme imkanı gelmiştir.
![](../_assets/4b4ada857f5ebb16885b.png)![](../_assets/e518b01fa8724772f53c.png)
Fatura bazlı liste ekranından dekont oluşturma işlemi ile atılan dekont kayıtları için e-fatura eşleştirmesi otomatik yapıldığı için ayrıca eşleştirme işlemine gerek kalmamaktadır. Ayrıca bu işlem ile b-formu ve indirilecek KDV bilgileri de oluşturulmaktadır.

#### e-Fatura Veri Aktarımı

Gelen ve giden e-faturaların şirket veri tabanında tutulmasıyla birlikte datanın boyutunda e- faturaların xml verileri nedeniyle büyüme yaşanmaktadır. Yapılan düzenleme ile e-fatura verisinin veri tabanında sıkıştırılmış olarak tutulması ve tüm işlemlerin sıkıştırılmış veri üzerinden yapılabilmesi sağlandı. Halihazırda mevcut olan kayıtların da bu sıkışmış formatta saklanabilmesi için efatura veri aktarımı işlemi mutlaka çalıştırılmalıdır. Bu işlem çalıştırıldığında ekranda sorulan tarih
aralığındaki faturalar ve bununla ilişkili zarflar ve yanıtları sıkıştırılarak tabloda saklanacaktır. Bu işlemde özellikle dikkat edilmesi gereken durum ekranda sorulan dosya yollarının düzgün şekilde girilmesi gerektiğidir. Özellikle gelen dizininde e-fatura parametrelerindeki dosya yolu yazılmamalıdır**. Sisteme ilk düşen e-faturaların tutulduğu web servisin kurulu olduğu** **makinede** **e-faturaların** **tutulduğu** **dizin** **veya** **dizinler** **belirtilmelidir.**
Gelen dosya yolu olarak entegrasyon çözümlerinde web servis(ler) üzerinde kullanılan dizin(ler) seçilmelidir. Özel dizin belirtilmemiş ise web servisin kurulu olduğu makinadaki temp dizini kullanılmaktadır. Özel dizin web servisin kurulu olduğu dizinde bulunan web.config dosyası içerisindeki **ReceivedDocumentsPath** değişkeninin değeri ile belirtilmiş olabilir. Özel dizin belirtilmiş olsa bile ilgili makinadaki temp dizininin eklenmesi **ReceivedDocumentsPath** değişkenin tanımlandığı zamandan önceki zarflar için faydalı olacaktır. Temp dizini makina üzerindeki Windows dizini altındaki Temp dizinidir(C:\\Windows\\Temp gibi).
Aktarım uygulaması farklı bir makinada çalışıyorsa bu dizinlere okuma yetkisi ile paylaşım verilmelidir.
Web servisin kullandığı dizinlerden emin olmak için SELECT INFOLOG FROM TBLEFATURALOG WHERE INFOLOG LIKE "%CONTENT%ZARFID%PATH%" sorgusunun sonucunda dönecek olan PATH bilgileri kullanılabilir.

Bu işlem e-faturaların herhangi bir değişikliğe uğramadan orijinal hallerinin sıkıştırılmış olarak veri tabanında tutulmasına imkan vermesi nedeniyle veri güvenliğini arttırıcı bir işlemdir. Aynı zamanda da yeni yıl devirlerinin daha hızlı yapılabilmesi için gerekli bir işlemdir. Veri aktarımı, e-faturaları mevcut saklandıkları tablo (TBLEFATZARF) üzerinde sıkıştıracak ve tablo boyutunu küçültecektir. Veri aktarımı, verilen klasörde bulabildiği e-faturaları orijinal halleriyle alacak, klasörde bulunamıyorsa veri tabanındaki haliyle alacak ve sıkıştıracaktır. Herhangi bir sebepten sıkıştırılamayan faturalar ise veri tabanında olduğu haliyle kalacaktır. Sonuç olarak bu işlemin çalıştırılması, mevcut e-fatura işleyişinde herhangi bir değişikliğe neden olmayacaktır.

#### Gelen E-faturalardaki Ekli Dosyaların Açılması

Sisteme gelen bazı e-faturalarda karşı tarafın eklediği ekli dosyalar (sözleşmenin dosyası, ödeme planı vb.) olabilmektedir. Netsis'teki mevcut e-fatura görüntüleme ekranlarında bu ekli dosyaların izlenebilmesi desteklenmiştir.
Görüntüleme aracı çalıştığında eğer açılan e-faturaya ekli dosya varsa, ekranda ekli dosyaları göster butonu aktif gelmektedir ve bu işlem çalıştırıldığında e-faturanın xml i ile gelen ekli dosyalar açılmaktadır.
