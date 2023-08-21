Welcome to the API documentation for the endpoints provided by your Django application. This API allows users to interact with various functionalities related to user authentication and profile management. Please refer to the following sections for detailed information on each endpoint.
Base URL

The base URL for these endpoints is the root URL of your Django application.
Table of Contents

    
    Endpoints
        Phone Enter
        Code Enter
        User Profile
        Token Refresh
    Error Handling
    Authentication
    Examples
        Phone Enter
        Code Enter
        User Profile
        Token Refresh


This API provides access to various functionalities related to user authentication and profile management. The following sections detail each available endpoint and the actions they support.
Endpoints <a name="endpoints"></a>
Phone Enter <a name="phone-enter"></a>

URL: /phone/
Method: POST
Description: This endpoint initiates the phone number verification process.
    

    Request

    Data Parameters:
    {
      "phone": "your_phone_number"
    }

    Response

    Status Code: 200 OK
    Content:
    
    json
    {
      "message": "Verification code sent successfully."
    }

Code Enter <a name="code-enter"></a>

URL: /code/
Method: POST
Description: This endpoint verifies the code sent to the user's phone number.
      
    Request

    Data Parameters:
    json

    {
      "phone": "your_phone_number",
      "code": "verification_code"
    }

    
    
    Response

    Status Code: 200 OK
    Content:

    json

    {
      "token": "your_access_token"
    }

User Profile <a name="user-profile"></a>

URL: /profile/<int:pk>/
Method: GET
Description: This endpoint retrieves the user profile information.
    
    Request

    Path Parameters:
        pk (integer): The ID of the user profile.

    


    Response

    Status Code: 200 OK
    Content:

    json

    {
       "id": id,
    "inv": "inv",
    "inv_phone": "phone",
    "password": "",
    "last_login": "",
    "phone": "+phone",
    "invite": "invite",
    "parent_invite": id
    }

Token Refresh <a name="token-refresh"></a>

URL: /token/refresh/
Method: POST
Description: This endpoint refreshes the access token.


    Request

    Data Parameters:

    json

    {
      "refresh": "your_refresh_token"
    }

    Response

    Status Code: 200 OK
    Content:

    json

    {
      "access": "your_new_access_token"
    }
