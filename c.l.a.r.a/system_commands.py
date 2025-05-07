import os
import subprocess
import psutil
import winreg
import ctypes
from datetime import datetime

class SystemCommands:
    def __init__(self):
        self.command_phrases = {
            'shutdown': {
                'phrases': [
                    "shutdown computer", "turn off computer", "power off",
                    "shutdown pc", "turn off pc", "shutdown system",
                    "power down", "shutdown now", "turn off now"
                ],
                'function': self.shutdown_computer
            },
            'restart': {
                'phrases': [
                    "restart computer", "reboot computer", "restart pc",
                    "reboot pc", "restart system", "reboot system",
                    "restart now", "reboot now"
                ],
                'function': self.restart_computer
            },
            'sleep': {
                'phrases': [
                    "sleep mode", "put computer to sleep", "sleep pc",
                    "sleep system", "go to sleep", "enter sleep mode"
                ],
                'function': self.sleep_computer
            },
            'volume_up': {
                'phrases': [
                    "volume up", "increase volume", "turn up volume",
                    "raise volume", "volume higher", "louder"
                ],
                'function': self.volume_up
            },
            'volume_down': {
                'phrases': [
                    "volume down", "decrease volume", "turn down volume",
                    "lower volume", "volume lower", "quieter"
                ],
                'function': self.volume_down
            },
            'mute': {
                'phrases': [
                    "mute", "mute volume", "silence", "turn off sound",
                    "no sound", "mute audio"
                ],
                'function': self.mute_volume
            },
            'brightness_up': {
                'phrases': [
                    "brightness up", "increase brightness", "brighter",
                    "turn up brightness", "more brightness"
                ],
                'function': self.brightness_up
            },
            'brightness_down': {
                'phrases': [
                    "brightness down", "decrease brightness", "dimmer",
                    "turn down brightness", "less brightness"
                ],
                'function': self.brightness_down
            },
            'battery_status': {
                'phrases': [
                    "battery status", "battery level", "check battery",
                    "how much battery", "battery percentage", "power status"
                ],
                'function': self.get_battery_status
            },
            'system_info': {
                'phrases': [
                    "system info", "system information", "computer info",
                    "pc information", "system specs", "computer specs"
                ],
                'function': self.get_system_info
            },
            'disk_space': {
                'phrases': [
                    "disk space", "free space", "storage space",
                    "hard drive space", "disk usage", "storage usage"
                ],
                'function': self.get_disk_space
            },
            'running_processes': {
                'phrases': [
                    "running processes", "active processes", "current processes",
                    "what's running", "show processes", "list processes"
                ],
                'function': self.get_running_processes
            },
            'network_status': {
                'phrases': [
                    "network status", "internet status", "connection status",
                    "check network", "check internet", "network info"
                ],
                'function': self.get_network_status
            }
        }
    
    def shutdown_computer(self):
        """Shutdown the computer"""
        try:
            os.system("shutdown /s /t 60")
            return "Computer will shutdown in 60 seconds. Say 'cancel shutdown' to abort."
        except Exception as e:
            return f"Error shutting down: {str(e)}"
    
    def restart_computer(self):
        """Restart the computer"""
        try:
            os.system("shutdown /r /t 60")
            return "Computer will restart in 60 seconds. Say 'cancel restart' to abort."
        except Exception as e:
            return f"Error restarting: {str(e)}"
    
    def sleep_computer(self):
        """Put computer to sleep"""
        try:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            return "Putting computer to sleep."
        except Exception as e:
            return f"Error putting computer to sleep: {str(e)}"
    
    def volume_up(self):
        """Increase system volume"""
        try:
            from ctypes import cast, POINTER
            from comtypes import CLSCTX_ALL
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            current_volume = volume.GetMasterVolumeLevelScalar()
            volume.SetMasterVolumeLevelScalar(min(1.0, current_volume + 0.1), None)
            return "Volume increased."
        except Exception as e:
            return f"Error adjusting volume: {str(e)}"
    
    def volume_down(self):
        """Decrease system volume"""
        try:
            from ctypes import cast, POINTER
            from comtypes import CLSCTX_ALL
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            current_volume = volume.GetMasterVolumeLevelScalar()
            volume.SetMasterVolumeLevelScalar(max(0.0, current_volume - 0.1), None)
            return "Volume decreased."
        except Exception as e:
            return f"Error adjusting volume: {str(e)}"
    
    def mute_volume(self):
        """Mute system volume"""
        try:
            from ctypes import cast, POINTER
            from comtypes import CLSCTX_ALL
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            volume.SetMute(1, None)
            return "Volume muted."
        except Exception as e:
            return f"Error muting volume: {str(e)}"
    
    def brightness_up(self):
        """Increase screen brightness"""
        try:
            # This requires additional setup with WMI
            import wmi
            wmi_obj = wmi.WMI(namespace="wmi")
            monitors = wmi_obj.WmiMonitorBrightnessMethods()
            for monitor in monitors:
                monitor.WmiSetBrightness(100, 0)
            return "Brightness increased."
        except Exception as e:
            return f"Error adjusting brightness: {str(e)}"
    
    def brightness_down(self):
        """Decrease screen brightness"""
        try:
            # This requires additional setup with WMI
            import wmi
            wmi_obj = wmi.WMI(namespace="wmi")
            monitors = wmi_obj.WmiMonitorBrightnessMethods()
            for monitor in monitors:
                monitor.WmiSetBrightness(0, 0)
            return "Brightness decreased."
        except Exception as e:
            return f"Error adjusting brightness: {str(e)}"
    
    def get_battery_status(self):
        """Get battery status"""
        try:
            battery = psutil.sensors_battery()
            if battery:
                percent = battery.percent
                power_plugged = battery.power_plugged
                status = "plugged in" if power_plugged else "on battery"
                return f"Battery is at {percent}% and {status}."
            return "No battery found."
        except Exception as e:
            return f"Error getting battery status: {str(e)}"
    
    def get_system_info(self):
        """Get system information"""
        try:
            info = {
                "OS": os.name,
                "Platform": os.sys.platform,
                "Machine": os.sys.machine,
                "Processor": os.sys.processor,
                "CPU Count": os.cpu_count(),
                "Memory": f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
            }
            return "\n".join(f"{k}: {v}" for k, v in info.items())
        except Exception as e:
            return f"Error getting system info: {str(e)}"
    
    def get_disk_space(self):
        """Get disk space information"""
        try:
            partitions = psutil.disk_partitions()
            space_info = []
            for partition in partitions:
                if partition.fstype:
                    usage = psutil.disk_usage(partition.mountpoint)
                    space_info.append(
                        f"{partition.device}: {usage.percent}% used "
                        f"({usage.free / (1024**3):.2f} GB free)"
                    )
            return "\n".join(space_info)
        except Exception as e:
            return f"Error getting disk space: {str(e)}"
    
    def get_running_processes(self):
        """Get list of running processes"""
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    pinfo = proc.info
                    processes.append(
                        f"{pinfo['name']}: CPU {pinfo['cpu_percent']}%, "
                        f"Memory {pinfo['memory_percent']:.1f}%"
                    )
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            return "\n".join(processes[:10])  # Return top 10 processes
        except Exception as e:
            return f"Error getting processes: {str(e)}"
    
    def get_network_status(self):
        """Get network status information"""
        try:
            net_io = psutil.net_io_counters()
            return (
                f"Network Status:\n"
                f"Bytes sent: {net_io.bytes_sent / (1024**2):.2f} MB\n"
                f"Bytes received: {net_io.bytes_recv / (1024**2):.2f} MB"
            )
        except Exception as e:
            return f"Error getting network status: {str(e)}"
    
    def process_command(self, query):
        """Process system command query"""
        query = query.lower()
        for command, data in self.command_phrases.items():
            if any(phrase in query for phrase in data['phrases']):
                return data['function']()
        return None 