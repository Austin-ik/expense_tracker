Design Decisions Explanation for Expenditure Approval Workflow Schema

Separation of Concerns:

I designed the schema with a clear separation between different entities, such as users, roles, requests, approval steps, and approvals. This modular approach helps keep each entity focused on specific responsibilities, making the system easier for me to maintain and scale as needed.
User and Role Modeling:

I decided to separate User and UserProfile to take advantage of Django's default User model for authentication while using UserProfile to extend user-related information, such as roles. This way, I avoid directly modifying the core User model, ensuring flexibility if I need to update or change user-related features in the future.
I created a dedicated Role table to store different roles (e.g., Manager, Finance Personnel) so that roles can easily be modified, added, or removed without impacting other parts of the system.

Expenditure Requests (AFE):

In the ExpenditureRequest model, I included important fields like cost, scope, and status to capture the essential details of each expenditure request. I also added a created_by field to link each request to the user who initiated it, ensuring accountability and making it easier to track who is responsible for each request.

Approval Workflow:

I modeled the approval process using the ApprovalWorkflowStep table, where each step has a name and a step_order. This design allows me to sequence approval steps and adapt workflows easily if business processes change.
I chose to represent the many-to-many relationship between ApprovalWorkflowStep and User through a join table (ApprovalWorkflowStep_Approvers). This allows multiple users to approve at different steps and provides flexibility if I need to assign multiple approvers to a step.

Approvals:

In the Approval model, I capture individual approval actions by linking users and workflow steps to specific ExpenditureRequest records. This way, I can track which user approved a particular request at each stage, along with the approval_date and status of the approval. This design ensures detailed tracking and auditing of the approval process.
I added a status field to the Approval model to record whether a request has been approved, rejected, or is still pending. This makes it easy to monitor the progress of requests throughout the approval workflow.

Many-to-Many Relationship Handling:

I explicitly used a join table (ApprovalWorkflowStep_Approvers) to represent the many-to-many relationship between ApprovalWorkflowStep and User. This decision allows me to model situations where multiple users can approve at different workflow steps, providing the flexibility needed in a dynamic approval system.