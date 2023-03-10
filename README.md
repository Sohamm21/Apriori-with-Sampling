# Apriori Algorithm with Sampling

Apriori Algorithm for Association Rule Mining
The Apriori algorithm is a popular algorithm in data mining used for mining frequent itemsets and relevant association rules from a dataset. It is mainly used for market basket analysis to identify items that are frequently purchased together. The algorithm works by generating a set of candidate itemsets, and then pruning the sets that do not meet the minimum support threshold. The process is repeated until no more frequent itemsets can be generated.

In a dataset with a large number of items, running Apriori on the entire dataset can be computationally expensive and time-consuming. To overcome this problem, we can use a sampling technique to reduce the size of the dataset while preserving the statistical properties of the original dataset.

There are two main sampling techniques that can be used to sample a dataset:
- Random sampling: where we randomly select a subset of the dataset.
- Stratified sampling: where we divide the dataset into strata based on some characteristic (e.g., age group, gender, etc.), and then sample from each stratum proportionally to its size.

In this repo, I have provided an implementation of the Apriori algorithm with sampling in Python using the apyori library. This implementation includes function for random sampling.

### Getting Started
NOTE: You should have streamlit environment setupped in your anaconda
To use our implementation of the Apriori algorithm, you will need to have Python 3.x installed on your machine. You will also need to install the apyori library by running the following command:
```python
pip install apyori
pip install streamlit
pip install mlxtend
```

After installing the required dependencies make a textfile file in the jupyter notebook and paste the code.
After pasting the code save the file with python extension and open the environment terminal where the streamlit has been setupped.
To run the code use the command 'streamlit run filename.py'
