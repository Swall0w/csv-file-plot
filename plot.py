import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'TakaoPGothic'

def plot_dataframe(dataframe,cycle_num):
    dataframe = dataframe[dataframe['INT']==cycle_num]
    del_columns = ['Index','Date','Clock','Raw','SampID','INT']
    dataframe = dataframe.drop(del_columns,axis=1)
    dataframe.reset_index(inplace=True,drop=True)

    dataframe.plot(subplots=True,figsize=(10,8))
    filename = 'cycle_{0}.png'
    plt.savefig(filename.format(cycle_num))

def main():
    dataframe = pd.read_csv('output.csv')
    cycle_list = dataframe['INT'].value_counts().index.tolist()
    for cycle_num in cycle_list:
        plot_dataframe(dataframe,cycle_num)

if __name__ == '__main__':
    main()
