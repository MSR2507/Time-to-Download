size_of_download = float(input('Size of Download (in GB): > '))
average_speed = float(input('Average download speed (in MB/s): > '))

size_mb = size_of_download * 1000
time_in_seconds = size_mb / average_speed
time_in_minutes = time_in_seconds / 60
time_in_hours = time_in_minutes / 60

print(f'Download will take approx {int(time_in_hours)} hour(s) and {int(time_in_minutes % 60)} minutes to complete.')
