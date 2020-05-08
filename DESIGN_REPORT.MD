# Phase II: Design Report for Team K: App: TeamUp
 
#### This report is meant to provide the data structure and logic to
carry out the functionalities dictated by the specification. Keep
in mind the implementation will be entirely based on this document,
adequate details should thus be given at length.
Google Docs of Report:
https://docs.google.com/document/d/1mg6cAZ5uQf2P2sezdsFmTxK0sVSXGgF_z8rX4OM0uTI/edit?usp=sharing

 ### 1. Introduction
 an overall picture of the system using collaboration class diagram 
 ![](PICoverallClassDiagram.png)

 ### 2. All use cases
    o Scenarios for each use case: normal AND exceptional scenarios
    o Collaboration or sequence class diagram for each use case, choose 
      3 or more use cases: draw the Petri-nets instead of class diagrams
#### DIAGRAMS:
#### A. Logging In (PETRI NET):
> When a user clicks the log in button, they are prompted with a pop-up window to enter their
> user name and password, if the login is successful, they are logged into their account and brought to the home page
> if it is not correct, it will prompt the user with an error message and an option to try again or reset their password. 
> the user will be redirected to the log in window again, or if they click to reset their password, will be redirected to reset their password
![](PIClogInClassDiagram.jpg)
#### B. Logging Out:
> When a user clicks the log out button, they are locked out.
![](PIClogOutClassDiagram.jpg)
#### C. Invite to Join Group:
> On the group page, a user can select to send an invitation to another user to join the group page. If the user selected is already in the group, they will get a notification that they cannot select the user as they are already in the group.
![](PICinvitetojoinclassdiagram.jpg)
#### D. Create Group:
> OUs, SUs, and VIPs can start a group
> There must be at least three members selected to join/ invite for the group to be requested to be created. Only when there are at least three acceptance responses will the group and its group page be created.
![](PICCreateGroupClassDiagram.jpg)
#### E. Forgot Password:
> Any user can click on the forget password link available on the log in page or after they fail to log in successfully. A change password request is sent and the user must enter their email. If their email entered does not maatch the email in the database, an error message is sent to the user, otherwise, the user's password will be sent to their email.
![](PICForgotPasswordClassDiagram.jpg)
#### F. Edit Profile:
> When a user presses the edit profile page, the edit GUI is opened and the user can edit their profile information.
![](PICEditProfileClassDiagram.jpg)
#### G. Accept Invitation:
> When clicked, the response of accepted is inputted and sent to be inserted into the database that the user has accepted to join the group. The user is added to the database table of the users that are members of the group.
![](PICAcceptInvitationClassDiagram.jpg)
#### H. Accept All Invitations:
> All responses to all invitations present in user's inbox will be recorded as "accepted" and will be inserted into the database.
![](PICAccepteAllInviteClassDigram.png)
#### I. Decline Invitation:
> When this button is clicked, the decline input is sent to the page and inserted into the database that the user declined to join the group
![](PICDeclineInvitationClassDiagram.png)
#### J. Decline All Invitations:
> When clicked, the decline input is inputted as the response to all invitations present in the user's inbox.
![](PICDeclineAllInvitationsClassDiagrram.png)
#### K. Register to Become an Ordinary User:
> User will be prompted to fill out form requesting basic personal information, interests, skills, and reference to be approved.Responses will be Inserted in corresponding table in the database.
![](PICRegisterClassDiagram.png)
#### L. Post to Group Page (PETRI NET):
> User will be able to click the create post button in which they will be prompted with a text box and insert their text. Then, the input will be read. If there is a taboo word, the amount of taboo words will be counted and the taboo word will be censored before posted the input onto the group page as a new post. According to the amount of taboo words, there will be a corresponding point deduction from the users reputation score. The current score will be retrieved, the point deduction will be deducted, then the new reputation score will be inputted into the user's data.
![](PICPosttoGroupPageClassDiagram.png)
#### M. Set Up Vote:
> Set up vote. The Vote can issue to a warning to a group member or praise a group member. If 80% of the users vote to do so, the group member will get a notification.
![](PICSetUpVoteClassDiagram.png)
#### N. Request Meet Up Time:
> Request to create a poll to vote on meet-up time.
![](PICRequestMeetUpTimeClassDiagram.png)
#### O. Vote for Democratic SU:
> Periodically, VIPS will get a notification in their inbox that will prompt a pop-up window for the VIP to vote for a democratic SU. The winner will get a notification.
![](PICVoteforDemocraticSUClassDiagram.png)
#### P. Vote to Close Group (PETRI NET):
> If 80% of the Members that vote, vote to close the group, the group will close.
> If it is less than 80%, the group will stay open.
![](PICVotetoCloseGroupClassDiagram.jpg)
#### Q. Evaluate Group Members:
> This is done after a group is closed.
> Members get a notification in their inbox that the group is closed,
> And Upon opening the notification, a pop up window for member evaluation opens.
![](PICEvaluateGroupMembersClassDiagram.png)
#### R. Send Complaint:
> OUs can send compaints to SUs to either report system malfunction or bad behavior of users. They click a button to complain to SU and the complaint info will be inputted into the database. Then the SU will be notified of the complaint.
![](PICSendComplaintClassDiagram.png)
#### S. Send Compliment:
> OUs can send compliments of other OUs to SUs who will increase the reputation score of the complimented OU. OUs do this through the inbox page as the previous one and will be inserted into the database. Then SU will be notified.
![](PICSendComplimentClassDiagram.png)
#### T. Leave Project Group:
> At any time, a user can click this button on the group page and leave the project group. They will be prompted to confirm they do want to leave. Then their input will be recorded and they will be removed from the members list of the groups table in the database.
![](PICleavegroupclassdiaam.jpg)     

### 3. E-R diagram for the entire system attributes and key for each class should be provided
![](PICerdiagram.png)

### 4. Detailed design:
      o for EVERY method use pseudo-code to delineate the input/output and
      o main functionalities
##### A. jump_Homepage1():
> Pre-Conditions: User must click the HomePage1 Button
> if Button is clicked, then jumpHomepage1_Button == true
> Post-Conditions: Current window will be closed from view and Homepage1 will be opened.
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
```
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
Pseudocode:
```
	void create_Comment() {
		if(create_comment_button) {
			new_Comment = new createCommentWindow()
			new_Comment.open()
		}
	}		
```
#### I. Publish_Comment():
> Pre-Conditions: 
> User has typed into comment text box window
> User has clicked publish_comment_button
> Post-Conditions:
> User input will be read and inserted into database for group’s posts in comment column
Pseudocode:
```
	void publish_comment() {
 		if(database.insert(new_comment.text)
			jumpGroupPage(this.groupID) 
			(refreshing group page to show new comment)
			new_Comment.close()
		}
	}
```			
#### J. LogIn():
> Pre Conditions: User is in HomePage1; User must click the PublishPoll_Button 
> If Button is clicked, then ClickPublishPoll_Button == true
> Post_Condition: redirected to HomePage2;
Pseudocode:
```
	Void Login(){
		Int k=3;
		Int x=0;
		cin<<username;
		cin<<password;
		if(username!=database.username[x]&&x!=#ofMember){
			x++;
			if(username==database.username[x]&&password==database.username[x].password){
				current_Window.close();
				Homepage2.open();
			} Else if(x=#ofMember+1){
				cout>>no username exist;
			} Else if (username==database.username[x]&&password!=database.username[x].password){
				cout>>password wrong, you have k tries before the username got lock down;
				k--;
			}
		}
	}
```

#### K. LogOut():
> Pre Conditions: User must click the Logout_Button 
> If Button is clicked, then Logout_Button == true
> Post_Condition: redirect to HomePage1
Pseudocode:
```
	If (Logout_Button){
		current_Window.close();
		Homepage1.open();
	}
```
#### L. DeletePost():
> Pre Conditions: User is viewing database.post[k]; User must click the DeletePost_Button 
> If Button is clicked, then DeletePost_Button == true
> Post_Condition: redirect to GroupPage; database.post[k] got deleted;
Pseudocode:
```
	If (Logout_Button){
		database.post[k]==null;
		current_Window.close();
		GroupPage.open();
	}
```
#### M. DeleteComment():
> Pre Conditions: User is viewing database.comment[k]; User must click the DeleteComment_Button 
> If Button is clicked, then DeleteComment_Button == true
> Post_Condition: redirect to GroupPage; database.comment[k] got deleted;
Pseudocode:
```
	If (Logout_Button){
		database.comment[k]==null;
		current_Window.close();
		GroupPage.open();
	}
```
#### N. AcceptInvitation():
> Pre Conditions: User is viewing InboxPage; User must click the AcceptInvitation_Button 
> If Button is clicked, then AcceptInvitation_Button == true
> Post_Condition: group[k] will be added into profile; delete the invitation notice
Pseudocode:
```
	If (AcceptInvitation_Button){
		add.database.group[k];
		delete.Invitation[k];
	}
```
#### O. DeclineInvitation():
> Pre Conditions: User is viewing InboxPage; User must click the DeclineInvitation_Button 
> If Button is clicked, then DeclineInvitation_Button == true
> Post_Condition: delete the invitation notice
Pseudocode:
```
	If (DeclineInvitation_Button){
		delete.Invitation;
	}
```
#### P. AcceptAll():
> Pre Conditions: User is viewing InboxPage; 
> User must click the AcceptAllInvitation_Button 
> If Button is clicked, then AcceptAllInvitation_Button == true
> Post_Condition: group[A….X] will be added into profile; delete the invitation notice
Pseudocode:
```
	If (AcceptAllInvitation_Button){
		add.database.group[A…..X];
		delete.Invitation[A...X];
	}
```
#### Q. DeclineAll():
> Pre Conditions: User is viewing InboxPage; 
> User must click the DeclineAllInvitation_Button 
> If Button is clicked, then DeclineAllInvitation_Button == true
> Post_Condition: delete the invitation notice
Pseudocode:
```
	If (DeclineAllInvitation_Button){
		delete.Invitation[A...X];
	}
```
#### R. CreatePoll():
> Pre Conditions: User must click the CreatePoll_Button 
> If Button is clicked, then ClickCreatePoll_Button == true
> Post Conditions: CreatePoll will be a pop-up window and pop-up in front of the main GUI
Pseudocode:
```
	Void CreatePoll(){
		if(ClickCreatePoll_Button == true){
			CreatePoll_Page.open()
		}
	}	 
```		
#### S. PublishPoll():
> Pre Conditions: User must click the PublishPoll_Button 
> If Button is clicked, then ClickPublishPoll_Button == true
> Post Conditions: Poll will be saved into the database and be published
Pseudocode
```
	Void PublishPoll(){
		if(ClickPublishPoll_Button == true){
			database.Create(NewPoll)	
			SentNotification(GroupMembers)
			CreatePoll_Page.Close()
		}
	}	 
```
#### T. VotePoll():
> Pre Conditions: User must click the VotePoll_Button 
> If Button is clicked, then ClickVotePoll_Button == true
> Post Conditions: vote will be updated into the database
Pseudocode
```
	Void VotePoll(){
		if(ClickVotePoll_Button == true){
			database.update(voteInfo)	
		}
	}	 
```
#### U. LeaveGroup():
> Pre Conditions: User must click the LeaveGroup_Button 
> If Button is clicked, then ClickLeaveGroup_Button == true
> Post Conditions: update the database and send notification
> Pseudocode
```
	Void LeaveGroup(){
		if(ClickLeaveGroup_Button == true){
			database.delete(MemberInfo)	
			SentNotification(GroupMembers)
		}
	}	 
```
#### V. SendInvitation():
> Pre Conditions: User must click the SendInvitation_Button 
> If Button is clicked, then ClickSendInvitation_Button == true
> Post Conditions: update the database and send notification
Pseudocode
```
	Void SendInvitation(){
		if(ClickSendInvitation_Button == true){	
			SentNotification(GroupMembers)
		}
	} 
```
#### W. EditSkills():
> Pre Conditions: User must click the EditSkills_Button 
> If Button is clicked, then ClickEditSkills_Button == true
> Post Conditions: update the database Pseudocode
```
	Void EditSkills(){
		if(ClickEditSkills_Button == true){
			database.update(skillInfo)	
		}
	}	 
```
#### X. EditInterests():
> Pre Conditions: User must click the EditInterests_Button 
> If Button is clicked, then ClickEditInterests_Button == true
> Post Conditions: update the database Pseudocode
```
	Void EditInterests(){
		if(ClickEditInterests_Button == true){
			database.update(InterestInfo)	
		}
	} 
 ```   
### 5. System screens:
> demonstrate major GUI screens of the system and a prototype of one
> functionality of your own choice.
> Codes for each found in this repo. Codes with prefix "OLD" are from the old code in Tkinter. We are now using PyQt5.
#### Home Page 1 
![](PIChomepage1.png)
#### Login Page
![](PICloginpage.png)
#### Profile Page
![](PICprofilepage.png)
#### Registration Page
![](PICregistrationpage.png)
#### Group Page
![](PICgrouppage.png)

### 6. Minutes of group meetings and possible concerns of team work
> Our team had 5 group meeting sessions adding up to a total of 7hrs and 22mins of group working together. 

### 7. Address of the git repo (github, gitlab, bitbucket, etc) of your 
    team's work so far - put all materials including this report there
    Git repo and such is all here.
> Google Docs of Report In case Missing Sections:
https://docs.google.com/document/d/1mg6cAZ5uQf2P2sezdsFmTxK0sVSXGgF_z8rX4OM0uTI/edit?usp=sharing
