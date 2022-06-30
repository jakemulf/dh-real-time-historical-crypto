from deephaven.plot.figure import Figure

all_plot = Figure().plot_xy(series_name="Price", t=all_data, x="Timestamp", y="Price").show()
historical_plot = Figure().plot_xy(series_name="Price", t=historical_data, x="Timestamp", y="Price").show()
real_time_plot = Figure().plot_xy(series_name="Price", t=real_time_data, x="Timestamp", y="Price").show()
