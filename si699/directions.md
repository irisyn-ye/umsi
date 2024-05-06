# Please update this file with the steps you took for each feature/issue/screen! 
This includes installation of modules, using a specific style guide, creating tabs etc. 
Doing so will help us have an understanding of what's going on and figure out errors along the way AND allow your team to easily duplicate the steps.

## Stack structure
For stack module installation, please follow steps 1-3 exactly from [here](https://reactnavigation.org/docs/stack-navigator#example).
We have all already installed modules required for tabs in the setup.


## To view the prototype on mobile devices:
### Problem
Your phone cannot access a backend running on localhost on your computer because localhost refers to the local device itself. When you use localhost on your phone, it looks for a server running on the phone, not elsewhere. Since localhost is an internal, loopback network interface that points to the device in use, trying to connect to localhost from your phone attempts to find the server on the phone, not on your computer, leading to a failure to connect to the actual backend server you have running on your computer.
### Suggested Solution - ngrok (Stella)
#### For the first time:
1. Sign up to [ngrok](https://dashboard.ngrok.com/).
2. Follow the installation steps provided on the ngrok website.
3. Under the "Deploy your app online" section, click on "Static Domain," then click on "Claim your free static domain."
4. After claiming your domain, click 'Visit Your Domain'. Note down the domain URL from the address bar for later use.
5. Create a file named `Secret.js`. Inside this file, assign the URL you noted in step 4 to a constant named `BASE_URL` as shown below.
    ```Secret.js
    export const BASE_URL = "[your domain url]";
    ```
6. In each feature slice file located at frontend/features/[feature name]/[feature name]Slice.js, modify the Axios import and the base URL setup.
   Change:
    ```
    import axios from 'axios';
    const url = 'http://localhost:3000/[feature name]' // For iOS simulator
    ```
   to:
    ```
    import axios from '../../axios'; // Utilize the customized Axios instance
    const url = '/[feature name]' // Simplified URL, leveraging the base URL defined in the custom Axios instance
    ```
  
#### After the first time:
Open a third terminal or tab. Replace `[your domain url]` with the URL you've noted previously, and then run the following command:
```bash
ngrok http --domain=[your domain url] 3000
```
This will start ngrok and expose your local server on the specified domain, making it accessible over the internet.
