---
title: "Sabit Kayıt Kontrolü"
page_id: "47073663"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Sene Sonu Devir"
  - "Kayıt / Sene Sonu Devir"
  - "Sabit Kayıt Kontrolü"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Sabit Kayıt Kontrolü"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMwMDg3MmY0LTY0ZmYtNGM3Mi04NjAxLWU2NjJjY2I5OGM2MiZsaW5rPTY3N2RiZDJmLWM5MDMtNDUzMS05YjVjLWFlOTUxM2Y2NTBlZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=300872f4-64ff-4c72-8601-e662ccb98c62&link=677dbd2f-c903-4531-9b5c-ae9513f650ed&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sabit-kayit-kontrolu_47073959_47073663.html"
source_version: "2022-10-19T10:30:36.647+03:00"
source_bytes: 88107
fetched_at: "2026-09-13T04:18:04+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sabit Kayıt Kontrolü

Sabit Kayıt Kontrolü işlemi, **Enterprise** ürününü kullanan ve birden fazla işletme tanımlanan firmalarda, işletmelerin merkezinde **Entegre** ve **Standard** ürünleri ile, işletme tanımlaması yapılmamış firmalarda, **Enterprise** ürünü ile merkezde eski sene şirketinde çalıştırılması gerekir.

"Yeni Yıl Kopyalama" işleminden sonra eski sene şirketinde açılan cari kart, stok kartı, muhasebe hesap planı ve banka hesap kayıtları gibi sabit bilgiler yeni sene şirketinde de tanımlanması gerekir. Tanımlamalar yapılmadığı taktirde, modül devirleri esnasında eski şirkette hareket gören bu tür kartların devir bilgileri, yeni sene şirketine aktarılmaz. "Sabit Kayıt Kontrol" işlemini kullanarak, "Yeni Yıl Kopyalama" yapıldıktan sonra ve modül bazında devirlere geçmeden önce, eski sene şirketinde açılan cari kart, banka hesap kayıtları, plasiyer bilgileri, stok kartı, stokların muhasebe detay kodları, ürün reçete bilgileri, muhasebe hesap planı, proje kodları ve referans kodları gibi sabit bilgilerin yeni sene şirketinde de otomatik olarak açılması sağlanır. Ayrıca, "Fiyat Güncellemesi Yapılsın" seçeneği ile daha önce aktarılan stok sabit kartlarında fiyatı değişen stokların fiyatı yeni sene şirketinde güncellenebilir.

Sabit Kayıt Kontrolü ekranı; Giriş, İşlem ve İşlem Sonucu olmak üzere üç sekmeden oluşur.

**Giriş**

**![](../../../../_assets/a235b719acb0b9bfee71.png)**

**İşlem**

**![](../../../../_assets/9c5adcfccac4e28d5639.png)**

Eski sene şirketinde bulunup, yeni sene şirketinde de tanımlanması istenen sabit bilgi türü işaretlenerek yeni sene şirketinde oluşturulur. "Hepsini Seç/Kaldır" seçeneğine tıklanması ile, tüm sabit bilgi türleri işaretlenebilir veya işaretleri kaldırılabilir.

**İşlem Sonucu**

İşlem sırasında oluşan hatalar "İşlem Sonucu" sekmesinde görüntülenerek farenin sağ tuşuna tıklanarak dosyaya kaydedilir. Gelen hataların incelenmesi gerekir.

"Yeni Yıl Kopyalama" işlemi, devir şirketi oluşturulduktan sonra, herhangi bir hatadan dolayı yarım kalabilir. İşlemin kesilmesine sebep olan problem çözüldükten sonra; yeni sene için açılan şirketi sıfırlayarak ya da, yeni sene hazırlık işlemine kalınan yerden devam etmek mümkündür.

Açılan şirketi sıfırlayarak yeni yıl kopyalama işlemine baştan başlamak için, "Şirket Silme" işlemi ile yeni şirketin silinmesi gerekir.

Kalınan yerden "Yeni Yıl Kopyalama" işlemine devam etmek için, işlem tekrar çalıştırılarak, sorgulanan sahalara daha önceden girilen bilgilerin girilmesi ve "Evet" butonuna tıklanması gerekir.

Bu durumda, kalınan yerden işleme devam etmek istenip istenmediğinin sorgulandığı bir ekran görüntülenir. “Evet” butonuna tıklanması ile yeni yıl şirketinin tekrar kopyalanmasına gerek kalmadan devir işlemine devam edilir.

İşlemler bittiğinde, modül devirleri öncesi, yeni sene kayıtlarına başlama ortamının hazırlanması işlemi tamamlanır. İstendiğinde eski senenin kayıtları bitene kadar, hiç bir modülün devri yapılmadan eski sene şirketinde ve yeni sene şirketinde ayrı ayrı çalışılarak kayıtlara devam edilebilir. Eski senenin devir kayıtları, eski sene kapatılıp devir yapıldığında yeni sene bilgilerine aktarılır. İstendiğinde modül devirleri programın içinden yapılmayıp, açılan yeni sene şirketinde elle kaydedilebilir. Bu işlemlerden biri yapılmadan yeni sene bakiyelerini doğru olarak izlemek mümkün değildir.

"Yeni Yıl Kopyalama" işlemi ile devri oluşturulan eski şirkete girerken, “Şirket devri yapılmıştır. Devir Şirketi: DEVIR. Bu şirketin sadece rapor amaçlı kullanılması tavsiye edilmektedir. Yeni yıla ait kayıtlarınızı veya düzeltme işlemlerinizi DEVIR şirketine yapabilirsiniz!” şeklinde bir uyarı mesajı görüntülenir.

Dosyaya bağlanan ve dosyası kapatılan dış ticaret belgelerinin yeni yıl şirketine aktarılmaması sağlanır.
