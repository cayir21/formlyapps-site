# FormlyBite Privacy Policy

Last updated: October 10, 2026

FormlyBite is an iPhone food diary developed by Süleyman Çayır. For privacy and support requests, contact destek@formlyapps.com.

## 1. Overview

- Your food diary, weight history, goals, water entries and favourites are stored in the app’s local files.
- When you start photo or written analysis, the relevant content is sent through Supabase to OpenAI.
- Weight and active energy read from Apple Health are not included in these analysis requests.
- The app does not display ads, track you across apps or sell your data.
- Apple processes subscription payments; RevenueCat verifies subscription status.

## 2. Data stored on your device

Age, height, weight, target weight, activity level and other plan answers; meals, calories and macros, meal photos, favourites, water entries, weight history and settings are stored on your device. Account backup and cross-device sync are not currently available. Deleting the app removes local entries. Apple device backups and restoration depend on your Apple Account and device settings.

The camera is used to take meal photos or read barcodes. The app processes images you select with the system photo picker. Saved and uploaded photos are resized JPEGs. Notifications provide meal reminders. Device tilt is used momentarily to animate the mascot and is not sent to our server.

## 3. Photo and written meal analysis

When you request analysis, the selected meal photo, written description or correction note and app language are sent to our Supabase server in an authenticated request. The server forwards the content to the OpenAI API to estimate meal name, calories, macros and a meal score. Personal plan details and Apple Health records are not included. Any personal information you add to the description is also transmitted; avoid including private information that is unnecessary for the analysis.

The app’s server database does not save photos, description text or the meal estimate itself. This does not mean service providers never retain content. OpenAI API data is not used for model training by default. The current request uses the Responses API’s default retention setting: response data may be retained for at least 30 days; abuse-monitoring logs are generally retained for up to 30 days, with longer legal or security exceptions. See [OpenAI data controls](https://developers.openai.com/api/docs/guides/your-data).

The Supabase project region is in the European Union. OpenAI and other service providers may also process data outside Türkiye or the EU. Providers’ own privacy and retention policies apply.

## 4. Anonymous session and technical records

The app creates a random Supabase account identifier without a sign-up screen. It does not contain your personal name, but it links usage within the same session. Session tokens are stored in the device Keychain; deleting the app does not guarantee that its Keychain entry is removed.

To manage free analysis allowances and abuse, we record analysis time, account identifier, model, whether food was detected, and input/output token counts. There is currently no automatic deletion schedule for these records; contact us to request deletion. Network and service providers may process technical information such as IP addresses, request times and error logs to operate and secure their services.

## 5. Barcode lookups

When you search a barcode, its product number is sent directly to Open Food Facts. The provider can also see the connection’s IP address and FormlyBite app information. Your food diary and personal plan are not included in the lookup. Product data may be incomplete or incorrect. The [Open Food Facts privacy policy](https://world.openfoodfacts.org/privacy) applies.

## 6. Apple Health

With your permission, FormlyBite reads weight and active energy and writes weight entered in the app to Health. Read data is used on your device for progress and the optional addition of burned calories to your goal. Health data is not sent to Supabase or OpenAI or used for advertising, marketing or data sales. Revoke permissions in the Health app. Previously written weight entries may remain in Health after deleting FormlyBite; manage those entries separately in Health.

## 7. Subscriptions

Apple handles purchases and payments; we do not see card details. RevenueCat processes the anonymous app account identifier, purchase, product, subscription status and restoration information. Its SDK may also process technical app, device and connection information needed to provide the service. The [RevenueCat privacy policy](https://www.revenuecat.com/privacy/) and Apple’s purchase terms apply. Cancel subscriptions in your Apple Account’s Subscriptions section; deleting the app does not cancel a subscription.

## 8. Choices and requests

You can log meals manually without using photo or written analysis and manage camera, notification and Health permissions in device settings. Edit or delete meals in the app. For access, correction or deletion requests concerning server records, email destek@formlyapps.com with FormlyBite in the subject. We will work with you to identify the technical information needed to verify ownership of anonymous records; you do not need to attach health history or meal photos. Legal retention requirements and records held by providers are considered separately.

## 9. Health information and changes

FormlyBite’s calories, macros, personal targets and meal scores are estimates. It does not diagnose or treat conditions and does not replace advice from a health professional. If our data processing changes, we will update this page and its last-updated date.
