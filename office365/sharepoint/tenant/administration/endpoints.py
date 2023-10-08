from office365.sharepoint.entity import Entity


class TenantAdminEndpoints(Entity):
    @property
    def o365_admin_center_endpoint(self):
        """
        :rtype: str or None
        """
        return self.properties.get("O365AdminCenterEndpoint", None)

    @property
    def entity_type_name(self):
        return "Microsoft.Online.SharePoint.TenantAdministration.TenantAdminEndpoints"
