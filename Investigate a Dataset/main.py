import pandas as pd

def count_feature(input_df, column_name):
    input_df["separated"] = input_df[column_name]
    
    new_df = input_df.separated.str.split(pat="|",expand=True).stack().value_counts().reset_index()
    
    new_df.columns = ['Word', 'Frequency'] 
    
    return new_df.head(10)


df = pd.read_csv("https://d17h27t6h515a5.cloudfront.net/topher/2017/October/59dd1c4c_tmdb-movies/tmdb-movies.csv")


dff = df.sort_values(by=['revenue_adj'], ascending=False).head(10)


# Top 10 keywords in top 10 revenue movies
print("keywords\n", count_feature(df, "keywords"))
# Top 10 genres in top 10 revenue movies 
print("genres\n", count_feature(df, "genres"))
# Top 10 production_companies in top 10 revenue movies 
print("production_companies\n", count_feature(df, "production_companies"))
# Top 10 cast in top 10 revenue movies 
print("cast\n", count_feature(df, "cast"))
# Average runtime of top 10 revenue movies 
print(dff['runtime'].mean(axis=0))
