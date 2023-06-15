from rest_framework.permissions import BasePermission



class EmployeePermission(BasePermission):
    def emp_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False