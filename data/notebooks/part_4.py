from deephaven.time import now
from deephaven.parquet import write

write(real_time_data, f"/data/parquet/{now().toDateString()}.parquet")
