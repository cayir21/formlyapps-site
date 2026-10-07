#!/usr/bin/env python3
"""formlyapps.com sayfalarını üretir (paket gerektirmez).

Kullanım: python3 scripts/build.py [FormlyStudy reposunun yolu]
Varsayılan yol: ../İOS/FormlyStudy. Gizlilik politikası oradaki
docs/legal/privacy-policy-tr.md'den üretilir; diğer sayfalar bu dosyada tanımlıdır.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STUDY_REPO = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "İOS" / "FormlyStudy"

CONVERT_STORE = "https://apps.apple.com/app/id6759096094"
STUDY_MAIL = "destek@formlyapps.com"
CONVERT_MAIL = "formlyconvert@gmail.com"


# MARK: Şablon

def page(path: str, title: str, description: str, body: str, theme: str = "study") -> None:
    nav = [
        ("/formlystudy/", "FormlyStudy"),
        ("/formlyconvert/", "FormlyConvert"),
        ("/destek/", "Destek"),
    ]
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if path.startswith(href) else ""}>{label}</a>'
        for href, label in nav
    )
    document = f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="theme-color" content="#F5F1EA" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1E1A16" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/assets/formi.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
</head>
<body class="theme-{theme}">
<header class="site-header"><div class="wrap">
<a class="brand" href="/"><span class="marks"><img src="/assets/formi.svg" alt=""><img src="/assets/tabi.svg" alt=""></span><span>Formly</span></a>
<nav aria-label="Ana menü">{links}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site-footer"><div class="wrap">
<span>© 2026 Süleyman Çayır</span>
<nav aria-label="Alt menü">
<a href="/formlystudy/gizlilik/">FormlyStudy gizlilik</a>
<a href="/formlystudy/destek/">FormlyStudy destek</a>
<a href="/formlyconvert/destek/">FormlyConvert destek</a>
<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Kullanım koşulları</a>
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


# MARK: Sayfalar

def home() -> None:
    body = f"""<div class="wrap">
<section class="hero">
<div>
<p class="eyebrow">Formly</p>
<h1>Belgelerin için iki küçük yardımcı.</h1>
<p class="lead">FormlyConvert dosyalarını dönüştürür, FormlyStudy onlardan öğrenmeni sağlar. İkisi de iPhone ve iPad için; sade, sakin ve gizliliğine saygılı.</p>
<a class="button primary" href="#uygulamalar">Uygulamaları gör</a>
</div>
<div class="mascots" aria-hidden="true"><img class="formi" src="/assets/formi.svg" alt=""><img class="tabi" src="/assets/tabi.svg" alt=""></div>
</section>
<section class="apps" id="uygulamalar">
<article class="app-card theme-convert">
<div><span class="badge">App Store'da</span><h2>FormlyConvert</h2>
<p>PDF, Word, Excel, PowerPoint, görsel ve UDF dosyalarını dönüştürür; PDF'leri sıkıştırır, doldurur ve imzalar. Yanında kâğıttan dostu Formi.</p></div>
<img class="mascot" src="/assets/formi.svg" alt="Formi">
<div class="actions"><a class="button primary" href="{CONVERT_STORE}">App Store'da aç</a><a class="button secondary" href="/formlyconvert/">Tanı</a></div>
</article>
<article class="app-card theme-study">
<div><span class="badge">Yakında</span><h2>FormlyStudy</h2>
<p>PDF'lerinden kaynak bağlantılı kartlar, testler, özetler ve zihin haritaları hazırlar; ne zaman tekrar edeceğini de söyler. Yanında ayraç dostu Tabi.</p></div>
<img class="mascot" src="/assets/tabi.svg" alt="Tabi">
<div class="actions"><a class="button primary" href="/formlystudy/">Tanı</a><a class="button secondary" href="/formlystudy/gizlilik/">Gizlilik</a></div>
</article>
</section>
<section class="section">
<h2>Nasıl yapıyoruz?</h2>
{tiles([
    ("1", "Önce cihazında", "Belgelerin varsayılan olarak cihazında işlenir. Buluta gönderme yalnız sen istediğinde olur."),
    ("2", "Hesap şart değil", "İki uygulamayı da hesap açmadan kullanabilirsin. Hesap yalnız ek özellikler için."),
    ("3", "Küçük ve odaklı", "Her uygulama tek bir işi iyi yapmaya çalışır. Gereksiz ekran, gereksiz izin yok."),
])}
</section>
</div>"""
    page("/", "Formly · FormlyConvert ve FormlyStudy", "FormlyConvert ve FormlyStudy: belgelerin için iki küçük iPhone ve iPad uygulaması.", body)


def study() -> None:
    body = f"""<div class="wrap">
<section class="app-hero">
<div>
<p class="eyebrow">FormlyStudy · Yakında App Store'da</p>
<h1>PDF'lerinden öğren, kaynağından kopmadan.</h1>
<p class="lead">FormlyStudy notlarından ve ders kitaplarından çalışma kartları, testler, özetler ve zihin haritaları hazırlar. Her kart PDF'teki satırına bağlıdır; bir dokunuşla kaynağını görürsün.</p>
<a class="button primary" href="/formlystudy/destek/">Destek</a> <a class="button ghost" href="/formlystudy/gizlilik/">Gizlilik</a>
</div>
<img class="mascot" src="/assets/tabi.svg" alt="Tabi, FormlyStudy'nin maskotu">
</section>
<section class="section">
<h2>Neler yapar?</h2>
{tiles([
    ("K", "Kaynak bağlantılı kartlar", "Kartlar geldiği sayfa ve satırla eşleşir; desteye eklemeden önce gözden geçirirsin."),
    ("T", "Akıllı tekrar", "Hatırlama gücüne göre ne zaman tekrar edeceğini planlar; sınav tarihine göre hızlanır."),
    ("Q", "Test ve özet", "Konuyu sınayan çoktan seçmeli sorular ve kaynak sayfalı özetler hazırlar."),
    ("H", "Zihin haritası", "Ana başlıkları ve kavramları canlı bir haritada bir araya getirir."),
    ("C", "Önce cihazında", "Yapay zekâ varsayılan olarak cihazında çalışır; istersen bulutta hazırlatırsın."),
    ("i", "iPhone ve iPad", "Pro ile kütüphanen iCloud üzerinden cihazların arasında eşitlenir."),
])}
</section>
<section class="section">
<h2>Tabi ile tanış</h2>
<p class="lead">Tabi, kitabının arasında yerini tutan turuncu kurdele ayraç. Kartların hazırlanırken bekler, serini korursan sevinir, unuttuğun kartı sana hatırlatır.</p>
</section>
</div>"""
    page("/formlystudy/", "FormlyStudy · PDF'lerinden öğren", "FormlyStudy: PDF'lerinden kaynak bağlantılı kartlar, testler, özetler ve zihin haritaları.", body)


def convert() -> None:
    body = f"""<div class="wrap">
<section class="app-hero">
<div>
<p class="eyebrow">FormlyConvert · App Store'da</p>
<h1>Dosyan hangi biçimde olursa olsun.</h1>
<p class="lead">FormlyConvert belgelerini birkaç dokunuşla dönüştürür ve düzenler. PDF'leri sıkıştırır, formları doldurur, imzalar; dışarıdan gelen dosyaları "Formly ile aç" ile doğrudan karşılar.</p>
<a class="button primary" href="{CONVERT_STORE}">App Store'da aç</a> <a class="button ghost" href="/formlyconvert/destek/">Destek</a>
</div>
<img class="mascot" src="/assets/formi.svg" alt="Formi, FormlyConvert'in maskotu">
</section>
<section class="section">
<h2>Neler yapar?</h2>
{tiles([
    ("⇄", "Dönüştürme", "PDF, Word, Excel, PowerPoint, görsel, metin ve UDF arasında dönüştürür."),
    ("↓", "Akıllı sıkıştırma", "PDF'i küçültür; metin ve bağlantılar korunur, dosya asla büyümez."),
    ("✎", "Doldur ve imzala", "Form alanlarını doldurur, tarih, işaret ve imzanı ekler."),
    ("A", "Metin tanıma", "Taranmış belgelerdeki metni okunabilir hâle getirir."),
    ("◎", "Tam ekran görüntüleyici", "Sayfalar, arama ve hızlı gezinme ile belgeni rahatça okursun."),
    ("↗", "Formly ile aç", "Mail ya da Dosyalar'dan gelen dosya doğrudan FormlyConvert'te açılır."),
])}
</section>
<section class="section">
<h2>Formi ile tanış</h2>
<p class="lead">Formi, köşesi kıvrık, kilden yumuşak bir kâğıt. Sakin ve biraz esprili; dönüştürme sürerken düşünür, iş bitince gülümser.</p>
</section>
</div>"""
    page("/formlyconvert/", "FormlyConvert · Belge dönüştürücü", "FormlyConvert: PDF, Word, Excel, PowerPoint, görsel ve UDF dönüştürme; sıkıştırma, doldurma ve imzalama.", body, theme="convert")


def support_hub() -> None:
    body = f"""<div class="wrap narrow prose">
<h1>Destek</h1>
<p class="meta">Hangi uygulama için yardım istiyorsun?</p>
<div class="apps" style="grid-template-columns:1fr;padding:0">
<article class="app-card theme-convert"><div><h2>FormlyConvert</h2><p>Dönüştürme, abonelik ve hesap soruları.</p></div><img class="mascot" src="/assets/formi.svg" alt=""><div class="actions"><a class="button primary" href="/formlyconvert/destek/">FormlyConvert desteği</a></div></article>
<article class="app-card theme-study"><div><h2>FormlyStudy</h2><p>Kartlar, tekrar, hesap ve abonelik soruları.</p></div><img class="mascot" src="/assets/tabi.svg" alt=""><div class="actions"><a class="button primary" href="/formlystudy/destek/">FormlyStudy desteği</a></div></article>
</div>
</div>"""
    page("/destek/", "Destek · Formly", "FormlyConvert ve FormlyStudy için destek.", body)


def study_support() -> None:
    body = f"""<div class="wrap narrow prose">
<h1>FormlyStudy Destek</h1>
<p class="meta">Soru, hata bildirimi ya da öneri için <a href="mailto:{STUDY_MAIL}">{STUDY_MAIL}</a> adresine yaz. Genelde birkaç gün içinde yanıtlarız.</p>
<h2>Sık sorulanlar</h2>
<h3>Aboneliğimi nasıl iptal ederim?</h3>
<p>Abonelikler Apple üzerinden yönetilir. iPhone'da Ayarlar › [adın] › Abonelikler › FormlyStudy Pro'ya gir ya da uygulamada Ayarlar › Aboneliği yönet'e dokun. İptal ettiğinde Pro, dönem sonuna kadar açık kalır.</p>
<h3>Satın aldığım Pro görünmüyor.</h3>
<p>Uygulamada Pro ekranındaki "Satın alımları geri yükle"ye dokun. Aynı Apple hesabıyla giriş yapmış olmalısın. Sorun sürerse bize yaz.</p>
<h3>Hesabımı nasıl silerim?</h3>
<p>Ayarlar › Hesap › Hesabı sil. Hesabın ve ona bağlı sunucu kayıtları silinir; cihazındaki PDF'ler ve kartlar kalır. Uygulamaya giremiyorsan kayıtlı e-posta adresinden bize yaz, biz sileriz. Aboneliğin varsa onu ayrıca Apple'dan iptal etmelisin.</p>
<h3>Kartlarım başka cihazımda görünmüyor.</h3>
<p>Kütüphanen, Pro ile açılan iCloud eşitleme sayesinde aynı Apple hesabındaki iPhone ve iPad'in arasında taşınır: Ayarlar › iCloud eşitleme. PDF'ler varsayılan olarak yalnız Wi-Fi'da eşitlenir.</p>
<h3>Belgelerim nereye gönderiliyor?</h3>
<p>Varsayılan olarak hiçbir yere; her şey cihazında hazırlanır. Bulutta hazırlamayı kendin seçersen yalnız gereken metin gönderilir. Ayrıntılar <a href="/formlystudy/gizlilik/">gizlilik politikasında</a>.</p>
</div>"""
    page("/formlystudy/destek/", "FormlyStudy Destek", "FormlyStudy için destek ve sık sorulan sorular.", body)


def convert_support() -> None:
    body = f"""<div class="wrap narrow prose">
<h1>FormlyConvert Destek</h1>
<p class="meta">Destek talepleri için <a href="mailto:{CONVERT_MAIL}">{CONVERT_MAIL}</a> adresine yaz. Lütfen uygulama sürümünü ve yaşadığın sorunu kısaca belirt.</p>
<h2>Sık sorulanlar</h2>
<h3>Aboneliğimi nasıl iptal ederim?</h3>
<p>Abonelikler Apple üzerinden yönetilir: iPhone'da Ayarlar › [adın] › Abonelikler › FormlyConvert. İptal ettiğinde Pro, dönem sonuna kadar açık kalır.</p>
<h3>Satın aldığım Pro görünmüyor.</h3>
<p>Uygulamadaki Pro ekranından satın alımları geri yükle. Aynı Apple hesabıyla giriş yapmış olmalısın. Sorun sürerse bize yaz.</p>
<h3>Dönüştürdüğüm dosyalar nerede?</h3>
<p>Dönüştürülen dosyalar uygulamanın Geçmiş bölümünde durur; oradan paylaşabilir ya da Dosyalar'a kaydedebilirsin.</p>
<h3>Bir dosyayı başka uygulamadan nasıl açarım?</h3>
<p>Mail, WhatsApp ya da Dosyalar'da dosyaya uzun bas, Paylaş'ı seç ve FormlyConvert'i seç. Dosya, ona uygun araçlarla birlikte açılır.</p>
<p class="meta">Kullanım koşulları: <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple standart son kullanıcı sözleşmesi</a>.</p>
</div>"""
    page("/formlyconvert/destek/", "FormlyConvert Destek", "FormlyConvert için destek ve sık sorulan sorular.", body, theme="convert")


# MARK: Gizlilik (Markdown'dan)

def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"([\w.+-]+@formlyapps\.com)", r'<a href="mailto:\1">\1</a>', text)
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
        elif line.startswith("Son güncelleme:"):
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


def study_privacy() -> None:
    source = STUDY_REPO / "docs" / "legal" / "privacy-policy-tr.md"
    title, updated, body = markdown(source.read_text(encoding="utf-8"))
    body = body.replace("<p>Kısaca:</p>\n<ul>", '<div class="summary"><p><strong>Kısaca</strong></p><ul>', 1)
    if 'class="summary"' in body:
        start = body.index('class="summary"')
        end = body.index("</ul>", start) + len("</ul>")
        body = body[:end] + "</div>" + body[end:]
    content = f'<div class="wrap narrow prose">\n<h1>{inline(title)}</h1>\n<p class="meta">{inline(updated)}</p>\n{body}\n</div>'
    page("/formlystudy/gizlilik/", title, "FormlyStudy'nin hangi verileri işlediği ve senin seçeneklerin.", content)


if __name__ == "__main__":
    home()
    study()
    convert()
    support_hub()
    study_support()
    convert_support()
    study_privacy()
