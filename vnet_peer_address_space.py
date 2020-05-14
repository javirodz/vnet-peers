from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient

#Global Variables => a resource group and a vnet name
# Resource Group
GROUP_NAME = 'acloud-palo'

#VNET
VNET_NAME = "acloud-vnet-hub2"

def main():
    #Get the login from the command line
    compute_client = get_client_from_cli_profile(ComputeManagementClient) #not use in this example
    network_client = get_client_from_cli_profile(NetworkManagementClient)
    resource_client = get_client_from_cli_profile(ResourceManagementClient) #not use in this example

    #CLI Equivalent: az network vnet peering list -g acloud-palo2 --vnet-name acloud-palo2-vnet
    #Get all the vnet peerings from "acloud-palo2-vnet"
    vnet_peerings = network_client.virtual_network_peerings.list(GROUP_NAME, VNET_NAME)
    #iterate vnet_peerings and print each
    for peer in vnet_peerings:
        print(peer.name)
        print(peer.remote_virtual_network)
        print(peer.remote_address_space)

if __name__ == "__main__":
    # calling the main function
    main()