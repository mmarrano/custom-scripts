from tenancy.models import Tenant
from extras.scripts import Script, StringVar
from django.utils.text import slugify

class CreateTenant(Script):

    class Meta: # type: ignore
        name = "Create Tenant"
        description = "Simple demo script to create a new tenant."

    tenant_name = StringVar(label="Tenant Name")
    tenant_description = StringVar(label="Tenant Description")

    def run(self, data, commit):
        tenant = Tenant(
            name=data["tenant_name"],
            slug=slugify(data["tenant_name"]),
            description=data["tenant_description"],
        )
        tenant.save()
        self.log_success(f"Created new tenant: {tenant}")