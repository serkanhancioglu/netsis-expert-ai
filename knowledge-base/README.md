# Logo Netsis 3 Enterprise Teknik Bilgi Tabanı

Bu yapı, resmi Logo Netsis 3 Enterprise dokümantasyonundan çıkarılan **1.936 Markdown dosyasını** AI asistanı için RAG kaynağı olarak düzenli biçimde saklamak amacıyla oluşturulmuştur.

## Klasörler

### `markdown/`
- Bilgi tabanının ana içeriğidir.
- Her makale tek bir `.md` dosyası olarak saklanır.
- Dosya adları benzersiz olmalıdır.

### `metadata/`
- Makale listesi, kaynak URL, modül, sürüm, etiket gibi alanları tutan indeks dosyaları burada yer alır.
- `articles-manifest.template.csv` başlangıç şablonu olarak eklenmiştir.
- `articles-manifest.schema.json` metadata alan sözleşmesini tanımlar.

### `rag/chunks/`
- Markdown dosyalarından üretilen metin parçaları (chunk) için ayrılmış klasör.

### `rag/embeddings/`
- Chunk'lar üzerinden oluşturulan embedding çıktıları için ayrılmış klasör.

## Beklenen akış

1. 1.936 Markdown dosyayı `markdown/` altına yükleyin.
2. Her dosya için metadata kaydını `metadata/articles-manifest.csv` içinde tutun.
3. RAG pipeline çıktılarınızı `rag/chunks/` ve `rag/embeddings/` altında saklayın.
