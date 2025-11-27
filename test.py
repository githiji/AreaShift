import tkinter as tk
from tkinter import ttk, messagebox
import pytz 
import time 
import subprocess
import phonenumbers
from phonenumbers import timezone, parse
from mullvad import set_mullvad_location, get_state_from_area_code
from dicts import IANA_TO_WINDOWS, STATE_TO_MULLVAD, MULLVAD_CITIES, STATE_COORDS

class VPNTimeZoneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VPN & Timezone Setup")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="VPN & Timezone Configuration", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Area code input
        ttk.Label(main_frame, text="Enter US Area Code:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.area_code_var = tk.StringVar()
        self.area_code_entry = ttk.Entry(main_frame, textvariable=self.area_code_var, width=10, font=("Arial", 12))
        self.area_code_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
        self.area_code_entry.bind('<Return>', lambda e: self.apply_settings())
        
        # Info display
        self.info_text = tk.Text(main_frame, height=8, width=40, font=("Arial", 10))
        self.info_text.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.apply_btn = ttk.Button(button_frame, text="Apply Settings", 
                                   command=self.apply_settings)
        self.apply_btn.pack(side=tk.LEFT, padx=5)
        
        self.clear_btn = ttk.Button(button_frame, text="Clear", 
                                   command=self.clear_all)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        self.quit_btn = ttk.Button(button_frame, text="Quit", 
                                  command=self.root.quit)
        self.quit_btn.pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Enter area code and click Apply")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
    def log_message(self, message):
        """Add message to info text area"""
        self.info_text.insert(tk.END, f"{message}\n")
        self.info_text.see(tk.END)
        self.root.update()
        
    def clear_all(self):
        """Clear all inputs and outputs"""
        self.area_code_var.set("")
        self.info_text.delete(1.0, tk.END)
        self.status_var.set("Cleared - Enter area code and click Apply")
        
    def apply_settings(self):
        """Main function to apply VPN and timezone settings"""
        area_code = self.area_code_var.get().strip()
        
        if not area_code:
            messagebox.showerror("Error", "Please enter an area code")
            return
            
        if not area_code.isdigit() or len(area_code) != 3:
            messagebox.showerror("Error", "Please enter a valid 3-digit area code")
            return
            
        self.clear_all()
        self.log_message(f"Processing area code: {area_code}")
        self.status_var.set("Processing...")
        
        try:
            # Get state from area code
            state = get_state_from_area_code(area_code)
            if state:
                self.log_message(f"📍 Detected state: {state}")
                
                # Set Mullvad location
                self.log_message("🔧 Setting VPN location...")
                success = set_mullvad_location(state)
                if success:
                    self.log_message("✅ VPN location set successfully")
                else:
                    self.log_message("❌ Failed to set VPN location")
            else:
                self.log_message("❌ Could not determine state from area code")
                
            # Set timezone
            tz = self.get_timezone_by_area_code(area_code)
            if tz:
                self.log_message(f"🕐 Setting timezone to: {tz}")
                self.set_system_timezone(tz)
                self.log_message("✅ Timezone set successfully")
            else:
                self.log_message("❌ Timezone not found for this area code")
                
            self.status_var.set("Settings applied successfully")
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.log_message(f"❌ {error_msg}")
            self.status_var.set("Error occurred")
            messagebox.showerror("Error", error_msg)
    
    def get_timezone_by_area_code(self, area_code):
        """Get Windows timezone from area code"""
        fake_number = f"+1{area_code}5559999"
        try:
            parsed = parse(fake_number, "US")
            time_zones = timezone.time_zones_for_number(parsed)
            if time_zones:
                return IANA_TO_WINDOWS.get(time_zones[0])
            else:
                return None
        except Exception as e:
            self.log_message(f"❌ Error parsing phone number: {e}")
            return None
    
    def set_system_timezone(self, tz: str):
        """Set system timezone"""
        try:
            subprocess.run(["tzutil", "/s", tz], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to set timezone: {e}")

def main():
    root = tk.Tk()
    app = VPNTimeZoneApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()