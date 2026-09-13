---
title: "Demirbaş Modülünden Dekont Oluşturma"
page_id: "50680122"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Demirbaş Modülünden Dekont Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Demirbaş Modülünden Dekont Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE2M2NiOGFiLTUyNjctNGU2NS04NTQyLWI5MjI2MGM3NjBmNSZsaW5rPTAzNjY0YmMyLTMyMGUtNDY2NS1iY2FjLWVkMjBmNDEwZjQxOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a63cb8ab-5267-4e65-8542-b92260c760f5&link=03664bc2-320e-4665-bcac-ed20f410f419&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "demirbas-modulunden-dekont-olusturma_78283867_50680122.html"
source_version: "2022-11-03T09:48:28.570+03:00"
source_bytes: 103570
fetched_at: "2026-09-13T04:26:12+00:00"
generator: "netsis-scraper 1.0.0"
---
# Demirbaş Modülünden Dekont Oluşturma

Demirbaş Modülünden Dekont Oluşturma ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Kaydedilen demirbaşların dekont kaydının demirbaş paketinden yapılması desteklenerek demirbaş kaydı ile ilgili kaydedilen dekontların düzeltme işlemi de bu ekrandan yapılabilmektedir.

![](../_assets/fa0f8616f4ff74a7b8a5.png)**Şekil 1**

Bu işlemin desteklenebilmesi için öncelikle demirbaş parametrelerindeki temelset entegrasyon veritabanı bilgileri girilmelidir. Buraya girilen bilgilere göre dekont belgesi oluşturulacaktır.

Entegrasyon veritabanı bilgileri girilip, Demirbaş kaydı tamamlandıktan sonra temelset datasına dekont kaydı da yapılmak isteniyorsa, demirbaş kartındaki bazı bilgilerin dolu olması gerekir.

Örneğin dekont kaydı sırasında kullanılacak olan cari hesabının alınması için demirbaş kartındaki "Satıcı" bilgisi girilmelidir. Bu alana doğru bilginin girilebilmesi için temelset datasından cari rehberin açılması ve bu ekrandan carilerin seçilebilmesi de desteklenmiş oldu.

Benzer şekilde kaydedilen demirbaşların KDV'si varsa, bu bilgilerinde demirbaş kartındaki KDV oranı ve tutarı alanlarına girilmiş olması gerekmektedir. Program temelset datasında dekont kaydını oluştururken demirbaş kartında girilmiş olan KDV oranının temelset datasının entegrasyon parametrelerinden ilgili hesap kodunu çalıştıracaktır.
![](../_assets/b5563312cd2ceb4795e7.png)**Şekil 2**

Her demirbaş için ayrı ayrı sabit kartlardan dekont oluşturulabildiği gibi tek seferde toplu dekont kaydı da oluşturulabilir.
![](../_assets/4f14ee709963013c11c7.png)**Şekil 3**
**Her Demirbaş** **İçin** **Ayrı** **Dekont** **oluşsun:** Her demirbaşın ayrı bir dekont numarası ile oluşması isteniliyorsa bu parametre işaretlenmelidir.
