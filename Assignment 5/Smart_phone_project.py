class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours

    def make_call(self, number):
       
        return f"Calling {number} from {self.brand} {self.model}..."

    def browse_internet(self):
      
        return f"Browsing the internet on {self.brand} {self.model}..."

    def display_specs(self):
        
        return (f"Brand: {self.brand}, Model: {self.model}, "
                f"Storage: {self.storage}GB, Battery Life: {self.battery_life} hours")


# Adding Inheritance: Smartwatch
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, is_water_resistant):
        super().__init__(brand, model, 0, battery_life)  # Storage is not applicable
        self.is_water_resistant = is_water_resistant

    def track_activity(self, activity):
      
        return f"Tracking your {activity} with {self.brand} {self.model}..."

    
    def display_specs(self):
        return (f"Brand: {self.brand}, Model: {self.model}, "
                f"Battery Life: {self.battery_life} hours, "
                f"Water Resistant: {'Yes' if self.is_water_resistant else 'No'}")



phone = Smartphone("Apple", "iPhone 14", 256, 20)
watch = Smartwatch("Apple", "Watch Series 8", 18, True)

print(phone.display_specs())
print(phone.make_call("123-456-7890"))
print(watch.display_specs())
print(watch.track_activity("running"))
