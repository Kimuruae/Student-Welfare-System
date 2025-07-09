from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hostel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    empty_slots = models.IntegerField()
    price_per_month = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=100)
    university = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    passport_number = models.CharField(max_length=50, null=True, blank=True)
    admission_number = models.CharField(max_length=50, null=True, blank=True, unique=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    year_of_study = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.nationality})"


class WelfareIssue(models.Model):
    id = models.AutoField(primary_key=True)
    ISSUE_TYPES = [
        ('Accommodation', 'Accommodation'),
        ('Health', 'Health'),
        ('Financial', 'Financial'),
        ('Legal', 'Legal'),
        ('Academic', 'Academic'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.title} - {self.status}"


class Response(models.Model):
    id = models.AutoField(primary_key=True)
    issue = models.ForeignKey(WelfareIssue, on_delete=models.CASCADE)
    responder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    response_text = models.TextField()
    response_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to Issue #{self.issue.id}"


class StaffProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class CounsellingSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'is_staff': True})
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Session {self.session_id} - {self.student.user.username} with {self.staff.username}"

class InternationalStudentCommunity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CommunityEvent(models.Model):
    community = models.ForeignKey(InternationalStudentCommunity, on_delete=models.CASCADE, related_name='events')
    event_name = models.CharField(max_length=150)
    event_date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.event_name} ({self.community.name})"
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username
class EmergencyReport(models.Model):
    TYPE_CHOICES = [
        ('medical', 'Medical'),
        ('security', 'Security'),
        ('psychological', 'Psychological'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.type}"    


