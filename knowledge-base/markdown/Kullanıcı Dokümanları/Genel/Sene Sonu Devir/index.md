---
title: "Sene Sonu Devir"
page_id: "22803550"
product: "netsis-3-enterprise"
depth: 3
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Sene Sonu Devir"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQyODIxNDVmLWQzMWItNGI0ZC1iMmUxLTdlODBiYzgzOWRkYSZsaW5rPTlhNzdkNWNiLWM0YjAtNDAyMS05OGYyLWFjOTUxMmQwMzg5MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=4282145f-d31b-4b4d-b2e1-7e80bc839dda&link=9a77d5cb-c4b0-4021-98f2-ac9512d03893&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sene-sonu-devir_24753393_22803550.html"
source_version: "2022-10-19T10:17:26.197+03:00"
source_bytes: 545777
fetched_at: "2026-09-13T04:18:02+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sene Sonu Devir

Enterprise, Standard ve Entegre paketlerinde bir cari yıla ait bilgiler bir şirkette bulunur ve her yeni cari yıl için yeni bir şirket oluşturulması gerekir.

**Örneğin;** D2019 ve D2020 gibi.

Program, yeni sene kayıtlarını eski sene kayıtlarının devamı olarak aynı şirkette oluşturulmasına izin verir. Ancak 5.0 sürümüyle birlikte gelen, “Muhasebeye Doğrudan Aktarım” özelliğinin kullanıldığı modüllerin - Fatura, Çek, Senet, Banka, Dekont gibi - yeni yıl kayıtlarının, mutlaka devir ile oluşturulan yeni yıl şirketine girilmesi gerekir.

**Örneğin,** Fatura modülünde muhasebeye doğrudan aktarım özelliği kullanılıyorsa, yeni yıla (2020) ilişkin fatura belgeleri yeni yıl şirketine girilir. Aksi durumda geçmiş yıla giriş yapılan yeni yıl belgeleri, modül devirlerinde dikkate alınmayarak yeni yıla aktarılmaz. Eski şirketteki yeni yıl kayıtları, doğrudan muhasebeye işlenir ve eski yıl şirketinde muhasebe kayıtları yeni yıl muhasebe kayıtlarını da içerir. Bu durumun oluşmaması için muhasebeye doğrudan aktarım özelliğinin kullanıldığı modüllerin yeni yıl kayıtları, mutlaka yeni yıl şirketine girilmesi gerekir.

Yıl sonunda yeni sene işlemlerine başlamadan önce, aşağıdaki yöntemlerden birinin belirlenip buna göre devir işlemlerinin planlanması gerekir:

- Yeni senenin başında, yeni sene şirketinin hazırlanıp tüm modüller için yeni seneye ait kayıtları yeni sene, eski seneye ait kayıtları eski sene şirketinden devam ettirilmesi sağlanabilir. Modül bazında devirleri - stok devri, cari hesaplar devri gibi - daha ileri bir tarihte yapıp devir kayıtlarının otomatik olarak yeni sene şirketinde oluşması sağlanabilir.
- Muhasebeye doğrudan aktarım özelliği kullanılmıyorsa, eski sene şirketinde yeni sene kayıtları girilmeye devam edilebilir ve modül bazında devirlerin - stok devri, cari devir gibi - yapılacağı tarihe kadar bu şekilde devam edilebilir. Bu tarihte yeni sene şirketi oluşturulup modül devirleri yapılabilir. Ancak, bu şekildeki bir çalışmada devir yapılma tarihine kadar eski sene şirketinde muhasebe entegrasyonu ve muhasebede fiş girişinin yapılmaması gerekir. Yine bu şekildeki bir çalışmada, yeni sene şirketinin hazırlanması ile modül devirlerinin aynı tarihte yapılması gerekir. Yeni sene şirketinin hazırlanması ile ilgili detaylı bilgi, [Kayıt/Sene Sonu Devir](<Kayıt - Sene Sonu Devir/index.md>) - Yeni Yıl Kopyalama - bölümünde yer alır.

- İstendiği zaman modül devirleri, eski seneden yeni seneye program tarafından otomatik olarak değil, her modülün kendi devir hareketleri kullanıcı tarafından - elle - işlenir. Modül devirleri ister program tarafından, ister kullanıcı tarafından yapılsın, yeni sene şirketinin hazırlanması için devir öncesi hazırlık - yeni yıl kopyalama - işleminin mutlaka yapılması gerekir.

- Yeni sene şirketi hazırlık ve modül bazında devir işlemlerinin eski sene şirketinden yapılması gerekir.

- Yeni sene şirketinde devir yapılmadan muhasebe kayıtlarına başlanacaksa, sonradan oluşturulacak açılış fişi için bir fiş numarası ayrılması gerekir. Detaylı bilgi "Muhasebe Devirlerinde" yer alır.

- Denetim Listeleri ile, modül bazında devir sonrası ilgili modülün devir tutarları ile muhasebe açılış fişindeki bağlantılı hesapların devir tutarlarının kıyaslanarak farklılıklar tespit edilebilir. Netsis Online e-Fatura veya Entegratör kullanan firmaların yeni yıla ve eski yıla ait gelen e-faturalarının doğru şirketlere aktarımının sağlanması için en geç 31.12.2019 tarihinde yeni yıl şirketlerini açması gerekir.

- "Yeni Yıl Kopyalama" işlemi ile TBLEIMZAREG tablosuna yeni yıl şirketine ait kayıt program tarafından otomatik olarak aktarılır. Efaturaayarlar.exe’den tekrar yeni sertifika tanımlamasına gerek yoktur. Entegratör kullanan firmalar için, önceki yıl data bilgisi alanına program tarafından eski yıl şirket ismi otomatik olarak getirilir.
- Online e-Fatura kullanan firmaların "Yeni Yıl Kopyalama" işlemi haricinde, yeni yıla ve eski yıla ait gelen faturalarının doğru şirketlere aktarımının sağlanması için web.config dosyasının düzenlemesi gerekir. 31.12.2019 tarihi öncesinde devir yapılması durumunda web.config dosyası 01.01.2020 tarihine kadar geçen süre için değiştirilmemesi gerekir.

web.config dosya düzenlemesinin yöntemleri aşağıdaki şekildedir:

- Netsis in kurulu olduğu dizinde bulunan "Servis" klasöründeki Efaturaayarlar.exe dosyası çalıştırılır ve "İşlemler" menüsünden "Web Servis Ayarları" seçilir. Açılan ekranda, sol tarafta görünen Default Web Site’ın altında değişiklik yapılacak olan kayıt seçilir. Veritabanı bilgilerinin olduğu satırdaki üç nokta ... işaretine tıklanır. Açılan ekranda VT Adı (Şirket) bölümüne yeni yıl şirketinin (2020) adı yazılır. Önceki Yıl Datası yazan bölüme de eski yıl şirketinin (2019) ismi yazılır ve kaydet butonuna basılır. Böylece web.config dosyası düzenlenir.

![](../../../_assets/334a9162029171de46e0.png)

- e-fatura web servisinin kurulduğu sunucu bilgisayarın C:\\inetpub\\wwwroot\\NetsisEFatura dizininde bulunan Web.config dosyası, notepad ile açılıp elle düzenlenebilir. Buna göre OldSchema bölümüne 2019 şirketi, Schema ve initial catalog bölümlerine de 2020 şirket adının yazılması ve kaydedilmesi gerekir.

![](../../../_assets/b8ce4e0f6720dfdc1917.png)

- 31.12.2019 tarihine kadar yeni yıl şirketi açılmamışsa, program içinde fatura tarihinin yılı \< sistem tarihinin yılı kontrolü yapılır ve 2019 faturalarını almaya devam eden firmaların faturaları 2018 yılı şirketine aktarılır. Bu durumda, eski yıl şirketine düşen faturalar tespit edilip yeni yıl şirketine aktarılması gerekir.
