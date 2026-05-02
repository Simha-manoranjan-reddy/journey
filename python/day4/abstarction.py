from abc import ABC, abstractmethod

class DataMiner(ABC):
    # This is the "Hiding" part. 
    # The user only calls this ONE method. They don't see the complex steps.
    def run_process(self):
        self.open_file()
        data = self.extract_data()  # <--- This is abstract!
        self.save_to_database(data)
        self.close_file()

    def open_file(self):
        print("Opening file...")

    @abstractmethod
    def extract_data(self):
        """Each file type does this differently"""
        pass

    def save_to_database(self, data):
        print(f"Saving {data} to the database...")

    def close_file(self):
        print("Closing file.\n")

# Concrete implementation for PDF
class PDFMiner(DataMiner):
    def extract_data(self):
        return "Data from PDF"

# Concrete implementation for CSV
class CSVMiner(DataMiner):
    def extract_data(self):
        return "Data from CSV"

# --- EXECUTION ---
pdf_tool = PDFMiner()
pdf_tool.run_process() # The user doesn't know 'extract_data' even exists!

csv_tool = CSVMiner()
csv_tool.run_process()
  