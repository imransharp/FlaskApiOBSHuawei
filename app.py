from flask import Flask
app = Flask(__name__)
from obs import ObsClient


# # Initialize the CMSS client with Access Key and Secret Key
obs_client = ObsClient(
  
)



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
