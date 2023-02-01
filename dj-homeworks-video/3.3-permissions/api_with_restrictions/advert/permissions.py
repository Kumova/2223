from rest_framework import permissions


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)




#class IsAdminOrReadOnly(permissions.BasePermission):
 #   def has_permission(self, request, view):
 #       if request.method in permissions.SAFE_METHODS:
 #           return True
  #      return bool(request.user and request.user.is_authenticated)



