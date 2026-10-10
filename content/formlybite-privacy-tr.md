# FormlyBite Gizlilik Politikası

Son güncelleme: 10 Ekim 2026

FormlyBite, Süleyman Çayır tarafından geliştirilen bir iPhone öğün günlüğü uygulamasıdır. Gizlilik ve destek talepleri için destek@formlyapps.com adresine yazabilirsin.

## 1. Kısa özet

- Öğün günlüğü, kilo geçmişi, hedefler, su kayıtları ve favoriler uygulamanın yerel dosyalarında tutulur.
- Fotoğraf veya yazıyla analiz başlattığında ilgili içerik Supabase üzerinden OpenAI’a gönderilir.
- Apple Sağlık’tan okunan kilo ve aktif enerji bu analiz isteğine eklenmez.
- Uygulama reklam göstermez, uygulamalar arası takip yapmaz ve verilerini satmaz.
- Abonelik ödemelerini Apple işler; abonelik durumunu RevenueCat doğrular.

## 2. Cihazında saklanan veriler

Kişisel plan için girdiğin yaş, boy, kilo, hedef kilo, hareket düzeyi ve diğer plan cevapları; öğünler, kalori ve makro değerleri, öğün fotoğrafları, favoriler, su kayıtları, kilo geçmişi ve ayarların cihazında saklanır. Şu anda uygulamaya ait hesapla yedekleme veya cihazlar arası eşitleme yoktur. Uygulamayı silmek yerel kayıtları kaldırır. Apple’ın cihaz yedekleri ve geri yüklemesi, Apple hesabının ve cihazının ayarlarına bağlıdır.

Kamera yalnız fotoğraf çekmek veya barkod okumak için kullanılır. Fotoğraf arşivinden sistem seçicisiyle seçtiğin görsel işlenir. Kaydedilen ve analiz için gönderilen fotoğraf küçültülmüş JPEG’dir. Bildirimler öğün hatırlatmaları içindir. Maskotun hareketi için telefonun eğim bilgisi anlık kullanılır; sunucuya gönderilmez.

## 3. Fotoğraf ve yazılı öğün analizi

Analiz başlattığında seçtiğin öğün fotoğrafı, yazılı tarif veya düzeltme notu ve uygulama dili, kimliği doğrulanmış bir istekle Supabase sunucumuza gönderilir. Sunucu içeriği OpenAI API’ye ileterek öğün adı, kalori, makro ve öğün puanı tahmini ister. Kişisel plan bilgilerin ve Apple Sağlık kayıtların bu isteğe eklenmez. Yazdığın metne kendin eklediğin kişisel bilgi de aktarılır; analiz için gerekli olmayan özel bilgileri eklememeni öneririz.

Uygulamanın sunucu veritabanı fotoğrafı, tarif metnini ve öğün tahmininin içeriğini kaydetmez. Bu, hizmet sağlayıcıların içeriği hiç tutmadığı anlamına gelmez. OpenAI API verileri varsayılan olarak model eğitimi için kullanılmaz. Mevcut analiz isteği Responses API’nin varsayılan saklama ayarını kullanır: yanıt verileri en az 30 gün saklanabilir; kötüye kullanım denetim kayıtları genel olarak 30 güne kadar, yasal veya güvenlik istisnalarında daha uzun tutulabilir. Ayrıntılar [OpenAI veri kontrollerinde](https://developers.openai.com/api/docs/guides/your-data) açıklanır.

Supabase proje bölgesi Avrupa Birliği’dir. OpenAI ve diğer hizmet sağlayıcıların işleme faaliyetleri Türkiye veya AB dışında da gerçekleşebilir. Sağlayıcıların kendi gizlilik ve saklama politikaları uygulanır.

## 4. Anonim oturum ve teknik kayıtlar

Uygulama kayıt ekranı olmadan rastgele bir Supabase hesap kimliği oluşturur. Bu kimlik kişisel adını içermez, ancak aynı oturumun kullanımını birbirine bağlayan bir tanımlayıcıdır. Oturum belirteçleri cihazın Keychain alanında tutulur; uygulamayı silmek Keychain kaydının da silindiği garantisini vermez.

Ücretsiz analiz hakkını ve kötüye kullanımı yönetmek için analiz zamanı, hesap kimliği, kullanılan model, içerikte yiyecek bulunup bulunmadığı ve giriş/çıkış token sayısı kaydedilir. Bu kayıtlar için şu anda otomatik silme takvimi tanımlı değildir; silme talebin için bize yazabilirsin. Ağ ve hizmet sağlayıcılar güvenlik ve hizmet işletimi için IP adresi, istek zamanı ve hata kayıtları gibi teknik verileri işleyebilir.

## 5. Barkod sorguları

Bir barkod aradığında ürün numarası doğrudan Open Food Facts’e gönderilir. Sağlayıcı bağlantının IP adresini ve FormlyBite uygulama bilgisini de görebilir. Öğün günlüğün ve kişisel planın barkod isteğine eklenmez. Ürün verileri eksik veya hatalı olabilir. [Open Food Facts gizlilik politikası](https://world.openfoodfacts.org/privacy) geçerlidir.

## 6. Apple Sağlık

İzin verirsen FormlyBite kilo ve aktif enerji verilerini okur; uygulamada girdiğin kiloyu Sağlık’a yazar. Okunan bilgiler ilerleme ve yakılan kaloriyi hedefe ekleme işlevleri için cihazda kullanılır. Sağlık verileri Supabase veya OpenAI’a gönderilmez; reklam, pazarlama veya veri satışı için kullanılmaz. İzinleri Sağlık uygulamasından kaldırabilirsin. Önceden Sağlık’a yazılan kayıtlar, FormlyBite silinse de Sağlık’ta kalabilir; bunları Sağlık uygulamasından yönetebilirsin.

## 7. Abonelikler

Satın alma ve ödemeler Apple üzerinden gerçekleşir; kart bilgilerini görmeyiz. RevenueCat, anonim uygulama hesap kimliğiyle satın alma, ürün, abonelik durumu ve geri yükleme bilgilerini işler. SDK ayrıca hizmetin işlemesi için uygulama/cihaz ve bağlantıya ilişkin teknik bilgileri işleyebilir. [RevenueCat gizlilik politikası](https://www.revenuecat.com/privacy/) ve Apple’ın satın alma koşulları geçerlidir. Abonelik iptali Apple hesabındaki Abonelikler bölümünden yapılır; uygulamayı silmek aboneliği iptal etmez.

## 8. Seçeneklerin ve taleplerin

Fotoğraf/yazılı analiz kullanmadan elle öğün kaydı tutabilir; kamera, bildirim ve Sağlık izinlerini cihaz ayarlarından yönetebilirsin. Uygulama içinden öğünlerini düzenleyebilir veya silebilirsin. Sunucu kayıtlarına erişim, düzeltme veya silme talebi için destek@formlyapps.com adresine FormlyBite başlığıyla yaz. Anonim kaydın sana ait olduğunu doğrulayabilmek için gereken teknik bilgileri birlikte belirleriz; e-postana sağlık geçmişi veya öğün fotoğrafı eklemen gerekmez. Yasal saklama gereklilikleri ve sağlayıcılara ait kayıtlar ayrı değerlendirilir.

## 9. Sağlık bilgisi ve değişiklikler

FormlyBite’ın kalori, makro, kişisel hedef ve öğün puanı sonuçları tahmindir; tanı veya tedavi sunmaz, sağlık uzmanının önerisinin yerine geçmez. Uygulamanın veri işleme şekli değişirse bu sayfa ve son güncelleme tarihi yenilenir.
