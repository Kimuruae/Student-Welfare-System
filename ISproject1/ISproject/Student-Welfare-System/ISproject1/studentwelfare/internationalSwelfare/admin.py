from django.contrib import admin
from .models import (
    Student,
    WelfareIssue,
    Response,
    StaffProfile,
    Hostel,
    CounsellingSession,
    InternationalStudentCommunity,
    CommunityEvent
)

# Register your models here
admin.site.register(Student)
admin.site.register(WelfareIssue)
admin.site.register(Response)
admin.site.register(StaffProfile)
admin.site.register(Hostel)
admin.site.register(CounsellingSession)
admin.site.register(InternationalStudentCommunity)
admin.site.register(CommunityEvent)




