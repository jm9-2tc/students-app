import re

class Table:
  def __init__(self, columns: list[str], records: list[dict]):
    self.header = columns
    self.records = records

  @staticmethod
  def from_csv(csv: str):
    rows = csv.splitlines()
    columns = rows[0].split(';')
    records = list(map(lambda row: Table.__prepare_record(columns, row), rows[1:]))
    return Table(columns, records)

  @staticmethod
  def __prepare_record(header: list, row: str):
    row_list = row.split(';')
    row_dict = {}
    for n, field in enumerate(row_list):
      row_dict[header[n]] = field if not re.match('^[0-9]+$', field) else int(field)
    return row_dict