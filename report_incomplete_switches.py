from extras.scripts import Script
from dcim.models import Rack

class ListRacks(Script):
    class Meta: #type: ignore
        name = "List Racks"
        description = "Displays a list of registered racks, including their site and status."

    def run(self, data, commit):
        racks = Rack.objects.all()
        if not racks:
            self.log_warning("No racks found.")
            return

        for rack in racks:
            self.log_info(f"ID: {rack.pk}, Rack: {rack.name}, Site: {rack.site.name}, Status: {rack.status}")
            