from deephaven.table_listener import listen

def listener_function(update, is_replay):
    print("Large change detected")

    added_dict = update.added()
    for key in added_dict.keys():
        print(f"Column: {key}")
        print(f"Value: {added_dict[key]}")

listener_table = real_time_data.where(["abs(1 - (Price_[i]/Price_[i-1])) > 0.01"])

handle = listen(listener_table, listener_function)
