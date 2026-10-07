# formlyapps.com

FormlyConvert ve FormlyStudy'nin ortak sitesi (GitHub Pages).

- Türkçe sayfalar kökte, İngilizceleri `/en/` altında; eşleşme `scripts/build.py` › `PATHS`. Üst çubukta TR/EN geçişi, her sayfada `hreflang`.
- Bütün sayfalar `scripts/build.py` ile üretilir: `python3 scripts/build.py [FormlyStudy reposu]`.
  FormlyStudy gizlilik politikası o repodaki `docs/legal/privacy-policy-tr.md` ve `privacy-policy-en.md`'den, FormlyConvert'inki `content/formlyconvert-privacy-en.md`'den gelir; diğer metinler betiğin içinde.
- Maskotlar `assets/formi.svg` ve `assets/tabi.svg`: uygulamalardaki çizim kodunun (Formi.swift, TabiGeometry.swift) birebir SVG'si.
- Renkler iki uygulamanın temalarından (`style.css` başı). Sayfa `theme-study` ya da `theme-convert` sınıfıyla vurgu rengini seçer.
- `app-ads.txt` FormlyConvert'in AdMob kaydı içindir; silinmemeli.
