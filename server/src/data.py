# data.py

# TODO: Look at faster data storage/retrievel technologies, like SQL
# TODO: How about firing an event after every 20 new FB data points come?

import glob, os, random

class Data:
    """ Data abstraction between raw data and classifiers """

    # Stores parsed data
    arr = []
    data_dir = None
    schema = "Type,Category,Credibility,Title,Content,Retrieval Source"
    stored_data_file = "stored_data.csv"

    def __init__(self, data_dir):
        """ Data constructor """

        self.data_dir = data_dir

    def store(self, line):
        """ Write given line to stored data file """

        with open(data_dir + "/" + stored_data_file) as f:
            f.write(line)

    def parse(self, csv_file):
        """
        Populate data arr from raw data_file
        NOTE: data_file must be .csv!
        """

        # Get all data files in res/data
        os.chdir(self.data_dir)
        for file in glob.glob("*.csv"):

            # Parse each file and add to total data
            file_parsed = self.parse_file(file)
            self.arr.join(file_parsed)

        # Shuffle data array (because training order has effects)
        random.shuffle(self.arr)

    def parse_file(self, file):
        """
        Parse given file in the format
            [[v_11, ..., v_1n], ..., [v_m1, ..., v_mn]]
            for each value v_ij, where i is the row number and j
            is the column number
        """

        file_parsed = []

        with open(file, 'r') as csv_file:

            # Check for schema compatibility
            file_schema = csv_file.readline()
            if file_schema != self.schema:
                raise ValueError("File's schema incompatible")

            # Grab CSV lines
            i = 0
            reader = csv.reader(csv_file)
            for line in reader:

                    # Skip schema row
                    if i == 0: continue

                    # Grab parsed line values
                    line_vals = line
                    file_parsed.append(line_vals)

                    i += 1

        return file_parsed
