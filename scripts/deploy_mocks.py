from brownie import MockV3Aggregator, network
from scripts.helpful_scripts import get_account

DECIMALS = 8

INITIAL_VALUE = 2000000000000000000

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")
    account = get_account()
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": account})
    print("Mocks Deployed!")

def main():
    deploy_mocks()