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
<div><span class="badge">{t["soon"]}</span><h2>FormlyBite</h2><p>{BITE[lang]["card"]}</p></div>
<img class="mascot app-icon" src="/assets/formlybite.png" alt="Çilek">
<div class="actions"><a class="button primary" href="{p("bite", lang)}">{t["meet"]}</a><a class="button secondary" href="{p("bite-privacy", lang)}">{UI[lang]["privacy"]}</a></div>
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

CONVERT = {
    "tr": {
        "title": "FormlyConvert · Belge dönüştürücü",
        "description": "FormlyConvert: PDF, Word, Excel, PowerPoint, görsel ve UDF dönüştürme; sıkıştırma, doldurma ve imzalama.",
        "eyebrow": "FormlyConvert · App Store'da",
        "h1": "Dosyan hangi biçimde olursa olsun.",
        "lead": "FormlyConvert belgelerini birkaç dokunuşla dönüştürür ve düzenler. PDF'leri sıkıştırır, doldurur ve imzalar; belgeni özetler, kayıtlarını metne çevirir.",
        "mascot_alt": "Formi, FormlyConvert'in maskotu",
        "open_store": "App Store'da aç",
        "features": "Neler yapar?",
        "tiles": [
            ("⇄", "Dönüştürme", "PDF, Word, Excel, PowerPoint, görsel, metin ve UDF arasında dönüştürür; işlem cihazında yapılır."),
            ("↓", "Sıkıştır, doldur, imzala", "PDF'i küçültür, form alanlarını doldurur, tarih ve imzanı ekler."),
            ("?", "Belge asistanı", "PDF'ini özetler, sorularını yanıtlar; taranmış sayfaları da okur. Varsayılan olarak cihazında çalışır."),
            ("♪", "Ses ve videodan metin", "Kayıttaki konuşmayı PDF, Word ya da metin dosyasına çevirir."),
            ("☁", "iCloud kütüphanesi", "Pro ile kütüphanen aynı Apple hesabındaki cihazlarında görünür."),
            ("▦", "Widget ve paylaşım", "Son dosyaların ana ekranda; başka uygulamadan paylaşılan dosya doğrudan FormlyConvert'e gelir."),
        ],
        "meet_h": "Formi ile tanış",
        "meet": "Formi, köşesi kıvrık, kilden yumuşak bir kâğıt. Sakin ve biraz esprili; dönüştürme sürerken düşünür, iş bitince gülümser.",
    },
    "en": {
        "title": "FormlyConvert · Document converter",
        "description": "FormlyConvert: convert PDF, Word, Excel, PowerPoint, image and UDF files; compress, fill in and sign PDFs.",
        "eyebrow": "FormlyConvert · On the App Store",
        "h1": "Whatever format your file is in.",
        "lead": "FormlyConvert converts and edits your documents in a few taps. It compresses, fills in and signs PDFs, summarizes your documents and turns recordings into text.",
        "mascot_alt": "Formi, the FormlyConvert mascot",
        "open_store": "Open in the App Store",
        "features": "What it does",
        "tiles": [
            ("⇄", "Conversion", "Converts between PDF, Word, Excel, PowerPoint, image, text and UDF, right on your device."),
            ("↓", "Compress, fill, sign", "Shrinks PDFs, fills in form fields, and adds dates and your signature."),
            ("?", "Document Assistant", "Summarizes your PDF and answers your questions, scanned pages included. Runs on your device by default."),
            ("♪", "Audio and video to text", "Turns the speech in a recording into a PDF, Word or text file."),
            ("☁", "iCloud Library", "With Pro, your library shows up on all devices signed in to the same Apple Account."),
            ("▦", "Widgets and sharing", "Your recent files on the Home Screen; files shared from other apps go straight to FormlyConvert."),
        ],
        "meet_h": "Meet Formi",
        "meet": "Formi is a soft, clay-like sheet of paper with a folded corner. Calm and a little witty, it thinks while your file converts and smiles when it's done.",
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


def convert(lang: str) -> None:
    t = CONVERT[lang]
    body = f"""<div class="wrap">
<section class="app-hero">
<div>
<p class="eyebrow">{t["eyebrow"]}</p>
<h1>{t["h1"]}</h1>
<p class="lead">{t["lead"]}</p>
<a class="button primary" href="{CONVERT_STORE}">{t["open_store"]}</a> <a class="button ghost" href="{p("convert-support", lang)}">{UI[lang]["support"]}</a> <a class="button ghost" href="{p("convert-privacy", lang)}">{UI[lang]["privacy"]}</a>
</div>
<img class="mascot" src="/assets/formi.svg" alt="{t["mascot_alt"]}">
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
<article class="app-card theme-bite"><div><h2>FormlyBite</h2><p>{BITE[lang]["support_intro"]}</p></div><img class="mascot app-icon" src="/assets/formlybite.png" alt=""><div class="actions"><a class="button primary" href="{p("bite-support", lang)}">FormlyBite {UI[lang]["support"]}</a></div></article>
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
BITE = {
    "tr": {
        "title": "FormlyBite · Öğün günlüğün", "soon": "FormlyBite · Yakında · iPhone",
        "h1": "Öğünlerini tanı, gününü takip et.",
        "card": "Fotoğraf, barkod veya yazıyla öğün ekle; kalori, makro, su ve kilo geçmişini takip et. Yanında çilek dostun Çilek.",
        "lead": "FormlyBite, öğünlerini kaydetmene ve kişisel hedeflerini takip etmene yardımcı olur. Fotoğraf veya yazılı tariften kalori ve makro tahmini alabilir, sonuçları kendin düzenleyebilirsin.",
        "features": "Neler yapar?", "support_intro": "Öğün analizi, günlük, Apple Sağlık ve abonelik soruları.",
        "tiles": [("+", "Öğün ekleme", "Fotoğraf, barkod, yazılı tarif, favoriler veya elle giriş. Tahminleri incele ve düzelt."), ("○", "Günlük hedefler", "Kişisel plan, kalori ve makro takibi; su kaydı ve öğün hatırlatmaları."), ("↗", "İlerleme", "Kilo geçmişi, günlük seri ve haftalık kalori görünümü. İsteğe bağlı Apple Sağlık bağlantısı.")],
        "notice": "Kalori, makro ve öğün puanı tahmindir; tıbbi tavsiye veya kişiye özel tedavi değildir.",
        "faq": [("Analiz nasıl çalışır?", "Fotoğraf veya yazılı tarif, Supabase sunucumuz üzerinden OpenAI’a iletilir. Sonuç bir tahmindir; porsiyon ve makroları kontrol ederek düzenleyebilirsin."), ("Kayıtlarım başka cihazımda görünür mü?", "Şu anda öğün günlüğü, kilo geçmişi ve favoriler bu cihazda tutulur. Hesapla yedekleme ve cihazlar arası eşitleme bulunmaz. Uygulamayı silmek yerel kayıtları kaldırır."), ("Aboneliğimi nasıl yönetirim?", "iPhone’da Ayarlar › [adın] › Abonelikler üzerinden yönetebilir veya iptal edebilirsin. Uygulamadaki geri yükleme seçeneğini aynı Apple hesabıyla kullan."), ("Apple Sağlık iznini nasıl kaldırırım?", "Sağlık uygulamasındaki profilinden Uygulamalar › FormlyBite bölümüne git ve izinleri kapat. Sağlık’a önceden yazılmış kilo kayıtları ayrıca Sağlık uygulamasından yönetilir."), ("Verilerimle ilgili talepte nasıl bulunurum?", "Aşağıdaki destek adresine FormlyBite başlığıyla yaz. Anonim sunucu kayıtlarının sana ait olduğunu doğrulayabilmek için gereken teknik bilgileri birlikte belirleriz. E-postana öğün fotoğrafı veya sağlık geçmişi eklemen gerekmez.")],
    },
    "en": {
        "title": "FormlyBite · Your food diary", "soon": "FormlyBite · Coming soon · iPhone",
        "h1": "Know your meals. Follow your day.",
        "card": "Add meals with photos, barcodes or text; track calories, macros, water and weight. With Çilek, your strawberry friend.",
        "lead": "FormlyBite helps you record meals and follow personal goals. Get calorie and macro estimates from a photo or written description, then review and adjust the results yourself.",
        "features": "What it does", "support_intro": "Questions about meal analysis, your diary, Apple Health and subscriptions.",
        "tiles": [("+", "Add meals", "Photos, barcodes, written descriptions, favourites or manual entry. Review and correct estimates."), ("○", "Daily goals", "A personal plan, calorie and macro tracking, water entries and meal reminders."), ("↗", "Progress", "Weight history, daily streaks and a weekly calorie view. Optional Apple Health connection.")],
        "notice": "Calories, macros and meal scores are estimates, not medical advice or personalised treatment.",
        "faq": [("How does analysis work?", "A photo or written description is sent through our Supabase server to OpenAI. Results are estimates; review portions and adjust macros before relying on them."), ("Will my entries appear on another device?", "Your food diary, weight history and favourites are currently stored on this device. Account backup and cross-device sync are not available. Deleting the app removes local entries."), ("How do I manage my subscription?", "Manage or cancel it in iPhone Settings › [your name] › Subscriptions. Use Restore purchases in the app with the same Apple Account."), ("How do I revoke Apple Health access?", "In the Health app, open your profile, then Apps › FormlyBite and turn off permissions. Weight entries already written to Health are managed separately in the Health app."), ("How do I make a data request?", "Email the support address below with FormlyBite in the subject. We will work with you to identify the technical information needed to verify ownership of anonymous server records. You do not need to attach meal photos or health history.")],
    },
}


def bite(lang: str) -> None:
    t = BITE[lang]
    body = f'''<div class="wrap">
<section class="app-hero"><div><p class="eyebrow">{t["soon"]}</p><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p><a class="button primary" href="{p("bite-support", lang)}">{UI[lang]["support"]}</a> <a class="button ghost" href="{p("bite-privacy", lang)}">{UI[lang]["privacy"]}</a></div><img class="mascot app-icon" src="/assets/formlybite.png" alt="Çilek"></section>
<section class="section"><h2>{t["features"]}</h2>{tiles(t["tiles"])}</section><p class="meta">{t["notice"]}</p></div>'''
    page("bite", lang, t["title"], t["card"], body, theme="bite")


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
