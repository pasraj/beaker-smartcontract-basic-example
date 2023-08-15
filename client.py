from beaker.client import ApplicationClient
from beaker import sandbox
from smartcontract import Calculator


client = sandbox.get_algod_client()
acct = sandbox.get_accounts().pop()
app_client = ApplicationClient(client=client, app=Calculator(), signer=acct.signer)
app_id, app_addr, txid = app_client.create()
print(f"Created App with id: {app_id} and address addr: {app_addr} in tx: {txid}")

