#!/usr/bin/env python3
"""formlyapps.com sayfalarını Türkçe ve İngilizce üretir (paket gerektirmez).

Kullanım: python3 scripts/build.py [FormlyStudy reposunun yolu]
Varsayılan yol: ../İOS/FormlyStudy. FormlyStudy gizlilik politikası oradaki
docs/legal/privacy-policy-tr.md ve privacy-policy-en.md'den, FormlyConvert'inki
content/formlyconvert-privacy-en.md'den üretilir; diğer metinler bu dosyadadır.

Türkçe sayfalar kökte, İngilizceleri /en/ altında. Her sayfanın iki adresi PATHS'te eşlenir.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STUDY_REPO = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "İOS" / "FormlyStudy"
SITE = "https://formlyapps.com"

CONVERT_STORE = "https://apps.apple.com/app/id6759096094"
BITE_STORE = "https://apps.apple.com/app/id6821417196"
STUDY_MAIL = "destek@formlyapps.com"
CONVERT_MAIL = "formlyconvert@gmail.com"
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"

PATHS = {
    "bite": {"tr": "/formlybite/", "en": "/en/formlybite/"},
    "bite-support": {"tr": "/formlybite/destek/", "en": "/en/formlybite/support/"},
    "bite-privacy": {"tr": "/formlybite/gizlilik/", "en": "/en/formlybite/privacy/"},
    "home": {"tr": "/", "en": "/en/"},
    "study": {"tr": "/formlystudy/", "en": "/en/formlystudy/"},
    "convert": {"tr": "/formlyconvert/", "en": "/en/formlyconvert/"},
    "support": {"tr": "/destek/", "en": "/en/support/"},
    "study-support": {"tr": "/formlystudy/destek/", "en": "/en/formlystudy/support/"},
    "convert-support": {"tr": "/formlyconvert/destek/", "en": "/en/formlyconvert/support/"},
    "study-privacy": {"tr": "/formlystudy/gizlilik/", "en": "/en/formlystudy/privacy/"},
    "convert-privacy": {"tr": "/formlyconvert/gizlilik/", "en": "/en/formlyconvert/privacy/"},
}

UI = {
    "tr": {
        "support": "Destek", "privacy": "Gizlilik", "menu": "Ana menü", "footer": "Alt menü",
        "study_privacy": "FormlyStudy gizlilik", "study_support": "FormlyStudy destek",
        "convert_privacy": "FormlyConvert gizlilik", "convert_support": "FormlyConvert destek",
        "terms": "Kullanım koşulları", "other": "EN", "other_label": "English",
    },
    "en": {
        "support": "Support", "privacy": "Privacy", "menu": "Main menu", "footer": "Footer menu",
        "study_privacy": "FormlyStudy privacy", "study_support": "FormlyStudy support",
        "convert_privacy": "FormlyConvert privacy", "convert_support": "FormlyConvert support",
        "terms": "Terms of use", "other": "TR", "other_label": "Türkçe",
    },
}


def p(key: str, lang: str) -> str:
    return PATHS[key][lang]


# MARK: Şablon

def page(key: str, lang: str, title: str, description: str, body: str, theme: str = "study", doc_lang: str | None = None) -> None:
    ui = UI[lang]
    other = "en" if lang == "tr" else "tr"
    path = p(key, lang)
    nav = [(p("study", lang), "FormlyStudy"), (p("convert", lang), "FormlyConvert"), (p("bite", lang), "FormlyBite"), (p("support", lang), ui["support"])]
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if path.startswith(href) else ""}>{label}</a>'
        for href, label in nav
    )
    switch = f'<a class="lang" href="{p(key, other)}" hreflang="{other}" lang="{other}" aria-label="{ui["other_label"]}" title="{ui["other_label"]}">{ui["other"]}</a>'
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{code}" href="{SITE}{p(key, code)}">' for code in ("tr", "en")
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}{p(key, "en")}">'
    document = f"""<!doctype html>
<html lang="{doc_lang or lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Formly">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{SITE}{path}">
<meta name="theme-color" content="#F5F1EA" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1E1A16" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{SITE}{path}">
{alternates}
<link rel="icon" href="/assets/formi.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
</head>
<body class="theme-{theme}">
<header class="site-header"><div class="wrap">
<a class="brand" href="{p("home", lang)}"><span class="marks"><img src="/assets/formi.svg" alt=""><img src="/assets/tabi.svg" alt=""></span><span>Formly</span></a>
<nav aria-label="{ui["menu"]}">{links}{switch}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site-footer"><div class="wrap">
<span>© 2026 Süleyman Çayır</span>
<nav aria-label="{ui["footer"]}">
<a href="{p("study-privacy", lang)}">{ui["study_privacy"]}</a>
<a href="{p("study-support", lang)}">{ui["study_support"]}</a>
<a href="{p("convert-privacy", lang)}">{ui["convert_privacy"]}</a>
<a href="{p("convert-support", lang)}">{ui["convert_support"]}</a>
<a href="{p("bite-privacy", lang)}">FormlyBite {ui["privacy"]}</a>
<a href="{p("bite-support", lang)}">FormlyBite {ui["support"]}</a>
<a href="{EULA}">{ui["terms"]}</a>
</nav>
</div></footer>
</body>
</html>
"""
    target = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(document, encoding="utf-8")
    print("yazıldı:", target.relative_to(ROOT))


def tiles(items: list[tuple[str, str, str]]) -> str:
    return '<div class="grid-3">' + "".join(
        f'<div class="tile"><div class="dot" aria-hidden="true">{mark}</div><h3>{title}</h3><p>{text}</p></div>'
        for mark, title, text in items
    ) + "</div>"


# MARK: Ana sayfa

HOME = {
    "tr": {
        "title": "Formly · FormlyConvert, FormlyStudy ve FormlyBite",
        "description": "Belgelerin, öğrenmen ve öğün günlüğün için Formly uygulamaları.",
        "h1": "Gününe eşlik eden küçük yardımcılar.",
        "lead": "FormlyConvert dosyalarını dönüştürür, FormlyStudy onlardan öğrenmeni sağlar. FormlyBite ise öğünlerini ve günlük hedeflerini takip etmene yardımcı olur.",
        "cta": "Uygulamaları gör", "anchor": "uygulamalar",
        "on_store": "App Store'da", "soon": "Yakında", "open_store": "App Store'da aç", "meet": "Tanı",
        "convert": "PDF, Word, Excel, PowerPoint, görsel ve UDF dosyalarını dönüştürür; PDF'leri sıkıştırır, doldurur ve imzalar. Yanında kâğıttan dostu Formi.",
        "study": "PDF'lerinden kaynak bağlantılı kartlar, testler, özetler ve zihin haritaları hazırlar; ne zaman tekrar edeceğini de söyler. Yanında ayraç dostu Tabi.",
        "how": "Nasıl yapıyoruz?",
        "tiles": [
            ("1", "Önce cihazında", "Belgelerin ve günlük kayıtların cihazında kalır. FormlyBite fotoğraf ve yazılı öğün analizini bulut üzerinden yapar."),
            ("2", "Hesap şart değil", "Uygulamaları hesap açmadan kullanmaya başlayabilirsin. Veri işleme ayrıntıları her uygulamanın gizlilik sayfasında."),
            ("3", "Küçük ve odaklı", "Her uygulama tek bir işi iyi yapmaya çalışır. Gereksiz ekran, gereksiz izin yok."),
        ],
    },
    "en": {
        "title": "Formly · FormlyConvert, FormlyStudy and FormlyBite",
        "description": "Formly apps for your documents, learning and food diary.",
        "h1": "Small helpers for your day.",
        "lead": "FormlyConvert converts your files, FormlyStudy helps you learn from them. FormlyBite helps you track meals and daily goals.",
        "cta": "See the apps", "anchor": "apps",
        "on_store": "On the App Store", "soon": "Coming soon", "open_store": "Open in the App Store", "meet": "Learn more",
        "convert": "Converts PDF, Word, Excel, PowerPoint, image and UDF files; compresses, fills in and signs PDFs. With Formi, its paper friend.",
        "study": "Turns your PDFs into source-linked cards, quizzes, summaries and mind maps, and tells you when to review. With Tabi, its bookmark friend.",
        "how": "How we build them",
        "tiles": [
            ("1", "On your device first", "Your documents and diary entries stay on your device. FormlyBite uses cloud processing for photo and written meal analysis."),
            ("2", "No account needed", "You can start using the apps without signing up. Each app’s privacy page explains how it handles data."),
            ("3", "Small and focused", "Each app tries to do one job well. No needless screens, no needless permissions."),
        ],
    },
}


def home(lang: str) -> None:
    t = HOME[lang]
    body = f"""<div class="wrap">
<section class="hero">
<div>
<p class="eyebrow">Formly</p>
<h1>{t["h1"]}</h1>
<p class="lead">{t["lead"]}</p>
<a class="button primary" href="#{t["anchor"]}">{t["cta"]}</a>
</div>
<div class="mascots" aria-hidden="true"><img class="formi" src="/assets/formi.svg" alt=""><img class="tabi" src="/assets/tabi.svg" alt=""></div>
</section>
<section class="apps" id="{t["anchor"]}">
<article class="app-card theme-convert">
<div><span class="badge">{t["on_store"]}</span><h2>FormlyConvert</h2><p>{t["convert"]}</p></div>
<img class="mascot" src="/assets/formi.svg" alt="Formi">
<div class="actions"><a class="button primary" href="{CONVERT_STORE}">{t["open_store"]}</a><a class="button secondary" href="{p("convert", lang)}">{t["meet"]}</a><a class="button secondary" href="{p("convert-privacy", lang)}">{UI[lang]["privacy"]}</a></div>
</article>
<article class="app-card theme-study">
<div><span class="badge">{t["soon"]}</span><h2>FormlyStudy</h2><p>{t["study"]}</p></div>
<img class="mascot" src="/assets/tabi.svg" alt="Tabi">
<div class="actions"><a class="button primary" href="{p("study", lang)}">{t["meet"]}</a><a class="button secondary" href="{p("study-privacy", lang)}">{UI[lang]["privacy"]}</a></div>
</article>
<article class="app-card theme-bite">
<div><span class="badge">{t["on_store"]}</span><h2>FormlyBite</h2><p>{BITE[lang]["card"]}</p></div>
<img class="mascot" src="/assets/muzi.svg" alt="Muzi">
<div class="actions"><a class="button primary" href="{BITE_STORE}">{t["open_store"]}</a><a class="button secondary" href="{p("bite", lang)}">{t["meet"]}</a><a class="button secondary" href="{p("bite-privacy", lang)}">{UI[lang]["privacy"]}</a></div>
</article>
</section>
<section class="section">
<h2>{t["how"]}</h2>
{tiles(t["tiles"])}
</section>
</div>"""
    page("home", lang, t["title"], t["description"], body)


# MARK: Uygulama sayfaları

STUDY = {
    "tr": {
        "title": "FormlyStudy · PDF'lerinden öğren",
        "description": "FormlyStudy: PDF'lerinden kaynak bağlantılı kartlar, testler, özetler ve zihin haritaları.",
        "eyebrow": "FormlyStudy · Yakında App Store'da",
        "h1": "PDF'lerinden öğren, kaynağından kopmadan.",
        "lead": "FormlyStudy notlarından ve ders kitaplarından çalışma kartları, testler, özetler ve zihin haritaları hazırlar. Her kart PDF'teki satırına bağlıdır; bir dokunuşla kaynağını görürsün.",
        "mascot_alt": "Tabi, FormlyStudy'nin maskotu",
        "features": "Neler yapar?",
        "tiles": [
            ("K", "Kaynak bağlantılı kartlar", "Kartlar geldiği sayfa ve satırla eşleşir; desteye eklemeden önce gözden geçirirsin."),
            ("T", "Akıllı tekrar", "Hatırlama gücüne göre ne zaman tekrar edeceğini planlar; sınav tarihine göre hızlanır."),
            ("Q", "Test ve özet", "Konuyu sınayan çoktan seçmeli sorular ve kaynak sayfalı özetler hazırlar."),
            ("H", "Zihin haritası", "Ana başlıkları ve kavramları canlı bir haritada bir araya getirir."),
            ("C", "Önce cihazında", "Yapay zekâ varsayılan olarak cihazında çalışır; istersen bulutta hazırlatırsın."),
            ("i", "iPhone ve iPad", "Pro ile kütüphanen iCloud üzerinden cihazların arasında eşitlenir."),
        ],
        "meet_h": "Tabi ile tanış",
        "meet": "Tabi, kitabının arasında yerini tutan turuncu kurdele ayraç. Kartların hazırlanırken bekler, serini korursan sevinir, unuttuğun kartı sana hatırlatır.",
    },
    "en": {
        "title": "FormlyStudy · Learn from your PDFs",
        "description": "FormlyStudy: source-linked cards, quizzes, summaries and mind maps from your PDFs.",
        "eyebrow": "FormlyStudy · Coming soon to the App Store",
        "h1": "Learn from your PDFs, never losing the source.",
        "lead": "FormlyStudy turns your notes and textbooks into study cards, quizzes, summaries and mind maps. Every card is linked to its line in the PDF, so the source is always one tap away.",
        "mascot_alt": "Tabi, the FormlyStudy mascot",
        "features": "What it does",
        "tiles": [
            ("K", "Source-linked cards", "Each card is matched to the page and line it came from; you review them before they join your deck."),
            ("T", "Smart review", "Schedules reviews based on how well you remember, and speeds up as your exam date gets closer."),
            ("Q", "Quizzes and summaries", "Builds multiple-choice questions that test the topic, and summaries with source pages."),
            ("H", "Mind maps", "Brings the main topics and concepts together in a living map."),
            ("C", "On your device first", "AI runs on your device by default; you can choose the cloud when you want."),
            ("i", "iPhone and iPad", "With Pro, your library syncs between your devices through iCloud."),
        ],
        "meet_h": "Meet Tabi",
        "meet": "Tabi is the orange ribbon bookmark that keeps your place in the book. It waits while your cards are being made, cheers when you keep your streak, and reminds you of the cards you forget.",
    },
}

def study(lang: str) -> None:
    t = STUDY[lang]
    body = f"""<div class="wrap">
<section class="app-hero">
<div>
<p class="eyebrow">{t["eyebrow"]}</p>
<h1>{t["h1"]}</h1>
<p class="lead">{t["lead"]}</p>
<a class="button primary" href="{p("study-support", lang)}">{UI[lang]["support"]}</a> <a class="button ghost" href="{p("study-privacy", lang)}">{UI[lang]["privacy"]}</a>
</div>
<img class="mascot" src="/assets/tabi.svg" alt="{t["mascot_alt"]}">
</section>
<section class="section">
<h2>{t["features"]}</h2>
{tiles(t["tiles"])}
</section>
<section class="section">
<h2>{t["meet_h"]}</h2>
<p class="lead">{t["meet"]}</p>
</section>
</div>"""
    page("study", lang, t["title"], t["description"], body)


CONVERT = {
    "tr": {
        "title": "FormlyConvert · PDF, Word, Excel ve UDF dönüştürücü",
        "description": "FormlyConvert: PDF, Word, Excel, PowerPoint, görsel ve UYAP UDF dosyalarını iPhone ve iPad'de dönüştür, sıkıştır, doldur ve imzala. 39 belge aracı, dönüşümler cihazında.",
        "h1": "Belge işlerinin hepsi, tek uygulamada.",
        "lead": "PDF, Word, Excel, PowerPoint, görsel ve UYAP UDF dosyalarını dönüştür; PDF'leri sıkıştır, doldur ve imzala. Dönüşümler iPhone ya da iPad'inde yapılır; dosyaların bunun için bir sunucuya yüklenmez.",
        "store_meta": "Ücretsiz · iPhone ve iPad · iOS 17 ve sonrası",
        "facts": [("39", "belge aracı"), ("10+", "dosya biçimi"), ("Cihazda", "yapılan dönüşümler"), ("iOS 17+", "iPhone ve iPad")],
        "formats_label": "Desteklenen biçimler",
        "formats": ["PDF", "Word", "Excel", "PowerPoint", "JPG", "PNG", "HEIC", "HTML", "TXT", "UYAP UDF", "Ses ve video"],
        "rows": [
            ("tools", "Dönüştür", "Hangi biçimde gelirse gelsin.",
             "Araç Kutusu'nda 39 aracın hepsi tek ekranda. Aradığın aracı yazarak bul, sık kullandıklarını yıldızla.",
             ["PDF'ten Word, Excel, PowerPoint, JPG, PNG ve metne", "Word, Excel, PowerPoint, HTML ve görsellerden PDF'e", "UYAP UDF dosyalarını saniyeler içinde PDF'e", "Birden fazla dosyayı tek seferde işle"]),
            ("workspace", "Düzenle", "Belgeyi seç, sonrasına sen karar ver.",
             "Açtığın belge bir çalışma alanına gelir: sayfalarını gör, sırayı değiştir, sonraki adımı oradan seç.",
             ["Form rehberi PDF'teki alanları bulur ve seni tek tek gezdirir", "\"Bilgilerimle doldur\" ile ad, T.C. kimlik no, telefon ve adres tek dokunuşta", "İmzanı çiz; tarih, onay işareti ve QR kod ekle", "Taranmış sayfaları OCR ile aranabilir PDF'e çevir"]),
            ("compress", "Sıkıştır ve paylaş", "Birkaç dokunuşla, gönderilmeye hazır.",
             "Boyut ile kalite arasındaki dengeyi sen seç. Metin net kalır, yalnız görsel ağırlıklı sayfalar hafifler.",
             ["Önce ve sonra karşılaştırması", "Mail, WhatsApp ya da Dosyalar'a tek dokunuşla", "Uzun işlemleri kilit ekranından ve Dynamic Island'dan izle", "Filigran, sayfa numarası, damga ve şifre ekle"]),
            ("library", "Kütüphane", "Her dosya düzenli, her an elinin altında.",
             "Dönüştürdüğün her belge kütüphanede tarih ve türe göre durur. Klasörlere ayır, önemlileri en üste sabitle.",
             ["Dosya adıyla ara, türe göre süz", "Pro ile iCloud üzerinden iPhone ve iPad arasında eşitle", "Uygulamayı Face ID ile kilitle", "Ana ekran ve kilit ekranı widget'ları"]),
        ],
        "all_h": "Tüm araçlar, dört başlıkta",
        "all_lead": "Araçlar işine göre gruplandı. Her biri kendi ekranında açılır ve ne yapacağını önceden gösterir.",
        "groups": [
            ("Dönüştür", ["PDF'ten Word", "PDF'ten Excel", "PDF'ten PowerPoint", "PDF'ten JPG ve PNG", "PDF'ten metin", "Word, Excel, PowerPoint'ten PDF", "HTML'den PDF", "Görsellerden PDF", "UDF'den PDF"]),
            ("Düzenle", ["Birleştir", "Böl", "Sıkıştır", "Döndür", "Sayfaları düzenle", "Filigran", "Sayfa numarası", "Bates numarası", "Damga"]),
            ("Doldur ve koru", ["Form doldur", "Bilgilerimle doldur", "İmza", "Şifrele", "Şifreyi kaldır", "Karart", "Onar", "Aranabilir PDF (OCR)"]),
            ("Akıllı araçlar", ["Belge Asistanı: özet ve soru-cevap", "Sesli okuma", "Ses ve videodan metne", "Kamerayla tara", "Apple Pencil ile not"]),
        ],
        "privacy_eyebrow": "Gizlilik",
        "privacy_h": "Dosyaların sende kalır.",
        "privacy_lead": "Dönüşümler telefonunda yapılır. Hesap açman gerekmez; form bilgilerin yalnız bu cihazda saklanır.",
        "privacy_points": [("Cihazda dönüşüm", "Belgelerin dönüştürülmek için bir sunucuya yüklenmez."), ("Hesap yok", "İndir ve hemen kullanmaya başla."), ("Önce cihazında", "Belge Asistanı ve sesten metne varsayılan olarak cihazında çalışır; buluta yalnız sen izin verirsen gider.")],
        "privacy_link": "Gizlilik politikasını oku",
        "faq_h": "Sık sorulanlar",
        "faq": [
            ("FormlyConvert ücretsiz mi?", "Uygulamayı ücretsiz indirip kullanabilirsin. Formly Pro ile sınırsız dönüşüm yapar, reklamsız kullanırsın; aylık, yıllık ve ömür boyu seçenekleri var. Abonelikler App Store hesap ayarlarından yönetilir."),
            ("Dosyalarım internete yükleniyor mu?", "Hayır. Dönüştürme, sıkıştırma ve düzenleme cihazında yapılır; dosya içeriği sunucularımıza yüklenmez. iCloud eşitlemeyi açarsan kütüphanen kendi iCloud hesabında saklanır."),
            ("UYAP UDF dosyasını nasıl açarım?", "UDF dosyasını Dosyalar, Mail ya da WhatsApp'tan FormlyConvert'e paylaş ve UDF'den PDF aracını seç. Sonucu PDF olarak kaydedip gönderebilirsin."),
            ("Hangi cihazlarda çalışır?", "iOS 17 ve sonrası yüklü iPhone ve iPad'de. iPad'de Apple Pencil ile not alabilirsin."),
            ("Sorun yaşarsam kime yazarım?", "Destek sayfasındaki adrese uygulama sürümünü ve sorunu kısaca yazman yeterli."),
        ],
        "cta_h": "Formi seni bekliyor.",
        "cta_p": "Köşesi kıvrık, kilden yumuşak bir kâğıt. İlk adımlarda yol gösterir, dönüştürme sürerken düşünür, iş bitince gülümser.",
        "mascot_alt": "Formi, FormlyConvert'in maskotu",
        "shot_alt": "FormlyConvert ekranı:",
    },
    "en": {
        "title": "FormlyConvert · PDF, Word, Excel and UDF converter",
        "description": "FormlyConvert: convert, compress, fill in and sign PDF, Word, Excel, PowerPoint, image and UDF files on iPhone and iPad. 39 document tools, conversions on your device.",
        "h1": "Every document task, in one app.",
        "lead": "Convert PDF, Word, Excel, PowerPoint, image and UDF files; compress, fill in and sign PDFs. Conversions happen on your iPhone or iPad; your files aren't uploaded to a server for it.",
        "store_meta": "Free · iPhone and iPad · iOS 17 or later",
        "facts": [("39", "document tools"), ("10+", "file formats"), ("On device", "conversions"), ("iOS 17+", "iPhone and iPad")],
        "formats_label": "Supported formats",
        "formats": ["PDF", "Word", "Excel", "PowerPoint", "JPG", "PNG", "HEIC", "HTML", "TXT", "UDF", "Audio and video"],
        "rows": [
            ("tools", "Convert", "Whatever format it arrives in.",
             "All 39 tools live on one screen in the Toolbox. Type to find the one you need and star the ones you use most.",
             ["PDF to Word, Excel, PowerPoint, JPG, PNG and text", "Word, Excel, PowerPoint, HTML and images to PDF", "UDF files to PDF in seconds", "Process several files at once"]),
            ("workspace", "Edit", "Pick a document, decide what's next.",
             "Every document opens in a workspace: see its pages, reorder them and choose your next step from there.",
             ["The form guide finds the fields in your PDF and walks you through them", "\"Fill with my details\" fills name, phone, email and address in one tap", "Draw your signature; add dates, check marks and QR codes", "Make scanned pages searchable with OCR"]),
            ("compress", "Compress and share", "Ready to send in a few taps.",
             "Choose the balance between size and quality. Text stays sharp; only image-heavy pages get lighter.",
             ["Compare before and after", "Send to Mail, WhatsApp or Files in one tap", "Follow long tasks on the Lock Screen and in the Dynamic Island", "Add watermarks, page numbers, stamps and passwords"]),
            ("library", "Library", "Every file organized, always at hand.",
             "Every document you convert is kept in the library by date and type. Sort them into folders and pin the important ones.",
             ["Search by file name, filter by type", "With Pro, sync between iPhone and iPad through iCloud", "Lock the app with Face ID", "Home Screen and Lock Screen widgets"]),
        ],
        "all_h": "Every tool, in four groups",
        "all_lead": "Tools are grouped by the job they do. Each opens on its own screen and shows what it will do first.",
        "groups": [
            ("Convert", ["PDF to Word", "PDF to Excel", "PDF to PowerPoint", "PDF to JPG and PNG", "PDF to text", "Word, Excel, PowerPoint to PDF", "HTML to PDF", "Images to PDF", "UDF to PDF"]),
            ("Edit", ["Merge", "Split", "Compress", "Rotate", "Organize pages", "Watermark", "Page numbers", "Bates numbering", "Stamp"]),
            ("Fill and protect", ["Fill forms", "Fill with my details", "Signature", "Protect", "Unlock", "Redact", "Repair", "Searchable PDF (OCR)"]),
            ("Smart tools", ["Document Assistant: summaries and Q&A", "Read aloud", "Audio and video to text", "Scan with camera", "Notes with Apple Pencil"]),
        ],
        "privacy_eyebrow": "Privacy",
        "privacy_h": "Your files stay with you.",
        "privacy_lead": "Conversions run on your phone. No account needed; your form details are stored on this device only.",
        "privacy_points": [("On-device conversion", "Your documents aren't uploaded to a server to be converted."), ("No account", "Download it and start right away."), ("On your device first", "The Document Assistant and transcription run on your device by default; nothing goes to the cloud unless you allow it.")],
        "privacy_link": "Read the privacy policy",
        "faq_h": "Frequently asked questions",
        "faq": [
            ("Is FormlyConvert free?", "You can download and use the app for free. Formly Pro gives you unlimited conversions without ads, with monthly, yearly and lifetime options. Subscriptions are managed in your App Store account settings."),
            ("Are my files uploaded to the internet?", "No. Converting, compressing and editing happen on your device; file content isn't uploaded to our servers. If you turn on iCloud sync, your library is stored in your own iCloud account."),
            ("How do I open a UDF file?", "Share the UDF file to FormlyConvert from Files, Mail or WhatsApp and choose the UDF to PDF tool. Save or send the result as a PDF."),
            ("Which devices does it run on?", "iPhone and iPad with iOS 17 or later. On iPad you can take notes with Apple Pencil."),
            ("Who do I contact if something goes wrong?", "Write to the address on the support page with your app version and a short description of the problem."),
        ],
        "cta_h": "Formi is waiting for you.",
        "cta_p": "A soft, clay-like sheet of paper with a folded corner. It shows you around at first, thinks while your file converts and smiles when it's done.",
        "mascot_alt": "Formi, the FormlyConvert mascot",
        "shot_alt": "FormlyConvert screen:",
    },
}

APPLE = '<svg aria-hidden="true" viewBox="0 0 384 512" width="20" height="24"><path fill="currentColor" d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>'


STORE_LABEL = {"tr": ("App Store'dan", "İndir"), "en": ("Download on the", "App Store")}


def store_button(lang: str, url: str = CONVERT_STORE) -> str:
    small, big = STORE_LABEL[lang]
    return f'<a class="store" href="{url}">{APPLE}<span><small>{small}</small>{big}</span></a>'


def phone(name: str, lang: str, eager: bool = False, app: str = "convert", alt: str = "") -> str:
    """App Store setinden kesilmiş ekran; assets/<app>/<name>-<lang>.jpg, 600 px genişlik."""
    height = {"convert": 1329, "bite": 1305}[app]
    alt = alt or f'{CONVERT[lang]["shot_alt"]} {name}'
    loading = "" if eager else ' loading="lazy"'
    return f'<div class="phone"><img src="/assets/{app}/{name}-{lang}.jpg" width="600" height="{height}" alt="{alt}"{loading} decoding="async"></div>'


def convert(lang: str) -> None:
    t = CONVERT[lang]
    facts = "".join(f"<li><strong>{n}</strong><span>{label}</span></li>" for n, label in t["facts"])
    formats = "".join(f"<li>{f}</li>" for f in t["formats"])
    rows = "".join(
        f'''<section class="pc-row">
<div class="pc-copy"><p class="eyebrow">{kicker}</p><h2>{h}</h2><p class="lead">{text}</p>
<ul class="checks">{"".join(f"<li>{b}</li>" for b in bullets)}</ul></div>
<div class="pc-shot">{phone(shot, lang)}</div>
</section>'''
        for shot, kicker, h, text, bullets in t["rows"]
    )
    groups = "".join(
        f'<div class="tool-group"><h3>{name}</h3><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>'
        for name, items in t["groups"]
    )
    points = "".join(f"<li><strong>{h}</strong><span>{p_}</span></li>" for h, p_ in t["privacy_points"])
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    body = f"""<section class="pc-hero"><div class="wrap">
<div class="pc-intro">
<p class="app-id"><img src="/assets/convert/icon.png" width="44" height="44" alt=""><span>FormlyConvert</span></p>
<h1>{t["h1"]}</h1>
<p class="lead">{t["lead"]}</p>
<div class="pc-cta">{store_button(lang)}<a class="button ghost" href="{p("convert-support", lang)}">{UI[lang]["support"]}</a></div>
<p class="store-meta">{t["store_meta"]}</p>
</div>
<div class="pc-stage" aria-hidden="false">
<div class="back">{phone("workspace", lang, eager=True)}</div>
<div class="front">{phone("tools", lang, eager=True)}</div>
<img class="pc-formi" src="/assets/formi.svg" alt="">
</div>
</div></section>
<div class="wrap">
<ul class="facts">{facts}</ul>
<div class="formats"><p>{t["formats_label"]}</p><ul>{formats}</ul></div>
{rows}
<section class="section tools-all">
<h2>{t["all_h"]}</h2>
<p class="lead">{t["all_lead"]}</p>
<div class="tool-groups">{groups}</div>
</section>
</div>
<section class="pc-privacy"><div class="wrap">
<div class="pc-copy"><p class="eyebrow">{t["privacy_eyebrow"]}</p><h2>{t["privacy_h"]}</h2><p class="lead">{t["privacy_lead"]}</p>
<ul class="points">{points}</ul>
<a class="more" href="{p("convert-privacy", lang)}">{t["privacy_link"]} →</a></div>
<div class="pc-shot">{phone("privacy", lang)}</div>
</div></section>
<div class="wrap">
<section class="section faq-list narrow">
<h2>{t["faq_h"]}</h2>
{faqs}
</section>
<section class="pc-final">
<img src="/assets/formi.svg" alt="{t["mascot_alt"]}" width="120" height="120">
<h2>{t["cta_h"]}</h2>
<p>{t["cta_p"]}</p>
{store_button(lang)}
</section>
</div>"""
    page("convert", lang, t["title"], t["description"], body, theme="convert")


# MARK: Destek

def support_hub(lang: str) -> None:
    t = {
        "tr": ("Destek", "Destek · Formly", "FormlyConvert, FormlyStudy ve FormlyBite için destek.", "Hangi uygulama için yardım istiyorsun?",
               "Dönüştürme, abonelik ve hesap soruları.", "FormlyConvert desteği",
               "Kartlar, tekrar, hesap ve abonelik soruları.", "FormlyStudy desteği"),
        "en": ("Support", "Support · Formly", "Support for FormlyConvert, FormlyStudy and FormlyBite.", "Which app do you need help with?",
               "Conversion, subscription and account questions.", "FormlyConvert support",
               "Cards, reviews, account and subscription questions.", "FormlyStudy support"),
    }[lang]
    body = f"""<div class="wrap narrow prose">
<h1>{t[0]}</h1>
<p class="meta">{t[3]}</p>
<div class="apps" style="grid-template-columns:1fr;padding:0">
<article class="app-card theme-convert"><div><h2>FormlyConvert</h2><p>{t[4]}</p></div><img class="mascot" src="/assets/formi.svg" alt=""><div class="actions"><a class="button primary" href="{p("convert-support", lang)}">{t[5]}</a></div></article>
<article class="app-card theme-study"><div><h2>FormlyStudy</h2><p>{t[6]}</p></div><img class="mascot" src="/assets/tabi.svg" alt=""><div class="actions"><a class="button primary" href="{p("study-support", lang)}">{t[7]}</a></div></article>
<article class="app-card theme-bite"><div><h2>FormlyBite</h2><p>{BITE[lang]["support_intro"]}</p></div><img class="mascot" src="/assets/muzi.svg" alt=""><div class="actions"><a class="button primary" href="{p("bite-support", lang)}">FormlyBite {UI[lang]["support"]}</a></div></article>
</div>
</div>"""
    page("support", lang, t[1], t[2], body)


def faq(items: list[tuple[str, str]]) -> str:
    return "".join(f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in items)


def study_support(lang: str) -> None:
    privacy = p("study-privacy", lang)
    if lang == "tr":
        title, description, h2 = "FormlyStudy Destek", "FormlyStudy için destek ve sık sorulan sorular.", "Sık sorulanlar"
        intro = f'Soru, hata bildirimi ya da öneri için <a href="mailto:{STUDY_MAIL}">{STUDY_MAIL}</a> adresine yaz. Genelde birkaç gün içinde yanıtlarız.'
        items = [
            ("Aboneliğimi nasıl iptal ederim?", "Abonelikler Apple üzerinden yönetilir. iPhone'da Ayarlar › [adın] › Abonelikler › FormlyStudy Pro'ya gir ya da uygulamada Ayarlar › Aboneliği yönet'e dokun. İptal ettiğinde Pro, dönem sonuna kadar açık kalır."),
            ("Satın aldığım Pro görünmüyor.", "Uygulamada Pro ekranındaki \"Satın alımları geri yükle\"ye dokun. Aynı Apple hesabıyla giriş yapmış olmalısın. Sorun sürerse bize yaz."),
            ("Hesabımı nasıl silerim?", "Ayarlar › Hesap › Hesabı sil. Hesabın ve ona bağlı sunucu kayıtları silinir; cihazındaki PDF'ler ve kartlar kalır. Uygulamaya giremiyorsan kayıtlı e-posta adresinden bize yaz, biz sileriz. Aboneliğin varsa onu ayrıca Apple'dan iptal etmelisin."),
            ("Kartlarım başka cihazımda görünmüyor.", "Kütüphanen, Pro ile açılan iCloud eşitleme sayesinde aynı Apple hesabındaki iPhone ve iPad'in arasında taşınır: Ayarlar › iCloud eşitleme. PDF'ler varsayılan olarak yalnız Wi-Fi'da eşitlenir."),
            ("Belgelerim nereye gönderiliyor?", f'Varsayılan olarak hiçbir yere; her şey cihazında hazırlanır. Bulutta hazırlamayı kendin seçersen yalnız gereken metin gönderilir. Ayrıntılar <a href="{privacy}">gizlilik politikasında</a>.'),
        ]
    else:
        title, description, h2 = "FormlyStudy Support", "Support and frequently asked questions for FormlyStudy.", "Frequently asked questions"
        intro = f'For questions, bug reports or suggestions, write to <a href="mailto:{STUDY_MAIL}">{STUDY_MAIL}</a>. We usually reply within a few days.'
        items = [
            ("How do I cancel my subscription?", "Subscriptions are managed by Apple. On your iPhone, go to Settings › [your name] › Subscriptions › FormlyStudy Pro, or tap Settings › Manage subscription in the app. After you cancel, Pro stays active until the end of the current period."),
            ("My Pro purchase doesn't show up.", "Tap \"Restore purchases\" on the Pro screen in the app. You need to be signed in with the same Apple Account. If the problem continues, write to us."),
            ("How do I delete my account?", "Settings › Account › Delete account. Your account and the server records linked to it are deleted; the PDFs and cards on your device stay. If you can't open the app, write to us from your registered email address and we'll delete it. If you have a subscription, cancel it separately with Apple."),
            ("My cards don't show up on my other device.", "With Pro, iCloud sync moves your library between the iPhone and iPad signed in to the same Apple Account: Settings › iCloud sync. By default, PDFs sync only over Wi-Fi."),
            ("Where are my documents sent?", f'Nowhere by default; everything is prepared on your device. If you choose to prepare something in the cloud, only the text that is needed is sent. Details are in the <a href="{privacy}">privacy policy</a>.'),
        ]
    body = f"""<div class="wrap narrow prose">
<h1>{title}</h1>
<p class="meta">{intro}</p>
<h2>{h2}</h2>
{faq(items)}</div>"""
    page("study-support", lang, title, description, body)


def convert_support(lang: str) -> None:
    privacy = p("convert-privacy", lang)
    if lang == "tr":
        title, description, h2 = "FormlyConvert Destek", "FormlyConvert için destek ve sık sorulan sorular.", "Sık sorulanlar"
        intro = f'Destek talepleri için <a href="mailto:{CONVERT_MAIL}">{CONVERT_MAIL}</a> adresine yaz. Lütfen uygulama sürümünü ve yaşadığın sorunu kısaca belirt.'
        items = [
            ("Aboneliğimi nasıl iptal ederim?", "Abonelikler Apple üzerinden yönetilir: iPhone'da Ayarlar › [adın] › Abonelikler › FormlyConvert. İptal ettiğinde Pro, dönem sonuna kadar açık kalır."),
            ("Satın aldığım Pro görünmüyor.", "Uygulamadaki Pro ekranından satın alımları geri yükle. Aynı Apple hesabıyla giriş yapmış olmalısın. Sorun sürerse bize yaz."),
            ("Dönüştürdüğüm dosyalar nerede?", "Dönüştürülen dosyalar uygulamanın Geçmiş bölümünde durur; oradan paylaşabilir ya da Dosyalar'a kaydedebilirsin."),
            ("Bir dosyayı başka uygulamadan nasıl açarım?", "Mail, WhatsApp ya da Dosyalar'da dosyaya uzun bas, Paylaş'ı seç ve FormlyConvert'i seç. Dosya, ona uygun araçlarla birlikte açılır."),
        ]
        legal = f'<a href="{privacy}">Gizlilik politikası</a> · Kullanım koşulları: <a href="{EULA}">Apple standart son kullanıcı sözleşmesi</a>.'
    else:
        title, description, h2 = "FormlyConvert Support", "Support and frequently asked questions for FormlyConvert.", "Frequently asked questions"
        intro = f'For support requests, write to <a href="mailto:{CONVERT_MAIL}">{CONVERT_MAIL}</a>. Please include your app version and a short description of the issue.'
        items = [
            ("How do I cancel my subscription?", "Subscriptions are managed by Apple: on your iPhone, go to Settings › [your name] › Subscriptions › FormlyConvert. After you cancel, Pro stays active until the end of the current period."),
            ("My Pro purchase doesn't show up.", "Restore your purchases from the Pro screen in the app. You need to be signed in with the same Apple Account. If the problem continues, write to us."),
            ("Where are my converted files?", "Converted files are kept in the app's History, where you can share them or save them to Files."),
            ("How do I open a file from another app?", "In Mail, WhatsApp or Files, touch and hold the file, choose Share, then choose FormlyConvert. The file opens with the tools that fit it."),
        ]
        legal = f'<a href="{privacy}">Privacy policy</a> · Terms of use: <a href="{EULA}">Apple Standard End User License Agreement</a>.'
    body = f"""<div class="wrap narrow prose">
<h1>{title}</h1>
<p class="meta">{intro}</p>
<h2>{h2}</h2>
{faq(items)}<p class="meta">{legal}</p>
</div>"""
    page("convert-support", lang, title, description, body, theme="convert")


# MARK: Gizlilik (Markdown'dan)

def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"(?<![\w/\">])([\w.+-]+@(?:formlyapps\.com|gmail\.com))", r'<a href="mailto:\1">\1</a>', text)
    return text


def markdown(source: str) -> tuple[str, str, str]:
    source = re.sub(r"<!--.*?-->", "", source, flags=re.S).strip()
    lines = source.splitlines()
    title, updated, out = "", "", []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("### "):
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith(("Son güncelleme:", "Last updated:")):
            updated = line.strip()
        elif line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            head, body = rows[0], rows[1:]
            table = ['<div class="table-wrap"><table><thead><tr>']
            table += [f"<th>{inline(c)}</th>" for c in head]
            table.append("</tr></thead><tbody>")
            for row in body:
                table.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
            table.append("</tbody></table></div>")
            out.append("".join(table))
            continue
        elif line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"<li>{inline(lines[i][2:])}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        else:
            para = [line.strip()]
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r"(#|- |\|)", lines[i + 1]):
                i += 1
                para.append(lines[i].strip())
            out.append(f"<p>{inline(' '.join(para))}</p>")
        i += 1
    return title, updated, "\n".join(out)


def privacy(source: Path, key: str, lang: str, description: str, theme: str, doc_lang: str | None = None, note: str = "") -> None:
    title, updated, body = markdown(source.read_text(encoding="utf-8"))
    for label in ("Kısaca:", "In short:"):
        body = body.replace(f"<p>{label}</p>\n<ul>", f'<div class="summary"><p><strong>{label.rstrip(":")}</strong></p><ul>', 1)
    if 'class="summary"' in body:
        start = body.index('class="summary"')
        end = body.index("</ul>", start) + len("</ul>")
        body = body[:end] + "</div>" + body[end:]
    note_html = f'<p class="meta" lang="{lang}">{note}</p>\n' if note else ""
    content = f'<div class="wrap narrow prose">\n{note_html}<h1>{inline(title)}</h1>\n<p class="meta">{inline(updated)}</p>\n{body}\n</div>'
    page(key, lang, title, description, content, theme=theme, doc_lang=doc_lang)


def study_privacy(lang: str) -> None:
    source = STUDY_REPO / "docs" / "legal" / f"privacy-policy-{lang}.md"
    description = {"tr": "FormlyStudy'nin hangi verileri işlediği ve senin seçeneklerin.",
                   "en": "Which data FormlyStudy processes and what choices you have."}[lang]
    privacy(source, "study-privacy", lang, description, "study")


def convert_privacy(lang: str) -> None:
    # FormlyConvert politikasının yalnız İngilizcesi var; Türkçe sayfa da aynı metni gösterir.
    note = "Bu politikanın şu an yalnız İngilizce sürümü var." if lang == "tr" else ""
    privacy(ROOT / "content" / "formlyconvert-privacy-en.md", "convert-privacy", lang,
            "How FormlyConvert handles documents and other data.", "convert", doc_lang="en", note=note)



# MARK: FormlyBite
# Ekranlar Figma'daki "App Store görselleri — tr/en" setinden (dosya 11GhXA67qZGXQiutt8PQiC, "Ekran" katmanları).
BITE = {
    "tr": {
        "title": "FormlyBite · Fotoğrafla kalori ve makro takibi",
        "description": "FormlyBite: öğününün fotoğrafını çek, kalori ve makroları Muzi hesaplasın. Barkod, yazı veya elle ekle; su, kilo ve ilerlemeni takip et.",
        "card": "Fotoğraf, barkod veya yazıyla öğün ekle; kalori, makro, su ve kilo geçmişini takip et. Yanında muz dostun Muzi.",
        "h1": "Fotoğrafını çek, gerisini Muzi hesaplasın.",
        "lead": "FormlyBite öğünlerini kaydetmeni ve kişisel hedeflerini takip etmeni kolaylaştırır. Fotoğraftan ya da yazdığın tariften kalori ve makro tahmini al, sonucu kendin düzenle.",
        "store_meta": "Ücretsiz · iPhone · iOS 17 ve sonrası",
        "facts": [("Fotoğraf", "barkod, yazı ya da elle"), ("Makrolar", "protein, karbonhidrat, yağ"), ("Su ve kilo", "günlük kayıt ve geçmiş"), ("Apple Sağlık", "isteğe bağlı bağlantı")],
        "rows": [
            ("meal", "Öğün analizi", "Bir fotoğraf, birkaç saniye.",
             "Tabağının fotoğrafını çek; Muzi yemeği tanır, malzemeleri ayırır, kalori ve makroları tahmin eder.",
             ["Malzeme dökümüyle kalori, protein, karbonhidrat ve yağ", "Porsiyonu ve malzemeleri kendin düzelt", "Kahvaltı, öğle, akşam ya da ara öğün olarak kaydet", "Sık yediklerini favorilere ekle"]),
            ("today", "Bugün", "Günün bir bakışta.",
             "Kalan kalorin, makro halkaların ve su kaydın tek ekranda. Geçmiş günlere üstteki takvimden dön.",
             ["Kişisel kalori ve makro hedefi", "Lif, şeker ve sodyum takibi", "Su kaydı tek dokunuşla", "İstersen hareketle yaktığın kaloriyi bütçene kat"]),
            ("add", "Ekle", "Nasıl istersen öyle ekle.",
             "Fotoğraf her zaman elinde olmayabilir. FormlyBite öğün eklemenin her yolunu bir arada sunar.",
             ["Fotoğraf çek ya da arşivden seç", "Paketli ürünlerde barkod okut, yemek ara", "Yediğini yazarak tarif et ya da elle gir", "Egzersizlerini de kaydet"]),
            ("widgets", "Widget'lar", "Muzi ana ekranında.",
             "Uygulamayı açmadan günün özetini gör; su widget'ından tek dokunuşla bardak ekle.",
             ["Kalan kalori ve makro özeti", "Su takibi widget'ı", "Öğün hatırlatmaları", "Günlük seriyle alışkanlık kur"]),
            ("progress", "İlerleme", "Değişimi gör.",
             "Kilonu kaydet, hedefine ne kadar yaklaştığını grafikte izle.",
             ["Kilo geçmişi ve hedef çizgisi", "Günlük seri ve vücut kitle indeksi", "Son 7 günün kalori ortalaması", "Kiloyu Apple Sağlık'tan oku ya da oraya yaz"]),
        ],
        "privacy_eyebrow": "Gizlilik",
        "privacy_h": "Günlüğün sende kalır.",
        "privacy_lead": "Öğünlerin, fotoğrafların ve kilo geçmişin cihazında tutulur; iCloud'a giriş yaptıysan kendi iCloud hesabına yedeklenir.",
        "privacy_points": [("Kayıt ekranı yok", "Hesap açmadan başlarsın; ad, e-posta ya da telefon istenmez."), ("Analizde yalnız gereken", "Analiz için sadece seçtiğin fotoğraf ya da tarif gönderilir; kişisel planın ve Apple Sağlık verin eklenmez."), ("Reklam yok", "Reklam göstermez, uygulamalar arası takip yapmaz, verini satmaz.")],
        "privacy_link": "Gizlilik politikasını oku",
        "faq_h": "Sık sorulanlar",
        "faq": [
            ("FormlyBite ücretsiz mi?", "İndirmek ve kullanmak ücretsiz; ücretsiz kullanımda günlük yapay zekâ analizi sınırlıdır. FormlyBite Pro ile fotoğraf ve yazıyla sınırsız analiz yaparsın. Aylık ve yıllık seçenekler uygulamada gösterilir."),
            ("Analiz nasıl çalışır?", "Fotoğraf veya yazılı tarif, Supabase sunucumuz üzerinden OpenAI’a iletilir. Sonuç bir tahmindir; porsiyon ve makroları kontrol ederek düzenleyebilirsin."),
            ("Kayıtlarım başka cihazımda görünür mü?", "iCloud’a giriş yaptıysan öğün günlüğün, fotoğrafların ve kilo geçmişin kendi iCloud hesabına yedeklenir ve aynı Apple hesabını kullanan cihazlarında görünür."),
            ("Aboneliğimi nasıl yönetirim?", "iPhone’da Ayarlar › [adın] › Abonelikler üzerinden yönetebilir veya iptal edebilirsin. Uygulamadaki geri yükleme seçeneğini aynı Apple hesabıyla kullan."),
            ("Apple Sağlık iznini nasıl kaldırırım?", "Sağlık uygulamasındaki profilinden Uygulamalar › FormlyBite bölümüne git ve izinleri kapat. Sağlık’a önceden yazılmış kilo kayıtları ayrıca Sağlık uygulamasından yönetilir."),
            ("Verilerimi nasıl silerim?", "Uygulamada Ayarlar’daki “Verilerimi sil” cihazdaki kayıtları, iCloud yedeğini ve sunucudaki anonim hesabı siler. Başka bir talebin için destek adresine FormlyBite başlığıyla yaz."),
        ],
        "notice": "Kalori, makro ve öğün puanı tahmindir; malzemeye ve porsiyona göre değişebilir. FormlyBite tıbbi tavsiyenin ya da diyetisyen desteğinin yerini tutmaz.",
        "cta_h": "Merhaba, ben Muzi.",
        "cta_p": "Biraz kayıtsız görünürüm ama hesabı hiç kaçırmam. Önce sana uygun bir plan çıkaralım, sonra tabağını göster.",
        "support_intro": "Öğün analizi, günlük, Apple Sağlık ve abonelik soruları.",
        "shot_alt": "FormlyBite ekranı:",
    },
    "en": {
        "title": "FormlyBite · Calorie and macro tracking from a photo",
        "description": "FormlyBite: snap a photo of your meal and let Muzi estimate calories and macros. Add by barcode, text or by hand; track water, weight and progress.",
        "card": "Add meals with photos, barcodes or text; track calories, macros, water and weight. With Muzi, your banana friend.",
        "h1": "Snap a photo. Muzi does the maths.",
        "lead": "FormlyBite makes it easy to log meals and follow your personal goals. Get calorie and macro estimates from a photo or a written description, then adjust the result yourself.",
        "store_meta": "Free · iPhone · iOS 17 or later",
        "facts": [("Photo", "barcode, text or by hand"), ("Macros", "protein, carbs, fat"), ("Water and weight", "daily entries and history"), ("Apple Health", "optional connection")],
        "rows": [
            ("meal", "Meal analysis", "One photo, a few seconds.",
             "Take a photo of your plate; Muzi recognizes the dish, breaks down the ingredients and estimates calories and macros.",
             ["Calories, protein, carbs and fat with an ingredient breakdown", "Adjust portions and ingredients yourself", "Log it as breakfast, lunch, dinner or a snack", "Save the meals you eat often as favourites"]),
            ("today", "Today", "Your day at a glance.",
             "Calories left, macro rings and water on one screen. Jump back to past days from the calendar at the top.",
             ["Personal calorie and macro goals", "Fibre, sugar and sodium tracking", "Log water in one tap", "Optionally add calories burned through activity to your budget"]),
            ("add", "Add", "Log it your way.",
             "You won't always have a photo. FormlyBite puts every way to add a meal in one place.",
             ["Take a photo or pick one from your library", "Scan packaged food barcodes or search for foods", "Describe your meal in words or enter it by hand", "Log your exercise too"]),
            ("widgets", "Widgets", "Muzi on your Home Screen.",
             "See your day without opening the app, and add a glass of water straight from the widget.",
             ["Calories left and macro summary", "Water tracking widget", "Meal reminders", "Build a habit with daily streaks"]),
            ("progress", "Progress", "See the change.",
             "Log your weight and watch how close you are to your goal on the chart.",
             ["Weight history with your goal line", "Daily streak and BMI", "Average calories over the last 7 days", "Read weight from Apple Health or save it there"]),
        ],
        "privacy_eyebrow": "Privacy",
        "privacy_h": "Your diary stays with you.",
        "privacy_lead": "Your meals, photos and weight history are kept on your device and, if you're signed in to iCloud, backed up to your own iCloud account.",
        "privacy_points": [("No sign-up screen", "Start without an account; no name, email or phone number needed."), ("Only what's needed", "Analysis sends just the photo or description you chose; your personal plan and Apple Health data aren't included."), ("No ads", "No ads, no cross-app tracking, and your data is never sold.")],
        "privacy_link": "Read the privacy policy",
        "faq_h": "Frequently asked questions",
        "faq": [
            ("Is FormlyBite free?", "It's free to download and use; free use includes a daily limit on AI meal analyses. FormlyBite Pro unlocks unlimited photo and text analysis. Monthly and annual options are shown in the app."),
            ("How does analysis work?", "A photo or written description is sent through our Supabase server to OpenAI. Results are estimates; review portions and adjust macros before relying on them."),
            ("Will my entries appear on another device?", "If you're signed in to iCloud, your food diary, photos and weight history are backed up to your own iCloud account and show up on devices using the same Apple Account."),
            ("How do I manage my subscription?", "Manage or cancel it in iPhone Settings › [your name] › Subscriptions. Use Restore purchases in the app with the same Apple Account."),
            ("How do I revoke Apple Health access?", "In the Health app, open your profile, then Apps › FormlyBite and turn off permissions. Weight entries already written to Health are managed separately in the Health app."),
            ("How do I delete my data?", "In the app, “Delete my data” in Settings removes the entries on your device, your iCloud backup and the anonymous account on our server. For any other request, email support with FormlyBite in the subject."),
        ],
        "notice": "Calories, macros and meal scores are estimates and may vary with ingredients and portion sizes. FormlyBite does not replace medical advice or guidance from a qualified dietitian.",
        "cta_h": "Hi, I’m Muzi.",
        "cta_p": "I may look unimpressed, but I never lose count. Let’s build a plan that fits you first, then show me your plate.",
        "support_intro": "Questions about meal analysis, your diary, Apple Health and subscriptions.",
        "shot_alt": "FormlyBite screen:",
    },
}


def bite(lang: str) -> None:
    t = BITE[lang]
    shot = lambda name, eager=False: phone(name, lang, eager, app="bite", alt=f'{t["shot_alt"]} {name}')
    facts = "".join(f"<li><strong>{n}</strong><span>{label}</span></li>" for n, label in t["facts"])
    rows = "".join(
        f'''<section class="pc-row">
<div class="pc-copy"><p class="eyebrow">{kicker}</p><h2>{h}</h2><p class="lead">{text}</p>
<ul class="checks">{"".join(f"<li>{b}</li>" for b in bullets)}</ul></div>
<div class="pc-shot">{shot(name)}</div>
</section>'''
        for name, kicker, h, text, bullets in t["rows"]
    )
    points = "".join(f"<li><strong>{h}</strong><span>{p_}</span></li>" for h, p_ in t["privacy_points"])
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    body = f"""<section class="pc-hero bite-hero"><div class="wrap">
<div class="pc-intro">
<p class="app-id"><img src="/assets/bite/icon.png" width="44" height="44" alt=""><span>FormlyBite</span></p>
<h1>{t["h1"]}</h1>
<p class="lead">{t["lead"]}</p>
<div class="pc-cta">{store_button(lang, BITE_STORE)}<a class="button ghost" href="{p("bite-support", lang)}">{UI[lang]["support"]}</a></div>
<p class="store-meta">{t["store_meta"]}</p>
</div>
<div class="pc-stage">
<div class="back">{shot("today", True)}</div>
<div class="front">{shot("meal", True)}</div>
<img class="pc-muzi" src="/assets/muzi.svg" alt="">
</div>
</div></section>
<div class="wrap">
<ul class="facts">{facts}</ul>
{rows}
<p class="notice">{t["notice"]}</p>
</div>
<section class="pc-privacy"><div class="wrap">
<div class="pc-copy"><p class="eyebrow">{t["privacy_eyebrow"]}</p><h2>{t["privacy_h"]}</h2><p class="lead">{t["privacy_lead"]}</p>
<ul class="points">{points}</ul>
<a class="more" href="{p("bite-privacy", lang)}">{t["privacy_link"]} →</a></div>
<div class="pc-shot">{shot("hello")}</div>
</div></section>
<div class="wrap">
<section class="section faq-list narrow">
<h2>{t["faq_h"]}</h2>
{faqs}
</section>
<section class="pc-final">
<img src="/assets/muzi-happy.svg" alt="Muzi" width="90" height="176">
<h2>{t["cta_h"]}</h2>
<p>{t["cta_p"]}</p>
{store_button(lang, BITE_STORE)}
</section>
</div>"""
    page("bite", lang, t["title"], t["description"], body, theme="bite")


def bite_support(lang: str) -> None:
    t = BITE[lang]
    title = "FormlyBite " + UI[lang]["support"]
    body = f'''<div class="wrap narrow prose"><h1>{title}</h1><p class="meta">{t["support_intro"]}</p><p><a href="mailto:{STUDY_MAIL}?subject=FormlyBite">{STUDY_MAIL}</a></p>{faq(t["faq"])}<p><a href="{p("bite-privacy", lang)}">{UI[lang]["privacy"]}</a> · <a href="{EULA}">{UI[lang]["terms"]}</a></p></div>'''
    page("bite-support", lang, title, t["support_intro"], body, theme="bite")


def bite_privacy(lang: str) -> None:
    privacy(ROOT / "content" / f"formlybite-privacy-{lang}.md", "bite-privacy", lang,
            BITE[lang]["support_intro"], "bite")


if __name__ == "__main__":
    for lang in ("tr", "en"):
        home(lang)
        study(lang)
        convert(lang)
        support_hub(lang)
        study_support(lang)
        convert_support(lang)
        study_privacy(lang)
        convert_privacy(lang)
        bite(lang)
        bite_support(lang)
        bite_privacy(lang)
