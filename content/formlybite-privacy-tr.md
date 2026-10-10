# FormlyBite Gizlilik Politikası

Son güncelleme: 11 Ekim 2026

FormlyBite, Süleyman Çayır tarafından geliştirilen bir iPhone öğün günlüğü uygulamasıdır. Gizlilik ve destek talepleri için destek@formlyapps.com adresine yazabilirsin.

## 1. Kısa özet

- Öğün günlüğü, egzersizler, kilo geçmişi, hedefler, su kayıtları ve favoriler cihazında tutulur; iCloud’a giriş yaptıysan kendi iCloud hesabına yedeklenir. Öğün ve ilerleme fotoğrafları yalnız cihazında kalır.
- Fotoğraf veya yazıyla analiz başlattığında ilgili içerik Supabase üzerinden OpenAI’a gönderilir.
- Apple Sağlık’tan okunan kilo ve aktif enerji bu analiz isteğine eklenmez.
- Uygulamayı geliştirmek için anonim kullanım olayları ve çökme tanıları toplanır; Ayarlar’dan kapatabilirsin. Öğün içeriği, fotoğraf, kilo ve sağlık verisi bu kayıtlara girmez.
- Uygulama reklam göstermez, uygulamalar arası takip yapmaz ve verilerini satmaz.
- Ayarlar’daki “Verilerimi sil” cihazdaki kayıtları, iCloud yedeğini ve sunucudaki anonim hesabı siler.
- Abonelik ödemelerini Apple işler; abonelik durumunu RevenueCat doğrular.

## 2. Cihazında ve iCloud’unda saklanan veriler

Kişisel plan için girdiğin yaş, boy, kilo, hedef kilo, hareket düzeyi ve diğer plan cevapları; öğünler, bunların kalori, makro, lif, şeker, sodyum değerleri ve malzeme dökümü; öğün fotoğrafları, ilerleme fotoğrafları, elle girdiğin egzersizler, favoriler, su kayıtları, kilo geçmişi ve ayarların cihazında saklanır.

Cihazında iCloud’a giriş yapılmışsa bu kayıtlar, fotoğraflar hariç, Apple’ın iCloud anahtar-değer deposu üzerinden kendi iCloud hesabına yedeklenir ve aynı Apple hesabını kullanan cihazların arasında eşitlenir. Bu yedek Apple tarafından saklanır; biz erişemeyiz. Öğün ve ilerleme fotoğrafları yedeklenmez ve yalnız eklendikleri cihazda durur. iCloud’a giriş yapılmamışsa veriler yalnız cihazda kalır. Uygulamayı silmek yerel kayıtları kaldırır, iCloud’daki yedeği kaldırmaz; yedeği de silmek için önce uygulamadaki “Verilerimi sil” seçeneğini kullan. Apple’ın cihaz yedekleri ve geri yüklemesi, Apple hesabının ve cihazının ayarlarına bağlıdır.

Ana ekran ve kilit ekranı araç takımları için günün kalori ve makro özeti, uygulama ile araç takımı arasında cihaz üzerinde paylaşılır; sunucuya gönderilmez.

Kamera yalnız fotoğraf çekmek veya barkod okumak için kullanılır. Fotoğraf arşivinden sistem seçicisiyle seçtiğin görsel işlenir. Kaydedilen ve analiz için gönderilen fotoğraf küçültülmüş JPEG’dir. Bildirimler öğün hatırlatmaları içindir. Maskotun hareketi için telefonun eğim bilgisi anlık kullanılır; sunucuya gönderilmez.

## 3. Fotoğraf ve yazılı öğün analizi

Analiz başlattığında seçtiğin öğün fotoğrafı, yazılı tarif veya düzeltme notu ve uygulama dili, kimliği doğrulanmış bir istekle Supabase sunucumuza gönderilir. Sunucu içeriği OpenAI API’ye ileterek öğün adı, malzeme dökümü, kalori, makro, lif, şeker, sodyum ve öğün puanı tahmini ister. Kişisel plan bilgilerin ve Apple Sağlık kayıtların bu isteğe eklenmez. Yazdığın metne kendin eklediğin kişisel bilgi de aktarılır; analiz için gerekli olmayan özel bilgileri eklememeni öneririz.

Uygulamanın sunucu veritabanı fotoğrafı, tarif metnini ve öğün tahmininin içeriğini kaydetmez. Bu, hizmet sağlayıcıların içeriği hiç tutmadığı anlamına gelmez. OpenAI API verileri varsayılan olarak model eğitimi için kullanılmaz. Mevcut analiz isteği Responses API’nin varsayılan saklama ayarını kullanır: yanıt verileri en az 30 gün saklanabilir; kötüye kullanım denetim kayıtları genel olarak 30 güne kadar, yasal veya güvenlik istisnalarında daha uzun tutulabilir. Ayrıntılar [OpenAI veri kontrollerinde](https://developers.openai.com/api/docs/guides/your-data) açıklanır.

Supabase proje bölgesi Avrupa Birliği’dir. OpenAI ve diğer hizmet sağlayıcıların işleme faaliyetleri Türkiye veya AB dışında da gerçekleşebilir. Sağlayıcıların kendi gizlilik ve saklama politikaları uygulanır.

## 4. Anonim oturum, kullanım verisi ve teknik kayıtlar

Uygulama ilk açılışta, kayıt ekranı olmadan rastgele bir Supabase hesap kimliği oluşturur. Bu kimlik adını, e-postanı veya telefon numaranı içermez, ancak aynı kurulumun kullanımını birbirine bağlayan bir tanımlayıcıdır. Oturum belirteçleri cihazın Keychain alanında tutulur; “Verilerimi sil” bu kaydı da siler, yalnız uygulamayı silmek ise Keychain kaydının silindiği garantisini vermez.

Ücretsiz analiz hakkını ve kötüye kullanımı yönetmek için analiz zamanı, hesap kimliği, kullanılan model, içerikte yiyecek bulunup bulunmadığı ve giriş/çıkış token sayısı kaydedilir.

Uygulamayı geliştirebilmek için ayrıca şu anonim kullanım olayları aynı hesap kimliğiyle Supabase sunucumuza (Avrupa Birliği) kaydedilir: uygulamanın açılması, karşılamanın tamamlanması ve seçilen hedef türü (kilo vermek, korumak, almak), bir öğünün hangi yolla eklendiği (fotoğraf, yazı, barkod, arama, favori, elle), analizin sonucu (başarılı, sınır doldu, yiyecek bulunamadı, hata), bir egzersizin türü, ödeme ekranının görülmesi, satın alma ve geri yükleme sonucu. Her olayla birlikte zamanı, uygulama sürümü, iOS sürümü ve cihazın dil/bölge ayarı kaydedilir. Uygulama çöker veya takılırsa Apple’ın cihazda ürettiği tanı kaydı da (hata türü, sinyal, sonlanma nedeni, takılma süresi ve işlev adreslerinden oluşan yığın izi) gönderilir. Öğün adı, kalori, fotoğraf, tarif metni, kilo, boy, yaş ve Apple Sağlık verisi bu kayıtlara girmez. Bu veriler reklam, pazarlama veya uygulamalar arası takip için kullanılmaz; üçüncü taraf bir analitik hizmetine aktarılmaz. Göndermeyi Ayarlar › “Anonim kullanım verisi” ile kapatabilirsin.

Analiz ve kullanım kayıtları için şu anda otomatik silme takvimi tanımlı değildir; “Verilerimi sil” ile hesabınla birlikte silinirler. Ağ ve hizmet sağlayıcılar güvenlik ve hizmet işletimi için IP adresi, istek zamanı ve hata kayıtları gibi teknik verileri işleyebilir.

## 5. Barkod sorguları ve ürün arama

Bir barkod aradığında ürün numarası, bir ürünü adıyla aradığında yazdığın arama sözcüğü doğrudan Open Food Facts’e gönderilir. Sağlayıcı bağlantının IP adresini ve FormlyBite uygulama bilgisini de görebilir. Öğün günlüğün ve kişisel planın bu isteklere eklenmez. Ürün verileri eksik veya hatalı olabilir. [Open Food Facts gizlilik politikası](https://world.openfoodfacts.org/privacy) geçerlidir.

## 6. Apple Sağlık

İzin verirsen FormlyBite kilo ve aktif enerji verilerini okur; uygulamada girdiğin kiloyu Sağlık’a yazar. Okunan bilgiler ilerleme ve yakılan kaloriyi hedefe ekleme işlevleri için cihazda kullanılır; elle girdiğin egzersizlerle karşılaştırma da cihazda yapılır. Sağlık verileri Supabase veya OpenAI’a gönderilmez; reklam, pazarlama veya veri satışı için kullanılmaz. İzinleri Sağlık uygulamasından kaldırabilirsin. Önceden Sağlık’a yazılan kayıtlar, FormlyBite silinse de Sağlık’ta kalabilir; bunları Sağlık uygulamasından yönetebilirsin.

## 7. Abonelikler

Satın alma ve ödemeler Apple üzerinden gerçekleşir; kart bilgilerini görmeyiz. RevenueCat, anonim uygulama hesap kimliğiyle satın alma, ürün, abonelik durumu ve geri yükleme bilgilerini işler. SDK ayrıca hizmetin işlemesi için uygulama/cihaz ve bağlantıya ilişkin teknik bilgileri işleyebilir. [RevenueCat gizlilik politikası](https://www.revenuecat.com/privacy/) ve Apple’ın satın alma koşulları geçerlidir. Abonelik iptali Apple hesabındaki Abonelikler bölümünden yapılır; uygulamayı silmek aboneliği iptal etmez.

## 8. Seçeneklerin ve taleplerin

Fotoğraf/yazılı analiz kullanmadan elle öğün kaydı tutabilir; kamera, bildirim ve Sağlık izinlerini cihaz ayarlarından yönetebilirsin. Anonim kullanım verisini Ayarlar’dan kapatabilirsin. Uygulama içinden öğünlerini, egzersizlerini ve ilerleme fotoğraflarını düzenleyebilir veya silebilirsin.

Ayarlar › “Verilerimi sil” cihazdaki günlüğü, fotoğrafları, kilo ve su kayıtlarını, favorileri, iCloud yedeğini ve sunucudaki anonim hesabı, ona bağlı analiz ve kullanım kayıtlarıyla birlikte kalıcı olarak siler. İşlem geri alınamaz. Aboneliğin iptal olmaz; onu Apple hesabından yönetirsin. Apple Sağlık’a yazılmış kilo kayıtları ile Apple ve RevenueCat’in tuttuğu satın alma kayıtları bu işlemle silinmez.

Sunucu kayıtlarına erişim, düzeltme veya uygulamayı kullanamıyorsan silme talebi için destek@formlyapps.com adresine FormlyBite başlığıyla yaz. Anonim kaydın sana ait olduğunu doğrulayabilmek için gereken teknik bilgileri birlikte belirleriz; e-postana sağlık geçmişi veya öğün fotoğrafı eklemen gerekmez. Yasal saklama gereklilikleri ve sağlayıcılara ait kayıtlar ayrı değerlendirilir.

## 9. Sağlık bilgisi ve değişiklikler

FormlyBite’ın kalori, makro, lif, şeker, sodyum, yakılan kalori, kişisel hedef ve öğün puanı sonuçları tahmindir; tanı veya tedavi sunmaz, sağlık uzmanının önerisinin yerine geçmez. Uygulamanın veri işleme şekli değişirse bu sayfa ve son güncelleme tarihi yenilenir.
