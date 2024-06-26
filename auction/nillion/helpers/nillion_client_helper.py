import os
import random
import py_nillion_client as nillion

def create_nillion_client(userkey):
    bootnodes = [os.getenv("NILLION_BOOTNODE_MULTIADDRESS")]
    payments_config = nillion.PaymentsConfig(
        os.getenv("NILLION_BLOCKCHAIN_RPC_ENDPOINT"),
        os.getenv("NILLION_WALLET_PRIVATE_KEY"),
        int(os.getenv("NILLION_CHAIN_ID")),
        os.getenv("NILLION_PAYMENTS_SC_ADDRESS"),
        os.getenv("NILLION_BLINDING_FACTORS_MANAGER_SC_ADDRESS"),
    )
    nodekey = nillion.NodeKey.from_seed(str(random.getrandbits(128)))

    return nillion.NillionClient(
        nodekey,
        bootnodes,
        nillion.ConnectionMode.relay(),
        userkey,
        payments_config,
    )