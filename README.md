# formlyapps.com

FormlyConvert, FormlyStudy ve FormlyBite'ın ortak sitesi (GitHub Pages).

- Türkçe sayfalar kökte, İngilizceleri `/en/` altında; eşleşme `scripts/build.py` › `PATHS`. Üst çubukta TR/EN geçişi, her sayfada `hreflang`.
- Bütün sayfalar `scripts/build.py` ile üretilir: `python3 scripts/build.py [FormlyStudy reposu]`.
  FormlyStudy gizlilik politikası o repodaki `docs/legal/privacy-policy-tr.md` ve `privacy-policy-en.md`'den, FormlyConvert'inki `content/formlyconvert-privacy-en.md`'den gelir; FormlyBite'ınki `content/formlybite-privacy-tr.md` ve `content/formlybite-privacy-en.md` dosyalarından gelir; diğer metinler betiğin içinde.
- Maskotlar `assets/formi.svg` ve `assets/tabi.svg`: uygulamalardaki çizim kodunun (Formi.swift, TabiGeometry.swift) birebir SVG'si.
- Renkler üç uygulamanın temalarından (`style.css` başı). Sayfa `theme-study`, `theme-convert` ya da `theme-bite` sınıfıyla vurgu rengini seçer.
- `app-ads.txt` FormlyConvert'in AdMob kaydı içindir; silinmemeli.

- FormlyBite 15 Ekim 2026'da App Store'da yayımlandı (`BITE_STORE`). Maskotu Muzi: `assets/muzi.svg`, uygulamadaki MuziFigure.swift ile aynı vektörlerden (FORMLYAPPS İNSTA/tools/characters.mjs üzerinden). `assets/formlybite.png` güncel uygulama simgesidir.
