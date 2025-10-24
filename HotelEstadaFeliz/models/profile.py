class profile:
    profile_array = []

    def create_profile(self, profile_name):
        id = len(profile.profile_array)+1
        new_profile = {"profile_id":id, "profile_name":profile_name}
        profile.profile_array.append(new_profile)