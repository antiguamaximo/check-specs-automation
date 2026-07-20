#!/usr/bin/env python3
"""
System Information Checker
Gathers and displays system information in a cross-platform way.
"""

import platform
import os
import sys
import socket
import psutil
from datetime import datetime


def get_system_info():
    """Gather and display system information."""
    print("=" * 60)
    print("SYSTEM INFORMATION REPORT")
    print("=" * 60)
    print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # OS Information
    print("--- Operating System ---")
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}\n")
    
    # Hostname and Network
    print("--- Network ---")
    print(f"Hostname: {socket.gethostname()}")
    try:
        print(f"IP Address: {socket.gethostbyname(socket.gethostname())}")
    except:
        print("IP Address: Unable to determine")
    print()
    
    # CPU Information
    print("--- CPU ---")
    print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
    print(f"Total Cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    cpu_freq = psutil.cpu_freq()
    if cpu_freq is not None and cpu_freq.current is not None:
        print(f"CPU Frequency: {cpu_freq.current:.2f} MHz")
    else:
        print("CPU Frequency: Unable to determine")
    print()
    
    # Memory Information
    print("--- Memory ---")
    memory = psutil.virtual_memory()
    print(f"Total RAM: {memory.total / (1024**3):.2f} GB")
    print(f"Available RAM: {memory.available / (1024**3):.2f} GB")
    print(f"Used RAM: {memory.used / (1024**3):.2f} GB")
    print(f"Memory Usage: {memory.percent}%\n")
    
    # Disk Information
    print("--- Disk ---")
    disk = psutil.disk_usage('/')
    print(f"Total Disk: {disk.total / (1024**3):.2f} GB")
    print(f"Used Disk: {disk.used / (1024**3):.2f} GB")
    print(f"Free Disk: {disk.free / (1024**3):.2f} GB")
    print(f"Disk Usage: {disk.percent}%\n")
    
    # Python Information
    print("--- Python ---")
    print(f"Python Version: {sys.version}")
    print(f"Python Implementation: {platform.python_implementation()}\n")
    
    print("=" * 60)


if __name__ == "__main__":
    try:
        get_system_info()
    except Exception as e:
        print(f"Error gathering system information: {e}", file=sys.stderr)
        sys.exit(1)
