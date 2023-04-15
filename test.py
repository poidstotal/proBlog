import requests
import json

# Set the API endpoint and post ID
endpoint = "https://api.medium.com/v1/users/{user_id}/posts/{post_id}"
user_id = "<YOUR_USER_ID>"
post_id = "<YOUR_POST_ID>"

# Set the URL of the updated image
updated_image_url = "<URL_OF_UPDATED_IMAGE>"

# Set the update data for the post
update_data = {
    "title": "Updated Post Title",
    "subtitle": "Updated Post Subtitle",
    "content": "Updated post content...",
    "tags": ["tag1", "tag2"],
    "virtuals": {
        "previewImage": {
            "imageId": "",
            "filter": "",
            "backgroundSize": "",
            "backgroundPos": "",
            "originalWidth": "",
            "originalHeight": "",
            "imageBase64": "",
            "imageURL": updated_image_url  # Update the image URL here
        }
    }
}

# Set the authorization header with your access token
headers = {
    "Authorization": "Bearer 2ae00f117b902b22d87eee7c0075f4b4f0ec92ba3a384944169932f8e5077018f",
    "Content-Type": "application/json"
}

# Make the PUT request to update the post
response = requests.put(
    url=endpoint.format(user_id=user_id, post_id=post_id),
    data=json.dumps(update_data),
    headers=headers
)

# Check the response status code
if response.status_code == 200:
    print("Post updated successfully!")
else:
    print("Failed to update post. Status code:", response.status_code)
    print("Response:", response.text)
