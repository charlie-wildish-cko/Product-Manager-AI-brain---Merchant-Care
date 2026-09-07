---
id: 29999633138706
section_id: 22286660216722
title: "Merchant Dashboard Login Troubleshooting Cheat Sheet"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29999633138706-Merchant-Dashboard-Login-Troubleshooting-Cheat-Sheet"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-06T07:11:48Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

Merchant Login Troubleshooting Infographic
    
    
    
    
    
        body {
            font-family: 'Inter', sans-serif;
        }
        .flowchart-step {
            border: 2px solid #93c5fd;
            background-color: #eff6ff;
            color: #1e3a8a;
            border-radius: 0.5rem;
            padding: 1rem;
            text-align: center;
            position: relative;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        }
        .flowchart-connector {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 3rem;
            color: #3b82f6;
            font-size: 2rem;
            font-weight: bold;
        }
        .flowchart-decision {
             background-color: #f59e0b;
             color: white;
             border-radius: 9999px;
             padding: 1rem;
             border: 4px solid white;
             box-shadow: 0 0 0 2px #f59e0b;
        }
    

    
        
        
            Merchant Dashboard Login Troubleshooting
            

A quick visual guide for support agents to resolve access issues efficiently.
        

        
            

## Start Here: The First 3 Triage Questions

            
                
                    1
                    

### Environment?

                    

Are they on Sandbox or Production?
                
                
                    2
                    

### Correct Email?

                    

Is this the email registered to the Dashboard?
                
                
                    3
                    

### Login Method?

                    

Password + MFA or Single Sign-On (SSO)?
                
            
        

        
            

## Main Troubleshooting Paths

            
                
                
                    

### 🔐 Path A: Password + MFA Issues

                    
                        Step 1: Encourage Self-Service
                        

Guide merchant to the "Reset Dashboard password" article.
                        MACRO: Access issue first response- Password+MFA
                    
                    ↓
                     
                        Did Self-Service Fail?
                    
                     ↓
                    
                        Step 2: Agent Intervention (Okta Tool)
                        

Search for user and select "Reset or Remove password".
                        
                            
                                

Recommended: Reset Link
                                

Link expires in 1 hour. Use the "Password reset- link valid for 1 hour" macro.
                            
                            
                                

Alternative: Temporary Password
                                

CRITICAL: Send ONLY to the user directly, using a side conversation if needed.
                            
                        
                    
                

                
                    

### 🌐 Path B: Single Sign-On (SSO) Issues

                    
                        Step 1: Direct to Administrator
                        

Guide merchant to contact their company's IDP Administrator.
                         MACRO: Access issue first response- SSO user login issue
                    
                    ↓
                    
                        Can IDP Admin Resolve It?
                    
                    ↓
                    
                        Step 2: Escalate to IAM Team
                        

If the IDP admin cannot fix the issue, create a ticket for the Identity & Access Management team. Provide all necessary details.
                    
                
            
        

        
            

## 🚨 Critical Reminders

            
                
                    

### Key Takeaways

                    

                        
- 
**Self-Service First:** Always guide users to self-service options before intervening.
                        
- 
**1 Hour Expiry:** Password reset links are only valid for one hour.
                        
- 
**Direct Contact Only:** Temporary passwords must only be shared directly with the dashboard user.
                        
- 
**No Shared Accounts:** Ensure all users sign in with their own credentials.
