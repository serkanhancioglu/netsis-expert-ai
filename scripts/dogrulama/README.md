# Doğrulama betikleri

Kazıma aracının doğru çalıştığını kanıtlayan kontroller. Her biri tek başına
çalışır ve sorun bulursa **sıfırdan farklı çıkış kodu** döner, yani CI'ya
doğrudan bağlanabilir.

`tests/` altındaki birim testlerinden farkları: bunlar gerçek veri (canlı site
ya da indirilmiş bir örneklem) üzerinde çalışır ve sayısal rapor üretir.

| Betik | Ne doğrular | Ağ |
|---|---|---|
| `01_agac_ve_csv_dogrula.py` | Ağaç/CSV kapsaması, yol benzersizliği, Windows yol uzunluğu | evet |
| `02_protokol_probu.py` | Oturum yeniden kullanımı, önyükleme atlama, appId sabitliği, geçersiz bağlantı | evet |
| `03_ayristirici_karsilastir.py` | Üç ayrıştırıcının `<tab>` metnini silmesi; ön kaçışlamanın bunu çözmesi | hayır |
| `04_korpus_donusum_dogrula.py` | Örneklemi toptan çevirip bozuk Markdown arar | hayır |
| `05_boyut_tahmini.py` | Tam çalışmanın boyutunu örneklemden ölçekler | hayır |
| `06_cikti_butunlugu.py` | Üretilmiş ağaçta kırık görsel/bağlantı arar | hayır |
| `07_indeks_sema_dogrula.py` | `articles-manifest.csv`'yi JSON şemasına karşı doğrular | hayır |
| `08_spa_kesfi.py` | Angular uygulamasını tersine çevirip üç adresi yeniden bulur | evet |
| `09_belirlenimlilik.py` | Aynı girdinin aynı çıktıyı verdiğini kanıtlar | hayır |

## Örnek kullanım

```bash
cd scripts
source .venv/bin/activate

# Canlı: ağaç sağlam mı, CSV kapsaması tam mı
python dogrulama/01_agac_ve_csv_dogrula.py ../Kitap1.csv

# Çevrimdışı: indirilmiş çıktıyı denetle
python dogrulama/06_cikti_butunlugu.py ../knowledge-base/markdown
python dogrulama/07_indeks_sema_dogrula.py ../knowledge-base/metadata/articles-manifest.csv

# Çevrimdışı: belirlenimlilik
python dogrulama/09_belirlenimlilik.py tests/fixtures/tree.json tests/fixtures
```

## Site değişirse

`08_spa_kesfi.py` protokolü baştan bulur: Angular paketlerini indirir,
yapılandırma adresini çıkarır ve `DYS_APP_URL` ile hiyerarşi API adresini
yazdırır. Değerler `netsis_scraper/config.py` içindekilerden farklıysa orayı
güncelleyin.
