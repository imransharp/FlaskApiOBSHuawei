from flask import Flask
app = Flask(__name__)
from obs import ObsClient


# # Initialize the CMSS client with Access Key and Secret Key
obs_client = ObsClient(
    access_key_id='GWDZ4VSDEYK9OXRMW14T',
    secret_access_key='p8SWMuaZPGsSvxmtWEZHmSMyWAlFN39JHCyAL9y1',
    server='eos.zongcloud.com.pk'
    # region = 'region-islamabad'
)

# Initialize the OBS client with Access Key and Secret Key
# obs_client = ObsClient(
#     access_key_id='A7RGTGVUJDREDIUKTLTX',
#     secret_access_key='zvThKFW90kES8gPYrl849473fsDwA87bcgacXPcC',
#     server='obsv3.zong-hpcc-isb.zongcloud.com.pk'
# )

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/List')
def List():
    """List all buckets in the account."""
    print("Listing all buckets...")
    response = obs_client.listBuckets()
    if response.status < 300:
        # Create a list of bucket details
        bucket_list = [
            {"name": bucket.name, "creationDate": bucket.creationDate}
            for bucket in response.body.buckets
        ]
        # Return the bucket list as JSON response
        return {"buckets": bucket_list}
    else:
        # Return an error response if the API call failed
        return {
            "error": True,
            "message": f"Error listing buckets: {response.errorMessage}",
            "status": response.status,
        }


if __name__ == '__main__':
    app.run(debug=True)