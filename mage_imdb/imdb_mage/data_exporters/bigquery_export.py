from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
import os
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    now = kwargs.get('execution_date')
    now = now.strftime('%Y_%m_%d')
    project = os.environ.get('GCP_PROJECT_ID')
    dataset = os.environ.get('BIGQUERY_DATASET')
    print(f'{os.environ.get("BIGQUERY_TABLE")}/{str(now)}')
    table = f'{os.environ.get("BIGQUERY_TABLE")}_{str(now)}'

    table_id = f'{project}.{dataset}.{table}'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        table_id,
        if_exists='replace',  # Specify resolution policy if table name already exists
    )
