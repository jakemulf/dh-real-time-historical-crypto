from deephaven.parquet import read
from deephaven import merge

historical_data = read("/data/parquet")
all_data = merge([historical_data, real_time_data])
