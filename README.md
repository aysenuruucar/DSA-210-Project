# DSA-210-Project
Apple vs Samsung

**Project Overview**

Two of the largest smartphone producing companies in the worldwide technology sector are Apple and Samsung. The performance of the company as well as more general market and social developments are reflected in their stock values. I want to know how external influences like the COVID-19 epidemic affected the growth of Apple and Samsung by comparing their price data after 2019. Through this study, I will be able to investigate the connection between business performance and world events and use data science techniques to financial statistics.

**Project Goal**

My goal is to gain an understanding of how global crises impact technology businesses by monitoring the stock prices of Apple and Samsung and comparing them with COVID-19 daily case data.  The objective is to compare and contrast their growth patterns and assess how external shocks affect the behavior of the stock market.

**Research Questions**

- What kind of change has occurred in prices of Apple and Samsung products between 2019 and 2024?
- Did Apple and Samsung show the same growth before and after COVID-19 pandemic
- Is there any relationship between price changes ofg Apple and Samsung products and daily COVID-19 cases?
- How can we compare average prices of Apple and Samsung products over time?
- Which company show a faster adaptation in terms of price changes to the pandemic period?

**Hypothesis**
H1: In the early months of the COVID-19 pandemic, Apple's stock price rose faster than Samsung's.   
H2: Due to its slow response to market shifts, Samsung's price growth behind Apple's by many months.
H3: Increases in the number of COVID-19 cases worldwide are positively correlated with rising Apple stock prices.  
H4: After 2021, Samsung's prices either remained or decreased, whereas Apple continued its more steady increasing path.  
H5: Apple often outperforms Samsung in terms of monthly average returns.

**Methodology**
To test these hypotheses, the following methods will be applied:
- Data Collection: Daily and monthly Apple and Samsung stock prices (2019–2024) and global number of COVID-19 daily cases  
- Data Cleaning: Sorting dates, correcting missing values, and converting prices to matching units.  
- Exploratory Data Analysis (EDA): Scatter plots, histograms, and time series visualizations to identify trends.  
- Statistical Testing: 
  - Correlation analysis (Pearson/Spearman) between COVID-19 cases and stock prices.  
  - T-tests or ANOVA to compare Apple vs Samsung monthly averages.
- Regression Models:
  - Time series regression to measure the impact of COVID-19 cases on stock prices.  
  - Comparing slope analysis to measure growth rates of Apple vs Samsung.  
- Volatility Analysis: Standard deviation and rolling-window variance to compare stability of both stocks.  

**Data Set**

I will use Apple and Samsung prices collected between 2019 and 2024, and COVID-19 cases in 2020.

https://drive.google.com/file/d/1sGcr0XrHXHw8YZJzJMbZOtYRHZ-aNMtw/view
https://drive.google.com/file/d/1Ofgj5of1Z2hqK7m56NUK9elm4o2gyTt8/view
https://drive.google.com/file/d/13XBYn3st4CzG28sLrm7aRFJ46WiPuxRH/view

**Primary Data Collection**

The dataset will be built using three main sources:  
1. Apple stock price records (daily and monthly averages).  
2. Samsung stock price records (daily and monthly averages).  
3. COVID-19 daily new cases dataset
Data will be merged by date to create a unified dataset. Cleaning steps will include handling missing values, aligning timestamps, and ensuring consistent units.

**Data Structure**

The dataset will include these variables:
- Date: The exact date of measurement.  
- Apple Price: Daily closing price of Apple stock.  
- Samsung Price: Daily closing price of Samsung stock.  
- Monthly Average Apple Price: Combined monthly average.  
- Monthly Average Samsung Price: Combined monthly average.  
- COVID-19 New Cases: Daily COVID-19 cases around the world. 

