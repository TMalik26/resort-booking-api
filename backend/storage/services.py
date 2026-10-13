import requests

from config.settings import SUPABASE_SERVICE_KEY, SUPABASE_URL

# filepath example:
#  "properties/property_id/filename.jpg"


def create_upload_url(file_path):
    """
    Generate a temporary signed upload URL for a file stored in Supabase.

    Returns a dictionary containing the signed upload URL,
    upload token and destination file path.

    Raises:
        Exception: If Supabase returns an unsuccessful response.
    """
    url = f"{SUPABASE_URL}/storage/v1/object/upload/sign/{file_path}"

    headers = {
        "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
        "apikey": SUPABASE_SERVICE_KEY,
    }

    response = requests.post(url, headers=headers)
    data = response.json()

    if response.status_code not in (200, 201):
        raise Exception(data)

    return {
        "upload_url": SUPABASE_URL + "/storage/v1" + data["url"],
        "token": data["token"],
        "path": file_path,
    }


def get_public_supabase_url(file_path):
    """
    Return the public URL for a file stored in Supabase.

    Returns None when the file path is empty.
    """
    if not file_path:
        return None
    return f"{SUPABASE_URL}/storage/v1/object/public/{file_path}"


def delete_file(file_path):
    """
    Delete a file from Supabase Storage.

    The request is sent regardless of whether the file exists.
    """
    url = f"{SUPABASE_URL}/storage/v1/object/{file_path}"
    headers = {
        "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
        "apikey": SUPABASE_SERVICE_KEY,
    }
    requests.delete(url, headers=headers)
