from rest_framework import permissions


class IsBrewOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, brew):
        if request.user:
            return brew.brewer.user == request.user
        return False

class IsBrewer(permissions.BasePermission):
    def has_object_permission(self, request, view, brewer):
        if request.user:
            return brewer.user == request.user
        return False
