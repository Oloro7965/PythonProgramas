import pandas as pd
projeto=pd.read_csv(r'https://gist.githubusercontent.com/guilhermesilveira/4d1d4a16ccbf6ea4e0a64a38a24ec884/raw/afd05cb0c796d18f3f5a6537053ded308ba94bf7/car-prices.csv')
print(projeto)
troca={
    'yes':1,
    'no':0
}
projeto.sold=projeto.sold.map(troca)
print(projeto)
projeto=projeto.drop(columns='0')
print(projeto)
