import pandas as pd

sample_info = pd.read_csv('https://raw.githubusercontent.com/Ignas12345/masters_project_data_and_notebooks/refs/heads/main/Data/sample_annotations/TCGA_TGCT_sample_data.csv', sep = '|', index_col=0)
mature_teratoma_burden = sample_info['Mature %'].fillna(0, inplace=False).rename('mature_teratoma_burden')
immature_teratoma_burden = sample_info['Immature %'].fillna(0, inplace=False).rename('immature_teratoma_burden')
total_teratoma_burden = (mature_teratoma_burden + immature_teratoma_burden).rename('total_teratoma_burden')

teratoma_burden_df = pd.concat([mature_teratoma_burden, immature_teratoma_burden, total_teratoma_burden], axis=1)
teratoma_burden_df.index.name = 'sample_id'
teratoma_burden_df.to_csv('teratoma_burden_df.csv')