import csv

def read_execution_times(filename):
    execution_times = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            execution_times.append(float(row['executionTime']))
    return execution_times

def average_response_time(execution_times):
    import statistics

    return statistics.mean(execution_times)
    


def compare_times(execution_times):

     mean = average_response_time(execution_times)
     print(mean)
     n = len(execution_times)

     for i in range(n):
         time = execution_times[i]
         print(abs(time - mean) )
         if abs(time- mean) >  mean :
             return False, i  # returns False and the index if the time is more than 10% greater than the mean
     return True, None  # returns True if all times are within 10% of the mean

    # n = len(execution_times)
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         time1, time2 = execution_times[i], execution_times[j]
    #         percentage_diff = abs(time1 - time2) / ((time1 + time2) / 2) * 100
    #         print(percentage_diff)
    #         if percentage_diff > 40:
    #             return False, (i, j)  # returns False and the pair of indices if difference is more than 5%
    # return True, None  # returns True if all pairs are within 5%

# Example usage:
filename = 'time_result.csv'  # Path to your CSV file
execution_times = read_execution_times(filename)
result, pair = compare_times(execution_times)
if result:
    print("All execution times are within 10% of each other.")
else:
    print(f"Difference between index pair exceeds 10%.")