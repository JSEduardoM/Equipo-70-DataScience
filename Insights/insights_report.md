# Business Insights & Recommendations Report

## Executive Summary
The E-commerce Churn Model project has successfully analyzed customer behavior, trained predictive models, and segmented customers based on risk. The overall churn rate is approximately **16.8%**. We have identified key drivers of churn and developed a Random Forest model with **~93% accuracy** to predict future churn.

## Key Findings
### 1. Primary Drivers of Churn
- **Tenure**: Newer customers are significantly more likely to churn. Long-term customers show high loyalty.
- **Cashback Amount**: Lower cashback amounts are associated with higher churn, suggesting that rewards programs are effective.
- **Warehouse to Home**: Distance does play a role, but less than tenure and rewards.
- **Complaints**: Customers with recent complaints have a higher propensity to churn.

### 2. Model Performance
- The **Random Forest** classifier outperformed Logistic Regression and Decision Trees.
- **Accuracy**: 93%
- **ROC-AUC**: 0.97 (Excellent discrimination between churners and non-churners).

### 3. Risk Segmentation
Customers have been grouped into three segments:
- **High Risk (>70% probability)**: Immediate attention required.
- **Medium Risk (30-70% probability)**: Watch list, preventative measures needed.
- **Low Risk (<30% probability)**: Loyal base, potential for upselling.

## Recommendations
### Strategic Actions
1. **Onboarding Focus**: Since low tenure is a major risk factor, improve the onboarding experience for new customers in their first 1-3 months.
2. **Complaint Resolution**: Implement a "White Glove" service recovery protocol for customers who log complaints, as this is a strong signal of potential churn.
3. **Reward Optimization**: Review the Cashback program. Ensure high-value customers are receiving competitive rewards to maintain their loyalty.
4. **Targeted Campaigns**:
    - **High Risk**: Send personalized "We miss you" offers or exclusive discounts to re-engage.
    - **Medium Risk**: Send engagement content (newsletters, product tips) to keep them active without aggressive discounting.

## Next Steps
- Deploy the model to run weekly on new data.
- Integrate risk scores into the CRM for the support team.
- A/B test retention offers on the High Risk segment.
