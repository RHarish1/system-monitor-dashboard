import psutil

def get_system_metrics():
    # Fetch system statistics
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory().percent
    disk_info = psutil.disk_usage('/').percent
    
    # Return the metrics as a dictionary
    return {
        'cpu': cpu_usage,
        'memory': memory_info,
        'disk': disk_info
    }
