from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)
from scripts.deploy_mocks import deploy_mocks


def deploy_fund_me():
    account = get_account()
    #pass the price feed address to our fundme contract
    
    #if we are on a persistent network line rinkbey, use the associated address
    #otherwise deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address


    fund_me = FundMe.deploy(
        price_feed_address, 
        {"from": account}, 
        publish_source=config["networks"][network.show_active()].get("verify")
    )
    print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me()