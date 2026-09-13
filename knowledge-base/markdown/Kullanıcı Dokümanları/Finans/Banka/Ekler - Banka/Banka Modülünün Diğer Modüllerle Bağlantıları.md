---
title: "Banka Modülünün Diğer Modüllerle Bağlantıları"
page_id: "22806372"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Banka"
  - "Ekler / Banka"
  - "Banka Modülünün Diğer Modüllerle Bağlantıları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / Ekler / Banka / Banka Modülünün Diğer Modüllerle Bağlantıları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ4ZmJmMDMzLTYxNjUtNDJjNS1iMmE1LTRhNDkyYWY0YWJlZSZsaW5rPTk5ODUzMWM3LWEyODUtNDdjNS1hYjdiLTg5ZmRjOTA0NmQ4NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d8fbf033-6165-42c5-b2a5-4a492af4abee&link=998531c7-a285-47c5-ab7b-89fdc9046d86&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "banka-modulunun-diger-modullerle-baglantilari_34224655_22806372.html"
source_version: "2022-12-05T17:02:10.233+03:00"
source_bytes: 3627
fetched_at: "2026-09-13T04:10:39+00:00"
generator: "netsis-scraper 1.0.0"
---
# Banka Modülünün Diğer Modüllerle Bağlantıları

Banka Modülünün Diğer Modüllerle Bağlantıları ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılır.

**Dekont Modülü:** Bankalar ile ilgili işlemler "Genel Dekont Kaydı" bölümünden de yapılır. Sadece, "Vadesiz" ve "Rotatif" hesaplar desteklenir. Dekontun çek/senet ile ilgili işlemlerinde, banka kodunun sorulduğu yerlerde Banka Modülünde hesap kodları sorgulanır.

**Çek/Senet:** Banka kodunun sorulduğu yerlerde, Banka Modülünde hesap kodu sorgulanır. "Teminata Çıkış" için hesap tipi "Teminat" olanların, "Tahsile Çıkış" işleminde ise hesap tipi "Tahsil" olanların seçilmesi gerekir.

Borç çeklerinde banka kodu girişi işaretli ise, banka menüsünden hesap kodu seçilebilir.

**Kasa:** "Kasa Kayıtları" bölümünde "Banka" isimli bir sekme yer alır. Bu alanda "Banka Hesap Kodu" sorgulanır. Bankaya nakit giriş çıkış işlemlerinin yapılmasını sağlar. Bu ekran üzerinden silme işlemi yapılmaz. İptal işlemi için ters kayıt yapılır. "Rotatif" ve "Vadesiz" hesaplar desteklenir.

**Cari:** Banka entegrasyonu, "Ödeme Emirleri" işleminde de desteklenir. Ödeme emri oluşturulacak satıcılar için, grid ekranda cari banka kayıtları sorgulanır. Cari kartlarda ödeme tipi "Havale" ise, cari hesaplara havale emri oluşturulur. Çek ise, borç çeki oluşturulur.

Finasman raporunda da banka ile ilgili rapor alınabilir. Banka Borçlar/Banka Alacaklar işaretli ise, finansman raporuna dahil edilir. Vadesiz ve rotatif hesapların son tutarı ile gelir. Vadesiz için yıllık faiz, rotatif için 3 ayda bir faiz kaydı aktarılır. Vadeli, repo ve kredi hesaplarında vade bitiş tarihleri ve faiz ödeme tarihlerine göre hesaplanıp ekrana getirilir.

**Cari Banka Kayıtları:** Giriş ekranı Cari Modülünde yer alır. Müşterilerle/Satıcılarla cari hesap bazında çalışılan firmaların banka kayıtlarının girildiği bölümdür. Bir cari hesap birden fazla banka ile çalışabilir. Müşteri/Satıcı ile ilgili bir banka işlemi yapılacağı zaman, ilgili cari hesaba ait burada tanımlanan banka hesapları arasından seçim yapılabilir. Default kutucuğu işaretlendiği zaman, ilgili hesap müşteri/satıcı ile ilgili işlemlerde ön değer olarak ekrana getirilir. İstendiğinde, kullanıcı tarafından üzerinde değişiklik yapılabilir.
