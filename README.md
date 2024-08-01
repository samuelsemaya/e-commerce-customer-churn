<div style='text-align: center'>
<img src='e-commerce_churn.png' alt='e-commerce_churn' style='width:600px; height:500px'>
</div>

## Context
---

<div style='text-align: justify'>
ShopWise is an e-commerce startup based in Indonesia, founded in 2018. The company offers a wide range of products, including electronics, fashion, household goods, and groceries. Since its inception, ShopWise has shown rapid growth, reaching 5 million monthly active users by 2023.  
<br><br>
Despite ShopWise's impressive user growth, the company faces challenges in retaining existing customers. The churn rate (customers who stop using the platform) has increased in recent months, becoming a serious concern for the management team. This situation is similar to that experienced by many other e-commerce platforms in a highly competitive market, where customers have numerous choices and can easily switch to other platforms <b>[1]</b>.
<br><br>
ShopWise has implemented various strategies to improve customer retention, including loyalty programs and regular promotions. However, the effectiveness of these programs has not been optimal due to a lack of personalization and precise targeting. This aligns with findings from a study showing that personalized customer retention strategies can increase customer loyalty by up to 20% <b>[2]</b>.
<br><br>
To address this issue, ShopWise plans to develop a churn prediction model that can identify customers at high risk of leaving the platform. This approach is based on best practices in the e-commerce industry, where predictive analytics has proven effective in improving customer retention <b>[3]</b>.
</div>
<br>
<b>References:</b><br>  
[1] Chen, J. (2022). "E-commerce Customer Retention Strategies in Competitive Markets". Journal of Digital Marketing, 15(3), 245-260.<br>  
[2] Smith, A. & Johnson, B. (2023). "The Impact of Personalization on E-commerce Customer Loyalty". International Journal of E-Business Research, 18(2), 112-128.<br>  
[3] Brown, L. (2021). "Predictive Analytics in E-commerce: A Comprehensive Guide". New York: Tech Publishing House.

## Problem Hypotesis
---

<div style='text-align: justify'>

The main problem lies in ShopWise's inability to differentiate between customers who are potential churners and those who are loyal. As a result, promotions are given indiscriminately, both to customers who are likely to leave the platform (churn) and those who already have a high level of loyalty. This not only leads to a waste of resources on customers who don't actually need additional incentives, but also reduces the effectiveness of retention efforts towards customers at risk of churning.

</div>

## Main Stakeholder
---

<div style='text-align: justify'>
The primary stakeholder for this project is the <b>Head of Customer Retention and Marketing Analytics</b>. This position is suitable as the main stakeholder because:<br>

1. Directly responsible for customer retention efforts and customer behavior analysis.

2. Has a vested interest in understanding the factors that cause churn and developing strategies to reduce it.

3. Can use the model's prediction results to design targeted marketing campaigns and loyalty programs.

4. Has the authority to implement recommendations based on insights from the model.

5. Typically collaborates with the data science team to apply analytical solutions in business strategy.

By using the churn prediction model, the team can take proactive measures to retain valuable customers before they leave the e-commerce platform.
</div>

## Goals
---

<div style='text-align: justify'>

To address this issue, ShopWise needs to develop a more targeted strategy for offering promotions. By identifying customers who are at high risk of churning, the company can allocate marketing resources more effectively, improve customer retention, and ultimately optimize the promotional budget.

</div>

## Conclusion
---

<div style='text-align: justify'>

Best Model: **LightGBM**

Based on the Classification Report of Tuned LGBM Tomek above, the following results were obtained:

- The model has an overall accuracy of 92%, indicating good performance in predicting both classes.
- The model successfully identified 89% of churning customers, enabling the implementation of targeted retention strategies.
- 93% of loyal customers were correctly identified, helping to maintain appropriate services for them.
- An average recall of 91% demonstrates the model's good ability to distinguish between the two groups, supporting effective customer retention strategies.

Based on the additional data references, the Customer Acquisition Cost (CAC) in an e-commerce business has an average of **$ 70** per customer.

Customer Acquisition Cost (CAC) is the total cost a business spends to acquire new customers, including sales and marketing expenses. It's an important metric for businesses to determine customer profitability and sales efficiency.

Customer Lifetime Value (CLV) is the total amount of profit a customer brings to a company over the course of their relationship with the business.

A healthy CLV:CAC ratio for e-commerce is typically around 3:1. So, it's understands that CLV is **\$ 210**

|Name|Price ($)|
|:---:|:-----:|
|Customer Acquisition Cost (CAC)| 70|
|Customer Lifetime Value (CLV)|  210|

<br>

<b>References:</b>  
[Reference 1](https://www.productplan.com/glossary/customer-acquisition-cost/) ; 
[Reference 2](https://userpilot.com/blog/average-customer-acquisition-cost/) ; 
[Reference 3](https://firstpagesage.com/reports/average-cac-for-ecommerce-companies/) ;
[Reference 4](https://www.shopify.com/blog/customer-acquisition-cost)

</div>

Based on the data above, we can derive the following information:
- Total customers: 654  
- CAC (promotional cost per customer): \$ 70  
- CLV: \$ 210  

**Without Machine Learning:**  
ShopWise provides promotions to all customers because the company cannot distinguish between churning and non-churning customers.  
Total cost = 654 * \$ 70 = \$ 45,780

**With Machine Learning:**  
ShopWise only needs to provide promotions to customers predicted to churn.   
 
Customers predicted to churn = TP + FP = 95 + 41 = 136  
Total cost = 136 * \$ 70 = \$ 9,520

Savings:  
Total savings = \$ 45,780 - \$ 9,520 = \$ 36,260  
Percentage savings = (\$ 36,260 / \$ 45,780) * 100 ≈ 79.2%

Considering False Negatives:  
FN = 12 customers who will actually churn but are not detected   
Potential loss = 12 * \$ 210 (CLV) = \$ 2,520

Net Savings:  
Net savings = \$ 36,260 - \$ 2,520 = \$ 33,740

From a business perspective, ShopWise can observe that:  
1. By using machine learning, ShopWise can save 79.2% of promotional costs, similar to the previous analysis, but with a higher nominal value.  
2. Net savings have significantly increased to $33,740, demonstrating a greater positive impact from implementing the ML model.  
3. ROI from ML implementation = (Net Savings / Promotional Cost with ML) * 100  
   = (\$ 33,740 / \$ 9,520) * 100 ≈ 354.4%.  

With this exceptionally high ROI, ShopWise is in a strong position not only to improve short-term profitability but also to make strategic investments that can drive long-term business growth and sustainability. This demonstrates that the implementation of machine learning is not just a tool for operational efficiency, but also a catalyst for broader business transformation.

**Feature Importance Affecting Churn**  
From the many factors influencing customer churn, 3 main factors have been identified:

|Feature|Description|
|-------|-----------|
|`Tenure`|Tenure has the largest impact on churn, with an influence level more than 200% compared to other factors. The lower the Tenure value, indicating newer customers, the higher the likelihood of churn. Conversely, customers with longer Tenure tend to be more loyal to the company's services.|
|`Complain`|Complain is the second strongest factor influencing churn. A higher Complain value indicates customer dissatisfaction with the service, thus increasing the risk of churn. On the other hand, customers without complaints tend to be more satisfied and have a lower likelihood of churning.|
|`NumberOfAddress`|NumberOfAddress is the third significant factor. A higher number of addresses may indicate high customer mobility or complexity in order management, potentially increasing the risk of churn. Customers with fewer addresses may have more stable purchasing patterns and a lower likelihood of churning.|

## Recommendation
---

### For Business
---

<div style='text-align: justify'>

1. **Tiered Loyalty Program**<br>
   Implement a tiered reward system with increasing cashback, access to exclusive offers, and free shipping based on shopping frequency and value.

2. **Customer Experience Personalization**<br>
   Enhance personalization across all touchpoints with tailored product recommendations, content, and offers based on shopping behavior data.

3. **Customer Education and Engagement**<br>
   Host webinars and educational content on topics relevant to ShopWise products to increase added value and strengthen brand relationships.

4. **Omnichannel Customer Service**<br>
   Integrate customer service across various channels with a robust CRM system to improve speed and quality of problem resolution.

5. **Continuous Feedback Program**<br>
   Launch a "Voice of Customer" initiative for regular collection and implementation of customer feedback, demonstrating commitment to improvement based on customer input.

</div>

### For Modeling
---

<div style='text-align: justify'>

1. Provide additional data information related to customer churn to further improve prediction accuracy.

2. Add a 'customer ID' column to identify duplicate data more accurately and minimize errors.

3. Integrate external data such as e-commerce market trends, macroeconomic data, or social media sentiment into the model to enhance the model's ability to understand factors influencing churn.

4. Implement an automated model monitoring and retraining system that can detect model performance degradation and trigger retraining processes with the latest data.

5. Develop other types of product trend prediction models that can anticipate future market demands.

</div>
