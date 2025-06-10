# Non-Parametric Tests

- Chi-square Goodness-of-Fit
    - Test if distributions are the same
    - Need sufficient sample size to use (N=?)

 - (Pearson) Chi-square Test of Independence
    - Tests if 2+ random variables are related
    - H0: our variables are not related
    - Data are categorical (nominal/orginal)
    - Each variable has at least 5 observations

 - (Wilcoxon) Mann-Whitney U Test
    - Ordinal data, independent samples
    - One-way (?) t-test on ranks: Do samples originate from same distribution?
        - AKA, are the two sample means equal?
        - AKA, are our data samples different?
    - Compare 2 independent samples of equal (?) sample size

 - Wilcoxon Signed Ranks (Matched Pairs) Test
    - Ordinal data, paired samples
    - One-way (?) t-test on ranks: Do samples originate from same distribution?
    - Compare 2 independent samples of equal (?) sample size

- Kruskall-Wallis H Test
    - H0: the population meadians are equal
    - Data: continuous/discrete
    - "One-way ANOVA on ranks": Do samples originate from same distribution?
    - Compare 2+ independent samples of equal or different sample size
    - Better at outlier detection than ANOVA F-test if data are skewed
    - Assumptions:
        - Data are non-normal / skewed
        - Three variables of interest or more (2 groups: use Mann-Whitney test)
        - Equal variance across variables
        - Random variables are IID
        - Each variable has at least 5 observations

 - Mood's Median Test
    - Quantitative data only  
    - Less power than Mann-Whitney, Kruskall-Wallis - but when their assumptions fail, fall back on median test
        - Median test is sensitive to symmetry/scale parameters
    - H0: the means of 2+ groups are identical
    - A special case of Pearson's Chi-square test

#### Correlation
 - Spearman Rank Correlation Coefficient
    - used to compute correlation for categorial data
    - describes monotonic relationship between 2 variables (how well a monotonic function could model their relationship)
    - monotonic: almost “one-directional” - as X increases, Y never decreases - the function never changes sign/direction
    - useful for non-normally distributed continuous data, ordinal data, fairly robust to outliers

 - Kendall's Tau Correlation Coefficient
    - Ordinal data
    - Preferred over Spearman's r when there are few data samples and many rank ties
    - Concordance / discordance
    - Returns value between 0 (no relationship) to 1 (perfect relationship)
        - You can get negative values, but their value should be considered abs||- make positive
    - Formulas:
        - tau A = ???
        - tau B = (C - D) / (C + D)                     # adjusts for tied ranks; square table
        - tau C = (C - D) / ( (C + D) - #_tied_pairs)   # adjusts for tied ranks; rectangular table
    - Possiby less sensitive to outliers than Spearman's r, simpler? [https://www.statisticshowto.com/kendalls-tau/]

- Random to add:
    - Ordinal regresssion
    - Sign test: paired alternative to median test?
    - Chi-square distribution /table
    - Cronbach's alpha
    - Cramer's V

Citations:
 - https://www.uv.es/visualstats/vista-frames/help/lecturenotes/lecture09/lec9part4.html
 - https://www.scribbr.com/statistics/ordinal-data/
 - https://www.technologynetworks.com/informatics/articles/the-kruskal-wallis-test-370025 
 - https://pmc.ncbi.nlm.nih.gov/articles/PMC4966396/




from scipy.stats import chi2_contingency

results=[]
for model_name in range(len(model_names)):
    print(f'Creating Histogram for model {model_names[model_name]}')
    for model_next in range(model_name+1, len(model_names)):
        column1=model_names[model_name] 
        column2=model_names[model_next]

        test_name=f'{model_names[model_name]}_{model_names[model_next]}'
        cont_table=pd.crosstab(wmh_ratings[column1], wmh_ratings[column2])

        chi2, p, dof, expected = chi2_contingency(cont_table)

        print(f"Test: {test_name}, Chi2: {chi2}, P-value: {p}")

        if p > 0.05:
            print(f'Related variables: {test_name}')
        results.append((test_name, chi2, p))