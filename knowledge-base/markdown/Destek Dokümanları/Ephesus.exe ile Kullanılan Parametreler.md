---
title: "Ephesus.exe ile Kullanılan Parametreler"
page_id: "102282167"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Ephesus.exe ile Kullanılan Parametreler"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Ephesus.exe ile Kullanılan Parametreler"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk2ZTQxYTkwLTllOTktNGVjMS1hMWYzLWZlN2Q4OGFjOWQ1YSZsaW5rPTA2NDBmYzVjLTZkZTEtNGVhNy1iODgxLThiYTgxOGFjZTM2MiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=96e41a90-9e99-4ec1-a1f3-fe7d88ac9d5a&link=0640fc5c-6de1-4ea7-b881-8ba818ace362&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ephesus-exe-ile-kullanilan-parametreler_102282167_102282167.html"
source_version: "2023-01-02T12:51:34.263+03:00"
source_bytes: 1153181
fetched_at: "2026-09-13T04:23:45+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ephesus.exe ile Kullanılan Parametreler

Ephesus.exe ile kullanılan parametreler hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

**"SHOWRESOURCEID"**

Ephesus.exe bu parametre ile kullanıldığında program içindeki her alanın numarası görünür hale gelir. Exe' nin kısayolu üzerinde sağ klik ile özellikler menüsü seçildiğinde aşağıdaki ekran gelir ve hedef alanındaki dizinin sonuna "SHOWRESOURCEID" yazılır.

(C:\\Netsis\\Enterprise9043\\TemelSet\\Ephesus.exe SHOWRESOURCEID)

![](../_assets/e5052e6b12b4f7add1ed.png)

Netsis açıldığında ilgili ekranların aşağıdaki şekilde geldiği görülür.

Örneğimiz, cari hesap kayıtları ekranındaki "Kod-1" alanının ismini değiştirmek yönünde olsun.

![](../_assets/f90a417588af0240feb4.png)

"Netsis Dil Düzenleyicisi" menüsü üzerinden ilgili alanı bulup çift klik ile "Hedef Açıklama" kısmına istediğiniz açıklamayı yazıp değişiklikleri kaydet dedikten sonra şirket değişikliği yapılır. Programa tekrar giriş yapıldığında düzenleme aktif hale gelmiş olur.

![](../_assets/5315b5d8370102533f1b.png)

![](../_assets/f92d2ded70ed83dc5a9e.png)

**"PROFILER"**

9.0.41 setiyle birlikte Netsis içinden profiler alınması sağlanmıştır.

Netsis'in kurulu olduğu dizinde "Servis" klasörü altından "Profiler.exe" çalıştırılır.

![](../_assets/86b8d59b1ab90b212b50.png)

Profiler alınmak istenen bilgisayarda "Ephesus.exe" iki yöntemle açılabilir;

- "Ephesus.exe" kısayolu üzerinde sağ klik ile özellikler menüsü seçildiğinde aşağıdaki ekran gelir ve hedef alanındaki dizinin sonuna "profiler" yazarak açılabilir.

(C:\\Netsis\\Enterprise9043\\TemelSet\\Ephesus.exe profiler)

![](../_assets/f2f7cea48e0fe9733712.png)

- Çalıştır kısmında "Ephesus.exe" kısayolunu belirttikten sonra sonuna "profiler" yazarak açılabilir.

![](../_assets/c584087b0ad3eb5d374a.png)

Program açıldığı andan itibaren aşağıdaki şekilde sorgular dönmeye başlar.

![](../_assets/b9a28f4299eb5d647a28.png)

**"NOBACKGROUND, NOTHEME, NOEFFECT"**

9.41 setiyle birlikte temaların devre dışı bırakılabilmesi için parametreler eklenmiştir.

"Ephesus.exe" kısayolu üzerinde sağ klik ile özellikler menüsü seçildiğinde aşağıdaki ekran gelir ve hedef alanındaki dizinin sonuna "NOBACKGROUND, NOTHEME, NOEFFECT" parametrelerinden biri veya birkaçı aralarına boşluk eklenerek kullanılabilir.

![](../_assets/04d204ea19b0e86db336.png)

**"DEBUG"**

Oracle tarafında WinDebug üzerinden sorguları takip edebilmek için kullanılır. Başlat\\ Programlar\\ Debugging Tools for Windows ile program çalıştırılır.

![](../_assets/11fedf6f368533b4e3cd.png)

File \\ Open Executable... menüsü tıklanır.

![](../_assets/e9bf980a5ce29d9ab3e9.png)

File name bölümüne Ephesus.exe dosyası belirtilip Arguments bilgisine DEBUG parametresi girilerek işlem başlatılır.

![](../_assets/d6a5b9e93988eba93b17.png)

Edit \\ Open Close Log File işlemi ile oluşan kayıtların bir text dosyaya kaydedilmesi sağlanır. Bu ekranda Append seçeneği işaretlendiğinde; eğer aynı isimli bir dosya mevcut ise eski dosyanın sonuna yeni kayıtları eklemeye başlar, işaretlenmezse eski dosyanın üzerine yazar.

Netsis'in login penceresi gelene kadar F5 tuşuna birkaç kez basılır. Netsis'e geçilip takip edilmek istenen işlem başlatılır.

![](../_assets/d69a9b6f751aad5fb290.png)

![](../_assets/9ddfe19a6a9adc51dc8a.png)

İşlemler tamamlanınca Debug \\ Break menüsünden kayıt etme işlemi sonlandırılır.

![](../_assets/6a58301866541644993e.png)

Ayrıca açık olan text dosyası Edit \\ Open Close Log File menüsüne tekrar girilip gelen ekranda Close Open Log File seçilip kapatılarak, işlem sonlandırılır.

![](../_assets/5543525fa003b5080f9a.png)

**"NOSPLASH"**

Ephesus.exe açılışında şirket ve kullanıcı bilgilerinin girildiği ilk ekran sonrasında çıkan aşağıdaki Logo Netsis 3 görselinin gelmesi engellenir.

![](../_assets/95aa4e7b8618ac48d7c5.png)

Bu parametre tanımlandığında şirket ve kullanıcı bilgilerinin girildiği ilk ekran sonrasında doğrudan aşağıdaki modül bilgilerinin sırasıyla okunduğu ekran gelir ve masaüstündeki ana menüler görüntülenir.

![](../_assets/f4f6a83fded9dfe07b36.png)
