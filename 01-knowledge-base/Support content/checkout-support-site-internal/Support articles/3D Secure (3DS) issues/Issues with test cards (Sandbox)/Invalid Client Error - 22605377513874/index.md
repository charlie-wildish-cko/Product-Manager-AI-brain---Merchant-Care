---
id: 22605377513874
section_id: 22604832741650
title: "Invalid Client Error"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605377513874-Invalid-Client-Error"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:57Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issues", "invalid_client_error", "case_3ds_issue_issues_with_test_cards_sandbox"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

**Issue**: the merchant is getting an Invalid Client Error with a test card.

**Resolution**: Check that the merchant has the correct API keys enabled to process payments within the Sandbox environment and check that the merchant is using the correct token and keys to retrieve API calls. 

## Process Steps

### ABC/HUB

1. Navigate to the Hub

2. Input the relevant merchant

3. Navigate to the "Keys" tab

4. Check the "secret key", "public key", and "Channel ID" used to call our endpoint are correct

5. Check that the merchant is using the correct keys to retrieve via the logs or email the merchant for additional information

6. If this information is not visible in Hub, please use Datadog

7. 
If this issue occurs due to an invalid client secret bad request, investigate the logs and check if the event message has an invalid client secret and 400 bad request for the [connect token](https://access.sandbox.checkout.com/connect/token) (please see the images below from the DD logs, which highlight the error 400: bad request and error message Invalid client secret):

8. The event message invalid_client indicates that the access key ID or access secret key are incorrect. Please see the DD logs [here](https://app.datadoghq.com/logs?query=%40Properties.ClientId%3Aack_6a43rq3ophauhov4aw56zj6ij4%20&agg_m=count&agg_m_source=base&agg_t=count&cols=source%2C%40ActionName%2C%40Properties.ApplicationName%2C%40duration%2C%40GatewayElapsed%2C%40HttpStatusCode&event=AgAAAZJDlolRU_J3awAAAAAAAAAYAAAAAEFaSkRsbzJtQUFCUDZFZHZKaXhMOFFBQwAAACQAAAAAMDE5MjQzOWEtYWEyMS00ZDJhLTg1NzctZGEyYzljMzY5NGRh&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1725099233473&to_ts=1727691233473&live=true) and the screenshot below from the logs:

**Resolution**

1. To resolve this issue, please refer the merchant to the API reference page and ensure that they are using the correct access keys in addition to the correct channel ID

2. Please use the secret key sk_nukubdy*****(format : bearer sk_) from the API reference as well as the correct channel ID

Please see this [article](https://www.checkout.com/docs/developer-resources/api/manage-api-keys/oauth-2-0-client-credentials#Using_your_access_key) for more information. Please also see this [ticket](https://checkout1360.zendesk.com/agent/tickets/24823) as an example.  
 

### NAS

1. Open CAT in [sandbox](https://client-admin.cko-sbox.ckotech.co/web/nas/) in the NAS environment

2. In the Search box enter the merchant's name and press enter

3. Navigate to "Keys" on the left-hand side

4. Check the "Public key", "Secret key", "API Key ID", and "Scopes" are correct

5. Check that the merchant is using the correct keys to retrieve via the logs or email the merchant for additional information

6. If this information is not visible in NAS, please use Datadog

7. 
If this issue occurs due to an invalid client secret bad request, investigate the logs and check if the event message has an invalid client secret and 400 bad request for the [connect token](https://access.sandbox.checkout.com/connect/token) (please see the images below from the DD logs, which highlight the error 400: bad request and error message Invalid client secret):

8. 
The event message invalid_client indicates that the access key ID or access secret key are incorrect. Please see the DD logs [here](https://app.datadoghq.com/logs?query=%40Properties.ClientId%3Aack_6a43rq3ophauhov4aw56zj6ij4%20&agg_m=count&agg_m_source=base&agg_t=count&cols=source%2C%40ActionName%2C%40Properties.ApplicationName%2C%40duration%2C%40GatewayElapsed%2C%40HttpStatusCode&event=AgAAAZJDlolRU_J3awAAAAAAAAAYAAAAAEFaSkRsbzJtQUFCUDZFZHZKaXhMOFFBQwAAACQAAAAAMDE5MjQzOWEtYWEyMS00ZDJhLTg1NzctZGEyYzljMzY5NGRh&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1725099233473&to_ts=1727691233473&live=true) and the screenshot below from the logs:

**Resolution**

1. To resolve this issue, please refer the merchant to the API reference page and ensure that they are using the correct access keys in addition to the correct channel ID

2. Please use the secret key sk_nukubdy*****(format : bearer sk_) from the API reference as well as the correct channel ID

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
