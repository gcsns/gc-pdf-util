financial_analysis_section_description="""
You are an expert analyst specializing in analyzing companies' annual reports and gleaning insights into their financial health.
The user will ask you to generate a financial report about various aspects of a company's health.
IMPORTANT NOTE: YOU ALREADY HAVE THE DATA FROM THAT SPECIFIC COMPANY'S ANNUAL REPORT INSIDE YOUR KNOWLEDGE BASE, DO NOT ASK TEH USER  TO SPECIFY THE COMPANY NAME, YOU ALREADY HAVE IT IN THE KNOWLEDGEBASE.
"""

financial_analysis_section_instructions = [
    "Your entire knowledgebase contains pages from a company's 10-k filings or annual report.",
    "Your task is to create a set of insights and and statistics and summaries asked for by the user.",
    "Try not to use special characters that would be hard to render",
    "Only use information given in knowledge base don't add things on your own.",
    "Your output must be in a markdown format that should be renderable in latex. DO NOT CREATE TABLES"
]

financial_analysis_section_queries = [
    """
You have all the information from a company's annual report inside your knowledge base, use it to generate the reports, insights and summaries that I ask for.
Using the combined information from Item 1 (Business Overview), Item 1A (Risk Factors), Item 7A (Quantitative and Qualitative Disclosures About Market Risk) from the latest 10-K filing of the company, perform a detailed analysis to provide:

1. **Business and Financial Overview**:
    - **Core Business Operations**: Summarize the main activities and market positions outlined in Item 1.
    - **Financial Health**: From Item 8, highlight key financial metrics and year-over-year changes.
    - **Management Analysis**: Extract key insights from Item 7 about financial trends, operational challenges, and management's strategic focus.

2. **Integrated Risk Profile**:
    - **Risk Landscape**: Using information from Item 1A and Item 7A, identify and describe the major operational and market risks.
    - **Impact and Mitigation**: Discuss the potential impacts of these risks on the business and financial performance, and outline the risk mitigation strategies provided by management across these sections.

Format your output as a markdown.
The first level heading should be 'Risk Analysis'.
Business and Financial Overview should be a second level heading.
Integrated Risk Profile should be a second level heading.
""",

"""
You have all the information from a company's annual report inside your knowledge base, use it to generate the reports, insights and summaries that I ask for.
Using the combined information from Item 1 (Business Overview), Item 1A (Risk Factors), Item 7A (Quantitative and Qualitative Disclosures About Market Risk) from the latest 10-K filing of the company,identify and analyze three positive and three negative aspects regarding the company's prospects. Organize your analysis in the following format:

1. **Positive Insights**:
    - **Strengths and Opportunities**: Detail three major strengths or opportunities that the company is poised to capitalize on.
    - **Potential Positive Outcomes**: Discuss the possible beneficial outcomes if these strengths and opportunities are effectively leveraged.

2. **Negative Insights**:
    - **Challenges and Threats**: Enumerate three significant challenges or threats facing the company.
    - **Potential Negative Consequences**: Explore the potential adverse impacts these challenges could have on the company's future performance.
Format your output as a markdown.
The first level heading should be 'Business Insights'.
Positive Insights should be a second level heading.
Negative Insights should be a second level heading.
""",

"""  
You have all the information from a company's annual report inside your knowledge base, use it to generate the reports, insights and summaries that I ask for.          
With reference to the information available in Item 1 (Business Overview), Item 1A (Risk Factors), Item 7A (Quantitative and Qualitative Disclosures About Market Risk) of the company's recent 10-K filing, synthesize a strategic report that addresses:

1. **Strategic Positioning and Opportunities**:
- **Market Dynamics**: Analyze the business landscape as described in Item 1 and Item 7, focusing on competitive positioning and market opportunities.
- **Operational Strengths**: Highlight operational strengths and efficiencies that bolster the company's market position.

2. **Future Financial Prospects**:
- **Financial Projections**: Discuss future financial prospects based on trends and data from Item 7 and Item 8.
- **Risk and Opportunities Balance**: Weigh the financial risks (Item 1A and 7A) against potential opportunities, and discuss how the company plans to leverage its strengths to mitigate these risks and capitalize on market trends.
Format your output as a markdown.
The first level heading should be 'Strategic Analysis'.
Strategic Positioning and Opportunities should be a second level heading.
Future Financial Prospects should be a second level heading.
"""
] 