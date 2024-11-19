import pandas as pd
import time
from abc import ABC, abstractmethod


# Change paths correspondingly matching your local machine
json_path = 'C:\\Users\\Aleksandar.Milanov\\Desktop\\data.json'
csv_path = 'C:\\Users\\Aleksandar.Milanov\\Desktop\\output.csv'

# Abstract Dataset Class
class Dataset(ABC):
    
    @abstractmethod
    def preview(self):
        pass
    
    @abstractmethod
    def show_schema(self):
        pass
    
    @abstractmethod
    def get_data(self):
        pass
    
    @abstractmethod
    def write_data(self, file_path):
        pass


# JSONDataset Implementation
class JSONDataset(Dataset):
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_json(file_path)
    
    def preview(self):
        return self.data.head()
    
    def show_schema(self):
        return self.data.dtypes
    
    def get_data(self):
        return self.data
    
    def write_data(self, file_path):
        self.data.to_json(file_path, orient='records', lines=True)


# CSVDataset Implementation
class CSVDataset(Dataset):
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
    
    def preview(self):
        return self.data.head()
    
    def show_schema(self):
        return self.data.dtypes
    
    def get_data(self):
        return self.data
    
    def write_data(self, file_path):
        self.data.to_csv(file_path, index=False)


# Source and Sink Classes
class Source:
    
    def __init__(self, dataset: Dataset):
        self.dataset = dataset


class Sink:
    
    def __init__(self, dataset: Dataset):
        self.dataset = dataset


# Abstract Activity Class
class Activity(ABC):
    
    @abstractmethod
    def start(self):
        pass


# WaitActivity Implementation
class WaitActivity(Activity):
    
    def __init__(self, time_in_seconds):
        self.time_in_seconds = time_in_seconds
    
    def start(self):
        print(f"Waiting for {self.time_in_seconds} seconds...")
        time.sleep(self.time_in_seconds)


# CopyActivity Implementation
class CopyActivity(Activity):
    
    def __init__(self, source: Source, sink: Sink):
        self.source = source
        self.sink = sink
    
    def start(self):
        print("Starting CopyActivity...")
        
        # Get data from source
        data = self.source.dataset.get_data()
        
        # Copy data to the sink's dataset
        self.sink.dataset.data = data
        
        # After copying data, write it to the sink (CSV or JSON depending on the dataset type)
        
        self.sink.dataset.write_data(csv_path)
        
        print(f"Data copied and saved to {csv_path}!")


# Pipeline Class
class Pipeline:
    
    def __init__(self):
        self.activities = []
    
    def add_activity(self, activity: Activity):
        self.activities.append(activity)
    
    def execute(self):
        for activity in self.activities:
            activity.start()


# Example Usage:
# Define dataset instances (mock paths for example purposes)
json_dataset = JSONDataset(json_path)  # Assuming data.json exists
csv_dataset = CSVDataset(csv_path)

# Define source and sink
source = Source(json_dataset)
sink = Sink(csv_dataset)

# Create activities
wait_activity = WaitActivity(time_in_seconds=2)
copy_activity = CopyActivity(source=source, sink=sink)

# Print priview of the set 
print(json_dataset.preview())

# Create pipeline and add activities
pipeline = Pipeline()
pipeline.add_activity(wait_activity)
pipeline.add_activity(copy_activity)

# Execute the pipeline
pipeline.execute()