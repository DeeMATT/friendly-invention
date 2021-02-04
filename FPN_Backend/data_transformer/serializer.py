from .views import toUiReadableDateFormat

def generateLoginResponse(user, accessToken):
    user = {
        "id": user.id,
        "firstName": user.firstName,
        "lastName": user.lastName,
        "email": user.email,
        "phone": user.phone,
        "username": user.username,
        "accessToken": accessToken.accessToken,
        "lastActive": toUiReadableDateFormat(user.lastActiveOn)
    }

    return user

def transformUser(user):
    return {
        "id": user.id,
        "firstName": user.firstName,
        "lastName": user.lastName,
        "username": user.username,
        "email": user.email,
        "phone": user.phone,
        "lastActiveOn": user.lastActiveOn, 
        "createdAt": toUiReadableDateFormat(user.createdAt),
    }

def transformUsersList(Users):
    results = []
    for user in Users:
        results.append(transformUser(user))

    return results
