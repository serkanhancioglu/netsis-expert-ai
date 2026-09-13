---
title: "Netsis Cari Muhasebe Açıklama Kayıtları"
page_id: "24753257"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Yardımcı Programlar"
  - "Kayıt / Yardımcı Programlar"
  - "Netsis Cari Muhasebe Açıklama Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / Netsis Cari Muhasebe Açıklama Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTVkMDkwMDBlLTQ5NGItNDdiNi04MWEwLWRjMTJiNTU3NjUxMyZsaW5rPWY3Mjg3MzEyLWQ4YmMtNGVjMy04YTUxLWU0MzMzYzhiYzJmMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5d09000e-494b-47b6-81a0-dc12b5576513&link=f7287312-d8bc-4ec3-8a51-e4333c8bc2f1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-cari-muhasebe-aciklama-kayitlari_47072921_24753257.html"
source_version: "2022-10-05T09:53:37.293+03:00"
source_bytes: 394964
fetched_at: "2026-09-13T04:17:20+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Cari Muhasebe Açıklama Kayıtları

Netsis Cari Muhasebe Açıklama Kayıtları, Genel Bölümü'nde, "Kayıt/Yardımcı Programlar" menüsünün altında yer alır.

![](../../../../_assets/27f876af5617d5bdd374.png)

Netsis Cari Muhasebe Açıklama Kayıtları ekranının yardımı ile, fatura girişi sırasında Cari ve Entegrasyon modülüne atılan açıklama kayıtları kullanıcı tarafından belirlenebilir. Netsis Cari Muhasebe Açıklama Kayıtları ekranında bulunan "Script Kodunuzu Buradan Girebilirsiniz" yazısının üzerine farenin sol tuşu ile tıklandığında, açıklamanın hangi bileşenlerden oluşacağı belirlenir.

![](../../../../_assets/dfb6865304341d4ed434.png)

Netsis Cari Muhasebe Açıklama Kayıtları ekranının üzerinde iken farenin sağ tuşuna tıklandığında görüntülenen "Saha Rehberi" seçeneği, tanımlama yapılmasını sağlar. Fatura Entegrasyon Stok Açıklaması için “Cari Kodu + Belge Numarası + Ekalan2” sahalarının birleşiminden oluşan açıklama aşağıdaki gibi bir script ile yapılabilir.

![](../../../../_assets/e5b0e2f61397dadc744c.png)

Dim Aciklama

Dim Ekalan1

Set qry = NETSISCORE.NetLibDB.GetNewQuery

qry.RecSQL ("SELECT TOP 1 EKALAN1 FROM TBLSTHAR WITH (NOLOCK)

WHERE FISNO = '" & GetProgValue("FATIRS_NO") & "'" &\_

" AND STHAR_FTIRSIP = '" & GetProgValue("FTIRSIP") & "'" &\_

" AND STHAR_ACIKLAMA= '" & GetProgValue("CARI_KODU") & "'")

Ekalan1 = qry.FieldByName("EKALAN1").AsString

qry.Close

Set qry = Nothing

Aciklama = GetProgValue("CARI_KODU")& "FT.MIZ No:" &

GetProgValue("FATIRS_NO") & Ekalan1

RESULT = Aciklama
