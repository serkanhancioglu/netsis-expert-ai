---
title: "Ek-3 (Bağlantı Takibi Uygulaması)"
page_id: "22805759"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Ekler"
  - "Ek-3 (Bağlantı Takibi Uygulaması)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Ekler / Ek-3 (Bağlantı Takibi Uygulaması)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ1ZTRlZmYzLTIwYzEtNDQ3Zi1iMjVjLTE1YTMyY2QyNjY1ZiZsaW5rPThiOWMzZWI1LWU1MjMtNDJmMy05YWMzLTY0OWNjZWUzNjMzYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=45e4eff3-20c1-447f-b25c-15a32cd2665f&link=8b9c3eb5-e523-42f3-9ac3-649ccee3633c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-3-baglanti-takibi-uygulamasi_29991025_22805759.html"
source_version: "2022-11-01T14:46:15.450+03:00"
source_bytes: 140490
fetched_at: "2026-09-13T04:08:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-3 (Bağlantı Takibi Uygulaması)

Ek 3 Bağlantı Takibi Uygulaması bölümünde, "Cari Modül" dışındaki modüllerde bağlantı takibi ile ilişkili kullanım hakkında bilgi verilir.

Bağlantı takibinin kullanım amacı ve uygulama için yapılan standart tanımlamalar hakkında detaylı bilgi; Cari → Kayıt → Bağlantı - Sipariş Kayıtları.

**Fatura Modülü Bağlantı** **İşlemleri**

Bağlantı takibinde sipariş, irsaliye ve fatura kayıtları sırasında bağlantılı işlem yapılması istendiğinde, "Cari Kod" alanına bağlantı fatura kontrol hesabının veya bağlantı için açılmış olan ana kodun (Örneğin, NETSISANA) girilmesi gerekir. Her iki koşulda da, program ilgili koda ait açık bağlantıları rehber ekranında gösterir. Bu ekrandan hangi bağlantıya ait işlem yapılması isteniyorsa, ilgili bağlantı fare (mouse) ile çift tıklanarak seçilir ve Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basılır. Bu sırada program tarafından, seçilen bağlantının o anki açık bağlantı tutarı (Bağlantı Tutar–Bağlantı Devir Kapatılmış Tutar–Teslim Edilmeyen Sipariş Tutarı–Teslim Edilen Mal Tutarı+İade Tutarı) gösterilir. Aynı zamanda, "Cari Kod" alanına bağlantı için açılan ana cari kodu yazılmışsa, yazılan ana kod fatura işlemleri için açılan cari kod ile değiştirilir.

**Örneğin:** NETSISBF.

Bağlantılı fatura işlemlerinde hiçbir zaman cari ana koda ve bağlantı cari hesap koduna işlem yapılmasına izin verilmez. Rehber ekranlarında sadece tek bir bağlantı numarası seçilebilir. Yani aynı anda birden fazla bağlantıyla ilgili işlem yapılamaz.

![](../../../../_assets/98176c36101f8ca8c5db.png)

Daha sonraki işlemlere normal prosedürde devam edilmesi gerekir. Bağlantı işlemi direkt fatura modülünden yapılıyorsa, cari (NETSISBF)ve entegrasyon kayıtları (NETSISBF muhasebe kodu kullanılarak) otomatik olarak yapılır. Eğer bağlantı takibi siparişten başlanarak yapılıyorsa, öncelikle bağlantı numarası seçilerek siparişin kaydedilmesi gerekir. Daha sonra sipariş, irsaliye yada fatura kullanılarak teslim edilir. Teslimler sırasında, satır bazlı sipariş numarası kullanılıyorsa, "Kalemler" sekmesindeki sipariş rehberine ilgili kaleme ait siparişler getirilir. Bu bölümde program farklı bağlantı numarasına sahip siparişlerin teslimatlarına izin vermez. Bağlantılı sipariş işlemi yapıldığında, bağlantı numarası sipariş kaydı sırasında sorulur. Sipariş teslimatıyla ilgili işlemlerde tekrar bağlantı numarası sorgulanmaz. İşlemler bittiğinde, bağlantı kaydı sırasında müşteri fatura kontrol hesaplarına alacak, satıcı fatura kontrol hesaplarına borç olarak işlenen kayıtlar, faturaların kesilmesiyle kapatılır. Müşteri bağlantı kayıtları için alış faturası seçeneği, satıcı bağlantı kayıtları için de satış faturası seçeneği ile iade kaydı yapılır. Bunun dışındaki durumları program kontrol eder ve izin vermez.

**Bağlantı Tahsilat/Ödeme İşlemleri**

Bağlantı takibinde yapılan tahsilatlarda (kasa/çek/senet/dekont) cari alt kod tanımlama bölümünden ana koda bağlanan bağlantı cari hesap kodunun kullanılması gerekir. Eğer ana koda bağlı bağlantı cari hesap kodu bilinmiyorsa, tahsilat veya ödemenin yapıldığı modüllerde "Cari Kod" alanına ana kod yazılarak klavyeden "Ctrl+B" tuşuna basıldığında ilgili ana koda ait bağlantı cari hesap kodları rehber ekranında listelenir. Cari kod üzerinde fare ile çift tıklanarak seçim yapılabilir.

![](../../../../_assets/02c93266f40c2b254ca6.png)

Cari hesap bağlantı hesap kodları açılırken hesap tipi olarak "Özel Hesap Kapatma" seçilmişse, tahsilat ve ödemelerde açılan özel hesap kapatma ekranlarında alınan tahsilatın veya yapılan ödemenin hangi bağlantı için olduğu kullanıcılar tarafından seçilebilir. Bağlantı kaydı yapıldığında, alıcılar için bağlantı cari hesap koduna borç, satıcılar için alacak hareketi işlenir. Dolayısıyla bağlantı cari hesap kodu kullanılarak yapılan tahsilatlar müşterilerin alacağına, ödemeler ise satıcıların borcuna işlenir ve bu hesaplar tüm ödeme ve tahsilatların yapılmasıyla kapatılır. Cari hesap bağlantı hesabı kontrol edilerek, hangi bağlantılardan ne kadar tahsilat alındığı ve daha ne kadar alınması gerektiği, hangi bağlantılar için ne kadar ödeme yapıldığı ve daha ne kadar ödeme yapılması gerektiği hesaplanır.

**Sipariş Cari Hesap Takibi**

Sipariş cari hesap takibi yapabilmek için öncelikle, siparişi veren müşteri için ana kodun, faturaların ve tahsilatların takip edileceği alt kodun cari hesap kayıtları bölümünden açılması gerekir. Daha sonra, Cari → Kayıt → Bağlantı-Sipariş Kayıtları → Cari Alt Kod Tanımlama bölümü kullanılarak ana kod ile alt kodların bağlanması gerekir. Sipariş uygulamasına göre kayıt oluşturulması için, sipariş işlemlerinde ana cari kodun kullanılmaması gerekir. Sipariş kaydederken ilgili ana koda bağlı fatura kontrol hesabının (örn:NETSISSF) kullanılması gerekir. Bu kod hatırlanmadığında "Cari Kod" alanına ana kodu yazılarak, klavyeden "Ctrl+B" tuşlarına basıldığında, program ilgili ana koda bağlı fatura kontrol hesabını rehber ekranında listeler.

![](../../../../_assets/3e2a1b0256a57df8d33a.png)

Müşteri sipariş kaydı tamamlandığında, fatura kontrol hesabına sipariş tutarı kadar alacak, cari hesap kontrol hesabına ise aynı tutar kadar borç hareketi işlenir. Aynı anda her iki hesabın muhasebe hesap kodları bazında entegrasyon kaydı, Entegrasyon Modülünde yer alan dekont mahsubuna aktarılır. Satıcı siparişi kesildiğinde ise, tam tersi kayıt oluşturulur. Yani fatura kontrol hesabına borç, cari hesap kontrol hesabına alacak hareketi işlenir. Proje kodu uygulaması varsa yapılan kayıtlar proje kodu bazında oluşur. Bu şekilde kaydedilen sipariş tutarları, müşterilerde sipariş fatura kontrol hesabına alacak (sipariş cari hesabına borç), satıcılarda ise sipariş kontrol hesabına borç hareketi (sipariş cari hesabına alacak) olarak izlenir. İş bitiminde veya iş devam ederken kesilen faturalar, sipariş fatura kontrol hesabının borcuna, satıcı hesaplarının da alacağına işleneceği için fatura kontrol hesapları kapanır.

**Sipariş Takibi Tahsilat/Ödeme İşlemleri**

Sipariş takibi yaparken oluşturulan tüm tahsilatlarda (kasa/ çek/ senet/ dekont), cari alt kod tanımlama bölümünden ana koda bağlanan bağlantı cari hesap kodunun kullanılması gerekir. Cari hesap bağlantı hesap kodları açılırken, hesap tipi olarak "Özel Hesap Kapatma" seçilmişse, tahsilat ve ödemelerde açılacak özel hesap kapatma ekranlarında, alınan tahsilatın veya yapılan ödemenin hangi sipariş için olduğu kullanıcılar tarafından seçilebilir. İşlenen tahsilatlar, sipariş cari hesaplarına işlenir ve dolayısıyla siparişten doğan borç yada alacaklar takip edilebilir. Sipariş cari hesabı kontrol edilerek hangi siparişten ne kadar tahsilat alındığı ve daha ne kadar alınması gerektiği, hangi siparişler için ne kadar ödeme yapıldığı ve daha ne kadar ödeme yapılması gerektiği hesaplanır.
