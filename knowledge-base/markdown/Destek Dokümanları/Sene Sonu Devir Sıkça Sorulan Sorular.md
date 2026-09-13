---
title: "Sene Sonu Devir Sıkça Sorulan Sorular"
page_id: "147554624"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Sene Sonu Devir Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Sene Sonu Devir Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdmOGU0ZmU4LWE5YzAtNDMwNS1hMzNhLTFiYjE2MGIxOTU5OSZsaW5rPWQ0N2Y5MDBhLWE0MTEtNGNlOC1iYzAyLTFmNmEwN2MyNmMzMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7f8e4fe8-a9c0-4305-a33a-1bb160b19599&link=d47f900a-a411-4ce8-bc02-1f6a07c26c30&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sene-sonu-devir-sss_147554624_147554624.html"
source_version: "2024-08-05T09:21:32.427+03:00"
source_bytes: 2858271
fetched_at: "2026-09-13T04:22:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sene Sonu Devir Sıkça Sorulan Sorular

**Soru 1: Yeni yıl kopyalama işleminde "The affinity mask specified conflicts with the IO affinity mask specified. Use the override option to force this configuration.(NetsisMS- 42000,5834) DLLName=D:\\Netsis\\Enterprise7\\Ortak\\NetDBCrt.DLL" uyarısı alındığında ne yapılmalıdır?**

-Sql server özelliklerindeki Processors menüsünden "Automaticaly set processor affinity mask for all processors" ve "Automaticaly set I/O mask for all processors" parametreleri enable edilerek, tekrar yeni yıl kopyalama çalıştırılır.

![](../_assets/d3c99d530d07fc6291f4.png)

-Sistem trigger nesneleri grubunda bulunan aşağıdaki trigger'ın, exec sp_configure 'show advanced options', 1 cümlesinin çalışmasını engellediği için trigger disabled edilerek yeni yıl kopyalama işlemi tamamlandıktan sonra tekrar enable edilebilir.

```text
CREATE TRIGGER [Stop_XP_CommandShell] ON ALL SERVER     FOR ALTER_INSTANCE   AS     BEGIN      DECLARE @SQL NVARCHAR(4000)   DECLARE  @Data xml    SET @Data = EVENTDATA();    BEGIN TRY         SET @SQL = @Data.value('(/EVENT_INSTANCE/TSQLCommand/CommandText)[1]','nvarchar(4000)')   END TRY        BEGIN CATCH   END CATCH     IF (CHARINDEX('sp_configure', @SQL) > 0)  BEGIN     WAITFOR DELAY '23:59:50'  END   END
```

GO

![](../_assets/00b5cd2bddced305bec6.png)

**Soru 2: Yeni yıl kopyalama işleminde " DATAISMI..TBLFATUIRS (DBQuery : FindQSQL : Delete From DATAISMI..TBLFATUIRS Where (TARIH \<= '12/31/2014') OR(TIPI = '6' AND FTIRSIP IN ('3', '4') ) Internal Query Processor Error: The query processor encountered an unexpected error during execution.(NetsisMS-42000,8630)) 30.12.2014 15:10:43 Operation aborted" uyarısı alındığında ne yapılmalıdır?**

Sql server da ilgili database üzerinde sağ klik özelliklerde SINGLE_USER seçilir Dbcc checkdb('TBLFATUIRS',repair_rebuild) komutu çalıştırılır. Data sonra MULTI_USER a geri çekilir. Tekrar yeni yıl kopyalama yapılabilir. (Öncesinde data yedeği alınması önerilir)

![](../_assets/56e9bbc88d8cb3aa4b7a.png)

**Soru 3: Yeni yıl kopyalama işleminde "Ad hoc update to system catalogs is notsupported" uyarısı alındığında ne yapılmalıdır?**

Sql Server' da aşağıdaki cümle çalıştırıldıktan sonra yeni yıl kopyalama işleminedevam edilir.

sp_configure 'show advanced options',1 GO

RECONFIGURE WITH OVERRIDE GO

sp_configure 'allow updates', 0 GO

RECONFIGURE WITH OVERRIDE

**Soru 4:** **Yeni yıl kopyalama işleminde (Oracle) "NLS_SORT DEĞERİ BINARY** **OLMALIDIR" uyarısı alındığında ne yapılmalıdır?**

Başlat\>Çalıştır\>Regedit HKEY_LOCAL_MACHINE\\SOFTWARE\\ORACLE\\HOME 0 altında NEW - STRING VALUE denilerek NLS_SORT DEĞERİNE BINARY yazılıp kaydedilmelidir. Ardından yeni yıl kopyalama işlemine devam edilebilir.

**Soru 5: Yeni yıl kopyalama işleminde "The default full-text language is not supported by the full-text** **search component.** **(NetsisMS-42000,5841) DLLName=** **C:\\Netsis\\RCEnterprise\\Ortak\\NetDBCrt.DLL " uyarısı alındığında ne yapılmalıdır?**

Sql server özelliklerinde advanced kısmında Default language "English" ve Default full-text Language "1033" olup olmadığı kontrol edilir. Farklı ise bu ayarlar "1033" olacak şekilde düzenlenir ve Sql Server ve Sql Server Full-text servisi restart edilir. Sonrasında Yeni yıl kopyalama işlemine devam edilir.

**Soru 6: Yeni yıl kopyalama işleminde "Foreign Key : FK_MGSTHAR_TBLSTHAR Operation Type : Delete Related Tables : MGSTHAR \<-\> TBLSTHAR SQL : Alter Table TEST2016..MGSTHAR Add constraint FK_MGSTHAR_TBLSTHAR FOREIGN KEY (STRANO) REFERENCES TEST2016..TBLSTHAR (INCKEYNO) ON DELETE CASCADE" uyarısı alındığında ne yapılmalıdır?**

Eski Netpos uygulaması kullanılıyor ise yeni yıl kopyalama işleminden önce Shopsdevir.exe dosyasının çalıştırılması gerekmektedir. Sonrasında yeni yıl kopyalama işlemi yapılmalıdır.

**Soru 7: Yeni yıl kopyalama işleminde "Aktif şirketin yedeği alınamadı. Veritabanı yedeği için başka dizin girdiyseniz dizin geçerliliğini kontrol ediniz" uyarısı alındığında ne yapılmalıdır?**

Sql server özelliklerinde Log On sekmesinde Local System Account seçilip kaydedilir. Sql servisi yeniden başlatılır. Daha sonra yeni yıl kopyalama işlemine devam edilir.

![](../_assets/b6f0d7314799eb71d3ed.png)

**Soru 8: Yeni yıl kopyalama işleminde (Oracle) "NLS_DATE_LANGUAGE değeri TURKISH olmalı.** **Operation aborted" uyarısı alınıyorsa ne yapılmalıdır?**

Başlat\>Çalıştır\>Regedit HKEY_LOCAL_MACHINE\\SOFTWARE\\ORACLE\\KEY_ORACLIENT11G_HOME1 anahtarında "NLS_LANG" değeri "TURKISH_TURKEY.TR8MSWIN1254" olmalıdır. (Oraclient10g ya da client olarak da geçiyor olabilir. NLS_LANG olarak aratılabilir)

![](../_assets/85c9a6aa2533eb5f3ce4.png)

**Soru 9: Yeni yıl kopyalama işleminde "Yedeği alınan şirket ... ismiyle sisteme geri dönülemedi Operation aborted" uyarısı alındığında ve Sql Server' dan bu yedek restore edilmek istendiğinde aşağıdaki uyarı alınıyorsa ne yapılmalıdır?**

![](../_assets/e081b98be07f1649054f.png)

Uyarıda yazan klasörün salt okunur ya da disk üzerinde az yer kaplaması için sıkıştırılmış formatta olup olmadığı kontrol edilir. (compress content to save disk space işaretliyse, işaret kaldırılmalıdır)

![](../_assets/1771e8b0a10a1426030d.png)

Bu yöntem ile çözüm sağlanamaması durumunda kullanılan datanın yedeği alınarak yeni oluşturulacak data ismi ile tekrar veri tabanı üzerinde dönülür. Yeni yıl kopyalama işleminde de yeni dönülen data ismi verilerek işlemlere devam edilir. Böylece sistem data kopyalama adımını geçerek verilerin silinmesine başlayacaktır.

**Soru 10: Yeni** **yıl kopyalama işleminde "User does not have permission to perform this** **action.." uyarısı alınıyorsa ne yapılmalıdır?**

Registry' de yazan veritabanı kullanıcısının (TEMELSET) sys admin yetkisinin olmamasından kaynaklanmaktadır. Sql' de Logins bölümünden "Sys Admin" yetkisi verildikten sonra programa tekrar giriş yapılarak yeni yıl kopyalama işlemine devam edilebilir.

**Soru 11: Yeni yıl kopyalama işleminde "…** [**Subquery returned more than 1 value.This is not permitted when the subquery follows =,!=,\<,\<=,\>,\>= or when the subquery is used as an expression**](https://stackoverflow.com/questions/16053907/subquery-returned-more-than-1-value-this-is-not-permitted-when-the-subquery-foll)**. The statement has been terminated" uyarısı alındığında ne yapılmalıdır?**

![](../_assets/2701fef53b45e83e856c.png)

İlgili tablosu altında Netsis' in triggerları dışında farklı bir trigger olabilir kontrol edilmelidir. Eğer varsa disable edilip işleme devam edilmelidir.

**Soru 12: Serili Stok devrinde "Seri bilgisi olmayan stok hareketi bulundu. Stok kodu: S01 inckeyno: 29716" uyarısı alındığında ne yapılmalıdır?**

TBLSERITRA tablosunda uyarıda verilen INCKEYNO ile eşleşen kayıt yok anlamına gelir. Stok bakiyesi ve seri bakiyesi tutuyordur fakat sonradan sene ortasında Seri uygulamasına geçilmiş veya düzenli seri takibi yapılmamış olabilir. Bu durumda Serili Stok devrinde stok ve seri bakiyesi ayrı atılsın parametresi işaretlenerek devir yapılabilir.

**Soru 13:** **İş emri devrinde "Alter Table TEST2024..TBLISEMRI Add constraintTBLISEMRI_FKEY3 FOREIGN KEY (ASORTIKOD) REFERENCES NET2016..TBLASORTIMAS(ASORTIKOD) There is already an object named 'TBLISEMRI_FKEY3' in the database.(NetsisMS-42S01,2714) Could not create constraint. See previous errors.(NetsisMS-42000,1750)" uyarısı alındığında ne yapılmalıdır?**

Eski yıl şirketinde TMPFOREIGNTBL tablosu varsa bu tablonun drop edilmesi(silinmesi) gerekmektedir. Bu tablo constraintlerin geçici olarak tutulduğu devirden sonra kendiliğinden silinen geçici bir tablodur.

**Soru 14: Banka devrinde "Cannot insert explicit value for identity column in table 'TBLBNKLOGTRA' when IDENTITY_INSERT is set to OFF**" **uyarısı alındığında ne yapılmalıdır?**

TBLBNKLOGTRA tablosuna eklenmiş özel bir kolon sebebi ile olabilir. Bu kolonkaldırılıp, view'i de alter edildikten sonra banka devrine devam edilir.

**Soru 15:** **Muhasebe kapanış fişi devrinde "Violation of PRIMARY KEY constraint 'TBLMUHMAS_PKEY'. Cannot insert duplicate key in object 'dbo.TBLMUHMAS'" uyarısı alındığında ne yapılmalıdır?**

TBLMUHMAS tablosunun

PKEY’i \[YIL_KODU\],\[AY_KODU\],\[MAS_FISNO\] alanlarını kontrol etmektedir, bu değerlerde mükerrer bir kayıt atmaya çalışıyor olabilir. Bu değerlerde bir fiş olup olmadığını kontrol edebilirsiniz. Ayrıca ilgili ay için tarih bazında yeniden numaralandırma yapılarak tekrar kapanış fişi oluşturma işlemi yapılabilir.

**Soru 16:** **Maliyet türü FIFO olan şubeli yapıdaki şirkette stok devir işleminde "Devir kayıtları detaylandırılsın" parametresi gelmiyorsa ne yapılmalıdır?**

Stok parametre kayıtlarında lokal depo uygulaması ve esnek yapılandırma parametreleri kapalı olmalıdır.

**Soru 17: Merkez şubede banka devri ekranında devir baz tarihi ve devir tarihi alanlarında 29.12.1989 gibi bir tarih geliyorsa, (devir baz tarihine yılın son günü, devir tarihine sonraki yılın ilk günü gelmesi gerekir) ne yapılmalıdır?**

Merkez şubede muhasebe parametrelerinde yer alan mali başlangıç yıl 0 olarak kaldı ise düzeltilip tekrar işlem yapılabilir.

**Soru 18:** **Muhasebe kapanış fişinin bakiye vermesi durumunda ne yapılmalıdır?**

Mizana bakılarak bakiye veren hesaplar tespit edilir. Bu hesapların TBLMUPLANSUBE tablosunda olup olmadığı kontrol edilir. Eğer olmayan kayıt var ise insert edilip yevmiye kontrol çalıştırılır. Bu yapılan çalışmalara rağmen mizan bakiye vermeye devam ediyorsa TBLMUHFIS tablosunda olup TBLMUPLAN tablosunda olmayan kayıt olabilir. (SELECT HES_KOD FROM TBLMUHFIS WHERE HES_KOD NOT IN (SELECT HESAP_KODU FROM TBLMUPLAN) Bu kayıtlar tespit edilip TBLMUPLAN, TBLMUPLANEK ve TBLMUPLANSUBE tablolarına kayıtlar eklendikten sonra tekrar yevmiye kontrol çalıştırıp kapanış fişi tekrar oluşturulabilir.

**Soru 19: Cari devrinde kısıt sekmesinde cari rehberinin boş gelmesi durumunda ne yapılmalıdır?**

32767 nolu şubenin merkez işaretli olmaması durumunda cari rehberi boşgelmektedir. Merkez parametresi işaretlenmelidir.

**Soru 20: Cari devir sonucunda işlem tamamlanmıştır uyarısı alınmasına rağmen yeni sene şirketinde cari hareket kayıtlarında şubeler bazında devir hareketleri görülmüyorsa ne yapılmalıdır?**

Cari parametre kayıtlarında cari kullanım tipi "Tüm cari hareketleri" seçili olarak devir yapılmış olabilir. Bu durumda devir hareketleri 32767 nolu şubede oluşacaktır. 32767 nolu şubede Cari Parametreleri, Cari Kullanım Tipi "İşletme/Şirket/Şube" seçildikten sonra cari devir tekrar yapılmalıdır.

**Soru 21: Cari devirde döviz tarihi alanı pasif geliyorsa** **ne yapılmalıdır?**

32767 numaralı şube için Yardımcı programlar\> Şirket Şube Parametreleri "Döviz uygulaması parametresi" açılmalıdır.

**Soru 22: Serisiz stok devri yapılmasına ve stoklarda seri parametreleri işaretli olmamasına rağmen bazı stokların hareketlerinin yeni sene şirketine devredilmemesi durumunda** **ne yapılmalıdır?**

Herhangi bir sebepten seri uygulaması açılıp sonra kapatılmış olabilir bu sebeple E değer kalmış olabilir. TBLSTSABIT tablosundaki GIRIS_SERI ve CIKIS_SERI sahalarında "E" değeri olmasından kaynaklanmaktadır. Bu saha "H" olarak güncellenmelidir.

**Soru 23: Stok devri sırasında bazı stoklar için "şimdiki aralığın dışında inckeyno=0" uyarısı alınıyorsa** **ne yapılmalıdır?**

İlgili stokların hareketlerinde (TBLSTHAR tablosunda STHAR_NF ve STHAR_IAF alanlarında) 10 hanenin üzerinde veya eksi değerli kayıtlar olabilir. Reel fiyatlar ile güncellenmelidir.

**Soru 24: Banka devri sonrasında eski sene şirketindeki bakiyesi ile yeni sene şirketindeki bakiye arasında kuruş farkı oluşuyor ne yapılmalıdır?**

32767 numaralı şube için TBLKULLANP tablosunda INTERNAL kullanıcısı olmadığından kaynaklanabilir. İlgili tabloya ilgili şube için INTERNAL kullanıcısı insert edilmelidir.

**Soru 25: Cari Hareket Döviz Tiplerine Göre cari devir yapılması durumunda eski sene şirketinde hesaplatılan kur farkı kayıtları yeni sene şirketine nasıl aktarılabilir?**

DEVIR/YASLANDIRMALICARI_KURFARKI_DEVREDILSIN özel parametresinin tanımlı olması gerekmektedir.

**Soru 26: Yeni yıl kopyalama işleminde RichEdit line insertion error uyarısı alınıyorsa ne yapılmalıdır?**

Yeni yıl kopyalama ekranı için parametre kayıtları ekranında herhangi bir dinamik kodlama yazılmış mı kontrol edilebilir, devir.dll dosyasının güncel ve engellemesinin olmadığı da kontrol edilmelidir.

**Soru 27: Yeni yıl kopyalama işleminde ALTER TABLE AAA2024..TBLSIPAMASSAHAEK ADD CONSTRAINT TBLSIPAMASSAHAEK_FKEY1 FOREIGN KEY (SUBE_KODU,FTIRSIP,FATIRS_NO,CARI_KODU) REFERENCES AAA2024..TBLSIPAMAS (SUBE_KODU,FTIRSIP,FATIRS_NO,CARI_KODU) ON DELETE CASCADE ON UPDATE CASCADE mesajı alınmaktadır,** **ne yapılmalıdır?**

9.0.55 ve üzeri setlerde sorun giderilmiştir.

**Soru 28:** **Yeni yıl kopyalamada "Attempt to fetch logical page in database 14 failed. It belongs to allocation unit...Bağlantı başarısız oldu" uyarısı alınmaktadır,** **ne yapılmalıdır?**

İletilen hata mesajı SQL kaynaklı bir uyarıdır. Veri tabanı nesnelerinde bozulma olabilir. İnternet üzerinden çözümler incelenebilir.

**Soru 29: Yeni şirkette bazı ihracat dosyaları görünmemektedir sebebi ne olabilir?**

Dış ticaret dosyaları yeni yıl kopyalama işlemi ile yeni sene şirketine aktarılmaktadır. Kapalı olmayan ihracat dosyalarının aktarılmamasının sebebi yeni yıl kopyalama işlemi sonrasında eski şirkette dosyaların açılmasından kaynaklanır. Yeni şirkette ilgili dosya verileri tekrar girilmelidir.

**Soru 30: Yeni yıl kopyalama işlemi yapılırken ekran donmaktadır?**

Sistem trigger nesneleri grubunda bulunan aşağıdaki trigger'ın, exec sp_configure 'show advanced options', 1 cümlesinin çalışmasını engellediği için trigger disabled edilerek yeni yıl kopyalama işlemi tamamlandıktan sonra tekrar enable edilebilir.

```text
CREATE TRIGGER [Stop_XP_CommandShell] ON ALL SERVER     FOR ALTER_INSTANCE   AS     BEGIN      DECLARE @SQL NVARCHAR(4000)   DECLARE  @Data xml    SET @Data = EVENTDATA();    BEGIN TRY         SET @SQL = @Data.value('(/EVENT_INSTANCE/TSQLCommand/CommandText)[1]','nvarchar(4000)')   END TRY        BEGIN CATCH   END CATCH     IF (CHARINDEX('sp_configure', @SQL) > 0)  BEGIN     WAITFOR DELAY '23:59:50'  END   END
```

GO

![](../_assets/00b5cd2bddced305bec6.png)

**Soru 31: Yeni yıl kopyalamada NSP_BEFOREDEVIR expects parameter @ESKISIRKET uyarısı alınması durumunda ne yapılmalıdır?**

İlgili uyarı devir.dll in yeni setlerden alınıp eski set kullanımı durumunda alınmaktadır. Eski set kullanımına devam edilecek ise NSP_AFTERDEVIR ve NSP_BEFOREDEVIR drop edildikten sonra işlem yapılmalıdır.

**Soru 32: Banka devrinde aşağıdaki şekilde Cannot insert duplicate key row in object 'dbo.TBLBNKHESTRA' with unique index 'TBLBNKHESTRA_IND_8'.** **uyarısı alınıyor, ne yapılmalıdır?**

DBQuery : xqTran SQL : INSERT INTO AAA..TBLBNKHESTRA( TARIH, NETHESKODU,HARTIPI,HARTURU,EFFEKTIFTARIH,FAIZORAN,BA,PLASIYERKODU,PROJEKODU,ENTEGREFKEY,INCKEYNO,TUTAR,DOVIZTIPI,DOVIZTUTAR,ACIKLAMA,BELGENO,KAYITYAPANKUL,KAYITTARIHI,SUBE_KODU,YEDEK1,YEDEK2,YEDEK4,YEDEK5,YEDEK6,YEDEK7,YEDEK8,YEDEK9,YEDEK10,YEDEK11,YEDEK12,YEDEK13,YEDEK14,YEDEK15,YEDEK16,ONAYTIPI,ONAYNUM,BNKKSTINCKEYNO,LIBORORAN,SPREADORAN,IHRACAT,TAKSIT,DONEM,HANGITAKSIT,TAKSITTUTAR,TAKSITDOVTUTAR,KALANTUTAR,KALANDOVTUTAR , VADETARIH, YEDEK3,OTOINCKEYNO ) SELECT BNKHESTRA.TARIH , BNKHESTRA.NETHESKODU,BNKHESTRA.HARTIPI,BNKHESTRA.HARTURU,BNKHESTRA.EFFEKTIFTARIH,BNKHESTRA.FAIZORAN,BNKHESTRA.BA,BNKHESTRA.PLASIYERKODU,BNKHESTRA.PROJEKODU,BNKHESTRA.ENTEGREFKEY,BNKHESTRA.**INCKEYNO+1511727776**,BNKHESTRA.TUTAR,BNKHESTRA.DOVIZTIPI,BNKHESTRA.DOVIZTUTAR,BNKHESTRA.ACIKLAMA,BNKHESTRA.BELGENO,BNKHESTRA.KAYITYAPANKUL,BNKHESTRA.KAYITTARIHI,BNKHESTRA.SUBE_KODU,BNKHESTRA.YEDEK1,BNKHESTRA.YEDEK2,BNKHESTRA.YEDEK4,BNKHESTRA.YEDEK5,BNKHESTRA.YEDEK6,BNKHESTRA.YEDEK7,BNKHESTRA.YEDEK8,BNKHESTRA.YEDEK9,BNKHESTRA.YEDEK10,BNKHESTRA.YEDEK11,BNKHESTRA.YEDEK12,BNKHESTRA.YEDEK13,BNKHESTRA.YEDEK14,BNKHESTRA.YEDEK15,BNKHESTRA.YEDEK16,BNKHESTRA.ONAYTIPI,BNKHESTRA.ONAYNUM,BNKHESTRA.BNKKSTINCKEYNO,BNKHESTRA.LIBORORAN,BNKHESTRA.SPREADORAN,BNKHESTRA.IHRACAT,BNKHESTRA.TAKSIT,BNKHESTRA.DONEM,BNKHESTRA.HANGITAKSIT,BNKHESTRA.TAKSITTUTAR,BNKHESTRA.TAKSITDOVTUTAR,BNKHESTRA.KALANTUTAR,BNKHESTRA.KALANDOVTUTAR , (case when LogTra.odeplan='E' then (SELECT MAX(odemetarih) FROM tblbnkodeplan WHERE hesacreferansno=logtra.referansno and netheskodu=logtra.netheskodu) else BNKHESTRA.VADETARIH end) VADETARIHI, 1, 'H' FROM TBLBNKHESTRA BNKHESTRA LEFT OUTER JOIN TBLBNKLOGTRA LOGTRA ON (BNKHESTRA.ENTEGREFKEY=LOGTRA.ENTEGREFKEY AND BNKHESTRA.NETHESKODU=LOGTRA.NETHESKODU ) LEFT OUTER JOIN TBLBNKLOGTRA LOGKAPAMA ON (BNKHESTRA.NETHESKODU=LOGKAPAMA.NETHESKODU AND LOGKAPAMA.IslemTipi=7 AND LOGKAPAMA.YEDEK15=LOGTRA.REFERANSNO AND (LOGKAPAMA.EFFEKTIFTARIH\<='12/31/2022') and (LOGKAPAMA.VADETARIH \<='12/31/2022') ) where (((BNKHESTRA.vadetarih is not null) and ((((LOGTRA.odeplan='H') or (LOGTRA.odeplan is null)) and (BNKHESTRA.vadetarih \> '12/31/2022')) or ((LOGTRA.odeplan='E') and ('12/31/2022'\<(SELECT MAX(odemetarih) FROM TBLbnkodeplan WHERE HESACREFERANSNO=LOGTRA.REFERANSNO AND NETHESKODU = LOGTRA.NETHESKODU)))) ) or ((BNKHESTRA.vadetarih is null) and (BNKHESTRA.Tarih \> '12/31/2022'))) and ( ((LOGTRA.ISLEMTIPI=9 or LOGTRA.ISLEMTIPI=8) and (LOGTRA.EFFEKTIFTARIH\>'12/31/2022') and (LOGTRA.VADETARIH \> '12/31/2022')) or (LOGTRA.ISLEMTIPI\<\>9 AND LOGTRA.ISLEMTIPI\<\>8) or (LOGTRA.ISLEMTIPI IS NULL)) AND LOGKAPAMA.REFERANSNO IS NULL and BNKHESTRA.netheskodu\>='101-02-004' and BNKHESTRA.netheskodu\<='101-02-004'

Cannot insert duplicate key row in object 'dbo.TBLBNKHESTRA' with unique index 'TBLBNKHESTRA_IND_8'. The duplicate key value is (\<null\>).(NetsisMS-23000,2601)

Arithmetic overflow occurred.(NetsisMS-01000,3606) The statement has been terminated.(NetsisMS-01000,3621)

Yeni sene şirketine devir yapılır iken, INCKEYNO sahasını TBLBNKHESTRASIRA tablosundan alıyor. TBLBNKHESTRASIRA tablosundaki NEXTINCKEYNO sahası, mevcut INCKEYNO sahasında yazan rakamdan bir büyük olmalıdır. Örn: TBLBNKHESTRA tablosundaki max inckeyno 134 ise, TBLBNKHESTRASIRA tablosundaki NEXTINCKEYNO alanı 135 olmalıdır.

SELECT MAX (INCKEYNO) FROM TBLBNKHESTRA (cümlesini çalıştırılıp maksimum INCKEYNO bulunur.)

SELECT \* FROM TBLBNKHESTRASIRA

UPDATE TBLBNKHESTRASIRA SET NEXTINCKEYO= 'INCKEYNO+1' (bir önceki cümleden bulunan sayının bir fazlası)

**Soru 33: Yeni yıl kopyalama menüsü gelmemesinin nedeni nedir?**

Yeni yıl kopyalama menüsü merkez işletme merkez şube altında gelmektedir.

**Soru 34: Yeni yıl kopyalama sonrasında aynı e-belge birim kodu kullanıldığında yeni şirkette belge numaralarında çakışma yaşanır mı?**

Fatura e-belgeleri yeni şirkete aktarılmamaktadır. Bu yüzden aynı belge numarası kullanılabilir fakat irsaliyeler devrediliyorsa aynı seri numarası kullanımında eski belgelerde mevcut olacağından sıralı gitmeyecektir. Yeni seri kullanımı ya da EIR025000000001 gibi seri numarası yanına 3 karakterin farklılaştırılması sağlanabilir. Böylece resmi fatura numarası EIR2025000000001 oluşacağı için gönderimde sıkıntı yaşanmayacaktır.

**Soru 35: Yeni yıl kopyalamada " TRIM is not a recognized built-in function name" uyarısının sebebi nedir?**

Devir.dll dosyası eski kalmış olabilir güncellenip tekrar kontrol edilebilir.

**Soru 36: Yeni yıl kopyalamada unable to find index entrey index ID 1, of table ZZZ, in database ZZZ....** **run DBCC CHEKDB or DBCC CHECKTABLE uyarısı alınması durumunda ne yapılmalıdır?**

DBCC CHECKTABLE(table_name ,REPAIR_REBUILD ) komutu çalıştıralım sorun düzelmez ise data kaybı olma olasılığına karşı datanın yedeği alınıp aşağıdaki komutun çalıştırılabilir.

DBCC CHECKTABLE(table_name ,REPAIR_ALLOW_DATA_LOSS)

Yukarıdaki işlemleri yapıp sql server da ilgili database üzerinde sağ klik özelliklerde SINGLE_USER seçilip yeni yıl kopyalama işlemi yapıldıktan sonra tekrar MULTIUSER'a çekilir.

**Soru 37: Yeni yıl kopyalamada mali başlangıç yılı dikkate alınsın parametresi hangi durumda işaretlenir?**

Muhasebe modülünde parametrelerde mali başlangıç ayı 1' den farklı olan şirketler için işaretlenmesi gereken parametredir. Bu parametre işaretlendiğinde Yeni Yıl Kopyalama ve modül bazında devirler özel döneme göre yapılacaktır.

**Soru 38: Yeni yıl kopyalama işleminde Invalid object name TBLEIMZAREG uyarısı alınması durumunda ne yapılmalıdır?**

NETSIS veri tabanı altında TBLEIMZAREG tablosunun olup olmadığı kontrol edilmelidir, mevcut değil ise oluşturulmalıdır.

**Soru 39: Stok devri tüm şubeler için toplu olarak yapılabilir mi?**

Her şube için ayrı ayrı yapılmalıdır.

**Soru 40: Dövizli stok devri için kontrol edilmesi gerekenler nelerdir?**

Dövizli stok devri için muhasebe parametrelerindeki FAS52, IAS29 veya Enf.Muh. seçeneklerinden birinin kullanılması gerekir.

Dövizli stok devri yapabilmek için öncelikle maliyet türü olarak Aylık Ağırlıklı Ortalama, FIFO, LIFO veya Maliyet Muhasebesi Fiyatı seçeneklerinden birinin işaretlenmiş olması gereklidir.Bu durumda program, seçilen maliyet türüne göre her stokun dövizli birim maliyet fiyatını bulacak, yeni yıl şirketinde döviz tutarına aktaracaktır. Döviz tipi olarak Genel Parametre Kayıtlarındaki firma döviz tipi kullanılacaktır.

**Soru 41: "Sipariş Bağlantılı D.A.T de teslimat ayrı takip edilsin" parametresi kullanımda iken sipariş ve stok devirleri yapılıp stok hareket kontrol çalıştırıldığında teslim miktarları değişiyorsa ne yapılmalıdır?**

"Sipariş Bağlantılı D.A.T de teslimat ayrı takip edilsin" parametresi işaretli olduğunda sırasıyla Sipariş Devri-Stok Devri - Stok Hareket Kontrol yapıldığında, yeni yıl şirketinde teslimat miktarı doğru gelmesi için DEVIR\\ SIPDEPTESAYRI\\0 özel parametresinin hem eski şirkette hem yeni şirkette tanımlanıp devir işlemlerinin yapılması gerekir.

**Soru 42: Stok Devri'nde İrsaliyeler Devredilsin seçeneği neden işaretli ve pasif gelmektedir?**

İrsaliyeler devredilsin seçeneği ile stok devri yapıldığı zaman TBLIRSALIYE_DEVIR tablosuna kayıt atılmaktadır. Bu parametre işaretli olarak ilk kez devir yapıldığında TBLIRSALIYE_DEVIR tablosuna aktarılan irsaliye numarası yazılacaktır, ikinci kez devir yapılmak istenirse TBLIRSALIYE_DEVIR tablosundaki kayıtlar aktarılmayacaktır. Bu sebeple; Stok hareket devrini öncelikle "İrsaliyeler devredilsin" parametresiyle çalıştırıp ardından parametreyi kaldırarak çalıştırmak stok bakiyelerinin bozulmasına yol açacağından stok hareket devri ekranının açılışında TBLIRSALIYE_DEVIR tablosunda bir kayıt bulunuyorsa "İrsaliyeler Devredilsin" parametresi işaretli ve parametre pasif hale getirilmiştir.

**Soru 43: Maliyet türü FIFO olan şubeli yapıdaki şirkette stok devir işleminde "Devir kayıtları detaylandırılsın" parametresi gelmiyorsa sebebi nedir?**

Stok parametre kayıtlarında lokal depo uygulaması ve esnek yapılandırma parametreleri kapalı olmalıdır. FIFO türündeki devirde elde kalan FIFO fiyatlarına göre detaylandırarak devir yapılması seçeneği lokal depo açık değilse desteklediğimiz bir durumdur.

Temel sebebi lokal depo bazında maliyet hesaplanmadığı içindir. Geçen yıl bu şekilde bir farklılık olmuş olabilir. Bunun dışında lokal depo açıksa önce fifo'ya göre kalan fiyatları bulup onların üzerinden kalan bakiyeye göre ağırlıklı ortalama yaparak elde kalan stokun fiyatını yeni seneye devrederiz.

**Soru 44: Stok devrinde the** **multi-part** **identifier "AAA" could not be bound uyarısı alınması durumunda ne yapılmlaıdır?**

Veri tabanı üzerinde ilgili datanın Compatibility Level'ı değiştirilerek kontrol edilebilir.

**Soru 45: Stok devri depo kısıtına göre yapılabilir mi?**

Kısıt ekranındaki depo kodu stok kartı kayıtlarında yer alan depo kodu bilgisi için kısıt verilebilmesini sağlamaktadır.

**Soru 46: Stok devrinde ek maliyet dağıtım uygulaması ile ilgili veritabanı nesneleri bulunamadı. Son set dosyaları ile DBupdate uygulamasını çalıştırmalısınız uyarısı alması durumunda ne yapılmalıdır?**

Data üzerinde bazı alanların oluşmamasından kaynaklanabilir. Dbupdate klasörünün güncel olduğuna emin olunduktan sonra tekrar dbupdate çalıştırılıp kontrol sağlanabilir.

**Soru 47: Serili stok devrinde Cannot insert the** **value NULL into** **column STHAR_GCKOD, table** **ZZZ.dbo.TBLSTHAR; column** **does not allow** **nulls. INSERT fails. uyarısı** **alınması durumunda ne yapılmalıdır?**

-Devir yapılmak istenen ve hata alınan stok bilgisine ait TBLSTHAR tablosunda mevcut kayıtlarının TBLSERITRA tablosunda karşılıklarının olup olmadığı kontrol edilmelidir. Karşılığı olmayan kayıtlar mevcut ise stokların stok hareket ve seri bağlantısız olarak devredilmesi gerekir.

-TBLSERITRA tablosunda MIKTAR alanı 0 olan kayıtlar olup olmadığı kontrol edilmeli, karşılık gelen INCKEYNO bilgisine göre TBLSTHAR tablosundaki miktarlarla aynı olması gerekir.

**Soru 48: Stok Devrinde Girilen Kayıt Sistemde Bulunmaktadır SQL :** **Insert** **InTo** **A2024..TBLSSATIRAC SELECT SSATIRAC.SUBE_KODU,SSATIRAC.BGTIP,SSATIRAC.FATNO... uyarısı alınıyorsa ne yapılmalıdır?**

TBLSSATIRAC içinde yer alan belge numarası aynı sırano, carikod, belgetipi ve şubekodu bilgileri ile hem eski yıl şirketinde hem de yeni yıl şirketinde mevcut olması, aynı belgenin iki şirkette de işlenmiş olması, sistemin primary key hatası vermesine neden olmuştur. Uyarıdaki cümle veritabanında çalıştırıldığında hangi numaralı belge için primary key hatası verdiği görülüp ilgili belge için gerekli düzeltme yapılmalıdır.

**Soru 49: Cari devir sonrasında yeni şirkette şube kodları 32767 olarak görünmektedir, ne yapılabilir?**

32767 nolu merkez şubede cari parametrelerinde yer alan cari kullanım tipi tüm şube hareketleri olarak seçili ise şube kodu bu şekilde atılmaktadır , işletme/şube olarak seçilip programa giriş yapılarak tekrar devir yapılabilir.

**Soru 50: Cari devir yapılırken aşağıdaki şekilde uyarı alındığında ne yapılmalıdır?**

Foreign Key : TBLCAHAR_FKEY1

Operation Type : Insert

Related Tables : TBLCAHAR \<-\> TBLCASABIT

DBQuery : xqTmp

SQL : Insert INTO AA2024..TBLCAHAR (CARI_KOD, TARIH, HKA, ACIKLAMA, Hareket_Turu, BORC, ALACAK, VADE_TARIHI, DOVIZ_TUTAR, DOVIZ_TURU, PROJE_KODU, PLASIYER_KODU, B_YEDEK1, SUBE_KODU, F_YEDEK1) SELECT CARI_KOD, '01/01/2015','A', 'DEVIR', 'A', CASE WHEN Sum(BORC-ALACAK) \> 0 THEN Sum(BORC-ALACAK) Else 0 END, CASE WHEN Sum(BORC-ALACAK) \< 0 THEN ABS(Sum(BORC-ALACAK)) Else 0 END, '',0,0,PROJE_KODU, NULL ,1,0 , SUM(F_YEDEK1) FROM CAHAR Where Cari_Kod = 'A01' And Tarih \<= '12/31/2014' Group By CARI_KOD ,PROJE_KODU HAVING (ABS(Sum(BORC-ALACAK)))\>0

Yeni şirket açıldıktan sonra eski şirkette yeni cari hesap kartları açılması durumunda bu uyarı ile karşılaşılmaktadır. Sabit kayıt kontrolü menüsü üzerinden cari hesap kayıtları seçilerek tamam denilerek cari devir işlemi tekrarlanmalıdır.

**Soru 51: Cari devir proje kırılımsız nasıl yapılabilir?**

Proje uygulaması açık ise yeni sene şirketine kayıtlar proje kodu bilgisi ile aktarılmaktadır. Ek bir seçenek olarak proje kırılımı olmadan kayıtların oluşturulması istenir ise proje kırılımlı devir işaretli kaldırılıp yanında bulunan alandan seçim yapılan genel proje kodu ile yeni sene şirketinde devir hareketlerine tek bir proje kodu ile yansıtılması sağlanabilir.

**Soru 52: Tek bir cari için cari devir işlemi tekrar yapılabilir mi?**

Cari devir ekranında ilgili cari kodu için kısıt verilmesi durumunda sadece o cari için tekrar cari devir yapılması sağlanabilir.

**Soru 53: Cari devir ekranında dövizli yaşlandırma seçenekleri aktif değil pasif gelmektedir ne yapılmalıdır?**

Yardımcı programlar şirket- şube parametre tanımları ekranında yer alan döviz uygulaması var parametresinin açık, döviz tipi seçili ve döviz çevrim tipi alanlarının birinin seçili olması gerekir. Seçili olmasına rağmen yine de gelmemesi durumunda döviz çevrim tipi alanı farklı bir seçenek seçilip kaydedilip tekrar eski haline getirilerek kaydedilerek yeniden kontrol sağlanabilir.

**Soru 54: Cari devir ekranındaki eski kayıtlara devir tarihi atılsın parametresi ne anlama gelmektedir?**

Eski sene şirketindeki cari hareketlerden kapatması yapılmayanları yeni sene şirketine aktarırken, "Kayıt Tarihi" alanına işlem sırasında belirlenen devir tarihinin aktarılması için kullanılan seçenektir. Bu şekilde yapılan devirde kayıt tarihleri düzenlenerek vade tarihlerinde değişiklik yapılmaz. Seçenek işaretlenmeden devir yapılması halinde ise, kayıt tarihleri olduğu gibi aktarılır.

**Soru 55: Cari devir işleminde this is not permitted** **when** **the** **subquery** **follows =, !=, \<, \<= , \>, \>= or** **when** **the** **subquery is used as an expression uyarısı alınmaktadır, ne yapılabilir?**

Veri tabanına yazılmış olan özel triggerlar hata alınmasına sebep olabilir. Triggerlar kontrol edilmelidir.

**Soru 56: Banka devri sonrasında devir TL bakiye eski şirket ile tutmamaktadır sebebi ne olabilir?**

Dövizli banka hesapları devredilirken, program döviz tiplerine göre ayrı ayrı devir alacak ve döviz bazında bakiyeleri ayrı ayrı yeni sene devri olarak oluşturacaktır. Döviz bazında yapılan bu devir hareketlerinin TL tutarları ise, her döviz tipi için burada girilen tarihteki kurdan yeniden hesaplanacaktır. Eğer eski sene şirketinde, devir yapılan tarih itibariyle kur farkı kapatma işlemi yapılmadıysa, bu yeniden hesaplama sonucu, bakiyeler, eski sene şirketiyle yeni sene şirketi arasında fark verebilir.

Bu nedenle devir programı, banka devir seçeneğine giriş sırasında kur farkı kapatma yapılması gerektiğine dair uyarı verilmektedir.

**Soru 57: Banka devrinde vadeli,** **spot, taksitli kredi, orta uzun vadeli kredi ve repo hesaplar nasıl devredilir**?

Banka hesapları devrinde, Vadeli, Spot, Taksitli Kredi, Uzun/Orta Vadeli Kredi ve Repo hesap hareketleri için, hesabın bakiye verip vermediğine bakılmaktadır. Eğer hesabın bakiyesi varsa, son hesap açma işleminde girilen tutar, devir baz tarihine bakılmaksızın yeni sene şirketine devredilmektedir.

Rotatif, Vadesiz ve Kredi Kartı hesaplarının devirleri vade tarihine göre yapılmaktadır. Vade tarihi, devir tarihinden büyük olan kayıtlar yeni yıl şirketine aynen aktarılmaktadır. Bunun dışındaki tüm hesap hareketleri, Cari Tarih Aralıklı Devir mantığına göre yeni sene şirketine aktarılacaktır. Yani, belirlediğiniz Devir Baz Tarihine kadar olan hareketlerin sadece bakiyesi devredilecek, bu tarihten sonraki hareketler aynen yeni sene şirketine aktarılacaktır.

**Soru 58: banka devrinde aşağıdaki şekilde uyarı alınıyorsa ne yapılmalıdır?**

SQL : Alter Table AA24..TBLBNKHESTRA Add constraint TBLBNKHESTRAFK1 FOREIGN KEY (NETHESKODU) REFERENCES AA24..TBLBNKHESSABIT (NETHESKODU)

There is already an object named 'TBLBNKHESTRAFK1' in the database.(NetsisMS-42S01,2714)

Could not create constraint. See previous errors.(NetsisMS-42000,1750)

Eski yıl şirketinde TMPFOREIGNTBL tablosu varsa bu tablonun drop edilmesi(silinmesi) gerekmektedir. Bu tablo constraintlerin geçici olarak tutulduğu devirden sonra kendiliğinden silinen geçici bir tablodur.

**Soru 59: Banka devri sırasında " AAA koduna yeni yıl şirketinde hareket girildiği için devir işlemi yapılamadı" uyarısı alınmaktadır tekrar devir işlemi nasıl yapılabilir?**

Devir sonrasında vadesiz hesap dışındaki banka hesaplarına yeni sene şirketinde hareket girildiyse tekrar devir işlemi yapılması engellenmiştir. Eskisi gibi çalışması isteniyorsa 'DEVIR','YENIYILHAREKET' özel parametresi tanımlanmalıdır.

**Soru 60: Banka devri sırasında Ambiguous column name REFERANSNO uyarısı alınması durumunda ne yapılmalıdır?**

Veri tabanı üzerinde ilgili datanın Compatibility Level'ı değiştirilerek kontrol edilebilir.

**Soru 61: Banka devrinde TBLBNKHESSABIT.NETHESKODU ve TBLBNKHESSABIT.SUBEKODU the** **multi-part** **identifier** **could not be bound uyarısı alınması durumunda ne yapılmalıdır?**

Veri tabanı üzerinde ilgili datanın Compatibility Level'ı değiştirilerek kontrol edilebilir.

**Soru 62: Banka devri ekranındaki eski kayıtlara devir tarihi atılsın parametresi ne anlama gelmektedir?**

Bu seçeneğin işaretlenmesi halinde devir baz tarihi öncesine denk gelen kayıtların işlem tarihi sahasına işlem sırasında belirlenen devir tarihi yazılacaktır. Bu seçenek işaretlenmeden devir yapılması halinde ise, işlem tarihleri olduğu gibi aktarılacaktır.

**Soru 63: Çek senet devrinde devir baz tarihi ve bekleyenleri aktar alanları nasıl çalışmaktadır?**

Devir baz tarihi; Vade tarihleri devir baz tarihinden büyük olan çek ve senetlerin tamamı yeni sene şirketine işlenecektir. Ancak vade tarihleri devir baz tarihinden büyük olan çek ve senetlerin durumu ödenmiş ise yeni yıl şirketine aktarılmayacaktır. Vade tarihleri devir baz tarihinden önceki tarihli çek ve senetler yeni sene şirketine aktarılmayacaktır.

Bekleyenleri aktar; Vade tarihleri devir baz tarihinden önce ve durumu Beklemede olan senet/çeklerin de yeni sene şirketine aktarılması için işaretlenmesi gereken sahadır. Senet çeklerin Beklemede olanlarının takiplerine yeni sene şirketinde devam etmek için bu sahayı kullanabilirsiniz. Bu saha işaretlenmediğinde senedin/ çekin durumuna bakılmaksızın baz tarihinden önceki senetler/ çekler yeni sene şirketine aktarılmayacaktır. Bu bölümdeki önemli nokta, yeni yıl için oluşturulan şirkette çek/ senet ve alındı/ verildi numaralarının, eski sene bilgilerinin kaldığı son numaradan takip edilerek kullanılmaya devam edilmesi gerektiğinin unutulmamasıdır.

**Soru 64: Çek senet devri tekrar yapılabilir mi?**

Senet/Çek devri yapıldıktan sonra, bir hata yapıldığı tespit edilirse, devir işlemi tekrar çalıştırılabilir. Daha önce devredilenler silinsin parametresi işaretli ise önceden devredilen kayıtlar silinecek, çek ve senet devri yeniden yapılacaktır. Bu parametrenin işaretlenmediği durumda, sadece devirden sonra yeni girilmiş olan kayıtlar yeni sene şirketine aktarılacaktır.

**Soru 65: Cari devri her şube için ayrı ayrı yapılabilir mi?**

Yardımcı Programlar/Özel Parametre Tanımları menüsünde DEVIR\\SUBELIYASLANDIRMA\\E şeklinde özel parametre tanımlanması durumunda cari devir işlemi her şube için ayrı ayrı çalıştırılabilir.

**Soru 66: Serili ve serisiz stok devri ayrı ayrı yapılabilir mi?**

Eski versiyonlarımızda farklı ekranlar altında bulunan serili ve serisiz stok devri ekranları Stok Hareket Devri adı ile tek bir ekranda farklı iki sekme altında birleştirilmiştir. Eski ekranlarımızın kullanılmak istenildiği durumda DEVIR/ STOK_DEVIR_ESKI_EKRAN özel parametresi kullanılabilir.

**Soru 67: Sipariş devrinde "Cannot insert an explicit** **value** **into a timestamp** **column. Use INSERT with a column** **list** **to** **exclude** **the** **timestamp** **column, or insert a DEFAULT into** **the** **timestamp** **column." Uyarısı alınması durumunda ne yapılmalıdır?**

TBLSIPAMAS ve TBLSIPATRA tablolarına fazladan kolon eklenmesi bu soruna yol açabilir. Netsis'in kendi oluşturduğu kolonlar dışında dışarıdan tablolara müdahale edilmemelidir. Eklenen kolonlar silinip tekrar devir yapılabilir.

**Soru 68: Sipariş devri sonrası yeni sene şirketine gelmeyen siparişler için ne yapılmalıdır?**

İlgili siparişler için TBLSIPATRA tablosunda FIRMA_DOVTUT kolonları dolu ve tamamı teslim edilmiş olabilir. Siparişlerin tamamı teslim edilmedi ise eski şirkette öncelikle stok hareket kontrol işlemi çalıştırılıp sipariş devri tekrar çalıştırılabilir.

**Soru 69: Yeni yıl şirketini nasıl oluşturmalıyım?**

Yeni yıl şirketi Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanmış olan firmalarda işletmelerin merkezinde, Netsis 3 Entegre, Netsis 3 Entegre Pro, Netsis Wings Entegre , Netsis Wings, Netsis 3 Standard ürünleri ile işletme tanımlanmamış Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerinde, merkez şubede Sene Sonu Devir / Yeni Yıl Kopyalama adımından oluşturulmalıdır.

**Soru 70: Yeni yıl şirketini ne zaman açmalıyım?**

Online muhasebe kullanan firmalar yeni yıl kayıtlarını yeni yıl şirketine girmelidir ve e-Süreçler nedeni ile de yeni yıl kopyalama en geç eski yılın son günü yapılmış olmalıdır.

**Soru 71: Her sene yeni şirket tanımlamalı mıyım?**

Teknik olarak her sene aynı şirket üzerinden devam edilebilse de özellikle muhasebe raporlarının doğru sonuç verebilmesi açısından dönem değişiminde yeni şirket tanımı önerilmektedir.

**Soru 72:Yeni yıl kopyalama tam olarak ne yapar?**

Eski senenin tüm bilgilerinin (table, view, vb.) yedeği alınıp (BACKUP).yedeklenen bu bilgiler, yeni yıl şirketine yüklenecektir (RESTORE).Yeni yıl şirketindeki hareket kayıtları iptal edilecek, sabit kayıtlar ise kalacaktır. Bazı tablolarda ise, birtakım koşullara bağlı iptaller yapılacaktır.

**Soru 73: Mevcut dizinde backup/restore işlemine yetecek kadar yer yoksa, farklı bir diske bu işlemi yönlendirebilir miyim?**

Yeni yıl kopyalama ekranında Veritabanı yedeği için başka dizin kullan seçeneği işaretlenerek yedeğin alınması için boş alana sahip olan diskteki bir dizin verilebilir.

**Soru 74: Özel dönem kullanıyorum. Bu duruma özel bir süreç var mıdır?**

Mali başlangıç ayı farklı olan şirketler, yeni yıl kopyalamada mali başlangıç ayı dikkate alınsın parametresini işaretlemelidir. Bu parametre işaretlendiğinde yeni yıl kopyalama ve modül bazında devirler özel döneme göre yapılacaktır.

**Soru 75: Yeni yıl kopyalama sonrasında eski sene şirketine açılan sabit kartları yeni sene şirketine nasıl aktarabilirim?**

Sene sonu devir modülü altında bulunan sabit kayıt kontrolü yeni yıl kopyalama sonrasında eski yıl şirketinde açılmış sabit kartların, yeni yıl şirketinde hızlıca oluşturulmasını sağlar.

**Soru 76: Modül devirlerini ne zaman yapmalıyım?**

Modül devirleri için zaman kısıtlaması yoktur .

**Soru 77: Modül devirleri için özel bir sıra var mıdır?**

Sadece Lojistik-Satış kısmı için bir sıra söz konusudur. Burada talep-sipariş-stok devri sırasında yapılması gerekmektedir.

**Soru 78: Modül devirleri tekrarlanabilir mi?**

Stok, cari, senet-çek, banka, maliyet muhasebesi devirleri tekrarlanabilir.

**Soru 79: Hem serili hem serisiz stoklarım var. Stok devrini nasıl yapmalıyım?**

Stokların bir kısmının serili bir kısmının serisiz kullanıldığı durumda, Serili ve Serisiz Stok Devri işlemlerinin her ikisi de çalıştırılmalıdır. Bu durumda hangi işlemde hangi stokların devredileceği stok kartındaki seri parametrelerine göre belirlenir. Stok kartında girişlerde ve çıkışlarda seri takibi olan stoklar serili devir işlemi ile devredilecektir. Seri parametreleri işaretli olmayan veya sadece çıkışlarda seri takibi açık olan stoklar ise serisiz stok devriyle devredilecektir.

**Soru 80: Cari devir işlemini şube bazında tek tek yapabilir miyim?**

Sadece girişlerde seri takibi açık olan stoklar ise hem serili devir ekranında hem de serisiz devir ekranından devredilebilir. Eğer serisiz devir ekranından devredilirse sadece stok hareketleri oluşacaktır, seri tablosundaki kayıtları oluşmayacaktır; serili devir ekranından ancak "Sadece Girişte seri takibi yapılan stoklarda devredilsin" parametresi işaretlenirse devredilebilecektir ve seri hareketleri de aktarılabilecektir. Bu yüzden stok devirlerinde işlem sırası olarak, önce serisiz stok devri ve ardından serili stok devrinin yapılması tavsiye edilmektedir.

Cari Hesap Tipine Göre Devir, bir özel parametre tanımlaması ile her şube için ayrı ayrı yapılabilir. Bunun için Yardımcı Programlar/Özel Parametre Tanımları menüsünde DEVIR/SUBELIYASLANDIRMA/E tanımlaması yapılmalıdır.

**Soru 81: Açılış fişi için 1 numaralı fişi boş bırakmayı unuttum, farklı fiş numarası verebilir miyim?**

Kullanılan fiş başka bir numaraya aktarılıp 1 numaralı fiş boşaltıldıktan sonra açılış fişi oluşturulabilir.

**Soru 82: Modül devirlerinde sonra eski/yeni sene bakiyelerini karşılaştıracağım kolay bir yol var mıdır?**

Modül bazında devirler sonucunda yeni sene şirketinde cari hesap, stok, çek/senet ve banka hareketlerinde oluşan devir kayıtları ile yine yeni sene şirketinde oluşan muhasebe açılış fişi arasındaki farkları Sene Sonu Devir modülü denetim listelerinden izleyebiliriz.

**Soru 83: e-Süreçler ile ilgili olarak devir işlemlerinde dikkat etmem gerekenler nedir?**

Yeni yıl kopyalama ile entegratör kullanan firmalar için, önceki yıl data bilgisi alanına program tarafından eski yıl şirket ismi getirilmektedir. Online e-Fatura kullanan firmaların yeni yıla ve eski yıla ait gelen faturalarının doğru şirketlere aktarımının sağlanabilmesi için web.config dosyalarındaki Schema bilgilerini düzenlemeleri gerekmektedir.

e-Defter için Mükellef ve Düzenleyen Bilgileri dönem başlangıç bitişi yeni döneme göre düzenlenmelidir.
