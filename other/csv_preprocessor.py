import pandas as pd

df = pd.read_csv('data/tmdbmovies.csv')


def insert_row(dataframe, row, index):
    row = pd.DataFrame(row).T
    return pd.concat([dataframe.iloc[:index], row, dataframe.iloc[index:]]).reset_index(drop=True)


new_df = pd.DataFrame(columns=['id', 'imdb_id', 'popularity', 'budget', 'revenue', 'original_title',
                               'cast', 'homepage', 'director', 'tagline', 'keywords', 'overview',
                               'runtime', 'genres', 'production_companies', 'release_date',
                               'vote_count', 'vote_average', 'release_year', 'budget_adj',
                               'revenue_adj'])
for i in df.iterrows():
    if i[1].get('director'):
        if isinstance(i[1]['director'], str):
            if '|' in i[1]['director']:
                base_row = i[1]
                directors = i[1]['director'].split('|')
                for d in directors:
                    new_row = base_row.copy()
                    new_row['director'] = d
                    new_df = pd.concat([new_df, pd.DataFrame(new_row).T])
            else:
                new_df = pd.concat([new_df, pd.DataFrame(i[1]).T])
        else:
            new_df = pd.concat([new_df, pd.DataFrame(i[1]).T])
    else:
        new_df = pd.concat([new_df, pd.DataFrame(i[1]).T])

new_df = new_df.reset_index(drop=True)
