---
title: "Fatura - İrsaliye - Stok - Cari Kontrolü"
page_id: "24767982"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Raporlar / Fatura"
  - "Raporlar / Denetim Listeleri"
  - "Fatura - İrsaliye - Stok - Cari Kontrolü"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Raporlar / Fatura / Raporlar / Denetim Listeleri / Fatura - İrsaliye - Stok - Cari Kontrolü"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWUwMTg0MzRhLTJkMDItNGQyMS05ZDg4LTQ1NjNiOTExZGFkNSZsaW5rPTRiNjU3ZThhLTkzZTItNGYwMS1hMGJjLTZkZjUxMDE4ZGNhYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e018434a-2d02-4d21-9d88-4563b911dad5&link=4b657e8a-93e2-4f01-a0bc-6df51018dcab&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "fatura-irsaliye-stok-cari-kontrolu_24768067_24767982.html"
source_version: "2022-10-25T13:57:17.023+03:00"
source_bytes: 127758
fetched_at: "2026-09-13T04:03:18+00:00"
generator: "netsis-scraper 1.0.0"
---
# Fatura - İrsaliye - Stok - Cari Kontrolü

Herhangi bir bağlantı veya hard diskte donanımla ilgili oluşabilecek bir sorun sonucu, faturaların bir kısmının stok kalemleri izlenemediğinde, stok hareketlerinin stoklarda var olup olmadığı kontrol edilir. Eğer faturaların stok hareketleri gerçekten kaybolmuşsa, bu faturaların sabit kayıtlarının tek tek iptal edilmesi ve tekrar girilmesi gerekir.

Stok veya cari hesap hareketleri kaybolan faturaların tespiti için Fatura-İrsaliye-Stok-Cari Kontrolü bölümü çalıştırılır.

Bu türden faturalar, Fatura Modülü → İşlemler → Tek Fatura - İrsaliye Silme Bölümünden silinebilir.

Fatura-İrsaliye-Stok-Cari Kontrolü ekranı; Kısıt, Ölçekleme ve Yazıcı Seçenekleri sekmelerinden oluşur.

**Kısıt**

Kısıt sekmesi bilgileri aşağıdaki şekildedir:

| Fatura - İrsaliye - Stok Cari Kontrolü Ekranı |  |
| --- | --- |
| Sahalar | Fatura/İrsaliye/Stok/Cari kontrolü yapmak için kısıt verilmesi istenen alanlar yer alır. Ekle ![](../../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "kısıt verilecek sahalar" kısmına eklenir. |
| Kısıt Verilecek Sahalar | Fatura/İrsaliye/Stok/Cari kontrolü yapmak için kısıt verilen sahaların yer aldığı alandır. Çıkar ![](../../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Eşit, Küçük, Küçük veya Eşit, Büyük, Büyük veya Eşit, Arasında, Benziyor, Eşit Boş, Eşit Değil, İçinde Eşit Değil | **Eşit:** İşaretlenen alanda belli bir sabit koşula göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "001" olan stok için liste alınacaksa "Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "001" girilir. Bu durumda, sadece "001" numaralı Stok Kodu için liste alınır. **Küçük:** İşaretlenen alanda belli bir değerden küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den küçük" numaralı Stok Kodu için liste alınır. **Küçük veya Eşit:** İşaretlenen alanda belli bir değere eşit veya küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den küçük" numaralı Stok Kodu için liste alınır. **Büyük:** İşaretlenen alanda belli bir değerden büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den büyük" numaralı Stok Kodu için liste alınır. **Büyük veya Eşit:** İşaretlenen alanda belli bir değere eşit veya büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den büyük" numaralı Stok Kodu için liste alınır. **Arasında:** Seçilen alanla ilgili bir aralık tanımlanması istendiğinde kullanılması gereken seçenektir. Eğer belli bir başlangıç ve bitiş değeri arasında kalan değerlerle ilgili kısıt verilecekse kullanılması gereken seçenektir. Örneğin; Stok Kodu kıstasında, "Arasında" seçeneği seçilip \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" ve yine \<tab\> tuşu ile ilerlenerek altta bulunan alana "200" yazıldığı varsayılsın. Böylece stok kodu 100 ile 200 arasındaki stok kodları için liste alınır. **Benziyor:** Cari ile ilgili kayıt ararken cari hesabın ismi tam olarak bilinmiyorsa benziyor seçeneği kullanılır. Örneğin; cari hesabın isminin CANEL ya da CENEL olacağı düşünülüyorsa, bu seçeneği seçtikten sonra alanın sağ tarafındaki kayıt alanına "C_NEL" yazıldığında, raporda cari ismi "C" ile başlayan ikinci karakteri herhangi bir karakter olan fakat sonu "NEL" ile biten kayıtlar listelenir. **Eşit Boş:** Seçilen sahada hiçbir bilgi olmadığında kullanılan seçenektir. Bu seçenek alfanumerik sahalar için geçerlidir. Sıfırdan büyük veya sıfıra eşit bilgilerin aranması durumunda "Eşit", "Büyük Eşit", "Küçük Eşit" seçenekleri kullanılabilir. **Eşit Değil:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında, Benziyor ve Eşit Boş seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Eşit Değil" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Eşit Değil" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| İse/Değil ise | **İse:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumlu (dahil) anlamını taşıyorsa "İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "İse" seçeneği işaretlenirse, rapora stok kodu "0101" olan stokların dahil edileceği anlaşılır. **Değil İse:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Değil İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Değil İse" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| Ve/Veya | **Ve:** Seçilen sahalarda zorunlu bağlantı koşulu sağlar. **Örnek 1:** Karmaşık bir stok kodlaması olduğu varsayıldığında; Bu kodlardan iki tanesinin raporda çıkması isteniyor fakat bu iki stok kodunun ortak hiçbir özelliği yok. Bu durumda, "Stok Kodu" sahası iki kez kısıt verilecek sahalar bölümüne aktarılır. 1.Stok Kodu kıstasında eşit bağlantısı kurularak ilk stok kodu girilir ve "VE" bağlacı işaretlenir. Daha sonra 2. Stok Kodu seçilerek yine eşit bağlantısı ile diğer bir stok kodu yazılır. Böylece, raporda sadece bu iki stok koduna ait bilgi alınır. Bu seçenekte tanımlanan her koşulun olması zorunludur. Yani, tanımlanan iki stok kodundan biri bile mevcut değil ise, rapor bilgi vermez. **Örnek 2:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; Verilen tanımlamalarda "VE" bağlacı kullanılırsa, mutlaka bu üç kısıta da sahip olan stoklar aranır ve bulunursa listelenir. Üç kısıttan herhangi birine sahip olmayan stoklar raporda listelenmez. **Veya:** Seçilen sahalarda olabilirlik koşulu sağlar. Yani, tanımlanan koşullardan biri bile sağlansa ilgili raporla ilgili bilgi alınabilir. **Örnek 1:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; Verilen tanımlamalarda "VEYA" bağlacı kullanılırsa, bu üç kısıttan birine bile sahip olan stoklar aranır ve bulunursa listelenir. |
| ![](../../../../../_assets/c7275efbddc154ea1579.jpg) Sakla | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| ![](../../../../../_assets/7ba39f9046a578093326.png) Rapor | Fatura/İrsaliye/Stok/Cari kontrolü yapmak için verilen kısıtlara göre Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Fatura/İrsaliye/Stok/Cari kontrolü yapmak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki Fatura/İrsaliye/Stok/Cari kontrolü rapor işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Fatura/İrsaliye/Stok/Cari kontrolü ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Fatura/İrsaliye/Stok/Cari kontrolü yapmak için verilen kısıtların iptal edildiği butondur. |

Kısıt tanımlaması yapılırken açılan her parantez mutlaka kapatılması gerekir. Kapatılmadığı taktirde rapor butonu aktif olmaz.

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

**Örneğin:** Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

Yazıcı Seçenekleri sekmesi bilgileri aşağıdaki şekildedir:

| Fatura-İrsaliye-Stok Cari Kontrolü Ekranı | Yazıcı Seçenekleri |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek Rapor ![](../../../../../_assets/21c20c78203acae9cce6.jpg)butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../../_assets/b2e157c1e0713bfefb94.png) |
| Fatura-İrsaliye-Stok Cari Kontrolü Ekranı | Yazıcı Seçenekleri-Yönlendirme |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Fatura-İrsaliye-Stok Cari Kontrolü Ekranı | Yazıcı Seçenekleri |
| Şirket Adı | Basılsın, Basılmasın ve Detaylı Basılsın olmak üzere üç seçenekten oluşur. Yazıcıdan alınacak raporun her bir sayfasında şirket unvanının yazılması istendiğinde "Basılsın" seçeneğinin kullanılması gerekir. Şirket unvanı Yardımcı Programlar/Şirket/Şube Parametre Tanımları menüsünde tanımlandığı şekilde otomatik olarak ekrana gelir. |
| Başlık Yazılsın | Yazıcıdan alınacak raporun her bir sayfasında, tanımlanan liste başlığının yazılması istendiğinde işaretlenmesi gereken seçenektir. |
| Tarih/Saat Yazılsın | Yazıcıdan alınacak raporun her bir sayfasında sistem tarihi ve saatinin yazılması istendiğinde işaretlenmesi gereken seçenektir. |
| Sayfa No Basılsın | Yazıcıdan alınacak raporun her bir sayfasında sayfa numarasının yazılması istendiğinde işaretlenmesi gereken seçenektir. |
| Taslak Basım | Birden fazla alanın yer aldığı raporlarda, yazıcıdan çıktı alırken kağıttan taşma sorununun çözülmesi ve raporların istenilen formatta ayarlanması için, "Taslak Basım Ayarları" bölümü kullanılır. Taslak basım ayarları her rapor için bir kez yapılır ve saklanır. Böylece, yazıcıdan çıktı alırken tekrar ayarlama yapmaya gerek kalmadan basım yapılır. Raporun "Taslak Basım Ayarlarında" kaydedilmiş formata göre dökülmesi istendiğinde "Taslak Basım" ve "Saklanmış" seçeneklerinin işaretlenmesi gerekir. Basım Dot Matrix (iğne vuruşlu yazıcı) türü bir yazıcıdan alınacaksa, basım ayarları yapılmasa da "Taslak Basım" seçeneğinin işaretlenmesi gerekir. |
| Saklanmış | Raporun "Taslak Basım Ayarlarında" kaydedilmiş formata göre dökülmesi istendiğinde "Taslak Basım" ve "Saklanmış" seçeneklerinin işaretlenmesi gerekir. |
| Perfore Satır Sayısı | Yazıcıya gönderilecek raporun kaç satırlık kağıda basılacağının belirlendiği alandır. 33’lük ya da 66’lık olabilir. Rapor yazıcıya dökülürken kaç satırdan sonra yeni kağıda geçileceği buradaki tanımlamaya göre belirlenir. Standart olarak 66 seçeneği ekrana gelir fakat kullanıcı isterse değişiklik yapabilir. |
| Yazıcı Ayarı Yapılsın | Seçenek işaretlendiğinde, Windows’un “Yazıcı Ayarları” ekrana gelir. Bu ekranda, tanımlı olan yazıcılar arasından seçim yapılır. Rapor ekrandan alındıktan sonra yazıcıya gönderildiği zaman, tanımlanmış olan yazıcı ayarlarına göre basım yapılır. |
| Nüsha Sayısı | Yazıcıdan alınacak dökümlerde, her sayfadan kaç adet basılacağının belirlendiği alandır. |
| Sıfır Basma | Raporda "sıfır" sayısının görüntülenmesinin istenmediği durumlarda işaretlenmesi gereken alandır. Listelenen kayıtlarda sıfır (0) değerini taşıyan alanlar boş olarak izlenir. |
| Excel Dosya Adı | Ekran ya da yazıcıdan alınacak raporun diske "Excel" formatında bir dosya halinde atılması istendiğinde işaretlenmesi gereken seçenektir. Bu alanda dosyanın hangi dizinde ve hangi isimle oluşturulacağının belirtilmesi gerekir. Excel’in File/Open seçeneği ile Excel'de dosya izlenebilir. |
| Text Dosya Adı | Ekran ya da yazıcıdan alınacak raporun diske "Text" formatında bir dosya halinde atılması istendiğinde işaretlenmesi gereken seçenektir. Bu alanda dosyanın hangi dizinde ve hangi isimle oluşturulacağının belirtilmesi gerekir. Bu dosyaya herhangi bir editör program kullanılarak erişilebilir. |
| HTML Dosya Adı | Ekran ya da yazıcıdan alınacak raporun diske "Html" formatında bir dosya halinde atılması istendiğinde işaretlenmesi gereken seçenektir. Bu alanda dosyanın hangi dizinde ve hangi isimle oluşturulacağının belirtilmesi gerekir. Bu bölümden Excel, Text veya Html formatında oluşturulacak dosyanın doğru ve eksiksiz oluşturulması için tanımlamalar yapıldıktan sonra, raporun tamamının yazıcı ya da ekrandan alınması gerekir. |
| Başlık | Yazıcı ya da ekran dökümleri için rapora genel başlık tanımlanan alandır. "Modül Standart Raporlarında" başlıklar otomatik olarak tanımlı gelir. İstendiğinde bu alandan değiştirilebilir. |
| ![](../../../../../_assets/7ba39f9046a578093326.png) Rapor | Raporun ekran ya da yazıcıdan dökümünün alınması için kısıt ve sıralama tanımlamaları yapıldıktan sonra kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Rapor dökülmeden önce tanımlaması yapılmış olan ön sorgu, genel sorgu, sıralama ve kısıt tanımlamalarının kaydedilmesini, saklanmasını sağlayan butondur. **Örneğin:** Kullanıcının, cari hareket dökümünü her alışında bazı standart kısıt ve sıralama seçeneklerini tanımladığı varsayıldığında, raporu her alışta aynı seçenekleri tekrar tanımlamak zorunda kalmaması için Oku ![](../../../../../_assets/e3223333470668512f5f.jpg) ve Sakla ![](../../../../../_assets/53859e19eb2737b88a17.jpg) butonları kullanılır. Kullanıcı, önce standart kısıt ve sıralama seçeneklerini tanımlayıp daha sonra Sakla ![](../../../../../_assets/53859e19eb2737b88a17.jpg) butonunu kullandığında, bu seçenekleri kaydetmiş olur. Sakla ![](../../../../../_assets/53859e19eb2737b88a17.jpg) butonu ile sadece son yapılan tanımlamalar saklanır. Kullanıcı daha sonra, saklanan kısıt ve sıralama seçenekleri ile rapor almak istediğinde, Oku![](../../../../../_assets/e3223333470668512f5f.jpg) butonunu kullanarak seçeneklerin ekrana getirilmesini sağlayabilir. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Rapor alınması ile ilgili yardım bilgisine ulaşmak için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Raporun ekran ya da yazıcıdan alınmasının vazgeçildiği durumlarda, rapor tanımlama ekranının kapatılmasını sağlayan butondur. |
