import seaborn as sns
import matplotlib.pyplot as plt

def plot(data, name1):
    d = data[['age_norm_inv', 'index_r']].melt()
    d = d.reset_index()
    d['index'] = [0, 0]
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 5))
    fig.tight_layout()
    for ax, name, text, set_xlabel in zip(axes, 
                                        ['age_norm_inv', 'index_r'], 
                                        [d[d.variable=='age_norm_inv']['value'][0], d[d.variable=='index_r']['value'][1]],
                                        ['Индекс возраст дома', 'Техническое состояние дома']):
        index = d[d['variable'] == name]['index'].values
        value = d[d['variable'] == name]['value'].values
        if value<0.5:
            ax.bar(index, value, color=sns.xkcd_rgb["pale red"])
        else:
            ax.bar(index, value, color=sns.xkcd_rgb["medium green"])
        ax.set_xticks([-1, 0, 1])
        ax.set_xticklabels(['', '', ''])
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
        ax.set_xlabel(set_xlabel)
        ax.text(-0.08, text + 0.01, str(int(round(text, 2)*100)) +' %', size=20) 
        plt.savefig('app/static/' + str(name1))