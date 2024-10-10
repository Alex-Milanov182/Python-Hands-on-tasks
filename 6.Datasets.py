import pandas as pd
from abc import ABC, abstractmethod
from datetime import datetime


class Dataset(ABC):
    @abstractmethod
    def _fetch_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def _transform_data(self):
        pass

    @abstractmethod
    def _clean_data(self):
        pass


class CSVDataset(Dataset):
    def __init__(self, src_filepath, target_filepath):
        self._src_filepath = src_filepath
        self._target_filepath = target_filepath
        self.data = None

    @property
    def src_filepath(self):
        return self._src_filepath

    @src_filepath.setter
    def src_filepath(self, value):
        self._src_filepath = value

    @property
    def target_filepath(self):
        return self._target_filepath

    @target_filepath.setter
    def target_filepath(self, value):
        self._target_filepath = value

    def _fetch_data(self):
     
        self.data = pd.read_csv(self.src_filepath)

    def _clean_data(self):
    
        self.data.Series_title_3 = 'Seasonally adjusted'
        self.data.Series_title_2 ='Mining'

    def _transform_data(self):
    
        self.data['timestamp'] = datetime.now()

    def save_data(self):
    
        self.data.to_csv(self.target_filepath, index=False)

    def __str__(self):
        return f"CSVDataset(src_filepath='{self.src_filepath}', target_filepath='{self.target_filepath}')"

    def __repr__(self):
        return f"CSVDataset(src_filepath='{self.src_filepath}', target_filepath='{self.target_filepath}')"


# deault source landing zone in vscode is c:\users\username   

def main():
    dataset = CSVDataset('employement-data.csv', 'cleaned-employement-data.csv')

    dataset._fetch_data()
    dataset._clean_data()
    dataset._transform_data()
    dataset.save_data()
    print(dataset.__str__())
    print(dataset.__repr__())


if __name__ == "__main__":
    main()


