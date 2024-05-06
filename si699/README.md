# Nurse Friend Programming Guide

If you are looking to setup the required packages and get basic code running, please refer to section 3.

#
# 1. Code Documentation
Please note down the steps and module installation done by you to achieve a screen, feature, or an issue in [directions.md](directions.md). This will help us with resolving errors, avoiding double effort to achieve same result, and easy duplication of steps by your team members.

#
# 2. Git Etiquette

## Branching
Create branches for each feature or issue you work on. For instance, an overlay component is a feature but fixing its styling or buttons are issues. If somebody is working on the same feature as you, please communicate and collaborate.
- **Always run ```git checkout``` to see which branch you are on before working. You should be running this command frequently.**

- **We will have 3 types of branches:** main, dev, and feature. The main branch is the production branch, which is the version that is sent to the customer and is always the working one. The dev branch is where all the feature branches are pull requested to aka merged. A feature branch is, well, for a feature.
- **Naming**: Please name all your branches according to the convenetion **"NSF-JiraTicketNumber"** and your commit message to **"NSF-JiraTicketNumber YourNameAbbr Feature/Issue"**. For example, my branch is "NSF-2", and one of my commit messages is "NSF-2 IYE Updated README doc naming convention"

  - ```git branch -a```
    - see all available branches in this repository/project.
  - ```git checkout -b <insertBranchNameHere>```
    - create a new branch ("-b" creates and switches to it).
  - ```git switch <insertBranchNameHere>```
    - switch between branches.

- **Adding it to working branch (not main)**
  - ```git add –i```
    - Opens interactive menu and it is used to update index using the current content.
      - There are alternative ways (e.g. git add .) to add changes to staging area but, they are not preferred unless you are experienced git user. Interactive menu gives easy access to control what changes we want to add to staging phase and push forward.
  - ```git status```
    - Shows which files are tracked by Git and which changes have been staged (which have been not).
  - ```git restore --staged <insertFileNameToUnstage>```
    - Note: Incase you added something you don't want to push.
  - ```git commit -m "<insertCommentsHere>"```
    - Record changes to the repository
  - ```git push --set-upstream origin <insertBranchNameHere>```
    - (You can do alias for this)

## Merging
Please DO NOT merge branches on your own. ALWAYS ALWAYS ALWAYS create a pull request from your feature branch to the dev branch! Before beginning work on any feature or issue, pull code from the main branch.
   
- The merge order is from feature branch to development branch, and then from development branch to main branch. This order ensures that changes are tested in the development branch before they are merged in to the main branch.
  - Simply said: the merge order is: feature > dev > main.
- Always open pull request from feature branch to dev branch (never to main!).
- Each issue equals to one feature which is represented by one feature branch.
- Always open pull request, instead of merging straight to the branch! This ensures that changes are peer reviewed and any potential problems can be identified before the changes are applied to the branch. Even if the problems were accepted via a pull request, it is still easy to revert back if needed.
  - ```git add -i```
  - ```git commit -m "<insertCommentsHere>"```
  - ```git checkout master```
  - ```git merge <insertBranchNameHere> --no-ff```

## Commit Messages
Always write good commit messages. This cannot be stressed enough. To maintain transparency and have a good idea of what your team partners are working on, good commit messages help a lot. They cost 30 seconds to a minute to write but save lengthy conversations between team members having to redundantly repeating what they did.
   
- ✅ Brief, concise, informative: "Added back/forward buttons to _ScreenName_" or "Added search bar to modal of _Resources Overlay_" or "Fixed redux/firebase storage aspect of logging in"
- ❌ Too brief/long, ambiguous: "Fixed _ScreenName_" or "Added buttons to overlay" or "Fixed logging in of users"
  - ```git commit -m "<insertCommentsHere>"```

# 
# 3. Platfrom Setup Prerequisites

Ensure these are installed before proceeding:

- **Node.js**: [Download](https://nodejs.org/en/download)
- **MongoDB Community Edition 7.0**: [Installation Guide](https://www.mongodb.com/docs/v7.0/administration/install-community/)
- **Visual Studio Code** (or any code editor): [Download](https://code.visualstudio.com/download)

## Pull Latest Changes
Regularly update your local codebase:

```bash
git pull origin dev
```

## Running the Program
### Frontend Setup
1. Open a terminal and navigate to the project's root.
2. Start the frontend:
```bash
cd frontend
npm install
npm start
```
3. Press **'i'** to launch the app on an IOS simulator, or press **'w'** to launch it on a web browser

# Backend Setup
1. Left the previous terminal open, and open **another** terminal window/tab.
2. Populate the database with an initial set of data:
```bash
cd backend
node seed.js
```
3. Start the backend:
```bash
npm install
npm start
```
Backend: Running on http://localhost:80/
