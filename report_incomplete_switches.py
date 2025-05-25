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
            
        # Prepare JSON data
        racks_data = []
        for rack in racks:
            site = Site.objects.get(pk=rack.site.pk)
            racks_data.append({
                "id": rack.pk,
                "name": rack.name,
                "site": rack.site.name,
                "status": rack.status
            })

        # Convert to JSON and log it
        racks_json = json.dumps(racks_data, indent=4)
        self.log_info("Racks data in JSON format:")
        self.log_info(racks_json)