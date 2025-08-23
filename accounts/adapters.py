from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        # Set full_name to Google's display name or fallback
        extra_data = sociallogin.account.extra_data
        user.full_name = (
            extra_data.get("name")
            or f"{extra_data.get('given_name', '')} {extra_data.get('family_name', '')}".strip()
            or data.get('username')
        )
        # Ensure email is set if present
        user.email = extra_data.get("email") or data.get("email") or user.email
        # Optionally, set mobile if available (Google doesn't provide by default)
        return user
