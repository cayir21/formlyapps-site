# formlyapps.com

FormlyConvert, FormlyStudy, FormlyBite ve VakitApp'in ortak sitesi (GitHub Pages).

- Türkçe sayfalar kökte, İngilizceleri `/en/` altında; eşleşme `scripts/build.py` › `PATHS`. Üst çubukta TR/EN geçişi, her sayfada `hreflang`.
- Bütün sayfalar `scripts/build.py` ile üretilir: `python3 scripts/build.py [FormlyStudy reposu]` (Python 3.12 ya da sonrası).
  FormlyStudy gizlilik politikası o repodaki `docs/legal/privacy-policy-tr.md` ve `privacy-policy-en.md`'den, FormlyConvert'inki `content/formlyconvert-privacy-en.md`'den gelir; FormlyBite'ınki `content/formlybite-privacy-tr.md` ve `content/formlybite-privacy-en.md` dosyalarından gelir; diğer metinler betiğin içinde.
- Maskotlar `assets/formi.svg` ve `assets/tabi.svg`: uygulamalardaki çizim kodunun (Formi.swift, TabiGeometry.swift) birebir SVG'si.
- Renkler üç uygulamanın temalarından (`style.css` başı). Sayfa `theme-study`, `theme-convert` ya da `theme-bite` sınıfıyla vurgu rengini seçer.
- `app-ads.txt` FormlyConvert ve VakitApp'in AdMob kaydı içindir (aynı yayıncı kimliği); silinmemeli.

- FormlyBite 15 Ekim 2026'da App Store'da yayımlandı (`BITE_STORE`). Maskotu Muzi: `assets/muzi.svg`, uygulamadaki MuziFigure.swift ile aynı vektörlerden (FORMLYAPPS İNSTA/tools/characters.mjs üzerinden). `assets/bite/icon.png` güncel uygulama simgesidir.
- VakitApp (App Store `id6759460194`, `VAKIT_STORE`) 21 Ekim 2026'da vakitapp.forvibe.app'ten buraya taşındı. Sayfaları Türkçe, İngilizce ve Almanca: `/vakitapp/`, `/en/vakitapp/`, `/de/vakitapp/`; altında destek, gizlilik ve kullanım koşulları. Gizlilik ve koşul metinleri `content/vakitapp-privacy-*.md` ve `content/vakitapp-terms-*.md`. Uygulamadaki Ayarlar linkleri ve App Store Connect URL'leri bu adreslere bakar; adresleri değiştirme.
- `assets/vakit/` 1.0.8 App Store setinden (tr: App Store Connect, en/de: VakitApp reposu `Docs/AppStore/1.0.8/screenshots`), 600 px genişlikte JPEG. Görseller zaten çerçeveli olduğu için `.shot` sınıfıyla gösterilir.
- FormlyStudy 21 Ekim 2026'da App Store'da yayında (`STUDY_STORE`, id6819411851). `assets/study/icon.png` uygulama simgesi.
- Ürün sayfalarındaki telefon ekranları: `assets/study/` FormlyStudy reposundaki `outputs/appstore/iphone-6.9` mağaza görsellerinin ekran alanından kesildi; `assets/convert/` FormlyConvert App Store görsellerinden kesildi; `assets/bite/` Figma'daki FormlyBite App Store setinin (dosya `11GhXA67qZGXQiutt8PQiC`, "Ekran" katmanları) ham görüntüleri. Hepsi 600 px genişlikte JPEG.
