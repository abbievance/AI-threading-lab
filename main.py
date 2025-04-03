import threading
import requests
import time

# List of URLs and filenames
urls = [
    'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD',
    'https://data.cityofnewyork.us/api/views/c3uy-2p5r/rows.csv?accessType=DOWNLOAD',
    'https://edg.epa.gov/EPADataCommons/public/OA/EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv',
    'https://ecos.fws.gov/ServCat/DownloadFile/173741?Reference=117348',
    'https://data.nasa.gov/api/views/gh4g-9sfh/rows.csv?accessType=DOWNLOAD'
]

filenames = [
    'ElectricVehicleData.csv',
    'AirQualityData.csv',
    'WalkabilityIndex.csv',
    'WaterQualityData.csv',
    'MeteoriteLandings.csv'
]

# Function to download the file and write to CSV
def download_files(url, filename, thread_number):
    print(f"Thread {thread_number} starting")
    start_time = time.time()
    
    # Send GET request to the URL, disable SSL verification
    response = requests.get(url, verify=False)
    
    # Write the content to a CSV file
    with open(filename, 'wb') as file:
        file.write(response.content)
    
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    
    print(f"Thread {thread_number}: {filename} downloaded in {elapsed_time} seconds")

# Create threads without using for loops
def create_threads():
    thread1 = threading.Thread(target=download_files, args=(urls[0], filenames[0], 1))
    thread2 = threading.Thread(target=download_files, args=(urls[1], filenames[1], 2))
    thread3 = threading.Thread(target=download_files, args=(urls[2], filenames[2], 3))
    thread4 = threading.Thread(target=download_files, args=(urls[3], filenames[3], 4))
    thread5 = threading.Thread(target=download_files, args=(urls[4], filenames[4], 5))
    
    # Start each thread
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    # Wait for all threads to finish
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

# Main function to execute the program
if __name__ == "__main__":
    create_threads()
