# Quantitative-Easing-and-Global-Oil-Futures-The-Unseen-Market-Choreography
This study examines the impact of unconventional monetary policies, specifically quantitative easing (QE) and quantitative tightening (QT), on daily WTI
and Brent futures return. Focusing on announcements from the Great Recession to COVID-19 by the Federal Reserve, European Central Bank, and Bank of Eng-
land, the research investigates how these policies influence the daily returns of oil futures. Key transmission channels, such as foreign exchange, economic expectations, supply, and investor displacement, are highlighted. Empirical evidence shows that Federal Reserve LSAP announcements primarily affect WTI futures the day after through the exchange rate and economic expectation channels, with effect of -2.95 and -0.16 log percentage points, respectively. Similar effects are observed for Bank of England and European Central Bank announcements on Brent Crude futures. Additionally, open interest changes in oil futures contracts surrounding policy announcements show greater variability for easing announcements compared to tightening suggesting there is more economic uncertainty surrounding oil when QE is announced.

---

## Introduction  
This repository accompanies my MSc research project, *Quantitative Easing and Global Oil Futures: The Unseen Market Choreography*. The study explores how unconventional monetary policy—specifically quantitative easing (QE) and quantitative tightening (QT)—affects global oil markets through their impact on WTI and Brent crude futures.  

Since the Great Recession of 2008, central banks in advanced economies have relied heavily on QE and other large-scale asset purchase (LSAP) programs to stabilize financial markets. While much of the literature has examined the effect of these policies on bond yields, equities, and exchange rates, relatively less attention has been paid to their impact on commodities, especially oil. Given oil’s role as the lifeblood of the global economy, understanding how central bank announcements shape futures pricing is crucial for both policymakers and market participants.  

This project investigates how LSAP announcements from the **Federal Reserve, European Central Bank, and Bank of England** between 2008 and 2024 influenced oil futures returns, with a focus on identifying the transmission channels through which these effects operate.  

---

## Literature Review  
The relationship between oil and the macroeconomy has been well documented since Hamilton’s (1983) seminal work, which established that oil shocks often precede recessions. Barsky and Kilian (2004) extended this literature by emphasizing the role of monetary policy responses to oil shocks. More recent studies, such as Bernanke et al. (1997) and Gagliardone & Gertler (2023), highlight the importance of monetary tightening in amplifying the macroeconomic effects of oil shocks.  

In parallel, research on quantitative easing has focused on its effects on asset prices through channels such as signaling, portfolio balance, and exchange rates (Krishnamurthy & Vissing-Jorgensen, 2011; Rosa, 2012; Lyonnet & Werner, 2012). Commodity-specific studies (Frankel, 2006; Anzuini et al., 2013; Rosa, 2014) show that monetary policy affects oil through inventory costs, speculative demand, and real economic expectations. Malliaris et al. (2020) and more recent post-COVID work (Yang et al., 2023; Miranda-Pinto et al., 2023) confirm the importance of unconventional monetary policy in shaping commodity price dynamics.  

This project contributes by bringing these strands together: analyzing how QE and QT announcements transmit to oil futures markets, and whether effects differ across the Fed, ECB, and BoE.  

---

## Overview of Quantitative Easing Programs  
- **Federal Reserve:** Four LSAP programs (2008–2024), ranging from QE1 during the Great Recession to QE4 during COVID-19, involving trillions of dollars in Treasury, MBS, and agency debt purchases.  
- **Bank of England:** Five QE rounds (2009–2022), with large-scale gilt purchases and, in QE4, corporate debt. QE5 was introduced during the pandemic and tapered in 2022.  
- **European Central Bank:** Began QE formally in 2015 with the Asset Purchase Programme (APP), later supplemented by the Pandemic Emergency Purchase Programme (PEPP) in 2020, with cumulative purchases exceeding €1 trillion.  

These programs provide a rich set of policy shocks to test their effects on oil futures pricing.  

---

## Transmission Channels  
The study identifies four main channels linking QE/QT announcements to oil futures markets:  

1. **Foreign Exchange:** Because oil is priced in U.S. dollars, QE that weakens the dollar can increase demand from foreign buyers, boosting futures prices.  
2. **Economic Expectations:** LSAP announcements convey information about future growth. Tapering often signals confidence in recovery, which can raise oil demand expectations.  
3. **Investor Displacement (Portfolio Balance):** Large-scale central bank purchases of Treasuries and MBS displace investors, who may reallocate into commodities. Changes in futures open interest capture this channel.  
4. **Inventory:** QE lowers financing costs, reducing the opportunity cost of holding oil inventories. This encourages stockpiling and supports futures prices, while QT does the opposite.  

---

## Data  
The dataset includes **47 LSAP-related announcements** between 2008 and 2024:  
- 20 from the Federal Reserve  
- 16 from the European Central Bank  
- 11 from the Bank of England  

Oil market data:  
- Daily front-month futures prices for WTI (CME/NYMEX) and Brent (ICE)  
- Weekly U.S. crude oil inventories (EIA)  
- Non-commercial open interest in WTI futures (CFTC)  

Other financial variables:  
- Exchange rates (DXY, GBP/USD, EUR/USD)  
- 10-year breakeven inflation rates (U.S. and U.K.)  
- CBOE VIX Index  
- MSCI World Equity Index  
- U.S. 10-Year Treasury futures (ZN1)  

---

## Methodology  
The empirical strategy uses an **event study framework** with narrow event windows (t–1 to t+1) to capture announcement effects.  

Regression specifications include:  
- **Dependent Variable:** Log-return of WTI or Brent front-month futures.  
- **Independent Variables:** Exchange rate returns, breakeven inflation changes, inventory changes, open interest changes, equity returns, VIX, and Treasury futures returns.  
- **LSAP Dummy:** Equals 1 on announcement days, 0 otherwise.  

This combination of event study logic and OLS regression allows identification of both announcement effects and the channels through which they operate.  

---

## Results  
The findings demonstrate that QE and QT announcements have significant and asymmetric effects on oil futures markets:  

- **Federal Reserve LSAPs:** Strongest effects on WTI futures, particularly the day after announcements. The exchange rate channel (–2.95%) and economic expectation channel (–0.16%) explain much of the variation.  
- **Bank of England and ECB LSAPs:** Greater influence on Brent futures, reflecting Europe’s pricing role in global oil markets.  
- **Investor Displacement:** Non-commercial open interest shows higher variability during QE than QT, consistent with greater uncertainty and speculative repositioning.  
- **Inventory Effects:** Evidence suggests QE lowers inventory costs and supports futures prices, while QT raises carrying costs and pressures prices downward.  

---

## Conclusion  
This project provides evidence that unconventional monetary policies by major central banks significantly influence global oil futures markets. The results highlight the importance of transmission channels—particularly exchange rates and economic expectations—while also showing that QE-induced investor displacement and inventory adjustments play a meaningful role.  

For policymakers, the findings suggest that QE has spillover effects beyond domestic financial markets, extending into commodities that are central to global economic stability. For investors, the study underscores that oil futures are sensitive to monetary policy surprises, with implications for risk management and hedging strategies.  

This repository contains the full research workflow, including data sources, analysis scripts, figures, and LaTeX files of the thesis, to enable reproducibility and future research extensions.  
