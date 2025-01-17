<div align="center">
  <img src="https://github.com/samuelsemaya/e-commerce-customer-churn/blob/main/e-commerce-customer-churn/e-commerce_churn.png?raw=true" alt="e-commerce-churn" style="width:600px; height:500px">
</div>

# 1. Business Understanding
---
> ## 1.1 Context
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

> ## 1.2 Problem Hypotesis
---
<div style='text-align: justify'>

The main problem lies in ShopWise's inability to differentiate between customers who are potential churners and those who are loyal. As a result, promotions are given indiscriminately, both to customers who are likely to leave the platform (churn) and those who already have a high level of loyalty. This not only leads to a waste of resources on customers who don't actually need additional incentives, but also reduces the effectiveness of retention efforts towards customers at risk of churning.

</div>

> ## 1.3 Main Stakeholder
---
<div style='text-align: justify'>
The primary stakeholder for this project is the <b>Head of Customer Experience and Marketing Optimization</b>. This position is suitable as the main stakeholder because:

1. <b>Comprehensive oversight</b>: This role manages customer retention efforts, customer behavior analysis, and marketing budget allocation, providing a holistic view of customer-centric strategies.

2. <b>Strategic alignment</b>: The position ensures that customer experience initiatives and marketing activities are in sync with broader business objectives.

3. <b>Data-driven decision making</b>: With access to customer behavior analytics, this stakeholder can make informed choices about retention strategies and budget optimization.

4. <b>Resource optimization</b>: By overseeing both customer experience and marketing budgets, this role can effectively balance resources between retention and acquisition efforts.

5. <b>Direct impact on key metrics</b>: The responsibilities of this position directly influence critical performance indicators such as customer retention rates, lifetime value, and marketing ROI.
</div>

> ## 1.4 Goals
---
<div style='text-align: justify'>

To address this issue, ShopWise needs to develop a more targeted strategy for offering promotions. By identifying customers who are at high risk of churning, the company can allocate marketing resources more effectively, improve customer retention, and ultimately optimize the promotional budget.

</div>

> ## 1.5 Analytic Approach
---
<div style='text-align: justify'>
Our analytic approach focuses on developing a predictive model to identify e-commerce customers at risk of churning. We will analyze historical customer data, perform feature engineering, and test various machine learning algorithms. The model will be optimized to maximize recall, ensuring early detection of at-risk customers. The result is a prediction system that enables the customer retention team to take proactive action, with the ultimate goal of reducing churn and increasing customer loyalty.
</div>

# 13. Conclusion & Recommendation
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

<b>A healthy CLV:CAC ratio for e-commerce is typically around 3:1</b>. So, it's understands that CLV is **\$ 210**

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

<b>Savings:</b>  
Total savings = \$ 45,780 - \$ 9,520 = \$ 36,260  
Percentage savings = (\$ 36,260 / \$ 45,780) * 100 ≈ 79.2%

<b>Considering False Negatives:</b>  
FN = 12 customers who will actually churn but are not detected   
Potential loss = 12 * \$ 210 (CLV) = \$ 2,520

<b>Net Savings:</b>  
Net savings = \$ 36,260 - \$ 2,520 = \$ 33,740

From a business perspective, ShopWise can observe that:  
1. By using machine learning, ShopWise can save 79.2% of promotional costs, similar to the previous analysis, but with a higher nominal value.  
2. Net savings have significantly increased to $33,740, demonstrating a greater positive impact from implementing the ML model.  
3. Total cost ML implementation = Promotional Cost with ML + Potential Loss from FN= \$ 9,520 + \$ 2,520 = \$ 12,040<br><br>
<b>ROI</b> = (Net Savings / Total Cost of ML Implementation) * 100
= (\$ 33,740 / \$ 12,040) * 100 ≈ 280.2%
<br><br>

<div style='text-align: justify'>
With this exceptionally high ROI, ShopWise is in a strong position not only to improve short-term profitability but also to make strategic investments that can drive long-term business growth and sustainability. This demonstrates that the implementation of machine learning is not just a tool for operational efficiency, but also a catalyst for broader business transformation.
</div>

<br>

**Feature Importance Affecting Churn**  
From the many factors influencing customer churn, 3 main factors have been identified:

|Feature|Description|
|-------|-----------|
|`Tenure`|Tenure has the largest impact on churn, with an influence level more than 200% compared to other factors. The lower the Tenure value, indicating newer customers, the higher the likelihood of churn. Conversely, customers with longer Tenure tend to be more loyal to the company's services.|
|`Complain`|Complain is the second strongest factor influencing churn. A higher Complain value indicates customer dissatisfaction with the service, thus increasing the risk of churn. On the other hand, customers without complaints tend to be more satisfied and have a lower likelihood of churning.|
|`NumberOfAddress`|NumberOfAddress is the third significant factor. A higher number of addresses may indicate high customer mobility or complexity in order management, potentially increasing the risk of churn. Customers with fewer addresses may have more stable purchasing patterns and a lower likelihood of churning.|

> ## 13.2 Recommendation
---
>> ### For Business
---
#### **1. Implement a Robust Loyalty Program**

**Key Feature: Tenure**

Our analysis shows that "Tenure" is the most important feature in predicting customer churn. A well-designed loyalty program can significantly increase customer tenure.

- Develop a tiered loyalty program that rewards long-term customers
- Offer exclusive benefits, early access to sales, or personalized discounts based on tenure
- Implement a points system that encourages frequent purchases and long-term engagement

#### **2. Enhance Customer Service and Complaint Resolution**

**Key Feature: Complain**

The "Complain" feature is the second most important, highlighting the critical role of effective complaint handling and customer service.

- Invest in training for customer service representatives to handle complaints efficiently
- Implement a streamlined process for quick complaint resolution
- Regularly analyze complaint data to identify and address recurring issues

#### **3. Personalize Customer Experience**

**Key Features: NumberOfAddress, NumberOfDeviceRegistered**

The high importance of "NumberOfAddress" and "NumberOfDeviceRegistered" suggests that personalization based on customer behavior is crucial.

- Utilize data on multiple delivery addresses and devices to create tailored shopping experiences
- Implement AI-driven product recommendations based on browsing and purchase history
- Develop targeted marketing campaigns for different customer segments

#### **4. Optimize Pricing and Cashback Strategies**

**Key Feature: CashbackAmount**

The significance of "CashbackAmount" indicates that financial incentives play a vital role in customer retention.

- Analyze the effectiveness of current cashback offerings and adjust as needed
- Implement dynamic pricing strategies based on customer segments and purchase history
- Consider bundled pricing or subscription models for frequently purchased items

#### **5. Improve Product Availability and Delivery Efficiency**

**Key Features: DaySinceLastOrder, WarehouseToHome**

The importance of "DaySinceLastOrder" and "WarehouseToHome" highlights the need for efficient inventory management and delivery processes.

- Optimize inventory levels to ensure product availability and reduce stockouts
- Improve logistics to decrease delivery times and enhance the "WarehouseToHome" experience
- Implement predictive analytics for demand forecasting and inventory management

  >> ### For Modeling
---
<div style='text-align: justify'>

1. Provide additional data information related to customer churn to further improve prediction accuracy.

2. Add a 'customer ID' column to identify duplicate data more accurately and minimize errors.

3. Integrate external data such as e-commerce market trends, macroeconomic data, or social media sentiment into the model to enhance the model's ability to understand factors influencing churn.

4. Implement an automated model monitoring and retraining system that can detect model performance degradation and trigger retraining processes with the latest data.

5. Develop other types of product trend prediction models that can anticipate future market demands.

</div>
