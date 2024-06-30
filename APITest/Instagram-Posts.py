from apify_client import ApifyClient
import json

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_IwHshWp92P8MCg9H5pommHfOVSfrNr4ryz3Z")
name="433"

# Prepare the Actor input
run_input = {
    "username": [name],
    "resultsLimit": 5,
}

# Run the Actor and wait for it to finish
run = client.actor("apify/instagram-post-scraper").call(run_input=run_input)

#total objects received
iter = client.dataset(run["defaultDatasetId"]).iterate_items()
total = sum(1 for _ in iter)
print(total)


# Fetch and print Actor results from the run's dataset (if there are any)
with open(name + "_3_posts.json", "w") as outfile:
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        json.dump(item, outfile, indent=4)