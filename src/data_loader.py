"""
ATSF-OSC Data Loader

Loads software component datasets used for training
and evaluating the AI-Powered Trust Scoring Framework.
"""

from pathlib import Path
import pandas as pd


class DataLoader:
    """
    Loads CSV datasets for ATSF-OSC.
    """

    def __init__(self, data_directory="data"):
        self.data_directory = Path(data_directory)

    def load_csv(self, filename):
        """
        Load a CSV dataset.

        Parameters
        ----------
        filename : str

        Returns
        -------
        pandas.DataFrame
        """

        file_path = self.data_directory / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {file_path}"
            )

        return pd.read_csv(file_path)

    def summary(self, dataframe):
        """
        Display basic dataset information.
        """

        print("=" * 50)
        print("Dataset Summary")
        print("=" * 50)
        print(f"Rows: {len(dataframe)}")
        print(f"Columns: {len(dataframe.columns)}")
        print(dataframe.head())