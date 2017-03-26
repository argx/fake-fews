# data.py

# TODO: Look at faster data storage/retrievel technologies, like SQL
# TODO: How about firing an event to retrain after every 20 new FB data points come?

import glob, os, random, csv

class Data:
    """ Data abstraction between raw data and classifiers """

    # Stores parsed data
    schema = "Type,Category,Credibility,Title,Content,Retrieval Source"
    stored_data_file = "stored_data.csv"

    def __init__(self, data_dir):
        """ Data constructor """

        # Populate self once created
        self.arr = []
        self.data_dir = data_dir
        self.populate()

    def store(self, line):
        """ Write given line to stored data file """

        with open(data_dir + "/" + stored_data_file) as f:
            f.write(line)

    def populate(self):
        """
        Populate data array from all CSV files in data directory
        """

        # Get all data files in res/data
        os.chdir(self.data_dir)
        for f in glob.glob("*.csv"):

            # Parse each file and add to total data
            file_parsed = self.parse_file(f)
            self.arr += file_parsed

            # Shuffle data array (because training order has effects)
            random.shuffle(self.arr)

    def parse_file(self, f):
        """
        Parse given file in the format
        [[v_11, ..., v_1n], ..., [v_m1, ..., v_mn]]
        for each value v_ij, where i is the row number and j
        is the column number
        """

        file_parsed = []

        with open(f, encoding = "utf8") as csv_file:

            # Check for schema compatibility
            file_schema = csv_file.readline().strip()
            if file_schema.encode("utf8") != self.schema.encode("utf8"):
                raise ValueError("File's schema incompatible")

            # Grab CSV lines
            i = 0
            reader = csv.reader(csv_file)
            for line in reader:

                i += 1

                # Skip schema row
                if i == 1: continue

                # Grab parsed line values
                line_vals = line
                file_parsed.append(line_vals)


            return file_parsed
