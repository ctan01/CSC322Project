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
![](SendComplaintClassDiagram.png)
#### S. Send Compliment
![](SendComplimentClassDiagram.png)
      
### 3. E-R diagram for the entire system attributes and key for each class should be provided
![](erdiagram.png)

### 4. Detailed design:
      o for EVERY method use pseudo-code to delineate the input/output and
      o main functionalities
##### A. jump_Homepage1():
>Pre-Conditions: User must click the HomePage1 Button
>if Button is clicked, then jumpHomepage1_Button == true
>Post-Conditions: Current window will be closed from view and Homepage1 will be opened.
Pseudocode:
```
	void jump_Homepage1() {
		if(jumpHomepage1_Button) {
			current_Window.close()
			homepage.open()
		}
	}
```
#### B. jump_Homepage2():
> Pre-Conditions: User must click the HomePage2 Button
> if Button is clicked, then jumpHomePage2_Button==true
> Post-Conditions: Current window will be closed from view and Homepage2 will be opened.
Pseudocode:
```
	void jump_Homepage2() {
		if(jumpHomeback2_Button) {
			curernt_Window.close()
			Homepage2.open()
		}
	}
```
#### C. jump_Inbox(userID):
> Pre-Conditions: User must click the Inbox_Button
> if Button is clicked, then jumpInbox_button == true
> Post-Conditions: Current window will be closed from view and Inbox_Page will be opened.
Pseudocode:
```

	void jump_Inbox() {
		if(jumpInbox_Button) {
			current_Window.close()
			Inbox_Page.open()
		}
	}
```
#### D. jump_GroupPage(groupID):
> Pre-Conditions: User must click Group_Page_Button
> Post-Conditions: Current window will be closed from view and Group Page will be opened. Then Current window will be set to Group Page.
Pseudocode:
```
	void jump_GroupPage(){
		if(this.Group_Page_Button) {
			current_window.close()
			this.Group_Page.open()
		}
	}
```
#### E. jump_Profile(userID): 
> Pre-Conditions: User must click Profile_Button
> if Profile_Button is clicked, Profile_Button==true
> Post-Conditions: Current window will be closed, User’s Profile Window will be opened.
Pseudocode:
```
	  void jump_Profile(){
		if(Profile_Button) {
			current_Window.close()  # close current window
 			profilepage = new ProfileWindow()	
			(create new ProfileWindow called profilepage)
			(ProfileWindow class is a Window subclass)
			profilepage.setPage(user.profile) 
			(Set profilepage info to current user’s profile info)
			profilepage.open() # open newly made profilepage
		}
	}
#### F. Create_Post():
> Pre-Conditions: 
> User Must Be in Group
> User Must Click Create_Post_Button
> Post-Conditions:
> Pop Up Window will appear to take user text input
Pseudocode:
```
	void Create_Post() {
		if(Create_Post_Button) {
			new_Post = new createPostWindow()
			new_Post.open()
		}
	}
```
#### G. Publish_Post():
> Pre-Conditions: 
> User has typed text input into a create_post box
> User has pressed publish_post_button.
> Post-Conditions: User Input will be read and stored in database for group’s posts and then a new textbox will appear at the top of the > group’s dashboard.
Pseudocode:
```
	void Publish_Post() {
			if (publish_post_button) {
				database.insert(new_Post.text)
				jumpGroupPage(this.groupID) 
				(refreshing group page to show new post)
				new_Post.close()
			}
		}
```
#### H. Create_Comment():
> Pre-Conditions:
> User has to have clicked create_comment_button
> Post-Conditions:
> Pop up window will appear to take in user input
> Pseudocode:
```
	void create_Comment() {
		if(create_comment_button) {
			new_Comment = new createCommentWindow()
			new_Comment.open()
		}
	}		
```
Publish_Comment()
Pre-Conditions: 
User has typed into comment text box window
User has clicked publish_comment_button
Post-Conditions:
User input will be read and inserted into database for group’s posts in comment column
Pseudocode:
void publish_comment() {
 			if(database.insert(new_comment.text)
				jumpGroupPage(this.groupID) 
#^refreshing group page to show new comment
new_Comment.close()
}
		    }
			
LogIn()
Pre Conditions: User is in HomePage1; User must click the PublishPoll_Button 
If Button is clicked, then ClickPublishPoll_Button == true
Post_Condition: redirected to HomePage2;
Pseudocode:
Void Login(){
Int k=3;
Int x=0;
cin<<username;
cin<<password;
if(username!=database.username[x]&&x!=#ofMember)
{
x++;
if(username==database.username[x]&&password==database.username[x].password)
{
current_Window.close();
Homepage2.open();
}
Else if(x=#ofMember+1)
{
cout>>no username exist;

}
Else if (username==database.username[x]&&password!=database.username[x].password)
{
cout>>password wrong, you have k tries before the username got lock down;
k--;
}
}

LogOut()
Pre Conditions: User must click the Logout_Button 
If Button is clicked, then Logout_Button == true
Post_Condition: redirect to HomePage1
Pseudocode:
If (Logout_Button){
current_Window.close();
Homepage1.open();
}

DeletePost()
Pre Conditions: User is viewing database.post[k]; User must click the DeletePost_Button 
If Button is clicked, then DeletePost_Button == true
Post_Condition: redirect to GroupPage; database.post[k] got deleted;
Pseudocode:
If (Logout_Button){
database.post[k]==null;
current_Window.close();
GroupPage.open();
}
DeleteComment()
Pre Conditions: User is viewing database.comment[k]; User must click the DeleteComment_Button 
If Button is clicked, then DeleteComment_Button == true
Post_Condition: redirect to GroupPage; database.comment[k] got deleted;
Pseudocode:
If (Logout_Button){
database.comment[k]==null;
current_Window.close();
GroupPage.open();
}
AcceptInvitation()
Pre Conditions: User is viewing InboxPage; User must click the AcceptInvitation_Button 
If Button is clicked, then AcceptInvitation_Button == true
Post_Condition: group[k] will be added into profile; delete the invitation notice
Pseudocode:
If (AcceptInvitation_Button){
add.database.group[k];
delete.Invitation[k];
}
DeclineInvitation()
Pre Conditions: User is viewing InboxPage; User must click the DeclineInvitation_Button 
If Button is clicked, then DeclineInvitation_Button == true
Post_Condition: delete the invitation notice
Pseudocode:
If (DeclineInvitation_Button){
delete.Invitation;
}
AcceptAll()
Pre Conditions: User is viewing InboxPage; 
User must click the AcceptAllInvitation_Button 
If Button is clicked, then AcceptAllInvitation_Button == true
Post_Condition: group[A….X] will be added into profile; delete the invitation notice
Pseudocode:
If (AcceptAllInvitation_Button){
add.database.group[A…..X];
delete.Invitation[A...X];
}
DeclineAll() 
Pre Conditions: User is viewing InboxPage; 
User must click the DeclineAllInvitation_Button 
If Button is clicked, then DeclineAllInvitation_Button == true
Post_Condition: delete the invitation notice
Pseudocode:
If (DeclineAllInvitation_Button){
delete.Invitation[A...X];
}
CreatePoll()
Pre Conditions: User must click the CreatePoll_Button 
If Button is clicked, then ClickCreatePoll_Button == true
Post Conditions: CreatePoll will be a pop-up window and pop-up in front of the main GUI
Pseudocode
Void CreatePoll(){
	if(ClickCreatePoll_Button == true){
	CreatePoll_Page.open()
}
} 
		
		
PublishPoll()
Pre Conditions: User must click the PublishPoll_Button 
If Button is clicked, then ClickPublishPoll_Button == true
Post Conditions: Poll will be saved into the database and be published
Pseudocode
Void PublishPoll(){
	if(ClickPublishPoll_Button == true){
	database.Create(NewPoll)	
	SentNotification(GroupMembers)
CreatePoll_Page.Close()
}
} 

VotePoll()
Pre Conditions: User must click the VotePoll_Button 
If Button is clicked, then ClickVotePoll_Button == true
Post Conditions: vote will be updated into the database
Pseudocode
Void VotePoll(){
	if(ClickVotePoll_Button == true){
	database.update(voteInfo)	
}
} 

LeaveGroup()
Pre Conditions: User must click the LeaveGroup_Button 
If Button is clicked, then ClickLeaveGroup_Button == true
Post Conditions: update the database and send notification
Pseudocode
Void LeaveGroup(){
	if(ClickLeaveGroup_Button == true){
	database.delete(MemberInfo)	
	SentNotification(GroupMembers)
}
} 

SendInvitation() 
Pre Conditions: User must click the SendInvitation_Button 
If Button is clicked, then ClickSendInvitation_Button == true
Post Conditions: update the database and send notification
Pseudocode
Void SendInvitation(){
	if(ClickSendInvitation_Button == true){	
	SentNotification(GroupMembers)
}
} 

EditSkills()
Pre Conditions: User must click the EditSkills_Button 
If Button is clicked, then ClickEditSkills_Button == true
Post Conditions: update the database Pseudocode
Void EditSkills(){
	if(ClickEditSkills_Button == true){
	database.update(skillInfo)	
}
} 

EditInterests()
Pre Conditions: User must click the EditInterests_Button 
If Button is clicked, then ClickEditInterests_Button == true
Post Conditions: update the database Pseudocode
Void EditInterests(){
	if(ClickEditInterests_Button == true){
	database.update(InterestInfo)	
}
} 

    
### 5. System screens:
    demonstrate major GUI screens of the system and a prototype of one
    functionality of your own choice.
### 6. Minutes of group meetings and possible concerns of team work

 ### 7. Address of the git repo (github, gitlab, bitbucket, etc) of your 
    team's work so far - put all materials including this report there
    Git repo and such is all here.
