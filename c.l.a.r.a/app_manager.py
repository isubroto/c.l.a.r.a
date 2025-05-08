import os
import subprocess
import psutil
import win32gui
import win32process
import win32con
import win32api
import time

class AppManager:
    def __init__(self):
        # Common Windows applications and their executable names
        self.app_aliases = {
            # Browsers
            'chrome': 'chrome.exe',
            'firefox': 'firefox.exe',
            'edge': 'msedge.exe',
            'opera': 'opera.exe',
            'brave': 'brave.exe',
            'safari': 'safari.exe',
            
            # Microsoft Office
            'word': 'WINWORD.EXE',
            'excel': 'EXCEL.EXE',
            'powerpoint': 'POWERPNT.EXE',
            'outlook': 'OUTLOOK.EXE',
            'access': 'MSACCESS.EXE',
            'publisher': 'MSPUB.EXE',
            'onenote': 'ONENOTE.EXE',
            'office': 'WINWORD.EXE',  # Opens Word as default
            
            # Windows Apps
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'paint': 'mspaint.exe',
            'explorer': 'explorer.exe',
            'cmd': 'cmd.exe',
            'powershell': 'powershell.exe',
            'task manager': 'taskmgr.exe',
            'control panel': 'control.exe',
            'settings': 'ms-settings:',
            'photos': 'ms-photos:',
            'store': 'ms-windows-store:',
            'mail': 'ms-outlook-mail:',
            'calendar': 'ms-outlook-calendar:',
            'maps': 'ms-maps:',
            'weather': 'ms-weather:',
            'camera': 'microsoft.windows.camera:',
            'alarms': 'ms-alarms:',
            'clock': 'ms-alarms:',
            'calculator': 'ms-calculator:',
            'camera': 'microsoft.windows.camera:',
            'cortana': 'ms-cortana:',
            'feedback': 'ms-feedback:',
            'help': 'ms-help:',
            'movies': 'ms-movies:',
            'music': 'ms-music:',
            'news': 'ms-news:',
            'phone': 'ms-phone:',
            'sports': 'ms-sports:',
            'tips': 'ms-tips:',
            'voice recorder': 'ms-voicerecorder:',
            'xbox': 'ms-xbox:',
            
            # Media Players
            'spotify': 'spotify.exe',
            'vlc': 'vlc.exe',
            'windows media player': 'wmplayer.exe',
            'itunes': 'itunes.exe',
            'quicktime': 'quicktime.exe',
            'realplayer': 'realplay.exe',
            
            # Communication
            'zoom': 'Zoom.exe',
            'teams': 'Teams.exe',
            'discord': 'Discord.exe',
            'skype': 'skype.exe',
            'whatsapp': 'whatsapp.exe',
            'telegram': 'telegram.exe',
            'slack': 'slack.exe',
            'microsoft teams': 'Teams.exe',
            
            # Development Tools
            'visual studio': 'devenv.exe',
            'code': 'code.exe',  # VS Code
            'vscode': 'code.exe',
            'visual studio code': 'code.exe',
            'pycharm': 'pycharm64.exe',
            'eclipse': 'eclipse.exe',
            'intellij': 'idea64.exe',
            'android studio': 'studio64.exe',
            'sublime': 'sublime_text.exe',
            'notepad++': 'notepad++.exe',
            
            # Design Tools
            'photoshop': 'photoshop.exe',
            'illustrator': 'illustrator.exe',
            'indesign': 'indesign.exe',
            'premiere': 'premiere.exe',
            'after effects': 'afterfx.exe',
            'lightroom': 'lightroom.exe',
            'gimp': 'gimp.exe',
            'inkscape': 'inkscape.exe',
            'blender': 'blender.exe',
            'autocad': 'acad.exe',
            'sketchup': 'sketchup.exe',
            
            # Games
            'minecraft': 'minecraft.exe',
            'steam': 'steam.exe',
            'epic games': 'EpicGamesLauncher.exe',
            'origin': 'Origin.exe',
            'battle.net': 'Battle.net.exe',
            'rockstar': 'Rockstar Games Launcher.exe',
            
            # Utilities
            '7zip': '7zFM.exe',
            'winzip': 'winzip.exe',
            'winrar': 'winrar.exe',
            'adobe reader': 'acrobat.exe',
            'acrobat': 'acrobat.exe',
            'foxit': 'foxitreader.exe',
            'chrome remote': 'chrome-remote-desktop-host.exe',
            'teamviewer': 'teamviewer.exe',
            'anydesk': 'anydesk.exe',
            'dropbox': 'dropbox.exe',
            'onedrive': 'onedrive.exe',
            'google drive': 'googledrivesync.exe',
            'utorrent': 'utorrent.exe',
            'qbittorrent': 'qbittorrent.exe',
            'ccleaner': 'ccleaner.exe',
            'malwarebytes': 'mbam.exe',
            'norton': 'norton.exe',
            'avast': 'avast.exe',
            'avg': 'avg.exe',
            'kaspersky': 'kaspersky.exe',
            
            # Additional Windows Apps
            'sticky notes': 'stikynot.exe',
            'snipping tool': 'snippingtool.exe',
            'remote desktop': 'mstsc.exe',
            'character map': 'charmap.exe',
            'registry editor': 'regedit.exe',
            'services': 'services.msc',
            'event viewer': 'eventvwr.msc',
            'disk management': 'diskmgmt.msc',
            'device manager': 'devmgmt.msc',
            'system configuration': 'msconfig.exe',
            'task scheduler': 'taskschd.msc',
            'performance monitor': 'perfmon.msc',
            'resource monitor': 'resmon.exe',
            'system information': 'msinfo32.exe',
            'system properties': 'sysdm.cpl',
            'network connections': 'ncpa.cpl',
            'power options': 'powercfg.cpl',
            'sound settings': 'mmsys.cpl',
            'display settings': 'desk.cpl',
            'mouse settings': 'main.cpl',
            'keyboard settings': 'main.cpl keyboard',
            'date and time': 'timedate.cpl',
            'language settings': 'intl.cpl',
            'user accounts': 'nusrmgr.cpl',
            'programs and features': 'appwiz.cpl',
            'windows features': 'optionalfeatures.exe',
            'windows defender': 'windowsdefender:',
            'windows security': 'windowsdefender:',
            'windows update': 'ms-settings:windowsupdate',
            'backup settings': 'ms-settings:backup',
            'recovery options': 'ms-settings:recovery',
            'about': 'ms-settings:about',
            'privacy settings': 'ms-settings:privacy',
            'ease of access': 'ms-settings:easeofaccess',
            'gaming settings': 'ms-settings:gaming',
            'network settings': 'ms-settings:network',
            'personalization': 'ms-settings:personalization',
            'apps settings': 'ms-settings:apps',
            'default apps': 'ms-settings:defaultapps',
            'storage settings': 'ms-settings:storagesense',
            'system settings': 'ms-settings:system',
            'time and language': 'ms-settings:time-language',
            'update and security': 'ms-settings:windowsupdate'
        }

    def get_running_apps(self):
        """Get list of currently running applications"""
        running_apps = []
        for proc in psutil.process_iter(['name']):
            try:
                running_apps.append(proc.info['name'].lower())
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return running_apps

    def find_window_by_process(self, process_name):
        """Find window handle for a given process name"""
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                try:
                    process = psutil.Process(pid)
                    if process.name().lower() == process_name.lower():
                        hwnds.append(hwnd)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        return hwnds[0] if hwnds else None

    def open_app(self, app_name):
        """Open an application by name"""
        try:
            # Convert app name to lowercase for case-insensitive matching
            app_name = app_name.lower()
            
            # Check if app is in our aliases
            if app_name in self.app_aliases:
                app_path = self.app_aliases[app_name]
                
                # Handle special Windows apps that use URI schemes
                if app_path.startswith('ms-'):
                    os.system(f'start {app_path}')
                    return f"Opening {app_name}"
                
                # Handle regular applications
                subprocess.Popen(app_path)
                return f"Opening {app_name}"
            else:
                # Check if app is already running
                running_apps = self.get_running_apps()
                for running_app in running_apps:
                    if app_name in running_app.lower():
                        return f"{app_name} is already running"
                
                # If not found in aliases and not running
                return f"Sorry, I don't know how to open {app_name}. Please try a different application name."
                
        except Exception as e:
            return f"Error opening {app_name}: {str(e)}"

    def close_app(self, app_name):
        """Close an application by name"""
        try:
            # Convert app name to lowercase for case-insensitive matching
            app_name = app_name.lower()
            
            # Check if app is in our aliases
            if app_name in self.app_aliases:
                process_name = self.app_aliases[app_name]
                
                # Find the window handle
                hwnd = self.find_window_by_process(process_name)
                if hwnd:
                    # Send close message to the window
                    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                    return f"Closing {app_name}"
                else:
                    return f"{app_name} is not currently running"
            else:
                # Check if app is running with a similar name
                running_apps = self.get_running_apps()
                for running_app in running_apps:
                    if app_name in running_app.lower():
                        # Try to close the running app
                        for proc in psutil.process_iter(['name']):
                            if proc.info['name'].lower() == running_app:
                                proc.terminate()
                                return f"Closing {running_app}"
                
                return f"Sorry, I don't know how to close {app_name}. Please try a different application name."
                
        except Exception as e:
            return f"Error closing {app_name}: {str(e)}"

    def is_app_running(self, app_name):
        """Check if an application is running"""
        try:
            if app_name.lower() in self.app_aliases:
                process_name = self.app_aliases[app_name.lower()]
                return process_name.lower() in self.get_running_apps()
            return False
        except Exception:
            return False 