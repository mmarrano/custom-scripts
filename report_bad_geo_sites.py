# site_address.py

# Make sure to add `geocoder` to your `local_requirements.txt` and make sure it is installed in your Python venv.

import geocoder
from extras.scripts import Script
from dcim.models import Site

class checkSiteAddress(Script):
    class Meta: #type: ignore
        name = "Report Bad Geo Sites"
        description = "Checks for sites with missing or inaccurate physical addresses or geo locations."
    
    def run(self, data, commit):
        for site in Site.objects.all():
            if site.physical_address:
                if site.latitude and site.longitude:
                    self.log_success(site)
                else:
                    self.log_info(site, f'Site name: {site.name}, Physical address {site.physical_address}')
                    g = geocoder.osm(site.physical_address)
                    self.log_info(site, f'Site name: {site.name}, Geocoding result: {g}')
                    if g:
                        self.log_warning(site, f'Missing geo location - possible ({round(g.x,6)}, {round(g.y,6)})')
                    else:
                        self.log_warning(site, f'Missing geo location ({site.latitude}, {site.longitude})')    
            else:
                self.log_failure(site, f'Site name: {site.name}, Missing physical address')
