# VakitApp Privacy Policy

Last updated: October 21, 2026

This policy explains which data VakitApp ("the app") processes, why, and what choices you have. The data controller is Süleyman Çayır; contact: destek@formlyapps.com.

In short:
- No account needed; we never ask for your name, email or phone number.
- Your settings, prayer tracking and other entries stay on your device. If you turn on iCloud sync with Pro, they are stored in your own iCloud account.
- To fetch prayer times, only the city you chose is sent to prayer time services; we don't store your location on our servers.
- The free version shows banner ads from Google AdMob. Ads are personalized only if you allow it.
- We never sell your data.

## 1. Data that stays on your device

Your chosen cities, notification and alarm settings, theme, prayer tracking, dhikr counts, reading progress and similar preferences are stored on your device. Notifications and alarms are scheduled on your device; no data is sent to a server for them.

If you turn on iCloud sync with Pro, these entries are stored in the private area of your own iCloud account through Apple's CloudKit. We cannot access this data.

## 2. Location

If you allow location access, your location is used on your device to find your city and the Qibla direction. Apple's location services are used to look up the city name. If you turn on automatic location and allow "Always" access, location changes are used in the background so your prayer times and notifications stay up to date when you change cities.

You don't have to allow location access; you can choose your city by hand.

## 3. Prayer time services

Prayer times are fetched through a relay server we operate on Cloudflare Workers. The relay gets the times of Türkiye's Presidency of Religious Affairs (Diyanet) from ezanvakti.emushaf.net, which publishes them. That request contains only the city ID or city name, the month and the year. If the service doesn't respond, ezanvakti.imsakiyem.com, Aladhan (api.aladhan.com) and vakit.vercel.app may be used as fallbacks. These fallbacks may receive the coordinates of your city or location.

Quran recitation is downloaded from cdn.islamic.network, and the Friday khutbah and Islamic days from Diyanet's websites. As with any internet request, these servers can see your IP address.

## 4. Shared Khatm

If you use Shared Khatm, the khatm's title, the display name you enter, a randomly generated reader ID and the status of the juz you take are stored in Apple's CloudKit public database. Anyone who knows the join code can see this information. The feature requires you to be signed in to iCloud. You don't have to use your real name.

## 5. Ads

The free version shows Google AdMob banner ads on some screens. There are no ads on the home countdown or the Qibla screen. Users in the European Economic Area, the UK and Switzerland are asked for consent through Google's consent tool (UMP). Apple's App Tracking Transparency permission is requested for personalized ads. If you decline, your advertising identifier (IDFA) is not shared and non-personalized ads are shown.

AdMob may process device information, your IP address and ad interactions for ad delivery, measurement and fraud prevention. See [Google's privacy policy](https://policies.google.com/privacy) for details. You can change your ad choices in the app's Settings. Pro removes ads completely.

## 6. Purchases

Purchases and subscriptions are made through Apple's App Store. Your card details never reach us. RevenueCat is used to record purchases and report revenue. It receives an anonymous user ID, the product, price, currency, country and transaction date.

## 7. Photos

If you want to save share cards to Photos, the app asks for add-only access. We never read your photo library.

## 8. Analytics and crash reports

The app contains no separate analytics or crash reporting tool. If you share analytics with app developers in your Apple settings, Apple may send us anonymous crash reports.

## 9. Retention and deletion

Deleting the app removes the data on your device. You can delete the iCloud copy on your iPhone in Settings › [your name] › iCloud › Manage Storage › VakitApp. To have Shared Khatm records deleted, write to us with the join code.

## 10. Your rights

Under laws such as the GDPR and Türkiye's KVKK, you have the right to know whether your data is processed, to request information, correction or deletion, to object to processing and to withdraw your consent. Write to destek@formlyapps.com to use these rights.

## 11. Children

VakitApp is not directed at children under 13 and does not knowingly collect personal data from them.

## 12. Changes

If this policy changes, the current version is published on this page and the date at the top is updated.
