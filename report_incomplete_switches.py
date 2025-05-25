import json
from extras.scripts import Script
from dcim.models import Rack, Site

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
            site = Site.objects.get(pk=rack.site.pk)
            self.log_info(f"ID: {rack.pk}, Rack: {rack.name}, Site: {site.name}, Status: {rack.status}")
            
        # Optionally, you can return the data in JSON format
        racks_data = [
            {
                "id": rack.pk,
                "name": rack.name,
                "site": rack.site.name,
                "status": rack.status
            }
            for rack in racks
        ]
        
        self.log_info(json.dumps(racks_data, indent=4))
        return racks_data