---
title: "Form Bazı Güvenlik"
page_id: "128581695"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Form Bazı Güvenlik"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Form Bazı Güvenlik"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPThiMDExZmQ3LTAwYTctNDgxYy05NDlmLWY5Y2FiYjIwMDhhMSZsaW5rPTQ4OGMyYjliLTgyOWUtNGU4ZC1hOGE5LWVjZWI0OTQ4NmVmNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8b011fd7-00a7-481c-949f-f9cabb2008a1&link=488c2b9b-829e-4e8d-a8a9-eceb49486ef7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "form-bazi-guvenlik_128581705_128581695.html"
source_version: "2023-11-29T18:17:27.650+03:00"
source_bytes: 2698173
fetched_at: "2026-09-13T04:23:10+00:00"
generator: "netsis-scraper 1.0.0"
---
# Form Bazı Güvenlik

Form Bazı Güvenlik Uygulaması, Netsis programı içerisinden açılan herhangi bir ekran üzerindeki alanların, kullanıcı ya da grup bazında kısıtlanarak görünebilirliğinin ve değiştirilebilirliğinin düzenlenebildiği bir uygulamadır.

Form Bazı Güvenlik Uygulaması'nın aktif hale getirilebilmesi için, Genel\\Yardımcı Programlar\\Kayıt\\Şirket- Şube Parametre Tanımları ekranındaki "Form Bazı Güvenlik Uygulaması Var" parametresi işaretlenmeli ve programa tekrar giriş yapılmalıdır.

![](../_assets/547258a490fcbb09a3c3.png)

Form Bazı Güvenlik Uygulaması'nda düzenleme yapabilmek için; ilgili ekranın sol üst köşesindeki L sembolü ile belirtilen menüye tıklayıp Netsis Form Bazı Güvenlik işlemi seçilir.

![](../_assets/15fbd62a1ae232bf4b34.png)

Açılan ekrandaki "Kullanıcı Bilgileri" bölümünden "Kullanıcı", "Grup" ya da "Tüm Kullanıcılar" seçimi yapılıp gride kaydedilerek Form Bazı Güvenlik tanımının uygulanacağı kullanıcılar için kısıt verilebilir.
![](../_assets/ee241e317519a121b6fa.png)

Kullanıcı Bilgileri'ni belirledikten sonra grid üzerindeki kaydı çift tıklayıp ekranın altındaki "Form Bazı Güvenlik Tanımlamasına Geç" butonu ile aşağıdaki ekrana ulaşılır.

![](../_assets/b2d921e78e716317feda.png)

Düzenleme yapılması istenen alanın üzerine gelip kırmızı renkli taranmış halde görüldüğünde klavyeden + tuşuna basılıp seçilen nesnenin gride eklenmesi sağlanır. "Görünür" ve "Değiştirilebilir" kolonları altındaki hücreler üzerinde çift tıklayarak "Evet" ya da "Hayır" seçimi yapılır ve ![](../_assets/ab3f855bb8d0ab56a760.png) butonu ile kaydedilir. Aşağıdaki tanımlama örneğinde, "Stok Kartı Kayıtları" ekranındaki "İngilizce İsim" alanının, önceki sekmede seçilen "EZEL" kullanıcısı için görünür ve değiştirilemez olması amaçlanmıştır.

![](../_assets/a6ffa18a8608f638c823.png)

Programa "EZEL" kullanıcısı ile giriş yapılıp "Stok Kartı Kayıtları" ekranı açıldığında görünümün aşağıdaki hali alması beklenir:
![](../_assets/3913df69bf0fbcd257ba.png)

Griddeki bir kolonda Form Bazı Güvenlik düzenlemesi istendiğinde, gridin üzerine gelip tamamını kırmızı renkli taranmış halde görüp klavyeden + tuşuna basılır. Nesne Adı "KalemListesi" olan satır gelir ve bu satırdaki Grid Kolon No değerine, düzenleme yapılması istenen kolon için manuel olarak kolon numarası yazılır ve ![](../_assets/ab3f855bb8d0ab56a760.png) butonu ile kaydedilir. Aşağıdaki tanımlama örneğinde, "Satış Faturası" ekranında kalemler sekmesindeki gridde yer alan "İsim" kolonunun, önceki sekmede seçilen "EZEL" kullanıcısı için görünemez ve değiştirilemez olması amaçlanmıştır.

![](../_assets/d389b97caacf786ac633.png)

Programa "EZEL" kullanıcısı ile giriş yapılıp "Satış Faturası" ekranında kalemler sekmesi açıldığında görünümün aşağıdaki hali alması beklenir:

![](../_assets/dfd2110986839d945f0f.png)

Not 1: Form Bazı Güvenlik tanımlamaları, veri tabanında TBLNFDMAS ve TBLNFDTRA tablolarında tutulmaktadır.

Not 2: Programa giriş yapan kullanıcılar admin ise, Form Bazı Güvenlik ile yapılan düzenlemeler dikkate alınmamaktadır.

Not 3: Grid kolon numarası, ilk kolon 0 kabul edilecek şekilde sayılmaktadır. Takip eden kolonların numaraları da ardışık olarak devam etmektedir.
