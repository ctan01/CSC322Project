# Phase II: Design Report for Team K: App: TeamUp
 
#### This report is meant to provide the data structure and logic to
carry out the functionalities dictated by the specification. Keep
in mind the implementation will be entirely based on this document,
adequate details should thus be given at length.
Google Docs of Report:
https://docs.google.com/document/d/1mg6cAZ5uQf2P2sezdsFmTxK0sVSXGgF_z8rX4OM0uTI/edit?usp=sharing

 ### 1. Introduction
 an overall picture of the system using collaboration class diagram 
 ![](overallClassDiagram.png)

 ### 2. All use cases
    o Scenarios for each use case: normal AND exceptional scenarios
    o Collaboration or sequence class diagram for each use case, choose 
      3 or more use cases: draw the Petri-nets instead of class diagrams
#### DIAGRAMS:
#### A. Logging In (PETRI NET):
![](logInClassDiagram.jpg)
#### B. Logging Out:
![](logOutClassDiagram.jpg)
#### C. Accept Invitation to Join Group:
![](AcceptInvitationClassDiagram.jpg)
#### D. Create Group:
![](CreateGroupClassDiagram.jpg)
#### E. Forgot Password:
![](ForgotPasswordClassDiagram.jpg)
#### F. Edit Profile:
![](EditProfileClassDiagram.jpg)
#### G. Accept Invitation:
![](AcceptInvitationClassDiagram.jpg)
#### H. Accept All Invitations:
![](AccepteAllInviteClassDigram.png)
#### I. Decline Invitation:
![](DeclineInvitationClassDiagram.png)
#### J. Decline All Invitations:
![](DeclineAllInvitationsClassDiagrram.png)
#### K. Register to Become an Ordinary User:
![](RegisterClassDiagram.png)
#### L. Post to Group Page (PETRI NET):
![](PosttoGroupPageClassDiagram.png)
#### M. Set Up Vote:
![](SetUpVoteClassDiagram.png)
#### N. Request Meet Up Time:
![](RequestMeetUpTimeClassDiagram.png)
#### O. Vote for Democratic SU:
![](VoteforDemocraticSUClassDiagram.png)
#### P. Vote to Close Group (PETRI NET):
> If 80% of the Members that vote, vote to close the group, the group will close.
> If it is less than 80%, the group will stay open.
![](VotetoCloseGroupClassDiagram.jpg)
#### Q. Evaluate Group Members:
> This is done after a group is closed.
> Members get a notification in their inbox that the group is closed,
> And Upon opening the notification, a pop up window for member evaluation opens.
![](EvaluateGroupMembersClassDiagram.png)
#### R. Send Complaint
#### S. Send Compliment
    
      
### 3. E-R diagram for the entire system attributes and key for each class should be provided

### 4. Detailed design:
    for EVERY method use pseudo-code to delineate the input/output and
    main functionalities
    
### 5. System screens:
    demonstrate major GUI screens of the system and a prototype of one
    functionality of your own choice.
### 6. Minutes of group meetings and possible concerns of team work

 ### 7. Address of the git repo (github, gitlab, bitbucket, etc) of your 
    team's work so far - put all materials including this report there
    Git repo and such is all here.
