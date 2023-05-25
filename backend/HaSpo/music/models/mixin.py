class CheckUserModelMixin:
    def check_user(self, required_user):
        paths = self.path_to_user.split('__')
        user = getattr(self, paths.pop(0))
        for path in paths:
            user = getattr(user, path)
        return user == required_user
