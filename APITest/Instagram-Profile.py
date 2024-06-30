from apify_client import ApifyClient
import json

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_IwHshWp92P8MCg9H5pommHfOVSfrNr4ryz3Z")
name = "laura__mgz"


# Prepare the Actor input
run_input = { "usernames": [name] }

# Run the Actor and wait for it to finish
run = client.actor("apify/instagram-profile-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
iter = client.dataset(run["defaultDatasetId"]).iterate_items()
total = sum(1 for _ in iter)
print(total)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    with open(name + ".json", "w") as outfile:
        json.dump(item, outfile, indent=4)