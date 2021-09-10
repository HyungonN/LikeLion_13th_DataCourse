### data_eda
import data_myeda
import seaborn as sns


tips = sns.load_dataset("tips")

data_myeda.basicinfo(tips)