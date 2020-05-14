# CSC322Project
Software Engineer group porject 

## NEW STUFF ADDED AFTER PRESENTATION
taboo word is working now on create new post. for detail go down to taboo word section, evidence is saved as picture in the git
demote base on rep score is also working now. evidence and detail are same as above. Fixed bug for connecting profile page to UserData.csv. Now user's reputation score will be automatically decrease based on complaints and user's status will be automatically promoted or demoted based on reputation score

## Pyqt 5 
PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in.

## Functionality
Our application provides a platform for users to form teams with other users who have similar interests and different skill sets to complete a specific do-good projects. Users in the system will be ranked and evaluated base on their reputations socre. 

## Vistors
Visitors may view home page, search projects and users, but cannot interact with any projects or users.

## Ordinary users (OU)
Vistors can register to become an OU after SU's approval. OUs can create or join groups to work on do good projects together. 

## VIP
An OU whose reputation score is equal to or more than 30 will be automatically promoted to VIP. VIP have the power to periodic vote for a SU who will be responsiblt for managing the system.

## Super user(SU)
SU will be periodically voted in by VIPs. The responsibilities of SU includes manually increasing or decreasing user's reputation score if necceasry, kicking out users with bad behavior, and review registration requests. 

## Search
Users or visitors can use the search bar and search button located on top left of every main pages to search for specific groups and users. Search key words can either be userID, groupID, user first name or last name, group name, and user's username.  

## Start a group
To start a group, any users can access the groups page from home page, and click the "New Group" button to create a new group. The user have to create a group name and write down project description describing the goal for this project. The user can invite up to 8 users to join the group. 

## Invites
Users can choose to accept or decline group invites in their inbox page. 

## Edit Profile
Users can view and edit their profile throught the profile page.

## Create Post
Members with in one group can create post that can be view by other group members from the group page. Other members can write comment below existing posts. 

## Create meet up time poll
Group members can create meet up time polls to have team meet ups.

## Create member poll
Group members can create member polls. There are 3 types of Member polls: vote to send warnings to member, vote to kick member out, and vote to send compliment to member. 


## Taboo Word
The taboo word contains 3 words : 'darn' 'hate' 'bad'
create post use those 3 words will be convert to * base on how many letters in the word

## Demote Base on Score
if a user's reputation score after got deducted drop below 30, then he will be demoted to OU, drop below 50 will be demoted to VIP

SU can also manually set up for reputation score MANUALLY and the status will be change automatically as well



