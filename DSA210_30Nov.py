#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DSA-210 Project – Apple vs Samsung
Final, cleaned & corrected version
"""

# ======================================
# 1. DATA COLLECTION
# ======================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, pearsonr

# --- Apple, Samsung ve Covid data yükleme ---
apple = pd.read_csv("apple.csv")
samsung = pd.read_csv("samsung.csv")
covid = pd.read_csv("corona.csv")

# ------------------------------------
# Samsung fiyat kolonunu otomatik bulma
# ------------------------------------
possible_price_cols = ["Close", "Price", "Adj Close", "Adj_Close", "Closing Price"]
samsung_price_col = None

for col in possible_price_cols:
    if col in samsung.columns:
        samsung_price_col = col
        break

print("Samsung price column found:", samsung_price_col)

if samsung_price_col is None:
    raise ValueError("Samsung veri setinde fiyat kolonu bulunamadı.")

# --- Tarih formatlarını düzenleme ---
apple['Date'] = pd.to_datetime(apple['Date'], format="mixed", dayfirst=True)
samsung['Date'] = pd.to_datetime(samsung['Date'], format="mixed", dayfirst=True)
covid['Date'] = pd.to_datetime(covid['Date'], format="mixed", dayfirst=True)

# ================================
# MERGE
# ================================
df = apple.merge(samsung, on='Date', how='inner')
df = df.merge(covid, on='Date', how='left')

# ================================
# RENAME
# ================================
df = df.rename(columns={
    "Close": "Apple_Price",             # Apple fiyat kolonu
    samsung_price_col: "Samsung_Price", # Samsung fiyat kolonu
    "New cases": "Covid_Cases"          # Covid günlük yeni vaka
})

# ================================
# SAYISAL KOLON TEMİZLİĞİ
# ================================
for col in ["Apple_Price", "Samsung_Price", "Covid_Cases"]:
    df[col] = (
        df[col]
        .astype(str)            # string yap
        .str.replace(",", "")   # 75,200 → 75200
        .str.replace(" ", "")   # boşluk varsa sil
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")

# İlk birkaç satır kontrol
df.head()

# ======================================
# 2. EXPLORATORY DATA ANALYSIS (EDA)
# ======================================

# ---- Summary statistics ----
print(df.describe())

# ---- Missing values ----
print(df.isnull().sum())

# ---- Time series plot ----
plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Apple_Price"], label="Apple")
plt.plot(df["Date"], df["Samsung_Price"], label="Samsung")
plt.title("Apple vs Samsung Stock Prices (2019–2024)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# ---- Covid cases plot ----
plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Covid_Cases"], alpha=0.4)
plt.title("Daily COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.show()

# ---- Correlation heatmap ----
plt.figure(figsize=(6,4))
sns.heatmap(df[['Apple_Price', 'Samsung_Price', 'Covid_Cases']].corr(), annot=True)
plt.title("Correlation Matrix")
plt.show()

# ---- Daily Returns ----
df['Apple_Return'] = df['Apple_Price'].pct_change()
df['Samsung_Return'] = df['Samsung_Price'].pct_change()

plt.figure(figsize=(10,5))
sns.histplot(df['Apple_Return'], kde=True, label="Apple")
sns.histplot(df['Samsung_Return'], kde=True, label="Samsung")
plt.legend()
plt.title("Daily Return Distribution")
plt.show()

# ======================================
# 3. HYPOTHESIS TESTS
# ======================================

# H1: Early COVID Growth Comparison (Apple vs Samsung)
early_period = df[df['Date'] < '2020-06-01']

apple_growth = early_period['Apple_Return'].dropna()
samsung_growth = early_period['Samsung_Return'].dropna()

t_stat, p_val = ttest_ind(apple_growth, samsung_growth)
print("H1 Apple vs Samsung Early Growth T-test")
print("t =", t_stat, " p =", p_val)

# H2 & H5: Monthly Price Comparison
df['Month'] = df['Date'].dt.to_period('M')
monthly = df.groupby('Month')[['Apple_Price', 'Samsung_Price']].mean().reset_index()

t_stat2, p_val2 = ttest_ind(monthly['Apple_Price'], monthly['Samsung_Price'])
print("Monthly Price Comparison T-test")
print("t =", t_stat2, " p =", p_val2)

# H3: Covid correlation (Apple & Samsung ile Covid aynı satırda dolu olanlar üzerinden)
# Apple için
apple_corr_df = df[['Covid_Cases', 'Apple_Price']].dropna()
corr_apple, p_apple = pearsonr(
    apple_corr_df['Covid_Cases'],
    apple_corr_df['Apple_Price']
)

# Samsung için
samsung_corr_df = df[['Covid_Cases', 'Samsung_Price']].dropna()
corr_samsung, p_samsung = pearsonr(
    samsung_corr_df['Covid_Cases'],
    samsung_corr_df['Samsung_Price']
)

print("COVID–Apple Price Correlation:", corr_apple, "p =", p_apple)
print("COVID–Samsung Price Correlation:", corr_samsung, "p =", p_samsung)

# H4: Post-2021 Volatility
post21 = df[df['Date'] > '2021-01-01']

vol_apple = post21['Apple_Return'].std()
vol_samsung = post21['Samsung_Return'].std()

print("Apple Volatility (post-2021):", vol_apple)
print("Samsung Volatility (post-2021):", vol_samsung)
