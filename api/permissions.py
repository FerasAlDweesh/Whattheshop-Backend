from rest_framework.permissions import BasePermission
from datetime import date


class IsOrderOwner(BasePermission):
	message = "You must be the owner of this Order"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user == request.user):
			return True
		else:
			return False