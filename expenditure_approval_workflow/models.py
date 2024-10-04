from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Unique constraint

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='users')

    class Meta:
        indexes = [
            models.Index(fields=['user']),  # Index for faster queries on user_id
        ]

    def __str__(self):
        return f"{self.user.username} - {self.role.name}"


class ExpenditureRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    scope = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenditure_requests')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['created_by']),  # Index for faster queries on created_by
            models.Index(fields=['status']),  # Index for faster queries on status
        ]

    def __str__(self):
        return f"{self.title} - {self.status}"


class ApprovalWorkflowStep(models.Model):
    name = models.CharField(max_length=100)
    step_order = models.PositiveIntegerField()
    approvers = models.ManyToManyField(User, related_name='workflow_steps')

    class Meta:
        unique_together = ('name', 'step_order')  # Unique constraint to ensure unique step order for each workflow
        indexes = [
            models.Index(fields=['step_order']),  # Index for faster queries on step order
        ]

    def __str__(self):
        return f"{self.name} - Step {self.step_order}"


class Approval(models.Model):
    request = models.ForeignKey(ExpenditureRequest, on_delete=models.CASCADE, related_name='approvals')
    workflow_step = models.ForeignKey(ApprovalWorkflowStep, on_delete=models.CASCADE, related_name='approvals')
    approver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approvals')
    approval_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')])

    class Meta:
        unique_together = ('request', 'workflow_step', 'approver')  # Unique constraint to prevent duplicate approvals
        indexes = [
            models.Index(fields=['request', 'workflow_step']),  # Composite index for request and workflow_step
            models.Index(fields=['status']),  # Index for faster queries on approval status
        ]

    def __str__(self):
        return f"Approval for {self.request.title} - {self.status}"
