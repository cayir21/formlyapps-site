# FormlyBite Privacy Policy

Last updated: October 11, 2026

FormlyBite is an iPhone food diary developed by Süleyman Çayır. For privacy and support requests, contact destek@formlyapps.com.

## 1. Overview

- Your food diary, workouts, weight history, goals, water entries and favourites are stored on your device and, if you are signed in to iCloud, backed up to your own iCloud account. Meal and progress photos stay on your device only.
- When you start photo or written analysis, the relevant content is sent through Supabase to OpenAI.
- Weight and active energy read from Apple Health are not included in these analysis requests.
- Anonymous usage events and crash diagnostics are collected to improve the app; you can turn this off in Settings. Meal content, photos, weight and health data are not part of these records.
- The app does not display ads, track you across apps or sell your data.
- “Delete my data” in Settings removes the records on your device, the iCloud backup and the anonymous account on our server.
- Apple processes subscription payments; RevenueCat verifies subscription status.

## 2. Data stored on your device and in your iCloud

Age, height, weight, target weight, activity level and other plan answers; meals with their calories, macros, fibre, sugar, sodium and ingredient breakdown; meal photos, progress photos, workouts you enter, favourites, water entries, weight history and settings are stored on your device.

If your device is signed in to iCloud, these records, except photos, are backed up to your own iCloud account through Apple’s iCloud key-value store and synced between devices using the same Apple Account. The backup is held by Apple; we cannot access it. Meal and progress photos are not backed up and stay only on the device where they were added. If you are not signed in to iCloud, the data stays on your device only. Deleting the app removes local entries but not the iCloud backup; to remove the backup too, use “Delete my data” in the app first. Apple device backups and restoration depend on your Apple Account and device settings.

For the Home Screen and Lock Screen widgets, the day’s calorie and macro summary is shared between the app and its widget on your device; it is not sent to our server.

The camera is used to take meal photos or read barcodes. The app processes images you select with the system photo picker. Saved and uploaded photos are resized JPEGs. Notifications provide meal reminders. Device tilt is used momentarily to animate the mascot and is not sent to our server.

## 3. Photo and written meal analysis

When you request analysis, the selected meal photo, written description or correction note and app language are sent to our Supabase server in an authenticated request. The server forwards the content to the OpenAI API to estimate meal name, ingredient breakdown, calories, macros, fibre, sugar, sodium and a meal score. Personal plan details and Apple Health records are not included. Any personal information you add to the description is also transmitted; avoid including private information that is unnecessary for the analysis.

The app’s server database does not save photos, description text or the meal estimate itself. This does not mean service providers never retain content. OpenAI API data is not used for model training by default. The current request uses the Responses API’s default retention setting: response data may be retained for at least 30 days; abuse-monitoring logs are generally retained for up to 30 days, with longer legal or security exceptions. See [OpenAI data controls](https://developers.openai.com/api/docs/guides/your-data).

The Supabase project region is in the European Union. OpenAI and other service providers may also process data outside Türkiye or the EU. Providers’ own privacy and retention policies apply.

## 4. Anonymous session, usage data and technical records

On first launch the app creates a random Supabase account identifier without a sign-up screen. It does not contain your name, email address or phone number, but it links usage from the same installation. Session tokens are stored in the device Keychain; “Delete my data” removes this entry, while deleting the app alone does not guarantee that it is removed.

To manage free analysis allowances and abuse, we record analysis time, account identifier, model, whether food was detected, and input/output token counts.

To improve the app, the following anonymous usage events are also stored on our Supabase server (European Union) under the same account identifier: opening the app, completing onboarding and the type of goal chosen (lose, maintain or gain weight), how a meal was added (photo, text, barcode, search, favourite or manual), the outcome of an analysis (success, limit reached, no food found, error), the type of a workout, viewing the paywall, and the outcome of a purchase or restore. Each event is stored with its time, the app version, the iOS version and the device’s language/region setting. If the app crashes or hangs, the diagnostic report Apple generates on the device (error type, signal, termination reason, hang duration and a stack trace made of function addresses) is sent as well. Meal names, calories, photos, description text, weight, height, age and Apple Health data are not part of these records. This data is not used for advertising, marketing or cross-app tracking and is not passed to a third-party analytics service. You can turn it off under Settings › “Anonymous usage data”.

There is currently no automatic deletion schedule for analysis and usage records; they are deleted together with your account when you use “Delete my data”. Network and service providers may process technical information such as IP addresses, request times and error logs to operate and secure their services.

## 5. Barcode lookups and product search

When you look up a barcode, its product number is sent directly to Open Food Facts; when you search for a product by name, the search term you type is sent. The provider can also see the connection’s IP address and FormlyBite app information. Your food diary and personal plan are not included in these requests. Product data may be incomplete or incorrect. The [Open Food Facts privacy policy](https://world.openfoodfacts.org/privacy) applies.

## 6. Apple Health

With your permission, FormlyBite reads weight and active energy and writes weight entered in the app to Health. Read data is used on your device for progress and the optional addition of burned calories to your goal; the comparison with workouts you enter manually also happens on your device. Health data is not sent to Supabase or OpenAI or used for advertising, marketing or data sales. Revoke permissions in the Health app. Previously written weight entries may remain in Health after deleting FormlyBite; manage those entries separately in Health.

## 7. Subscriptions

Apple handles purchases and payments; we do not see card details. RevenueCat processes the anonymous app account identifier, purchase, product, subscription status and restoration information. Its SDK may also process technical app, device and connection information needed to provide the service. The [RevenueCat privacy policy](https://www.revenuecat.com/privacy/) and Apple’s purchase terms apply. Cancel subscriptions in your Apple Account’s Subscriptions section; deleting the app does not cancel a subscription.

## 8. Choices and requests

You can log meals manually without using photo or written analysis and manage camera, notification and Health permissions in device settings. You can turn off anonymous usage data in Settings. Edit or delete meals, workouts and progress photos in the app.

Settings › “Delete my data” permanently deletes the diary on your device, photos, weight and water entries, favourites, the iCloud backup and the anonymous account on our server together with its analysis and usage records. This cannot be undone. It does not cancel your subscription, which you manage in your Apple Account. Weight entries already written to Apple Health and purchase records held by Apple and RevenueCat are not removed by this action.

For access or correction requests concerning server records, or for deletion if you can no longer use the app, email destek@formlyapps.com with FormlyBite in the subject. We will work with you to identify the technical information needed to verify ownership of anonymous records; you do not need to attach health history or meal photos. Legal retention requirements and records held by providers are considered separately.

## 9. Health information and changes

FormlyBite’s calories, macros, fibre, sugar, sodium, calories burned, personal targets and meal scores are estimates. It does not diagnose or treat conditions and does not replace advice from a health professional. If our data processing changes, we will update this page and its last-updated date.
