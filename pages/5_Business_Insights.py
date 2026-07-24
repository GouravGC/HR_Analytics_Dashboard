import streamlit as st

st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Business Insights and Recommendations")

st.markdown("""
This section synthesizes the analytical findings into actionable business insights and provides recommendations for HR strategies. 
""")

st.subheader("Key Findings")
st.markdown("""
- **High Attrition in Sales and Human Resources:** These departments show the highest attrition rates, suggesting a need for targeted retention strategies.
- **Age Group '26-35' Dominance:** The workforce is relatively young, indicating potential for long-term career development but also a need for clear career progression paths to retain talent.
- **Gender Pay Gap:** A slight discrepancy in average salaries between genders warrants further investigation to ensure pay equity.
- **Promotion Stagnation:** A notable portion of employees has 'Long Pending' promotion status, which could impact morale and lead to attrition. Reviewing promotion policies and career ladders is essential.
- **Work-Life Balance:** Average work-life balance ratings are consistent but not exceptional across departments, suggesting a company-wide initiative could be beneficial.
- **Distance from Home Impact:** Sales employees have a higher average commute distance, which could be a contributing factor to attrition or dissatisfaction.
""")

st.subheader("Recommendations")
st.markdown("""
1.  **Targeted Retention Programs:** Develop specific retention programs for the Sales and Human Resources departments, focusing on understanding and addressing their unique challenges (e.g., workload, career development, compensation).
2.  **Review Compensation & Equity:** Conduct a deeper dive into salary structures, especially focusing on the identified gender pay gap. Ensure compensation is competitive and equitable across all roles and demographics.
3.  **Enhance Career Development:** Implement structured career development plans and mentorship programs, particularly for the '26-35' age group and employees with 'Long Pending' promotion status. This can improve engagement and reduce perceived stagnation.
4.  **Improve Work-Life Balance Initiatives:** Explore company-wide or department-specific initiatives to enhance work-life balance, such as flexible working arrangements, wellness programs, or workload management training.
5.  **Optimize Commute Strategies:** For roles requiring significant travel or long commutes (e.g., Sales), consider implementing solutions like remote work options, subsidized transport, or regional office hubs to mitigate the impact of distance from home.
6.  **Regular Feedback & Engagement Surveys:** Implement regular pulse surveys and feedback mechanisms to continuously monitor employee satisfaction, identify emerging issues, and adapt HR strategies proactively.
""")

st.info("These insights are derived from the data analysis and aim to provide a starting point for strategic HR decisions. Further qualitative research and deeper dives into specific areas may be required.")
