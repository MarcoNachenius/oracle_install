from db_operations.db_writer import DatabaseWriter

db_writer = DatabaseWriter()
db_writer.populate_combinatorials_table(batchSize=1000)