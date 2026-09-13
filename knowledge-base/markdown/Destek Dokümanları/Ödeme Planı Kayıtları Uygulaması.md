---
title: "Ödeme Planı Kayıtları Uygulaması"
page_id: "74716796"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Ödeme Planı Kayıtları Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Ödeme Planı Kayıtları Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTg5MTBhZTBjLTZkYmYtNGVmYi05OWI4LWNmYzIxYjc1YjYzOSZsaW5rPWNiZjllZDUwLWI3YzgtNGM2Ny1iZDY5LTM2MWI0MTM0NWUwZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8910ae0c-6dbf-4efb-99b8-cfc21b75b639&link=cbf9ed50-b7c8-4c67-bd69-361b41345e0e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "odeme-plani-kayitlari-uygulamasi_80087916_74716796.html"
source_version: "2022-11-02T14:48:10.810+03:00"
source_bytes: 113826
fetched_at: "2026-09-13T04:24:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ödeme Planı Kayıtları Uygulaması

Ödeme Planı Kayıtları Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Açık hesap satış işlemlerinde borç tutarının cari hareketlere belirli vade, taksit ve tutarda yansıtılması ödeme planı uygulaması ile sağlanmaktadır. Ödeme Planı Kayıtları uygulamasının çalışması için Fatura/Satış Parametreleri-Genel 4 sekmesinde bulunan "C/H vadelere bölünerek geçsin" parametresinin işaretlenmesi gerekmektedir. Uygulanacak ödeme planları Cari/Ödeme Planı Kayıtları ekranından tanımlanmaktadır.
![](../_assets/bce9f0a60b286971c064.png)

Ödeme Planı Kayıtları; Ödeme Planı-1, Ödeme Planı-2 ve Ödeme Planı İzleme olmak üzere 3 sekmeden oluşmaktadır.
Kullanılacak olan ödeme planına bir kod ve açıklama verilir. İşletme şube bilgileri tanımlandıktan sonra kaydedilir. Kaydedilen ödeme kodu grid alandan detayları tanımlanmak üzere çift tıklanarak çağırılır ve Ödeme Planı-2 ekranına geçilir.
![](../_assets/0f1fae3c14a7b3cfabdd.png)
**Vade** **Tipi** alanında, oluşacak ödeme planında vadeleri belirleyecek 6 yöntem bulunur.
Fatura Tarihi, vade tarihini, faturanın kesildiği gün olarak belirlemek amacıyla kullanılır.
Vade Günü, fatura tarihi üzerine gün ekleyerek vade tarihi belirlemek amacıyla kullanılır.
Sabit Gün, ayın belirli bir gününün vade tarihi olarak belirlemek için kullanılır.
Son Gün, vade tarihini, ayın son günü olarak belirlemek için kullanılır.
Son Gün+Vade Günü, ayın son üzerine gün sahasına yazılan değer eklenerek vade tarihi bulmak için kullanılır.
Vade Tarihi+Ayın Son Günü, vade tarihinin bulunduğu ayın son gününü yeni vade tarihi olarak belirlemek için kullanılır.
Vade tarihleri oluşturulurken ilk verilen vade tarihi, diğer vade tarihlerinin oluşturulmasına baz olmaktadır.
**Oran** alanı, fatura toplamının oranlar bazında istenildiği kadar vadeye bölünmesini sağlar. Oran alanında, oluşturulan ödeme planı oranlar toplamının 100 olmasına dikkat edilmelidir.

#### Ödeme Planı İzleme

Oluşturulan ödeme planı Ödeme Planı İzleme ekranı aracılığı ile test edilmektedir.
![](../_assets/4041b46eb3b1d88f1c7b.png)
Örnek ödeme planında fatura toplamının %25'lik kısmı fatura tarihinde, %20'lik kısmı fatura tarihinden 5 gün sonra(22.02 vade tarihi), %20 lik kısmı vadenin olduğu ayın son gününde, %30'luk kısmı ayın son günü üzerinde 15 gün eklenerek bulunan günde ve son olarak %5'lik kısmı bir sonraki ayın sabit 16'sında olacak şekilde planlanmıştır. Bu bilgilerle 17.02 tarihinde girilen fatura için oluşacak ödeme planı aşağıdaki gibi olacaktır.
![](../_assets/43c8e05417774f541e6a.png)

#### Ödeme Planının Fatura Modülünde Kullanımı

Ödeme Planının Fatura Modülünde Kullanımı uygulamasının çalışması için Fatura/Satış Parametreleri-Genel 4 sekmesinde bulunan "C/H vadelere bölünerek geçsin" parametresinin işaretlenmesi gerekmektedir.
Parametre işaretlendiğinde koşul yoksa üst bilgilerde, koşul varsa koşul bilgileri sayfasında ödeme kodu sorgulanmaktadır.
![](../_assets/445277d7405dd4001832.png)![](../_assets/194e285f1fc6a743ce33.png)
Satış faturası ödeme kodu seçilerek girilip toplamlardan Tamam butonuna basıldığında Vadelere Bölme ekranı açılır ve seçilen ödeme planına uygun şekilde fatura vadelere bölünür.
Bu fatura cari hareketlere belirlenen vadede yansır.
![](../_assets/269b96e6b300bc22174e.png)
Koşul uygulaması açık ise ödeme kodu genel koşul kayıtlarından koşula bağlanabilir. Böylece koşulun bağlandığı faturada ödeme planı otomatik oluşacaktır. Proje uygulaması varsa ödeme planı uygulamasının kullanılabilmesi için Fatura/Satış Parametreleri-Genel 4 sekmesinde bulunan "Kayıtlarda Her Satırda Vade Tarihi Sorulsun" parametresi işaretlenmelidir.
