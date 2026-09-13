---
title: "Otomatik Seri No Üretme Tanımlamaları"
page_id: "150569070"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Otomatik Seri No Üretme Tanımlamaları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Otomatik Seri No Üretme Tanımlamaları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ4YzMzNDkxLWY3N2UtNGI4Mi1hOTBhLWYwYzUyYzlkOWNiYyZsaW5rPThkY2M5M2RhLTI2ZmItNGRmZC04YmFmLTRkN2U3ZTg4ODgzOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=48c33491-f77e-4b82-a90a-f0c52c9d9cbc&link=8dcc93da-26fb-4dfd-8baf-4d7e7e888839&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "otomatik-seri-no-uretme-tanimlamalari_150569070_150569070.html"
source_version: "2024-09-03T08:20:43.373+03:00"
source_bytes: 382744
fetched_at: "2026-09-13T04:22:40+00:00"
generator: "netsis-scraper 1.0.0"
---
# Otomatik Seri No Üretme Tanımlamaları

Stok seri kodlarının program tarafından otomatik olarak üretilmesi istenen durumlarda, kodların belli bir formüle göre, düzen içinde yaratılması için Otomatik Seri No Üretme Tanımlamaları ekranı kullanılır. Otomatik seri no üretme tanımları ekranı ile sabit, değişken ve script ile serilerin nasıl oluşturulacağına karar verilebilir.

**Otomatik** **Üretim** **Kodu:** Otomatik seri kodu üretilmesi için kod girilen alandır. Farklı stok grupları için, farklı formüllerle birden fazla seri kodu üretme tanımı yapılabilir.

- **Sabit:** Oluşturulacak seri yapılandırma kodu başlangıç karakterinin, girilen sabit değerle başlaması istendiğinde "Sabit" seçeneğinin işaretlenmesi gerekir.
- **Değişken:** Otomatik seri kodunun SQL cümlesinden dönen sonuç ile üretilmesi istendiğinde "Değişken" seçeneğinin işaretlenmesi gerekir.
- **Script:** Oluşturulacak seri kodunun Script ifadesi ile oluşturulması için kullanılan seçenektir.

*Not:* *Script* *seçeneği Netsis* *9.0.36* *ve* *üzeri* *versiyonlarda* *desteklenmektedir.*

**Başlangıç Numarası:** Otomatik seri kodunun, başlangıç karakterinden sonraki bölümde yer alacak sıra numarasının başlangıç değerini ifade eden alandır.

**Uzunluk:** Otomatik seri kodunun kaç karakterden oluşacağının belirlendiği alandır.

**Aktif:** Otomatik üretim kodunun geçerli olup olmadığını ifade eden alandır. Program tarafından kod üretilirken, tanımlanan kod parametresinin dikkate alınmaması istendiğinde aktif seçeneğinin işaretlenmemesi gerekir.

**Başlangıç** **Karakteri:** "Sabit" seçeneği işaretlendiğinde seri kodları, belirtilen sabit değer ile başlar." Değişken" seçeneği işaretlendiğinde ise başlangıç karakteri ekranına, bir SQL cümlesi yazılarak değişken bir şekilde başlangıç karakteri oluşturulması sağlanır. Script seçeneğinde ise dinamik kodlama ifadesi ile oluşturulan seri kodu Result değişkenine atanarak serinin oluşturulması sağlanır.

"Başlangıç Karakteri" alanında iken, sağ tuş ile ekrana gelen "Stok Kodu Değişkeni" seçeneğine tıklanarak imlecin bulunduğu yere "($StokKodu)" ifadesi eklendiğinde ve bu şekilde başlangıç karakteri verildiğinde, seri numarası üretileceği sırada içinde bulunulan stok kodu bilgisinin, üretilecek seri numarasının başlangıç karakteri olarak yazılır.

**Test:** Girilen formüle uygun olarak oluşan ilk seri kodunun görüntülenmesi için kullanılan butondur.

*Not:* *Başlangıç* *Karakteri* *alanında* *eğer* *Stok* *Kodu* *Değişkeni* *eklendiyse* *test* *butonu* *çalışmayacak* *ve* *aşağıdaki* *uyarı ekrana gelecektir. Bu değişkenin tanımlandığı durumlarda, seri kodun kullanılacağı ekranlardan test* *işlemi* *gerçekleştirebilir.*

![](../_assets/89fa0bf9e23e6f7b228c.png)

**Geçerli** **Stoklar**

Geçerli Stoklar, program tarafından üretilecek seri kodlarına ait tanımlanan formülün, hangi stoklar için geçerli olacağı ile ilgili tanımlamalar yapılan sekmedir.

Otomatik seri kodu oluşturulacağı zaman, ilgili stok için mevcut otomatik kod üretim tanımlarına bakılır. Eğer birden fazla aktif kod üretme tanımı varsa ilk bulunan tanıma göre kod üretilir.

![](../_assets/ab602639b8d7ff893e96.png)

**Otomatik** **Seri** **Kodu** **Üretme** **Tanımlamalarında** **yapılan** **tanımlamanın** **geçerli** **olması** **için;** **Stok** → **Kayıt**→ **Stok** **Kartı** **Kayıtları** → **Seri** **Takibi** → **"Otomatik** **Hesaplansın"** **seçeneğinin** **işaretlenmesi** **gerekir.**

![](../_assets/f6cd2a65747fcf532424.png)

**Örnek** **Tanım-1** **(Sabit)**

![](../_assets/75593f0924e4923a5d8d.png)

![](../_assets/0b394dde978032deac32.png)

**Örnek** **Tanım-2** **(Değişken)**

![](../_assets/1c45aee0c89d494c4784.png)

DECLARE @RND NVARCHAR(8) = LEFT(REPLACE(CONVERT(NVARCHAR(36), NEWID()), '-', ''), 8); DECLARE @DATE NVARCHAR(10) = REPLACE(CONVERT(VARCHAR(10), GETDATE(), 103), '/', '');
SELECT
'S' +
RIGHT('00000000' + REPLACE(**($StokKodu),** '.', ''), 8) + CAST(SUBE_KODU AS VARCHAR) +
@DATE + @RND
FROM
TBLSUBELER
INNER JOIN NETCONTEXT ON SUBE_KODU = V$SUBE_KODU

![](../_assets/7846e0a0bb1e62ee0c74.png)

*Otomatik* *üretilen* *seri* *kodu* *ekran* *görüntüsündeki* *gibidir.*

**Örnek** **Tanım-3** **(Script)**

![](../_assets/21b2ff85ca7abb86695e.png)

Dim GrupKodu
set rs = NETSISCORE.NetLibDB.GetNewQuery
query = "SELECT GRUP_KODU FROM STSABIT WHERE STOK_KODU='"&($StokKodu)&"'"
rs.RecSql(query)
GrupKodu = rs.FieldByName("GRUP_KODU").AsString Result = GrupKodu
set rs = Nothing

![](../_assets/eeea47cbb4783f6b746b.png)

*Otomatik* *üretilen* *seri* *kodu* *ekran* *görüntüsündeki* *gibidir.*

**Örnek** **Tanım-4** **(Script)**

Aşağıdaki tanımda Result değişkenine atanan ilk iki karakter date fonksiyonundan dönen sonucun yıl bilgisini içeren son iki karakteridir. Random sınıfından üretilen 8 karakter uzunluğundaki değer, yıl bilgisinden sonra gelmektedir. Serinin sonundaki değer ise daha önce aynı otomatik üretim kodu kullanılarak oluşturulan seri numarasının 1 artırılarak elde edilen değeridir.

![](../_assets/28d043a95f375dadbeaa.png)
*Randomize*

*Dim* *chars*

*chars* = *"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"*

*Dim length*

*length* = *8*

*Dim* *i,* *randomIndex,* *randomString* *randomString* = ""

*For* *i =* *1* *To* *length*

*randomIndex* = *Int(Len(chars)* \* *Rnd)* + *1*
*randomString* = *randomString* & *Mid(chars,* *randomIndex,* *1)*

*Next*

*Dim* *result*

*result* = *Mid(Date,* *9, 2)* + *randomString*

![](../_assets/b4dd8064a8b80ca58381.png)

*Otomatik* *üretilen* *seri* *kodu* *ekran* *görüntüsündeki* *gibidir.*
