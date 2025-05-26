ngeniusKnowledgeDescription = """Generates multiple semantically similar variations of a user query to improve search relevance and retrieval from a knowledge base."""

ngeniusKnowledgeRole = "You are a helpful assistant that helps create multiple variation of the given query which can be passed to ohter agent to fetch data from knowledge base."

ngeniusKnowledgeInstructions = [
    "Fetch information only from the official NGENIUS documentation - https://docs.ngenius-payments.com/reference/set-up-n-genius uning 'TavilyTools'.", 
    "Always include examples", 
    "When referring to documentation, include the relevant section or direct link if available"
    "If you have resolved customer's question in a chat session (i.e., over the course of preceding chat messages), then politely ask a follow up question if there is any thing else that you can help the customer with or whether the customer needs more details?"
]

# ngeniusKnowledgeInstructions=[
#     "Fetch information only from the official NGENIUS documentation - https://docs.ngenius-payments.com/reference/set-up-n-genius uning 'TavilyTools'.",
#     "Focus on answering questions related to troubleshooting, setup, and integration of NGENIUS.",
#     "Always provide accurate and concise responses based on official documentation.",
#     "If multiple solutions exist, list them in order of most commonly effective to least.",
#     "Do not provide information about licensing, billing, or sales unless explicitly available on the NGENIUS documentation.",
#     "When referring to documentation, include the relevant section or direct link if available.",
#     "Clarify ambiguous user questions by asking follow-up questions before providing an answer.",
#     "Respond in a professional and helpful tone suitable for technical support.",
#     "Avoid speculation—only respond based on verifiable content from the NGENIUS site.",
#     "If no relevant information is found, acknowledge the limitation and suggest contacting NGENIUS support directly."
# ]

ngeniusKnowledgeMdStrings_small = [
"""
Below is an illustration of a conversation between 'Customer' and 'Customer Service Agent' in a question answer format:

Customer:
I Signed up for ecommerce but am unable to proceed ahead.

Customer Service Agent:
What is your Customer ID and outlet ID.

Customer:
Where can I find MID and outlet ID ?

Customer Service Agent:
You can get it from the mail subject of the N-Genius welcome kit or navigate to Settings > Organization Hierarchy > MID.

Customer:
I have not received any emails. How do I get the API key and the outlet ID ?

Customer Service Agent:
To get you started, please click on the link in the invitation e-mail you have received to set your password and log in to the LIVE Customer portal. Kindly check your junk folder if you cannot find the email in your mailbox. If you still have not received the email, then please write to us.

In case you are performing web integration, please use the below details to perform integration.

API KEY - Available in the N-Genius online Portal:
Settings >> Integrations >> Customer Service accounts

Available in the N-Genius online Portal:
Settings >> Organisational Hierarchy >> Outlet >> Reference

Token URL https://api-gateway.ngenius-payments.com/identity/auth/access-token

Transaction: https://api-gateway.ngenius-payments.com/transactions/outlets/

Finally, Please ensure that the readiness checklist is validated before going live to the public# FAQ Asuransi AXA SmartTravel

**Customer:**
How do I get an access token?

**Customer Service Agent:**
You can click on this link for access token.
https://docs.ngenius-payments.com/reference/request-an-access-token-direct

**Customer:**
How long is an Access token valid for?

**Customer Service Agent:**
The Access token expires after 5 minutes.

**Customer:**
What are the possible error codes?

**Customer Service Agent**
https://docs.ngenius-payments.com/reference/error-codes-details
Additional HTTP errors attached.
"""
]


ngeniusKnowledgeMdStrings = [

"""# Ecommerce Integration FAQs

## General Questions

1. **What are the steps to GO LIVE?**
   - Configure API Keys and Outlet IDs.
   - Perform at least one successful VISA and Master card TEST transaction and confirm go live readiness by sharing the Merchant checklist.
   - The integration team will validate transactions and initiate Live Account creation.

2. **How many days will it take for LIVE credentials to be shared?**
   - The LIVE welcome kit will ideally be shared within 3-5 business days after UAT signoff.

3. **What changes need to be done after receiving LIVE credentials?**
   - Please change the API key and Outlet ID, and the posting URL should be without the "sandbox" tag.

4. **How can we go public to customers?**
   - One actual VISA and Mastercard transaction (pilot transactions with 1 AED or your MID currency) each should be done and sent to ecomsupport@network.global for validation and signoff.

5. **How can we get the TEST cards for the sandbox?**
   - The TEST cards are available here: [https://docs.ngenius-payments.com/reference#sandbox-test-environment](https://docs.ngenius-payments.com/reference#sandbox-test-environment)

Copyright@2022 Network International | [www.network.global](http://www.network.global)# Ecommerce Integration FAQs

6. **Is there any TEST card available for the LIVE account?**
   A live N-Genius account does not have any test card. You need to use real cards for transactions and pilot testing.

7. **Can we enter the customer card details from our website?**
   YES, but you need a PCI compliance certificate for that. You must submit a copy of the same for processing.

8. **What are the payment channels available?**
   N-Genius gives you almost all top payment channel options like VISA, Mastercard, Diners, Discover, American Express etc.

9. **How can I get the API KEY?**
   Log in to the portal -> Settings-> Integration-> Service Account: You will find the API Key here.

10. **How can I get the Outlet ID?**
    Log in to the portal ->Organisational Hierarchy-> Left, you can see the outlet associated-> click on the outlet and you can see the Reference.

11. **What is the difference between AUTH and SALE?**
    AUTH: Money will be on hold in the customer bank account and not credited to the merchant account until and unless you do a manual capture from the portal level using the capture API.
    SALE: Money will be automatically credited to the merchant account.

12. **How to create users?**
    Login to the portal-> Settings-> Users: Create the user according to your business needs.

13. **How to do a Refund/Partial refund?**
    You can do a refund from the portal by clicking on the refund button after the transaction can be settled. The Refund API can also be used (you will need to pass the amount and currency type). Link: https://docs.ngenius-payments.com/reference#refund-a-capture.

14. **How long is an Access token valid?**
    The Access token expires after 5 minutes.

15. **How many programming languages can N-Genius support?**
    N-Genius supports leading programming languages such as Java, C#, PHP, Ruby, Node etc.

16. **How to redirect to the payment website after payment?**
    Include the attribute merchantAttributes.redirectUrl in the request.

17. **Why does '10' show when I pass a value of 1000?**
    N-Genius uses minor units. (Usage: Actual value * 100).

Ecommerce Integration FAQs
Copyright@2022 Network International | www.network.global# Ecommerce Integration FAQs

18. **Can I implement the card entering feature without PCI compliance?**
   You have an option called WEB SDK which gives the customer the impression that he/she isin the same website and entering the details.

19. **How can I implement the saved card feature?**
   If you have PCI compliance, then go for the saved card feature, otherwise go for tokenization.
   Please contact your Relationship Manager to enable the feature.

20. **Is the customer billing address a mandatory field?**
   Yes, it is. Customer email and billing address are mandatory.

21. **Where can I find the Merchant ID (MID)?**
   You can get it from the mail subject of the N-Genius welcome kit or navigate to Settings > Organization Hierarchy > MID.

22. **How can I log in if I forgot the password?**
   Click on the 'Forgot password' option in the login screen. A password reset link will be sent to your registered email ID (check your spam/junk folders if you don't find your link in the inbox]. Set the password and log in again. Login URL: https://portal.sandbox.ngenius-payments.com/#/login

23. **How do I create a web developer or any other user?**
   Go to settings after logging into the merchant portal. Click on 'Users' and give a suitable name and email ID. Select the appropriate role from the list of user roles, then select the organization.

24. **Is it possible to change the payment page?**
   No, but we can customize the payment page.

25. **How can I customize the payment page?**
   Go to settings after Login. Under 'Branding' you can apply your logo and set the theme.

26. **How can I add new Organizational units?**
   Please contact your Relationship Manager who will assist you in creating a new Organizational Unit ID.

27. **How can we activate Webhook?**
   Add the webhook URL in webhooks under 'Integrations.' Once entered in the sandbox please notify our team by sending an email. In sandbox, we have to manually whitelist the webhook URL. In the LIVE section this will be automatically whitelisted once entered in the merchant portal.

28. **How can the customer enter card details from our own website if we don't have PCI DSS compliance?**
   You can go with Hosted session [WEB SDK] integration.
   Docs: https://docs.ngenius-payments.com/docs/web-sdk-integration-guide

Copyright@2022 Network International | www.network.global# Ecommerce Integration FAQs

29. **Can we go LIVE directly without sandbox testing?**
   
   It is recommended that you do a test using one VISA and Mastercard transaction and once verified we will give a signoff for you to go public. If you have already received live credentials you can request our Support team to skip UAT.

30. **What are the documents required for the Tokenization feature?**
   
   You should provide an Indemnity Letter and credit risk approval docs for the tokenization feature.

""",

"""

31. **Please share the steps to follow once we install the N-Genius WooCommerce plugin [single currency] and change it to a multicurrency plugin later on.**
   
   If you encounter errors:
   
   If you are using older versions of the N-Genius WooCommerce extension, then please remove the table below
   
   Note: Backing up this database is mandatory.
   
   If you want to use old data (for N-Genius Online) you need to create a custom script.
   
   The latest extension will work for fresh instances of WooCommerce.
   
   Delete the table ngenius_networkinternational;
   
   Then uninstall the old extension and install the new one.

32. **Does Network International provide an SDK/library for PG Android and iOS?**
   
   Yes, Network does provide an SDK for Android, iOS and React Native.
   
   React Native - https://github.com/network-international/react-native-ngenius
   
   Android - https://github.com/network-international/payment-sdk-android
   
   iOS - https://github.com/network-international/payment-sdk-ios

33. **What data should be passed to the SDK in order to make a transaction?**
   
   Create-order API response will be enough to trigger the SDK in React Native, Android and iOS.

34. **Does Network provide a sample code for SDKs?**
   
   Yes, you can find the sample code from the GitHub repo of each SDK.

35. **Can I as a merchant customize the SDK pay page?**
   
   Yes, but only if you have a PCI DSS compliance certificate.

36. **How will the app get to know the payment status after the transaction?**
   
   Our SDK does provide a callback function after transaction success/ failure, which your developer can make use of at their convenience.

37. **Is the SDK/library available for Flutter?**
   
   No, we don't have a Flutter SDK for now, but the SDK can be integrated to iOS and Android using a separate native SDK available on GitHub.

Ecommerce Integration FAQs

Copyright@2022 Network International | www.network.global# Ecommerce Integration FAQs

38. **Is Tokenization/saved card available on mobile SDK?**

Saved card is not built in our SDK, but you can save card on your database and continue transacting with the API using the SDK.

39. **Is Apple Pay available on the SDK?**

Yes, Apple Pay can be directly integrated by using the N-Genius SDK for iOS.

40. **Can N-Genius APIs be called directly from the mobile application?**

No, APIs should be called from a backend language such as PHP, ASP.Net, node.js etc., otherwise you will be served CORS issue.

41. **Is recurring payment available in the SDK?**

No, our SDK doesn't include recurring payment. It should be done from the server side. But card token saving can be done using the application to store in the database.

42. **Can payment page customisation be done without PCI DSS on the mobile SDK?**

No, SDK customisation is not possible without PCI DSS , but one type of integration method called 'Hosted session' would be helpful for customising the payment page .

The Hosted session simply supports the loading of the N-Genius web SDK on a webpage which can be customised. This page can be loaded to a mobile application Android-webview, and iOS-UIWebview.

43. **How can I configure Apple Pay?**

You can refer to the steps in the video accessible here: [https://drive.google.com/file/d/1U2glirdlJyjQu_Di9ENOVHeWaQyMm4Wp/view?usp=sharing](https://drive.google.com/file/d/1U2glirdlJyjQu_Di9ENOVHeWaQyMm4Wp/view?usp=sharing)

44. **Does Network's SDK support Samsung Pay?**

Yes, it does. You can refer to the link below for step-by-step documentation on integrating Samsung Pay. [https://docs.ngenius-payments.com/reference#samsung-pay](https://docs.ngenius-payments.com/reference#samsung-pay)

45. **Where can Samsung Pay integration sample code be found?**

It can be found in the GitHub repo accessible here: [https://docs.ngenius-payments.com/reference#samsung-pay](https://docs.ngenius-payments.com/reference#samsung-pay)

46. **Does Network's SDK provide notification after payment success on the mobile application?**

No, our SDK doesn't provide that, but we have a webhook service to acknowledge the payment. Push notification can also be done from your end after fetching the order status by order retrieval API.

47. **How to install iOS SDK?**

Installation can be done by using CocoaPods or Carthage. Refer below for more info: [https://docs.ngenius-payments.com/reference#ios-sdk-integration-guide](https://docs.ngenius-payments.com/reference#ios-sdk-integration-guide)

Copyright@2022 Network International | [www.network.global](http://www.network.global)# FAQ Asuransi AXA SmartTravel

## 48. How to install Network's SDK on Android apps?
Use the dependencies below:

```
allprojects {
    repositories {
        ...
        maven { url 'https://jitpack.io' }
    }
}
dependencies {
    // Required
    implementation 'com.github.network-international.payment-sdk-android:payment-sdk-core:1.0.0'

    // For card payment
    implementation 'com.github.network-international.payment-sdk-android:payment-sdk:1.0.0'

    //For samsung payment
    implementation 'com.github.network-international.payment-sdk-android:payment-sdk-samsungpay:1.0.0'
}
```

Refer below link to find latest SDK and to know more updates:
[https://github.com/network-international/payment-sdk-android](https://github.com/network-international/payment-sdk-android).

## 49. Does Android SDK support multiple languages?
Yes, as of now Android SDK supports English and Arabic.

## 50. What are the currencies supported by Network's SDK?
All the currencies which are configured for the particular N-Genius account will be supported by our SDK.

## 51. Is there any sample server API for testing purposes?
We do have one sample server application created by node js and PHP project which you can use for demo purposes and move to actual API-based server calls later on. You can find the demo server projects here:

- PHP - [https://github.com/network-international/sample-merchant-server-php](https://github.com/network-international/sample-merchant-server-php)
- Javascript - [https://github.com/network-international/sample-merchant-server-javascript](https://github.com/network-international/sample-merchant-server-javascript)

## 52. How to install Network's SDK on the React Native app?
To install our SDK on React Native apps, the developer can directly download the package by following the command below:

```
npm i @network-international/react-native-ngenius
```

Ecommerce Integration FAQs

Copyright@2022 Network International | [www.network.global](http://www.network.global)# Ecommerce Integration FAQs

## 53

**Are there any prerequisites for using Network's SDK for React Native?**

Yes, if your project is using iOS deployment target 10, you need to increase it to 11.

In order to upgrade the versions, do the following changes:

Change the iOS deployment version in your-project/ios/Podfile as follows: platform:ios, '11.0'

Open the .xcworkspacefile inside the following directory your-project/ios/yourproject.xcworkspace and change the deployment target to 11.0.

## 54

**What data need to be passed to React Native SDK in order to invoke payment?**

Passing a whole order response will take you to payment activity - refer to sample code snippet below:

```javascript
// order is the order response received from N-Genius create order API
const makeCardPayment = async () => {
  try {
    const resp = await initiateCardPayment(order);
  } catch (err) {
    console.log({ err });
  }
};
```

## 55

**How to invoke Apple Pay using React Native in Network's SDK?**

It can be done by applying the sample code snippet below:

```javascript
import { initiateApplePay } from '@network-international/react-native-ngenius';
// order is the order response received from N-Genius create order API
// mid is the merchant ID that is generated in the Apple developer portal
// countryCode is the country code of the transaction country Eg: AE for UAE
const makeApplePayPayment = async () => {
  try {
    const resp = await initiateApplePay(order, mid, countryCode);
  } catch (err) {
    console.log({ err });
  }
};
```

## 56

**How to invoke Samsung Pay using Network's SDK in React Native?**

It can be done by applying the sample code snippet below:

```javascript
import { initiateSamsungPay } from '@network-international/react-native-ngenius';
// order is the order response received from N-Genius create order API
// merchantName is the name of merchant's establishment
// serviceld is the serviceld that is generated in the Samsung Pay developer portal
const makeSamsungPayPayment = async () => {
  try {
    const resp = await initiateSamsungPay(order, merchantName, serviceld);
  } catch (err) {
    console.log({ err });
  }
};
```

Ecommerce Integration FAQs

Copyright@2022 Network International | www.network.global# Ecommerce Integration FAQs

57

**How to configure SDK language in React Native?**

Language configuration can be done by applying the code snippet below:

```javascript
import { configureSDK } from '@network-international/react-native-ngenius';
configureSDK({
   language: isEnglish ? 'en' : 'ar'
});
```

58

**How to show/hide the order amount in React Native SDK?**

It can be done by applying the code below:

```javascript
import { configureSDK } from '@network-international/react-native-ngenius';
configureSDK({
   shouldShowOrderAmount: true/false
});
//true for show amount
//false for hide amount
```

59

**How to check if Samsung Pay is enabled on React Native in Network's SDK?**

This can be checked by applying the code below:

```javascript
import { isSamsungPaySupported } from '@network-international/react-native-ngenius';
const isSamsungPayEnabled = await isSamsungPaySupported();
```

60

**How to check if Apple Pay is enabled in Network's SDK React Native app?**

This can be checked by applying the code below:

```javascript
import { isApplePaySupported } from '@network-international/react-native-ngenius';
const isApplePayEnabled = await isApplePaySupported();
```

61

**Does Network's SDK for iOS have multi-language compatibility?**

No, as of now only Android has multi-language support for both English and Arabic.

Copyright@2022 Network International | www.network.global# Pay By Link FAQs

""",

"""
## General Questions

1. **Which payment methods are supported by Pay by Link integration?**
   
   Supported payment methods include Visa, Mastercard, Diners Club, UnionPay, Samsung Pay and Amex (make sure you have a separate contract with Amex).

2. **How can I add users to my portal?**
   
   You can add users to your portal through Settings >> Users >> NEW. More details can be found at [https://docs.ngenius-payments.com/docs/users](https://docs.ngenius-payments.com/docs/users).

3. **Can the same Email ID be used for multiple roles?**
   
   No, you cannot use the same email ID for multiple roles. You can assign the user email either to the top level hierarchy or to any particular outlet. You also cannot assign a single user to multiple outlets.

4. **How do I configure the transaction limit and Black Listing of countries/e-mails/domains ?**
   
   Go to Settings >> Risk Rules >> Basic Risk Rules >> Set Currency limit. Update the amount accordingly. Details can be found at [https://docs.ngenius-payments.com/docs/risk-rules](https://docs.ngenius-payments.com/docs/risk-rules).

5. **How can I find the Outlet MID from the portal?**
   
   You can check the Outlet MID from Settings >> Organizational hierarchy >> MIDS.

6. **How can I find the assigned payment channels for the Outlet?**
   
   You can check the assigned payment channels for your MID from Settings >> Organizational hierarchy >> Payment Channels.

Copyright@2022 Network International | [www.network.global](http://www.network.global)# Pay By Link FAQs

1. Can we assign separate users to different outlets under our organization?
   Yes, you can assign separate users to each of your outlets if they are created as separate organizational units.

2. What is Email notifications?
   If you want to receive notifications on orders and transactions, you can add your email address in Settings >> General >> Email notifications. You can add multiple email addresses here. Details can be found at https://docs.ngenius-payments.com/docs/email-notifications.

3. Why are my customers not receiving any notification regarding payment status?
   You should make sure that card holder notification is enabled in Settings >> General >> Card holder notifications. Details can be found at https://docs.ngenius-payments.com/docs/card-holder-notifications.

4. My customers say they are not receiving the email link. What do I tell them?
   Request your customer to check their Junk Mail.

## Pay by Link configuration

1. What needs to be filled in the "From email address" field?
   You can enter the email address like yourcompanyname@ngenius-payments.com and Pay by Link will create from this email address.

2. Can we use our own email domain instead of "@ngenius-payments.com"?
   No, the payment link is generated from the N-Genius portal so by default the domain will be "@ngenius-payments.com".

3. What are the Auth and Sale transaction types?
   In "Auth," money will be held in the customer account [customer will get debit message from bank] and will not be credited to the merchant unless the merchant performs a manual capture from the portal. You can do the capture by going to Portal >> Orders >> Open order >> Capture.
   In "Sale," both Auth and Capture take place automatically. You can select the transaction type based on your business. Ex: Auth type will be suitable for a Hotel business.

4. What is the maximum limit for payment re-attempts?
   The maximum allowed re-attempts is five (5).

Copyright@2022 Network International | www.network.global# Pay By Link FAQs

5. **What should we use if we do not have a Pay by Link logo URL, is it a mandatory field?**
   Yes, it is a mandatory field and if you don't have the Pay by Link logo URL, you can create a logo link through Google Drive. Please refer to the steps below:
   > Log in/set up your account in Google Drive
   > Upload your image, make sure to check the specification (pixel size, doc type - png, <500KB)
   > Right-click and chose "get sharable link"
   > Copy the link which should look like "https://drive.google.com/file/d/118LW1WiWCk_6oN4x0ChNZitEycQHmQYSp/view?usp=sharing"
   > Change it to `<img src="https://drive.google.com/uc?export=view&id=XXXXX">`
   > Replace the ID highlighted above in green with the link highlighted in yellow

## Payments

1. **How can I create a payment link from the N-Genius portal?**
   You can create the payment link by going to Portal >> payments >> NEW.

2. **What should be used in the payment link order reference ID field?**
   The payment link order reference ID is the Order ID/Reference ID/Invoice ID you are using to track the orders or customers.

3. **What unique reference number can be used in the portal and settlement report?**
   Use the payment link order reference ID as the unique reference number which you can enter while creating the payment link. If you are enabling the "unique reference number" feature, then the portal will check the uniqueness of the Order ID / if it is already used or not.

4. **Can we change the expiry date for a particular customer?**
   Yes, it possible. Even if you are providing a default link expiry date in the configuration page, you can change it for a particular customer. You can see the option "Expiry date" in the payment creation page and from there you can change the default expiry date.

## Orders

1. **Can I void a capture and then cancel an Auth ?**
   Yes, you can select the "cancel authorization" option to cancel the payment.

2. **Within how many hours/days should I capture the transaction?**
   You will need to capture the payment within four (4) business days.

3. **When will the Cancel Authorization/Refund reflect on the Customer account?**
   It ideally reflects within 5 to 7 working days but is dependent on the card issuing bank's policies.

---

Pay By Link FAQs

Copyright@2022 Network International | [www.network.global](http://www.network.global)# Pay By Link FAQs

4
Is recurring billing available on Pay by Link?
No, this option is not available on Pay by Link.

5
How can I find the "Auth code" of a transaction?
You can get the Auth code by navigating to Orders >> Open order >> History.

Reports
1
How can I generate a report for all my transactions from the portal?
Reports can be downloaded by navigating to Portal >> Reports >> Generate. You will need to filter data such as Date, Order Status, Payment Type, Channel, Currency, and Outlet and click 'Generate.' Once the status changes from pending to done, you can download the report.

2
Can a report be used for reconciliation?
Yes, through a combination of Auth Code, Transaction Amount, and Date.

Pay by Link Email Template
1
Why I am not able to use the Arabic language to create email templates?
Arabic is currently not supported in the portal, you can only use English to create an Email template.

2
What is the purpose of the smart tag option?
Using smart tag options in the email template replaces customer details once sent to the customer. Smart tag options are available for First Name, Last Name, Order ID and Expiry Date. You should use options like {{orderId}}, {{firstName}} {{lastName}} and {{expiryDate}}.

3
Why am I receiving the "Invoice featuring disabled" error?
You need to make sure Pay by Link is enabled in your account. Please follow the steps below to enable the service:
1. Log in to the portal
2. Click on the profile icon at the top right corner
3. Click on 'Navigate organizational hierarchy'
4. Click on the organizational unit Merchant listed (Outlet name)
5. Click on the select button near the heading with the Merchant name
6. The page will refresh with a Services menu under the Settings Menu
7. Enable Pay by Link

4
Why I am receiving the "Failed to create order" error?
There are multiple reasons for this issue, including:
> Creating a payment link with a higher amount than the specified transaction limit. Please check the maximum transaction limit for your order from Risk rules>> Basic risk rules >> Currency limit.
> Incorrect details in the Success URL/Pay by Link logo URL field on the configuration page.
If both are fine and the issue still persists, please contact our Integration Team at ecom-integration@network.global for assistance.

Note:
1. Pay by Link User Guide: https://docs.ngenius-payments.com/docs/pay-by-link
2. Test Card Details: https://docs.ngenius-payments.com/reference#sandbox-test-environment
3. Supported Browser Languages: Arabic and English

Copyright@2022 Network International | www.network.global# ESCALATION MATRIX

For Live escalations, please get in touch with the following persons:

| Escalation     | Name          | Designation                           | Contact Details                     |
|----------------|---------------|---------------------------------------|-------------------------------------|
| First Level    | Ecomsupport   | mailbox                               | ecomsupport@network.global          |
| Second Level   | Rohit Naik    | E-Commerce Team Lead                  | Rohit.Naik@network.global           |
|                |               |                                       | +971 4 406 5574                     |
| Back Up        | Rakesh Kumar  | E-Commerce Manager                    | Rakesh.Kumar@network.global         |
|                |               |                                       | +971 4 406 5128                     |
| Escalation     | Pylee Varghese| AVP - Head of E-com Delivery and Support | Pylee.VM@network.global             |
| Level 3        |               |                                       | +971 4 704 5772                     |

For Sandbox escalations, please get in touch with the following persons:

| Escalation     | Name          | Designation                           | Contact Details                     |
|----------------|---------------|---------------------------------------|-------------------------------------|
| First Level    | Integration   | mailbox                               | ecom-integration@network.global     |
| Second Level   | Rajeevan PT   | E-Commerce Integration Lead           | Rajeevan.PT@network.global          |
|                |               |                                       | +971 4 876 4977 Ext: 140            |
| Back Up        | Swathy Nair   | E-Commerce Support Engineer           | Swathy.Nair@network.global          |
|                |               |                                       | +971 4 876 4977 Ext: 145            |
| Escalation     | Rakesh Kumar  | E-Commerce Manager                    | Rakesh.Kumar@network.global         |
| Level 3        |               |                                       | +971 4 406 5128                     |

For any issues/queries after office hours, please contact our call center at +971 4 316 0183

For queries related to Fraud Management, please contact below:

| Escalation     | Name                  | Contact Details                     |
|----------------|-----------------------|-------------------------------------|
| First Level    | Ecom Fraud Management | ecomfraudmgmt@network.global        |
| Second Level   | Shruthi Rao           | Shruthi.Rao@network.global          |
|                |                       | +971 4 704 5888                     |

For escalations, please contact below:

| Name        | Contact Details                     |
|-------------|-------------------------------------|
| Yaaser Khan | Yaaser.Khan@network.global          |
|             | +971 4 704 5922                     |

For queries related to Settlement/Reconciliation, please contact below:

| Escalation  | Name             | Contact Details                     |
|-------------|------------------|-------------------------------------|
| First Level | Merchant HD Team | MerchantHD@network.ae               |

network>

WWW.NETWORK.GLOBAL""",

"""
Error Codes and Scenarios
401 - Unauthorized
1. Incorrect URL when generating access token
2. Access token expired
3. Incorrect headers


403 - Forbidden
1. Incorrect access token
2. Incorrect Outlet ID
3. API Key from hosted service account


405 - Method Not Allowed
1. Incorrect request, such as using PUT instead of POST


422 - Unprocessable Entity
1. Service account not enabled
2. Amount limit exceeded
3. Currency not set as base currency for the account


"""

]



