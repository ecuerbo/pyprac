import seaborn as sns

sns.set_style('ticks')

tips=sns.load_dataset('tips')

sns.relplot(x='total_bill',
            y='tip',
            hue='day',
            size='size',
            data=tips)