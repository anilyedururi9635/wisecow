import psutil
import time

CPU_THRESHOLD = 80  
MEM_THRESHOLD = 80  
DISK_THRESHOLD = 85 

def check_system_health():
    print("--- System Health Check ---")

    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f" ALERT: High CPU usage detected: {cpu_usage}%")
    else:
        print(f" CPU usage is normal: {cpu_usage}%")

    mem_info = psutil.virtual_memory()
    mem_usage = mem_info.percent
    if mem_usage > MEM_THRESHOLD:
        print(f" ALERT: High Memory usage detected: {mem_usage}%")
    else:
        print(f" Memory usage is normal: {mem_usage}%")
  
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        print(f" ALERT: High Disk usage detected: {disk_usage}%")
    else:
        print(f" Disk usage is normal: {disk_usage}%")
      
    running_processes = len(psutil.pids())
    print(f"Running processes: {running_processes}")
    
    print("---\n")

if __name__ == "__main__":
    try:
        while True:
            check_system_health()
            time.sleep(30) 
    except KeyboardInterrupt:
        print("Monitoring stopped.")
